"""Module for logger singleton."""

# logger from https://gist.github.com/huklee/cea20761dd05da7c39120084f52fcc7c
import datetime
import logging
import os


class SingletonType(type):
    """Provides the singleton helper class for the logger."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call to redirect new instances to the singleton instance."""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PrimeLogger(object, metaclass=SingletonType):
    """Provides the singleton logger for PyPrimeMesh.

    Parameters
    ----------
    to_file : bool, optional
        Whether to include the logs in a file. The default is ``False``.
    """

    _logger = None

    def __init__(self, logger_name: str = "PyPrimeMesh"):
        """Logger initializer."""
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s'
        )
        # stdout
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        """Get the logger.

        Returns
        -------
        Logger
            Logger.
        """
        return self._logger

    def add_file_handler(self, logs_dir: str = "./.log"):
        """Save logs to a file in addition to printing them to stdout.

        Parameters
        ----------
        logs_dir : str, optional
            Directory of the logs. The default is ``"./.log"``.
        """
        now = datetime.datetime.now()
        if not os.path.isdir(logs_dir):
            os.mkdir(logs_dir)
        file_handler = logging.FileHandler(logs_dir + "/log_" + now.strftime("%Y-%m-%d") + ".log")
        file_handler.setFormatter(self.formatter)
        self._logger.addHandler(file_handler)


LOG = PrimeLogger().get_logger()
