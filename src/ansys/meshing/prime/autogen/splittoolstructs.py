""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class SplitParams(CoreObject):
    """Parameters to split face elements at longest edge.
    """
    _default_params = {}

    def __initialize(
            self,
            split_ratio: float):
        self._split_ratio = split_ratio

    def __init__(
            self,
            model: CommunicationManager=None,
            split_ratio: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the SplitParams.

        Parameters
        ----------
        model: Model
            Model to create a SplitParams object with default parameters.
        split_ratio: float, optional
            Minimum ratio of split edge length to original edge length.
        json_data: dict, optional
            JSON dictionary to create a SplitParams object with provided parameters.

        Examples
        --------
        >>> split_params = prime.SplitParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["splitRatio"] if "splitRatio" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [split_ratio])
            if all_field_specified:
                self.__initialize(
                    split_ratio)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "SplitParams")
                    json_data = param_json["SplitParams"] if "SplitParams" in param_json else {}
                    self.__initialize(
                        split_ratio if split_ratio is not None else ( SplitParams._default_params["split_ratio"] if "split_ratio" in SplitParams._default_params else (json_data["splitRatio"] if "splitRatio" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            split_ratio: float = None):
        """Set the default values of SplitParams.

        Parameters
        ----------
        split_ratio: float, optional
            Minimum ratio of split edge length to original edge length.
        """
        args = locals()
        [SplitParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of SplitParams.

        Examples
        --------
        >>> SplitParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SplitParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._split_ratio is not None:
            json_data["splitRatio"] = self._split_ratio
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "split_ratio :  %s" % (self._split_ratio)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def split_ratio(self) -> float:
        """Minimum ratio of split edge length to original edge length.
        """
        return self._split_ratio

    @split_ratio.setter
    def split_ratio(self, value: float):
        self._split_ratio = value
