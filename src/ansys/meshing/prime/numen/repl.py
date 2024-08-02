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

"""Numen repl module."""

import inspect
import json
import logging
import os
import re
import sys
import time
from typing import Dict, List

from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.checks import check_param, type_check
from ansys.meshing.prime.numen.utils.communicator import call_method
from ansys.meshing.prime.numen.utils.evaluate import evaluate_expression
from ansys.meshing.prime.numen.utils.param_defs import ParamDefs


def _str(input: tuple) -> str:
    if isinstance(input, tuple):
        return " ".join(input)
    else:
        return input


class Repl:
    """Handles execution of numen workflow."""
    def __init__(self, model: prime.Model, n_threads: int = 12):
        """Construct Repl object."""
        dir = os.path.dirname(os.path.abspath(__file__))
        file = open(os.path.join(dir, "types.json"))
        self._param_map = json.load(file)
        file.close()
        self._function_map = {}
        method_modules = [
            prime.numen.misc,
            prime.numen.surface,
            prime.numen.controls,
            prime.numen.settings,
            prime.numen.connect,
            prime.numen.topology,
            prime.numen.volume,
        ]
        for module in method_modules:
            self._function_map.update(self.__get_function_map(module))
        self._model = model
        self._verbosity = 0
        self._logger = logging.getLogger(__name__)
        self._setup_logging(self._verbosity)
        # self._logger.setLevel(20)
        # self._logger.addHandler(logging.StreamHandler(sys.stdout))
        # self._cached_data = CachedData(self._model, self._logger)
        self._param_defs = ParamDefs(model)
        self._write_on_error = False
        if model:
            self._n_procs = self._model.get_num_compute_nodes()
            # self._logger = self._model.logger.python_logger
            # self._setup_logging(self._verbosity)
            self._cached_data = CachedData(self._model, self._logger)
            self._model.set_num_threads(n_threads)
            self._model._comm.serve(
                self._model,
                "PrimeMesh::Model/SetPyPrimeSettings",
                self._model._object_id,
                args={"settings": "encode_hidden_params"},
            )
            self._model._sync_up_model()

    def __load_step(self):
        pass

    def __collect_traceback(self, e: Exception, trace_level: int = 5):
        traces = []
        if self._verbosity > 0:
            traceobj = e.__traceback__
            for i in range(trace_level):
                if traceobj:
                    traces.append((traceobj.tb_frame.f_code.co_filename, traceobj.tb_lineno))
                    traceobj = traceobj.tb_next
        return traces

    def __log_exception_details(self, info):
        if len(info) > 0:
            self._logger.error("    Exception traceback:")
            for i in info:
                self._logger.error(f"        \"{i[0]}\" line:{i[1]}")

    def __log_exception(self, header: str, e: Exception, info=[]):
        if self._write_on_error:
            self.__write_intermediate("error")
        self._logger.error(header)
        for message in str(e).splitlines():
            self._logger.error("    " + message)
        self.__log_exception_details(info)

    def __get_function_map(self, module):
        module_name = module.__name__.split(".")[-1]
        dir = os.path.dirname(os.path.abspath(__file__))
        file = open(os.path.join(dir, module_name + ".json"))
        obj = json.load(file)
        file.close()
        method_to_function = {}
        members = inspect.getmembers(module)
        for member in members:
            if not member[0].startswith("_") and inspect.isfunction(member[1]):
                if module_name == member[0]:
                    method_to_function["numen." + member[0]] = member[1]
                else:
                    method_to_function["numen." + module_name + "." + member[0]] = member[1]

        method_map = {}
        for step in obj:
            if "method" in step:
                method = step["method"]
                if method in method_to_function:
                    method_map.update(
                        {method: {"details": step, "function": method_to_function[method]}}
                    )
        return method_map

    def __get_param_val(self, param_name: str) -> any:
        return self._param_defs.get(param_name)

    def __get_param_type(self, type):
        if not type:
            return [None, None]
        d = re.split(r"\[|\]", type)
        e = []
        for c in d:
            f = c.strip()
            if len(f) > 0:
                e.append(f)
        if len(e) == 1:
            e.append(None)
        return e

    def __is_param_enabled(
        self, method_name: str, type_name: str, parameter_name: str, parameters: Dict
    ):
        parameter_def = self._param_map[type_name]
        parameter_def_entry = next((p for p in parameter_def if p["name"] == parameter_name), None)
        if parameter_def_entry == None:
            raise TypeError(f"Parameter definition not found for \"{parameter_name}\"")
        if "enabled" in parameter_def_entry:
            enabled_val = parameter_def_entry["enabled"]
            if isinstance(enabled_val, str):
                enabled_val = evaluate_expression(self._param_defs, parameters, enabled_val)
            return enabled_val
        return True

    def __get_params(
        self,
        method_name: str,
        type_name: str,
        param_inputs: dict,
        parent_vals: dict,
        parent_param_name: str = "",
    ):
        scope_vals = parent_vals.copy()
        parameters = {}
        parameter_type_map = {}
        parameter_def = self._param_map[type_name]

        # Create parameters with default values
        self.__initialize_parameters(parameter_def, parameter_type_map, parameters)

        # Set parameter values from user input and perform checks
        nested_params = {}
        self.__process_param_inputs(
            method_name, type_name, param_inputs, parameters, parameter_type_map, scope_vals
        )

        self.__process_param_checks(
            parameter_def, parameters, parameter_type_map, nested_params, parent_param_name
        )

        self._param_defs.push_override_for_global(scope_vals)
        # Handle nested parameters
        self.__handle_nested_params(
            method_name, nested_params, param_inputs, scope_vals, parameters
        )
        self._param_defs.pop_override()

        return parameters

    def __initialize_parameters(self, parameter_def, parameter_type_map, parameters):
        for parameter in parameter_def:
            parameter_name = parameter["name"]
            parameter_type = self.__get_param_type(parameter["type"])
            parameter_type_map[parameter_name] = parameter_type
            if "default" in parameter:
                default_param = self.__resolve_default_param(parameter["default"])
            else:
                default_param = None
            parameters[parameter_name] = default_param

    def __resolve_default_param(self, default_param):
        if default_param == "$null":
            default_param = None
        elif isinstance(default_param, str) and default_param.startswith("$"):
            default_param = evaluate_expression(self._param_defs, {}, default_param)
        return default_param

    def __process_param_inputs(
        self, method_name, type_name, param_inputs, parameters, parameter_type_map, scope_vals
    ):
        for parameter_name, param_value in param_inputs.items():
            # check if parameter is defined
            if parameter_name not in parameter_type_map:
                self._logger.warning(f"    Ignoring parameter \"{parameter_name}\"")
                continue

            # check if parameter is enabled
            if self.__is_param_enabled(method_name, type_name, parameter_name, parameters):
                scope_vals[parameter_name] = param_value
                parameters[parameter_name] = param_value
            else:
                parameters.pop(parameter_name)

    def __process_param_checks(
        self, parameter_def, parameters, parameter_type_map, nested_params, parent_param_name
    ):
        error_list = []
        for p_name, param_value in parameters.items():
            if param_value == None:
                error_list.append(f"    Parameter \"{p_name}\" must be specified")
                continue
            parameter_type = parameter_type_map[p_name]
            if parameter_type[0] == "list" and self._param_map.get(parameter_type[1]):
                nested_params[p_name] = parameter_type
            else:
                parameter_def_entry = next((p for p in parameter_def if p["name"] == p_name), None)
                if parameter_def_entry is None:
                    raise TypeError(
                        _str(
                            (
                                f"    Parameter definition not found for",
                                "\"{parent_param_name}{p_name}\"",
                            )
                        )
                    )

                if parameter_type[0] == "range":
                    if param_value not in parameter_def_entry["range"]:
                        error_list.append(
                            _str(
                                (
                                    "    Type check failed for parameter",
                                    f"\"{parent_param_name}{p_name}\".",
                                    f"Given value \"{param_value}\".",
                                    f"Allowed values are {parameter_def_entry['range']}",
                                )
                            )
                        )
                        continue
                elif not type_check(param_value, parameter_type[0], parameter_type[1]):
                    type_name = parameter_type[0]
                    if type_name == "list":
                        type_name = f"list[{parameter_type[1]}]"
                    error_list.append(
                        _str(
                            (
                                "    Type check failed for parameter",
                                f"\"{parent_param_name}{p_name}\".",
                                f"Given value \"{param_value}\".",
                                f"Allowed type is \"{type_name}\"",
                            )
                        )
                    )
                    continue

                checks = parameter_def_entry.get("checks", [])
                for c in checks:
                    if not check_param(self._param_defs, parameters, p_name, c):
                        error_list.append(
                            _str(
                                (
                                    f"    Check \"{c}\" failed for parameter",
                                    f"\"{parent_param_name}{p_name}\"",
                                )
                            )
                        )
        if len(error_list) > 0:
            raise ValueError("\n".join(error_list))

    def __handle_nested_params(
        self, method_name, nested_params, param_inputs, scope_vals, parameters
    ):
        for parameter_name, parameter_type in nested_params.items():
            if parameter_type[0] == "list" and self._param_map[parameter_type[1]]:
                param_val_arr = []
                if parameter_name in param_inputs:
                    param_input = param_inputs[parameter_name]
                    for i in range(len(param_input)):
                        input_item = param_input[i]
                        param_val_arr.append(
                            self.__get_params(
                                method_name,
                                parameter_type[1],
                                input_item,
                                scope_vals,
                                f"{parameter_name}[{i}].",
                            )
                        )
                parameters[parameter_name] = param_val_arr

    def __construct_parameters(self, step: dict):
        try:
            method_name = step["method"]
            parameter_type_name = self._function_map[method_name]["details"]["parameters"]
            parameter_inputs = step["parameters"]
            parameters = self.__get_params(method_name, parameter_type_name, parameter_inputs, {})
            return parameters
        except Exception as e:
            self.__log_exception(
                _str(("Exception while evaluating parameters", f"in method '{method_name}'")),
                e,
                self.__collect_traceback(e),
            )
            return None

    def __execute_method(self, method: any, params: dict) -> bool:
        try:
            start_time = time.time()
            method(self._model, params, self._cached_data)
            end_time = time.time()
            measured_time = end_time - start_time
            time_mins = int(measured_time) // 60
            time_secs = int(measured_time) % 60
            if method.__name__ != "settings":
                if time_mins:
                    self._logger.info(f"    Elapsed time: {time_mins} mins {time_secs} seconds")
                else:
                    self._logger.info(f"    Elapsed time: {time_secs} seconds")
            '''
            else:
                if(params.get('verbosity')>0):
                    self._verbosity = params['verbosity']
            '''
            return True
        except Exception as e:
            self.__log_exception(
                f"Exception while executing method '{method.__name__}'",
                e,
                self.__collect_traceback(e),
            )
            return False

    def __write_intermediate(self, method_name: str):
        fileio = prime.FileIO(self._model)
        fileio.write_pmdat(method_name + ".pmdat", prime.FileWriteParams(self._model))

    def get_params(self, method_name: str, type_name: str, param_inputs: dict):
        """Parse params_input to construct parameters object depending upon type_name."""
        try:
            parameters = self.__get_params(method_name, type_name, param_inputs, {}, True)
            return parameters
        except Exception as e:
            self.__log_exception(
                str("Exception while evaluating parameters", f" in method '{method_name}'"),
                e,
                self.__collect_traceback(e),
            )
            return None

    def execute(self, method: str, params: Dict):
        """Execute numen method."""
        method = self._function_map[method]["function"]
        self.__execute_method(method, params)

    def run(self, steps: List[Dict]):
        """Run numen workflow."""
        try:

            if not isinstance(steps, list):
                raise TypeError("steps should be a list of dictionaries")

            self._param_defs.clear_overrides()

            for step in steps:
                if isinstance(step, list):
                    if not self.run(step):
                        return False
                    continue
                elif not isinstance(step, dict):
                    raise TypeError("Each step should be a dictionary")

                if "method" in step:
                    method_name = step["method"]
                    if "skip" in step and step["skip"]:
                        self._logger.warning(f"skipping method \"{method_name}\"...")
                        continue
                    if method_name not in self._function_map:
                        raise KeyError(f"Method '{method_name}' not found in function map")
                    method = self._function_map[method_name]["function"]
                    self._logger.info(f"Executing {method_name}")
                    params = self.__construct_parameters(step)
                    success = False
                    if params != None:
                        success = self.__execute_method(method, params)
                    if success and "write_file" in step and step["write_file"] == True:
                        self.__write_intermediate(method_name)
                    if not success:
                        raise Exception(f"Failed to execute {method_name}")
                else:
                    raise Exception("No method found in step")
            mem_stats = call_method(
                self._model, "PrimeMesh::Model/GetMemoryStatistics_Beta", self._model._object_id, {}
            )
            peak_memory = mem_stats["peakMemory"] / (1024 * 1024 * 1024)
            current_memory = mem_stats["currentMemory"] / (1024 * 1024 * 1024)
            self._logger.info(f"Current memory: {current_memory:.2f} GB")
            self._logger.info(f"Peak memory   : {peak_memory:.2f} GB")
            try:
                logger_info = json.loads(
                    call_method(
                        self._model,
                        "PrimeMesh::Model/GetChildObjectsJson",
                        self._model._object_id,
                        {},
                    )
                )
                call_method(self._model, "PrimeMesh::Logger/StopLogFile", logger_info["Logger"], {})
            except:
                pass
            return True
        except Exception as e:
            self.__log_exception("REPL run failed", e)
            return False

    def __get_default_val_for_type(self, type, range_val, param_name):
        parameter_type = self.__get_param_type(type)
        if parameter_type[0] == "int":
            return 1
        elif parameter_type[0] == "float":
            if param_name == "min_size":
                return 1.0
            elif param_name == "max_size":
                return 10.0
            else:
                return 5.0
        elif parameter_type[0] == "string":
            return "*"
        elif parameter_type[0] == "boolean":
            return True
        elif parameter_type[0] == "path":
            return "<file_path>"
        elif parameter_type[0] == "range":
            return range_val[0]
        elif parameter_type[0] == "list":
            if parameter_type[1] == "int" or parameter_type[1] == "float":
                return [1, 2]
            elif parameter_type[1] == "string":
                return ["val0", "val1"]
            elif parameter_type[1] == "boolean":
                return [True, False]
            elif parameter_type[1] == "path":
                return ["<file_path_1>", "<file_path_2>"]
            else:
                return [self.__get_help_parameters(parameter_type[1])]
        return None

    def __get_help_parameters(self, param_type_name):
        if param_type_name in self._param_map:
            params = self._param_map.get(param_type_name)
            param_details = {}
            for param in params:
                param_name = param["name"]
                if param_name.startswith("_"):
                    continue
                param_default = None
                if "default" in param and param["default"] != []:
                    param_default = evaluate_expression(self._param_defs, {}, param["default"])
                else:
                    range_val = []
                    if "range" in param:
                        range_val = param["range"]
                    param_default = self.__get_default_val_for_type(
                        param["type"], range_val, param_name
                    )
                param_details[param_name] = param_default
            return param_details
        return None

    def help(self, arg=None):
        """Print help on numen methods."""
        help_str = _str(
            (
                "Access help with one of the following arguments:\n",
                "   methods\n",
                "   method:<method name>",
            )
        )
        if arg == None:
            print(help_str)
        elif arg.strip() == "methods":
            methods = self._function_map.keys()
            print("\n".join(methods))
        elif re.match(r"^method\s*:", arg.strip()):
            self._param_defs.push_override_for_global(
                {"min_size": 1.0, "max_size": 10.0, "growth_rate": 1.2}
            )
            method_name = arg.split(":", 1)[1].strip()
            if method_name in self._function_map:
                method_details = self._function_map[method_name]["details"]
                method_details_copy = {}
                method_details_copy["name"] = method_details["name"]
                method_details_copy["method"] = method_details["method"]
                method_details_copy["parameters"] = self.__get_help_parameters(
                    method_details["parameters"]
                )
                print(json.dumps(method_details_copy, indent=4))
            else:
                print(f"Method \"{method_name}\" not found")
            self._param_defs.pop_override()
        else:
            print(help_str)

    def is_param_enabled(
        self, method_name: str, type_name: str, parameter_name: str, parameters: Dict
    ) -> bool:
        """Check if parameter is enabled or not."""
        return self.__is_param_enabled(method_name, type_name, parameter_name, parameters)

    def test(self, arg=None):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        test_folder = os.path.join(current_directory, "test")
        for filename in os.listdir(test_folder):
            if filename.endswith(".json"):
                file_path = os.path.join(test_folder, filename)
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    for entry in data:
                        if 'cwd' in entry['parameters']:
                            updated_path = os.path.join(test_folder, entry['parameters']['cwd'])
                            entry['parameters']['cwd'] = os.path.normpath(updated_path)
                    self.run(data)

    def _setup_logging(self, custom_level):
        level_mapping = {
            -2: logging.CRITICAL,
            -1: logging.ERROR,
            0: logging.WARNING,
            1: logging.INFO,
            2: logging.DEBUG,
        }
        self._verbosity = custom_level
        level = level_mapping.get(custom_level, logging.WARNING)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(level=level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(level)
        self._logger.propagate = False
