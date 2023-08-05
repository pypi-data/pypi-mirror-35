"""
Copyright 2016 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging
from os.path import join, isfile
import os
import platform
from time import sleep
import hashlib
import six

import mbed_lstools

from mbed_flasher.common import retry, FlashError
from mbed_flasher.mbed_common import MbedCommon
from mbed_flasher.daplink_errors import DAPLINK_ERRORS
from mbed_flasher.reset import Reset
from mbed_flasher.return_codes import EXIT_CODE_SUCCESS
from mbed_flasher.return_codes import EXIT_CODE_FLASH_FAILED
from mbed_flasher.return_codes import EXIT_CODE_FILE_COULD_NOT_BE_READ
from mbed_flasher.return_codes import EXIT_CODE_PYOCD_NOT_INSTALLED
from mbed_flasher.return_codes import EXIT_CODE_EGDB_NOT_SUPPORTED
from mbed_flasher.return_codes import EXIT_CODE_OS_ERROR
from mbed_flasher.return_codes import EXIT_CODE_FILE_STILL_PRESENT
from mbed_flasher.return_codes import EXIT_CODE_TARGET_ID_MISSING
from mbed_flasher.return_codes import EXIT_CODE_DAPLINK_TRANSIENT_ERROR
from mbed_flasher.return_codes import EXIT_CODE_DAPLINK_SOFTWARE_ERROR


class FlasherMbed(object):
    """
    Implementation class of mbed-flasher flash operation
    """
    name = "mbed"
    supported_targets = None
    DRAG_AND_DROP_FLASH_RETRIES = 5

    def __init__(self, logger=None):
        self.logger = logger if logger else logging.getLogger('mbed-flasher')

    @staticmethod
    def get_supported_targets():
        """
        Load target mapping information
        """
        if not FlasherMbed.supported_targets:
            mbeds = mbed_lstools.create()

            # this should works for >=v1.3.0
            # @todo this is workaround until mbed-ls provide public
            #       API to get list of supported platform names
            FlasherMbed.supported_targets = sorted(set(name for id, name in mbeds.plat_db.items()))

        return FlasherMbed.supported_targets

    @staticmethod
    def get_available_devices():
        """
        Get available devices
        """
        mbeds = mbed_lstools.create()
        return mbeds.list_mbeds()

    # pylint: disable=unused-argument
    @staticmethod
    def can_flash(target):
        """
        Check if target should be flashed by drag and drop method.
        Currently there is no reason not to try it.
        :param target: target board
        :return: True
        """
        return True

    # pylint: disable=too-many-return-statements, duplicate-except
    def flash(self, source, target, method, no_reset):
        """copy file to the destination
        :param source: binary to be flashed
        :param target: target to be flashed
        :param method: method to use when flashing
        :param no_reset: do not reset flashed board at all
        """
        if not isinstance(source, six.string_types):
            return

        if method == 'pyocd':
            self.logger.debug("pyOCD selected for flashing")
            return self.try_pyocd_flash(source, target)

        if method == 'edbg':
            raise FlashError(message="edbg is not supported for Mbed devices",
                             return_code=EXIT_CODE_EGDB_NOT_SUPPORTED)

        return retry(
            logger=self.logger,
            func=self.try_drag_and_drop_flash,
            func_args=(source, target, no_reset),
            retries=FlasherMbed.DRAG_AND_DROP_FLASH_RETRIES,
            conditions=[EXIT_CODE_OS_ERROR,
                        EXIT_CODE_DAPLINK_TRANSIENT_ERROR,
                        EXIT_CODE_DAPLINK_SOFTWARE_ERROR])

    def try_pyocd_flash(self, source, target):
        """
        try pyOCD flash
        """
        try:
            from pyOCD.board import MbedBoard
        except ImportError:
            # python 3 compatibility
            # pylint: disable=superfluous-parens
            raise FlashError(message="PyOCD is missing",
                             return_code=EXIT_CODE_PYOCD_NOT_INSTALLED)

        try:
            with MbedBoard.chooseBoard(board_id=target["target_id"]) as board:
                ocd_target = board.target
                ocd_flash = board.flash
                self.logger.debug("resetting device: %s", target["target_id"])
                sleep(0.5)  # small sleep for lesser HW ie raspberry
                ocd_target.reset()
                self.logger.debug("flashing device: %s", target["target_id"])
                ocd_flash.flashBinary(source)
                self.logger.debug("resetting device: %s", target["target_id"])
                sleep(0.5)  # small sleep for lesser HW ie raspberry
                ocd_target.reset()
            return EXIT_CODE_SUCCESS
        except AttributeError as err:
            msg = "Flashing failed: {}. tid={}".format(err, target["target_id"])
            self.logger.error(msg)
            raise FlashError(message="PyOCD flash failed",
                             return_code=EXIT_CODE_FLASH_FAILED)

    def try_drag_and_drop_flash(self, source, target, no_reset):
        """
        Try to flash the target using drag and drop method.
        :param source: file to be flashed
        :param target: target board to be flashed
        :param no_reset: whether to reset the board after flash
        :return: 0 if success
        """

        target = MbedCommon.refresh_target(target["target_id"])
        if not target:
            raise FlashError(message="Target ID is missing",
                             return_code=EXIT_CODE_TARGET_ID_MISSING)

        destination = MbedCommon.get_binary_destination(target["mount_point"], source)

        try:
            if 'serial_port' in target and not no_reset:
                Reset(logger=self.logger).reset_board(target["serial_port"])
                sleep(0.1)

            self.copy_file(source, destination)
            self.logger.debug("copy finished")

            target = MbedCommon.wait_for_file_disappear(target, source)

            if not no_reset:
                Reset(logger=self.logger).reset_board(target["serial_port"])
                sleep(0.4)

            # verify flashing went as planned
            self.logger.debug("verifying flash")
            return self.verify_flash_success(
                target, MbedCommon.get_binary_destination(target["mount_point"], source))
        # In python3 IOError is just an alias for OSError
        except (OSError, IOError) as error:
            msg = "File copy failed due to: {}".format(str(error))
            self.logger.exception(msg)
            raise FlashError(message=msg,
                             return_code=EXIT_CODE_OS_ERROR)

    def copy_file(self, source, destination):
        """
        copy file from os
        """
        self.logger.debug('read source file')
        try:
            with open(source, 'rb') as source_file:
                aux_source = source_file.read()
        except (IOError, OSError):
            self.logger.exception("File couldn't be read")
            raise FlashError(message="File couldn't be read",
                             return_code=EXIT_CODE_FILE_COULD_NOT_BE_READ)

        self.logger.debug("SHA1: %s", hashlib.sha1(aux_source).hexdigest())

        if platform.system() == 'Windows':
            self.logger.debug('copying file: "{}" to "{}"'.format(source, destination))
            os.system("copy \"%s\" \"%s\"" % (os.path.abspath(source), destination))
        else:
            self.logger.debug("writing binary: %s (size=%i bytes)", destination, len(aux_source))
            new_file = self.get_file(destination)
            os.write(new_file, aux_source)
            os.close(new_file)

    @staticmethod
    def get_file(destination):
        """
        Get file
        """
        if platform.system() == 'Darwin':
            return os.open(
                destination,
                os.O_CREAT | os.O_TRUNC | os.O_RDWR | os.O_SYNC)

        return os.open(
            destination,
            os.O_CREAT | os.O_DIRECT | os.O_TRUNC | os.O_RDWR)

    @staticmethod
    def _read_file(path, file_name):
        with open(join(path, file_name), 'r') as fault:
            return fault.read().strip()

    def verify_flash_success(self, target, file_path):
        """
        verify flash went well
        """
        mount = target['mount_point']
        if isfile(join(mount, 'FAIL.TXT')):
            fault = FlasherMbed._read_file(mount, "FAIL.TXT")
            self.logger.error("Flashing failed: %s. tid=%s",
                              fault, target["target_id"])

            try:
                errors = [error for error in DAPLINK_ERRORS if error in fault]
                assert len(errors) <= 1
                raise FlashError(message=fault, return_code=DAPLINK_ERRORS[errors[0]])
            except AssertionError:
                msg = "Found multiple errors from FAIL.TXT: {}".format(fault)
                self.logger.exception(msg)
                raise FlashError(message=msg, return_code=EXIT_CODE_FLASH_FAILED)
            except IndexError:
                msg = "Error in FAIL.TXT is unknown: {}".format(fault)
                self.logger.exception(msg)
                raise FlashError(message=msg, return_code=EXIT_CODE_FLASH_FAILED)

        if isfile(join(mount, 'ASSERT.TXT')):
            fault = FlasherMbed._read_file(mount, "ASSERT.TXT")
            msg = "Found ASSERT.TXT: {}".format(fault)
            self.logger.error("{} found ASSERT.txt: {}".format(target["target_id"], fault))
            raise FlashError(message=msg, return_code=EXIT_CODE_FLASH_FAILED)

        if isfile(file_path):
            msg = "File still present in mount point"
            self.logger.error("{} file still present in mount point".format(target["target_id"]))
            raise FlashError(message=msg, return_code=EXIT_CODE_FILE_STILL_PRESENT)

        self.logger.debug("ready")
        return EXIT_CODE_SUCCESS
