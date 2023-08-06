import logging
import os

class IWSAgentLogger():
    """
    IWS Agent Logger

    Standardised logger factory for use within agent.
    """
    _logger   = None
    _base_dir = None

    def __init__(self, base, name, log_file, level):
        self._base_dir = base
        self._logger = self.get_logger(name, log_file, level)

    def get_logger(self, name, log_file, level=logging.INFO):
        """
        Factory to generate a new logger
        """

        # define log file location
        log_dir = os.path.join(self._base_dir, 'logs')
        log_file = os.path.join(log_dir, log_file)

        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)

        # get a new logger and set options
        # we only want to log to a file as the intended
        # use is as a daemon
        l = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler.setFormatter(formatter)
        l.setLevel(level)
        l.addHandler(fileHandler)

        return l  # return the logger

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
