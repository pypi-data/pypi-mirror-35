# -*- coding: utf-8 -*-

"""
logger module
"""

import logging


def setup(logfile, level=logging.WARNING):
    """
    Setup the logger instance
    :param logfile: Name of the file to use for logging output
    :param level: Log level to set
    """
    logger = logging.getLogger(__package__)
    logger.setLevel(level)
    logger_fh = logging.FileHandler(logfile)
    logger_fh.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s.%(funcName)s() - %(levelname)s - %(message)s')
    logger_fh.setFormatter(formatter)
    logger.addHandler(logger_fh)


class StreamToLogger:
    """
    Implement a file-like interface to redirect writes to the 'log'
    method using a logger instance
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        """
        Write using the logger's instance 'log' method
        :param buf: Content to log
        """
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        """
        Mock the 'flush' method
        """
        pass
