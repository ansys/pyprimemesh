from ansys.meshing import prime

class ParamDefs():
    def __init__(self, model: prime.Model):
        self._model = model
        self._params = {
            "global.min_size": self.__global_min_size,
            "global.max_size": self.__global_max_size,
            "global.growth_rate": self.__global_growth_rate
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
