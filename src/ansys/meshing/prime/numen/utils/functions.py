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

"""Module for functions."""
import inspect
import sys
from os.path import exists, isfile


def equals_(data1, data2):
    """Check for equality."""
    return data1 == data2


def add_(data1, data2):
    """Add a data."""
    return data1 + data2


def in_list_(value, value_list):
    """Check whether value present in list or not."""
    return value in value_list


def non_empty_string_(value):
    """Check for non empty string."""
    return len(value) > 0


def valid_file_on_disc_(value):
    """Check for valid file on disc."""
    return exists(value) and isfile(value)


def positive_value_(value):
    """Check for positive value."""
    return value > 0


def min_(value, check):
    """Check for minimum value."""
    return value >= check


def max_(value, check):
    """Check for maximum value."""
    return value <= check


def range_(value, check1, check2):
    """Check for value in range."""
    return min_(value, check1) and max_(value, check2)


def unique_name_(value):
    """Check for unique name."""
    return True


function_map = {}
__functions = [
    obj
    for name, obj in inspect.getmembers(sys.modules[__name__])
    if (inspect.isfunction(obj) and not name.startswith("_"))
]

for i in range(len(__functions)):
    function_map[__functions[i].__name__[0:-1]] = __functions[i]
