import logging
import os

class IWSAgentLogger():
    """
    IWS Agent Logger

    Standardised logger factory for use within agent.
    """
    _logger   = None

    def __init__(self, name, log_file, level):
        self._logger = self.get_logger(name, log_file, level)

    def get_logger(self, name, log_file, level=logging.INFO):
        """
        Factory to generate a new logger
        """
        # get a new logger and set options
        # we only want to log to a file as the intended
        # use is as a daemon
        logger = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(fileHandler)

        return logger  # return the logger

    """
    Log messages at various log levels
    """
    def info(self, msg):
        if self._logger != None:
            self._logger.info(msg)

    def warn(self, msg):
        if self._logger != None:
            self._logger.warn(msg)

    def error(self, msg):
        if self._logger != None:
            self._logger.error(msg)

    def debug(self, msg):
        if self._logger != None:
            self._logger.debug(msg)
