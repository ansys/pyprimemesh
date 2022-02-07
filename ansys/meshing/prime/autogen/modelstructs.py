""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, List
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *

from ansys.meshing.prime.params.primestructs import *

class GlobalSizingParams(CoreObject):
    """Global sizing parameters.
    """
    _default_params = {}

    def __initialize(
            self,
            min: float,
            max: float,
            growth_rate: float):
        self._min = min
        self._max = max
        self._growth_rate = growth_rate

    def __init__(
            self,
            model: CommunicationManager=None,
            min: float = None,
            max: float = None,
            growth_rate: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the GlobalSizingParams.

        Parameters
        ----------
        model: Model
            Model to create a GlobalSizingParams object with default parameters.
        min: float, optional
            Minimum value of global sizing parameters.
        max: float, optional
            Maximum value of global sizing parameters.
        growth_rate: float, optional
            Growth rate of global sizing parameters.
        json_data: dict, optional
            JSON dictionary to create a GlobalSizingParams object with provided parameters.

        Examples
        --------
        >>> global_sizing_params = prime.GlobalSizingParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["min"],
                json_data["max"],
                json_data["growthRate"])
        else:
            all_field_specified = all(arg is not None for arg in [min, max, growth_rate])
            if all_field_specified:
                self.__initialize(
                    min,
                    max,
                    growth_rate)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    json_data = model._communicator.initialize_params("GlobalSizingParams")["GlobalSizingParams"]
                    self.__initialize(
                        min if min is not None else ( GlobalSizingParams._default_params["min"] if "min" in GlobalSizingParams._default_params else json_data["min"]),
                        max if max is not None else ( GlobalSizingParams._default_params["max"] if "max" in GlobalSizingParams._default_params else json_data["max"]),
                        growth_rate if growth_rate is not None else ( GlobalSizingParams._default_params["growth_rate"] if "growth_rate" in GlobalSizingParams._default_params else json_data["growthRate"]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min: float = None,
            max: float = None,
            growth_rate: float = None):
        """Sets the default values of GlobalSizingParams.

        Parameters
        ----------
        min: float, optional
            Minimum value of global sizing parameters.
        max: float, optional
            Maximum value of global sizing parameters.
        growth_rate: float, optional
            Growth rate of global sizing parameters.
        """
        args = locals()
        [GlobalSizingParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Prints the default values of GlobalSizingParams.

        Examples
        --------
        >>> GlobalSizingParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in GlobalSizingParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        json_data["min"] = self._min
        json_data["max"] = self._max
        json_data["growthRate"] = self._growth_rate
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min :  %s\nmax :  %s\ngrowth_rate :  %s" % (self._min, self._max, self._growth_rate)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min(self) -> float:
        """Minimum value of global sizing parameters.
        """
        return self._min

    @min.setter
    def min(self, value: float):
        self._min = value

    @property
    def max(self) -> float:
        """Maximum value of global sizing parameters.
        """
        return self._max

    @max.setter
    def max(self, value: float):
        self._max = value

    @property
    def growth_rate(self) -> float:
        """Growth rate of global sizing parameters.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value
