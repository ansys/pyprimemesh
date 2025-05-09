# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module for logger singleton."""

# logger from https://gist.github.com/huklee/cea20761dd05da7c39120084f52fcc7c
import datetime
import logging
import os
from typing import Union

from ansys.meshing.prime.internals import utils


class SingletonType(type):
    """Provides the singleton helper class for the logger."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call to redirect new instances to the singleton instance."""
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PrimeLogger(object, metaclass=SingletonType):
    """Provides the singleton logger for PyPrimeMesh."""

    _logger = None

    def __init__(self, level: int = logging.WARNING, logger_name: str = "PyPrimeMesh"):
        """Logger initializer."""
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(level)
        self._formatter = logging.Formatter(
            '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s'
        )

    @property
    def python_logger(self) -> logging.Logger:
        """Get the python logger.

        Returns
        -------
        logging.Logger
            Logger.
        """
        return self._logger

    def set_level(self, level: Union[int, str]):
        """Set logger output level.

        Parameters
        ----------
        level : int
            Level of the logger.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        utils.print_beta_api_warning(self._logger, "set_level")
        self._logger.setLevel(level=level)

    def enable_output(self, stream=None):
        """Enable logger output to given stream.

        If stream is not specified, sys.stderr is used.

        Parameters
        ----------
        stream: TextIO, optional
            Stream to output the log output to stream

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        # stdout
        utils.print_beta_api_warning(self._logger, "enable_output")
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setFormatter(self._formatter)
        self._logger.addHandler(stream_handler)

    def add_file_handler(
        self, log_dir: str = "./.log", log_file: str = None
    ) -> logging.FileHandler:
        """Save logs to a file.

        Parameters
        ----------
        log_dir : str, optional
            Directory of the logs. The default is ``"./.log"``.

        log_file : str, optional
            Log filename. The default is ``"log_<datestamp>.log"``.

        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.
        """
        utils.print_beta_api_warning(self._logger, "add_file_handler")
        if log_file is None:
            now = datetime.datetime.now()
            log_file = "log_" + now.strftime("%Y-%m-%d") + ".log"
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
        file_handler.setFormatter(self._formatter)
        self._logger.addHandler(file_handler)
        return file_handler
