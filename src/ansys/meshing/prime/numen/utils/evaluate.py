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

"""Module for evaluating expression."""
import ast
import json
import re
from typing import Dict

from ansys.meshing.prime.numen.utils.functions import function_map
from ansys.meshing.prime.numen.utils.param_defs import ParamDefs


def __get_params(repl_params: ParamDefs, param_name: str):
    return repl_params.get(param_name)


def __get_value(context: Dict, var_name: str):
    if var_name in context:
        return context[var_name]
    else:
        return None


def __eval_function(function_str: str):
    f_str = function_str.replace("'", "\"")
    function_name, args_str = f_str.split(',', 1)
    function_name = function_name.strip()
    if function_name in function_map:
        args = []
        args = ast.literal_eval(f'({args_str})')
        if not isinstance(args, tuple):
            args = (args,)
        arg_count = len(args)
        if arg_count == 0:
            return function_map[function_name]()
        elif arg_count == 1:
            return function_map[function_name](args[0])
        elif arg_count == 2:
            return function_map[function_name](args[0], args[1])
        elif arg_count == 3:
            return function_map[function_name](args[0], args[1], args[2])
        elif arg_count == 4:
            return function_map[function_name](args[0], args[1], args[2], args[3])
        elif arg_count == 5:
            return function_map[function_name](args[0], args[1], args[2], args[3], args[4])
        elif arg_count == 6:
            return function_map[function_name](args[0], args[1], args[2], args[3], args[4], args[5])
    return None


def evaluate_expression(repl_params: ParamDefs, context: Dict, exp: str):
    """Evaluate expression."""
    if not isinstance(exp, str):
        return exp
    expression = exp
    # evaluate all values
    search_pattern = r"\$value\s*\(\s*([\w|\d]*)\s*\)"
    found = True
    while found:
        val = re.search(search_pattern, expression)
        if val != None:
            val_str = expression[val.span()[0] : val.span()[1]]
            val_name = val.groups()[0]
            param_val = __get_value(context, val_name)
            param_val = json.dumps(param_val)
            expression = expression.replace(val_str, param_val)
        else:
            found = False

    # evaluate all params
    search_pattern = r"\$param\s*\(\s*([\w|\d|\.]*)\s*\)"
    found = True
    while found:
        val = re.search(search_pattern, expression)
        if val != None:
            val_str = expression[val.span()[0] : val.span()[1]]
            val_name = val.groups()[0]
            param_val = __get_params(repl_params, val_name)
            param_val = json.dumps(param_val)
            expression = expression.replace(val_str, param_val)
        else:
            found = False

    # evaluate all functions
    search_pattern = r"\$func\s*\(([^\$\)]*)\)"
    found = True
    while found:
        val = re.search(search_pattern, expression)
        if val != None:
            val_str = expression[val.span()[0] : val.span()[1]]
            val_name = val.groups()[0]
            param_val = __eval_function(val_name)
            param_val = json.dumps(param_val)
            expression = expression.replace(val_str, param_val)
        else:
            found = False

    try:
        return json.loads(expression)
    except Exception as e:
        return expression
