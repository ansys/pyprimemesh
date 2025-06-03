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

""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class ShellBLControlGrowthParams(CoreObject):
    """Growth parameters for ShellBL control.

    Parameters
    ----------
    model: Model
        Model to create a ``ShellBLControlGrowthParams`` object with default parameters.
    n_layers: int, optional
        Number of layers to be generated.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    offset_type: ShellBLOffsetType, optional
        Offset type for ShellBL.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    growth_rate: float, optional
        Ratio of height of the current layer to the previous layer.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    first_height: float, optional
        Height of first layer of ShellBL.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ShellBLControlGrowthParams`` object with provided parameters.

    Examples
    --------
    >>> shell_bl_control_growth_params = prime.ShellBLControlGrowthParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            n_layers: int,
            offset_type: ShellBLOffsetType,
            growth_rate: float,
            first_height: float):
        self._n_layers = n_layers
        self._offset_type = ShellBLOffsetType(offset_type)
        self._growth_rate = growth_rate
        self._first_height = first_height

    def __init__(
            self,
            model: CommunicationManager=None,
            n_layers: int = None,
            offset_type: ShellBLOffsetType = None,
            growth_rate: float = None,
            first_height: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ShellBLControlGrowthParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ShellBLControlGrowthParams`` object with default parameters.
        n_layers: int, optional
            Number of layers to be generated.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        offset_type: ShellBLOffsetType, optional
            Offset type for ShellBL.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        growth_rate: float, optional
            Ratio of height of the current layer to the previous layer.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        first_height: float, optional
            Height of first layer of ShellBL.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ShellBLControlGrowthParams`` object with provided parameters.

        Examples
        --------
        >>> shell_bl_control_growth_params = prime.ShellBLControlGrowthParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nLayers"] if "nLayers" in json_data else None,
                ShellBLOffsetType(json_data["offsetType"] if "offsetType" in json_data else None),
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["firstHeight"] if "firstHeight" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [n_layers, offset_type, growth_rate, first_height])
            if all_field_specified:
                self.__initialize(
                    n_layers,
                    offset_type,
                    growth_rate,
                    first_height)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ShellBLControlGrowthParams")
                    json_data = param_json["ShellBLControlGrowthParams"] if "ShellBLControlGrowthParams" in param_json else {}
                    self.__initialize(
                        n_layers if n_layers is not None else ( ShellBLControlGrowthParams._default_params["n_layers"] if "n_layers" in ShellBLControlGrowthParams._default_params else (json_data["nLayers"] if "nLayers" in json_data else None)),
                        offset_type if offset_type is not None else ( ShellBLControlGrowthParams._default_params["offset_type"] if "offset_type" in ShellBLControlGrowthParams._default_params else ShellBLOffsetType(json_data["offsetType"] if "offsetType" in json_data else None)),
                        growth_rate if growth_rate is not None else ( ShellBLControlGrowthParams._default_params["growth_rate"] if "growth_rate" in ShellBLControlGrowthParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        first_height if first_height is not None else ( ShellBLControlGrowthParams._default_params["first_height"] if "first_height" in ShellBLControlGrowthParams._default_params else (json_data["firstHeight"] if "firstHeight" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_layers: int = None,
            offset_type: ShellBLOffsetType = None,
            growth_rate: float = None,
            first_height: float = None):
        """Set the default values of the ``ShellBLControlGrowthParams`` object.

        Parameters
        ----------
        n_layers: int, optional
            Number of layers to be generated.
        offset_type: ShellBLOffsetType, optional
            Offset type for ShellBL.
        growth_rate: float, optional
            Ratio of height of the current layer to the previous layer.
        first_height: float, optional
            Height of first layer of ShellBL.
        """
        args = locals()
        [ShellBLControlGrowthParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ShellBLControlGrowthParams`` object.

        Examples
        --------
        >>> ShellBLControlGrowthParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ShellBLControlGrowthParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_layers is not None:
            json_data["nLayers"] = self._n_layers
        if self._offset_type is not None:
            json_data["offsetType"] = self._offset_type
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._first_height is not None:
            json_data["firstHeight"] = self._first_height
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_layers :  %s\noffset_type :  %s\ngrowth_rate :  %s\nfirst_height :  %s" % (self._n_layers, self._offset_type, self._growth_rate, self._first_height)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_layers(self) -> int:
        """Number of layers to be generated.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._n_layers

    @n_layers.setter
    def n_layers(self, value: int):
        self._n_layers = value

    @property
    def offset_type(self) -> ShellBLOffsetType:
        """Offset type for ShellBL.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._offset_type

    @offset_type.setter
    def offset_type(self, value: ShellBLOffsetType):
        self._offset_type = value

    @property
    def growth_rate(self) -> float:
        """Ratio of height of the current layer to previous layer.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def first_height(self) -> float:
        """Height of first layer of ShellBL.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._first_height

    @first_height.setter
    def first_height(self, value: float):
        self._first_height = value
