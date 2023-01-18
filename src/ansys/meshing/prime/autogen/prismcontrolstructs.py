""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class PrismControlOffsetType(enum.IntEnum):
    """Offset type for prism control.
    """
    UNIFORM = 0
    """Option to grow prism layers with uniform offset height based on first height."""
    ASPECTRATIO = 1
    """Option to grow prism layers based on first aspect ratio specified."""
    LASTRATIO = 2
    """Option to grow prism layers based on first height and last aspect ratio."""

class PrismControlGrowthParams(CoreObject):
    """Growth parameters for prism control.
    """
    _default_params = {}

    def __initialize(
            self,
            offset_type: PrismControlOffsetType,
            n_layers: int,
            growth_rate: float,
            first_height: float,
            first_aspect_ratio: float,
            last_aspect_ratio: float,
            min_aspect_ratio: float):
        self._offset_type = PrismControlOffsetType(offset_type)
        self._n_layers = n_layers
        self._growth_rate = growth_rate
        self._first_height = first_height
        self._first_aspect_ratio = first_aspect_ratio
        self._last_aspect_ratio = last_aspect_ratio
        self._min_aspect_ratio = min_aspect_ratio

    def __init__(
            self,
            model: CommunicationManager=None,
            offset_type: PrismControlOffsetType = None,
            n_layers: int = None,
            growth_rate: float = None,
            first_height: float = None,
            first_aspect_ratio: float = None,
            last_aspect_ratio: float = None,
            min_aspect_ratio: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the PrismControlGrowthParams.

        Parameters
        ----------
        model: Model
            Model to create a PrismControlGrowthParams object with default parameters.
        offset_type: PrismControlOffsetType, optional
            Offset type controls the method that is used to compute prism layer heights. The following options are supported.The aspect ratio option takes first aspect ratio, number of layers and growth rate. It ignores first height as input.The uniform option takes first height, number of layers and growth rate. It ignores first aspect ratio as input.Aspect ratio is ratio of prism base to height.
        n_layers: int, optional
            Number of prism layers to be generated. It is used for all prism control offset types.
        growth_rate: float, optional
            Growth rate to be used to compute prism layer heights. It is used when prism control offset type is ASPECTRATIO or UNIFORM.
        first_height: float, optional
            Height to be used for first layer and adjust following layer height based on other settings. It is used when prism control offset type is UNIFORM.
        first_aspect_ratio: float, optional
            Aspect ratio to be used to compute first layer height. It is used only when prism control offset type is ASPECTRATIO.
        last_aspect_ratio: float, optional
            Apsect ratio of the last layer. The heights of the other layers is computed based on number of layers and first height. This is used only when prism control offset type is LASTRATIO.
        min_aspect_ratio: float, optional
            Minimum apsect ratio limit to be used for all the layers. This condition is respected in all offset types.
        json_data: dict, optional
            JSON dictionary to create a PrismControlGrowthParams object with provided parameters.

        Examples
        --------
        >>> prism_control_growth_params = prime.PrismControlGrowthParams(model = model)
        """
        if json_data:
            self.__initialize(
                PrismControlOffsetType(json_data["offsetType"] if "offsetType" in json_data else None),
                json_data["nLayers"] if "nLayers" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["firstHeight"] if "firstHeight" in json_data else None,
                json_data["firstAspectRatio"] if "firstAspectRatio" in json_data else None,
                json_data["lastAspectRatio"] if "lastAspectRatio" in json_data else None,
                json_data["minAspectRatio"] if "minAspectRatio" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [offset_type, n_layers, growth_rate, first_height, first_aspect_ratio, last_aspect_ratio, min_aspect_ratio])
            if all_field_specified:
                self.__initialize(
                    offset_type,
                    n_layers,
                    growth_rate,
                    first_height,
                    first_aspect_ratio,
                    last_aspect_ratio,
                    min_aspect_ratio)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "PrismControlGrowthParams")
                    json_data = param_json["PrismControlGrowthParams"] if "PrismControlGrowthParams" in param_json else {}
                    self.__initialize(
                        offset_type if offset_type is not None else ( PrismControlGrowthParams._default_params["offset_type"] if "offset_type" in PrismControlGrowthParams._default_params else PrismControlOffsetType(json_data["offsetType"] if "offsetType" in json_data else None)),
                        n_layers if n_layers is not None else ( PrismControlGrowthParams._default_params["n_layers"] if "n_layers" in PrismControlGrowthParams._default_params else (json_data["nLayers"] if "nLayers" in json_data else None)),
                        growth_rate if growth_rate is not None else ( PrismControlGrowthParams._default_params["growth_rate"] if "growth_rate" in PrismControlGrowthParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        first_height if first_height is not None else ( PrismControlGrowthParams._default_params["first_height"] if "first_height" in PrismControlGrowthParams._default_params else (json_data["firstHeight"] if "firstHeight" in json_data else None)),
                        first_aspect_ratio if first_aspect_ratio is not None else ( PrismControlGrowthParams._default_params["first_aspect_ratio"] if "first_aspect_ratio" in PrismControlGrowthParams._default_params else (json_data["firstAspectRatio"] if "firstAspectRatio" in json_data else None)),
                        last_aspect_ratio if last_aspect_ratio is not None else ( PrismControlGrowthParams._default_params["last_aspect_ratio"] if "last_aspect_ratio" in PrismControlGrowthParams._default_params else (json_data["lastAspectRatio"] if "lastAspectRatio" in json_data else None)),
                        min_aspect_ratio if min_aspect_ratio is not None else ( PrismControlGrowthParams._default_params["min_aspect_ratio"] if "min_aspect_ratio" in PrismControlGrowthParams._default_params else (json_data["minAspectRatio"] if "minAspectRatio" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            offset_type: PrismControlOffsetType = None,
            n_layers: int = None,
            growth_rate: float = None,
            first_height: float = None,
            first_aspect_ratio: float = None,
            last_aspect_ratio: float = None,
            min_aspect_ratio: float = None):
        """Set the default values of PrismControlGrowthParams.

        Parameters
        ----------
        offset_type: PrismControlOffsetType, optional
            Offset type controls the method that is used to compute prism layer heights. The following options are supported.The aspect ratio option takes first aspect ratio, number of layers and growth rate. It ignores first height as input.The uniform option takes first height, number of layers and growth rate. It ignores first aspect ratio as input.Aspect ratio is ratio of prism base to height.
        n_layers: int, optional
            Number of prism layers to be generated. It is used for all prism control offset types.
        growth_rate: float, optional
            Growth rate to be used to compute prism layer heights. It is used when prism control offset type is ASPECTRATIO or UNIFORM.
        first_height: float, optional
            Height to be used for first layer and adjust following layer height based on other settings. It is used when prism control offset type is UNIFORM.
        first_aspect_ratio: float, optional
            Aspect ratio to be used to compute first layer height. It is used only when prism control offset type is ASPECTRATIO.
        last_aspect_ratio: float, optional
            Apsect ratio of the last layer. The heights of the other layers is computed based on number of layers and first height. This is used only when prism control offset type is LASTRATIO.
        min_aspect_ratio: float, optional
            Minimum apsect ratio limit to be used for all the layers. This condition is respected in all offset types.
        """
        args = locals()
        [PrismControlGrowthParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of PrismControlGrowthParams.

        Examples
        --------
        >>> PrismControlGrowthParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PrismControlGrowthParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._offset_type is not None:
            json_data["offsetType"] = self._offset_type
        if self._n_layers is not None:
            json_data["nLayers"] = self._n_layers
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._first_height is not None:
            json_data["firstHeight"] = self._first_height
        if self._first_aspect_ratio is not None:
            json_data["firstAspectRatio"] = self._first_aspect_ratio
        if self._last_aspect_ratio is not None:
            json_data["lastAspectRatio"] = self._last_aspect_ratio
        if self._min_aspect_ratio is not None:
            json_data["minAspectRatio"] = self._min_aspect_ratio
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "offset_type :  %s\nn_layers :  %s\ngrowth_rate :  %s\nfirst_height :  %s\nfirst_aspect_ratio :  %s\nlast_aspect_ratio :  %s\nmin_aspect_ratio :  %s" % (self._offset_type, self._n_layers, self._growth_rate, self._first_height, self._first_aspect_ratio, self._last_aspect_ratio, self._min_aspect_ratio)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def offset_type(self) -> PrismControlOffsetType:
        """Offset type controls the method that is used to compute prism layer heights. The following options are supported.The aspect ratio option takes first aspect ratio, number of layers and growth rate. It ignores first height as input.The uniform option takes first height, number of layers and growth rate. It ignores first aspect ratio as input.Aspect ratio is ratio of prism base to height.
        """
        return self._offset_type

    @offset_type.setter
    def offset_type(self, value: PrismControlOffsetType):
        self._offset_type = value

    @property
    def n_layers(self) -> int:
        """Number of prism layers to be generated. It is used for all prism control offset types.
        """
        return self._n_layers

    @n_layers.setter
    def n_layers(self, value: int):
        self._n_layers = value

    @property
    def growth_rate(self) -> float:
        """Growth rate to be used to compute prism layer heights. It is used when prism control offset type is ASPECTRATIO or UNIFORM.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def first_height(self) -> float:
        """Height to be used for first layer and adjust following layer height based on other settings. It is used when prism control offset type is UNIFORM.
        """
        return self._first_height

    @first_height.setter
    def first_height(self, value: float):
        self._first_height = value

    @property
    def first_aspect_ratio(self) -> float:
        """Aspect ratio to be used to compute first layer height. It is used only when prism control offset type is ASPECTRATIO.
        """
        return self._first_aspect_ratio

    @first_aspect_ratio.setter
    def first_aspect_ratio(self, value: float):
        self._first_aspect_ratio = value

    @property
    def last_aspect_ratio(self) -> float:
        """Apsect ratio of the last layer. The heights of the other layers is computed based on number of layers and first height. This is used only when prism control offset type is LASTRATIO.
        """
        return self._last_aspect_ratio

    @last_aspect_ratio.setter
    def last_aspect_ratio(self, value: float):
        self._last_aspect_ratio = value

    @property
    def min_aspect_ratio(self) -> float:
        """Minimum apsect ratio limit to be used for all the layers. This condition is respected in all offset types.
        """
        return self._min_aspect_ratio

    @min_aspect_ratio.setter
    def min_aspect_ratio(self, value: float):
        self._min_aspect_ratio = value
