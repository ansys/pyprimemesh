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

from ansys.meshing import prime


class ParamDefs:
    def __init__(self, model: prime.Model):
        self._model = model
        self._params = {
            "global.min_size": self.__global_min_size,
            "global.max_size": self.__global_max_size,
            "global.growth_rate": self.__global_growth_rate,
        }
        self._overrides = []

    def get(self, param_name: str):
        if len(self._overrides) > 0 and param_name in self._overrides[0]:
            result = self._overrides[0][param_name]
            if callable(result):
                return result()
            else:
                return result
        elif param_name in self._params:
            result = self._params[param_name]
            if callable(result):
                return result()
            else:
                return result
        RuntimeError(f"Parameter '{param_name}' not defined")
        return None

    def push_override(self, override):
        self._overrides.insert(0, override)

    def pop_override(self):
        if len(self._overrides) > 0:
            self._overrides.pop(0)

    def clear_overrides(self):
        self._overrides.clear()

    def push_override_for_global(self, override: dict):
        global_overrides = {}
        for key, value in override.items():
            global_overrides["global." + key] = value
        self.push_override(global_overrides)

    def __global_min_size(self):
        gs_params = self._model.get_global_sizing_params()
        return gs_params.min

    def __global_max_size(self):
        gs_params = self._model.get_global_sizing_params()
        return gs_params.max

    def __global_growth_rate(self):
        gs_params = self._model.get_global_sizing_params()
        return gs_params.growth_rate
