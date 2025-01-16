# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

"""Util functions for lucid modules."""
import re


def match_pattern(pattern: str, name: str) -> bool:
    """Pattern matching function for strings.

    Parameters
    ----------
    pattern : str
        Pattern you are looking for in the string.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if the pattern is found.
    """
    pattern = "^" + pattern.replace("*", ".*").replace("?", ".") + "$"
    x = re.search(pattern, name)
    if x:
        return True
    else:
        return False


def check_name_pattern(name_patterns: str, name: str) -> bool:
    """Check several patterns in one string.

    Parameters
    ----------
    name_patterns : str
        Patterns to check, separated by commas.
        If pattern starts with !, it shouldn't be found.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if all found.
    """
    patterns = []
    a = name_patterns.split(",")
    for aa in a:
        patterns.append(aa)

    for pattern in patterns:
        bb = pattern.split("!")
        if match_pattern(bb[0].strip(), name):
            if len(bb) > 1:
                nv = False
                for nvbb in bb[1:]:
                    if match_pattern(nvbb.strip(), name):
                        nv = True
                        break
                if not nv:
                    return True
            else:
                return True

    return False
