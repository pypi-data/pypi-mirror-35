"""Enables Logging for PPExtensions."""

import logging
import getpass
import os

from pathlib import Path


class Log:
    """
    Custom Logging for PPExtensions.
    """

    def __init__(self, logger_name, module='',
                 filename='{}/logs/ppextensions.log'.format(str(Path.home())),
                 level=logging.INFO):
        self.logger_name = logger_name
        self._module = module
        if not os.path.isdir("{}/logs/".format(str(Path.home()))):
            os.mkdir("{}/logs/".format(str(Path.home())))
        logging.basicConfig(
            filename=filename,
            level=level,
            format='%(asctime)-4s %(levelname)-4s %(name)-4s {} %(message)s'.format(getpass.getuser()),
            datefmt='%m-%d %H:%M:%S'
        )
        self._init_logger_()

    def _init_logger_(self):
        """
        Initialize logger.
        """
        self.logger = logging.getLogger(self.logger_name)

    def debug(self, message):
        """
        Logging debug messages.
        """
        self.logger.debug(self._format_message_(message))

    def error(self, message):
        """
        Logging error messages.
        """
        self.logger.error(self._format_message_(message))

    def info(self, message):
        """
        Logging info.
        """
        self.logger.info(self._format_message_(message))

    def exception(self, message):
        """
        Logging exceptions.
        """
        self.logger.exception(self._format_message_(message))

    def _format_message_(self, message):
        """
        Formatting log messages.
        """
        if self._module is None or len(self._module) is 0:
            return message
        return '{} {}'.format(self._module, message)
