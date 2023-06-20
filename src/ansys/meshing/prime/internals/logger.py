"""Module for logger singleton."""

# logger from https://gist.github.com/huklee/cea20761dd05da7c39120084f52fcc7c
import datetime
import logging
import os


class SingletonType(type):
    """Singleton helper class for the Logger."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call to redirect new instances to single instance."""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PrimeLogger(object, metaclass=SingletonType):
    """Singleton logger for PyPrimeMesh.

    Logger for PyPrimeMesh library.

    Parameters
    ----------
    to_file : bool, optional
        Whether to include the logs in a file or not, by default False
    """
    _logger = None

    def __init__(self, to_file: bool = False):
        """Logger initializer."""

        self._logger = logging.getLogger("PyPrimeMesh")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s'
        )

        # save to file
        if to_file:
            now = datetime.datetime.now()
            dirname = "./.log"
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log")
            fileHandler.setFormatter(formatter)
            self._logger.addHandler(fileHandler)

        # stdout
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        self._logger.addHandler(streamHandler)

    def get_logger(self):
        """Getter for the logger.

        Returns
        -------
        Logger
            The logger.
        """
        return self._logger


LOG = PrimeLogger().get_logger()
