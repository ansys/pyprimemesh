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

import re

from ansys.meshing.prime.numen.utils.evaluate import evaluate_expression
from ansys.meshing.prime.numen.utils.param_defs import ParamDefs


def check_param(param_defs: ParamDefs, input_param: dict, param_name: str, exp: str):
    # convert the check notation to func notation
    # "range:10,20"  ->  "$func(range,$value(param_name),10,20)"
    search_re = r"^\ *([^\ \:]*):"
    search_result = re.search(search_re, exp)
    if search_result != None:
        val_str = exp[search_result.span()[0] : search_result.span()[1]]
        val_name = search_result.groups()[0]
        exp = exp.replace(val_str, "$func(" + val_name + ",$value(" + param_name + "),") + ")"
    else:
        exp = "$func(" + exp + ",$value(" + param_name + "))"
    return evaluate_expression(param_defs, input_param, exp)


def null_check(param_value):
    return param_value == "$null"


def type_check(param_value, param_type, sub_param_type=None):
    if param_type == "string" or param_type == "path":
        return isinstance(param_value, str)
    elif param_type == "int":
        return isinstance(param_value, int)
    elif param_type == "float":
        return isinstance(param_value, float) or isinstance(param_value, int)
    elif param_type == "boolean":
        return isinstance(param_value, bool)
    elif param_type == "list":
        if isinstance(param_value, list):
            for val in param_value:
                if not type_check(val, sub_param_type):
                    return False
            return True
        else:
            return False
    ValueError(f"Unexpected type \"{param_type}\" found.")
    return False
