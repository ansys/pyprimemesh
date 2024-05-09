# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

import datetime

from ansys.meshing.prime.internals.logger import PrimeLogger


def test_logger(tmp_path):
    logs_path = str(tmp_path) + "/logs"
    prime_logger_setup = PrimeLogger(logger_name="Test_logger")
    prime_logger_setup.add_file_handler(log_dir=logs_path)
    logger = prime_logger_setup.python_logger

    logger.setLevel("INFO")
    msg = "this is an error"
    logger.error(msg)

    now = datetime.datetime.now()

    # Another call to singleton, should be configured already
    prime_logger_setup_2 = PrimeLogger()
    logger_2 = prime_logger_setup_2.python_logger
    msg_2 = "this is another error"
    logger_2.error(msg_2)

    # Assert we are using a singleton.
    with open(logs_path + '/log_' + now.strftime("%Y-%m-%d") + '.log', 'r') as file:
        line_1 = file.readline()
        assert msg in line_1
        line_2 = file.readline()
        assert msg_2 in line_2
