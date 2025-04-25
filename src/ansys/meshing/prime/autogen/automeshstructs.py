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

class VolumeFillType(enum.IntEnum):
    """Types of volume fill options.
    """
    TET = 0
    """Volume fill using tetrahedral cells."""
    POLY = 1
    """Volume fill using polyhedral cells."""
    HEXCORETET = 2
    """Volume fill using hexahedral cells in the core and tetrahedral cells near the boundary."""
    HEXCOREPOLY = 3
    """Volume fill using hexahedral cells in the core and polyhedral cells near the boundary."""

class HexCoreCellElementType(enum.IntEnum):
    """Cell element type of hex-shaped cells.
    """
    ALLPOLY = 0
    """Generates poly type cells."""
    ALLHEX = 1
    """Generates hex type cells."""
    HEXANDPOLY = 2
    """Generates a mix of poly type and hex type cells."""

class HexCoreTransitionLayerType(enum.IntEnum):
    """Handle size transition of hex cells.
    """
    HANGINGNODES = 0
    """Allow different size hexes to be neighbors."""
    DELETESMALL = 1
    """Remove neighboring hexes of different size by deleting a layer of smaller cells. The voids are filled with tetrahedral or polyhedral cells depending on volumeFillType in AutoMeshParams structure."""
    DELETELARGE = 2
    """Remove neighboring hexes of different size by deleting a layer of larger cells. The voids are filled with tetrahedral or polyhedral cells depending on volumeFillType in AutoMeshParams structure."""
    DELETEBOTH = 3
    """Remove neighboring hexes of different size by deleting both smaller and larger cell layers. The voids are filled with tetrahedral or polyhedral cells depending on volumeFillType in AutoMeshParams structure."""

class AutoMeshResults(CoreObject):
    """Results of volume meshing.

    Parameters
    ----------
    model: Model
        Model to create a ``AutoMeshResults`` object with default parameters.
    error_code: ErrorCode, optional
        Provides error message when automesh fails.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.
    error_locations: Iterable[float], optional
        Error location coordinates returned when automesh fails.
    json_data: dict, optional
        JSON dictionary to create a ``AutoMeshResults`` object with provided parameters.

    Examples
    --------
    >>> auto_mesh_results = prime.AutoMeshResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode],
            error_locations: Iterable[float]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes
        self._error_locations = error_locations if isinstance(error_locations, np.ndarray) else np.array(error_locations, dtype=np.double) if error_locations is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            error_locations: Iterable[float] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``AutoMeshResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``AutoMeshResults`` object with default parameters.
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        error_locations: Iterable[float], optional
            Error location coordinates returned when automesh fails.
        json_data: dict, optional
            JSON dictionary to create a ``AutoMeshResults`` object with provided parameters.

        Examples
        --------
        >>> auto_mesh_results = prime.AutoMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                json_data["errorLocations"] if "errorLocations" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes, error_locations])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes,
                    error_locations)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "AutoMeshResults")
                    json_data = param_json["AutoMeshResults"] if "AutoMeshResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( AutoMeshResults._default_params["error_code"] if "error_code" in AutoMeshResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( AutoMeshResults._default_params["warning_codes"] if "warning_codes" in AutoMeshResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        error_locations if error_locations is not None else ( AutoMeshResults._default_params["error_locations"] if "error_locations" in AutoMeshResults._default_params else (json_data["errorLocations"] if "errorLocations" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            error_locations: Iterable[float] = None):
        """Set the default values of the ``AutoMeshResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Provides error message when automesh fails.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        error_locations: Iterable[float], optional
            Error location coordinates returned when automesh fails.
        """
        args = locals()
        [AutoMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``AutoMeshResults`` object.

        Examples
        --------
        >>> AutoMeshResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoMeshResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._error_locations is not None:
            json_data["errorLocations"] = self._error_locations
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s\nerror_locations :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._error_locations)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Provides error message when automesh fails.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def error_locations(self) -> Iterable[float]:
        """Error location coordinates returned when automesh fails.
        """
        return self._error_locations

    @error_locations.setter
    def error_locations(self, value: Iterable[float]):
        self._error_locations = value

class PrismStairStep(CoreObject):
    """Parameters to control prism stairsteping.

    Parameters
    ----------
    model: Model
        Model to create a ``PrismStairStep`` object with default parameters.
    check_proximity: bool, optional
        Check whether to enable or disable stairstepping at prisms within proximity of boundary or prism cap.
    gap_factor_scale: float, optional
        Scale factor for prism proximity detection gap factor.
    json_data: dict, optional
        JSON dictionary to create a ``PrismStairStep`` object with provided parameters.

    Examples
    --------
    >>> prism_stair_step = prime.PrismStairStep(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            check_proximity: bool,
            gap_factor_scale: float):
        self._check_proximity = check_proximity
        self._gap_factor_scale = gap_factor_scale

    def __init__(
            self,
            model: CommunicationManager=None,
            check_proximity: bool = None,
            gap_factor_scale: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``PrismStairStep`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``PrismStairStep`` object with default parameters.
        check_proximity: bool, optional
            Check whether to enable or disable stairstepping at prisms within proximity of boundary or prism cap.
        gap_factor_scale: float, optional
            Scale factor for prism proximity detection gap factor.
        json_data: dict, optional
            JSON dictionary to create a ``PrismStairStep`` object with provided parameters.

        Examples
        --------
        >>> prism_stair_step = prime.PrismStairStep(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["checkProximity"] if "checkProximity" in json_data else None,
                json_data["gapFactorScale"] if "gapFactorScale" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [check_proximity, gap_factor_scale])
            if all_field_specified:
                self.__initialize(
                    check_proximity,
                    gap_factor_scale)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "PrismStairStep")
                    json_data = param_json["PrismStairStep"] if "PrismStairStep" in param_json else {}
                    self.__initialize(
                        check_proximity if check_proximity is not None else ( PrismStairStep._default_params["check_proximity"] if "check_proximity" in PrismStairStep._default_params else (json_data["checkProximity"] if "checkProximity" in json_data else None)),
                        gap_factor_scale if gap_factor_scale is not None else ( PrismStairStep._default_params["gap_factor_scale"] if "gap_factor_scale" in PrismStairStep._default_params else (json_data["gapFactorScale"] if "gapFactorScale" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            check_proximity: bool = None,
            gap_factor_scale: float = None):
        """Set the default values of the ``PrismStairStep`` object.

        Parameters
        ----------
        check_proximity: bool, optional
            Check whether to enable or disable stairstepping at prisms within proximity of boundary or prism cap.
        gap_factor_scale: float, optional
            Scale factor for prism proximity detection gap factor.
        """
        args = locals()
        [PrismStairStep._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``PrismStairStep`` object.

        Examples
        --------
        >>> PrismStairStep.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PrismStairStep._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._check_proximity is not None:
            json_data["checkProximity"] = self._check_proximity
        if self._gap_factor_scale is not None:
            json_data["gapFactorScale"] = self._gap_factor_scale
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "check_proximity :  %s\ngap_factor_scale :  %s" % (self._check_proximity, self._gap_factor_scale)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def check_proximity(self) -> bool:
        """Check whether to enable or disable stairstepping at prisms within proximity of boundary or prism cap.
        """
        return self._check_proximity

    @check_proximity.setter
    def check_proximity(self, value: bool):
        self._check_proximity = value

    @property
    def gap_factor_scale(self) -> float:
        """Scale factor for prism proximity detection gap factor.
        """
        return self._gap_factor_scale

    @gap_factor_scale.setter
    def gap_factor_scale(self, value: float):
        self._gap_factor_scale = value

class PrismParams(CoreObject):
    """Parameters to control prism mesh generation.

    Parameters
    ----------
    model: Model
        Model to create a ``PrismParams`` object with default parameters.
    stair_step: PrismStairStep, optional
        Prism stairstep parameters.
    no_imprint_zonelets: Iterable[int], optional
        Option to specify zonelets to skip prism imprint.
    json_data: dict, optional
        JSON dictionary to create a ``PrismParams`` object with provided parameters.

    Examples
    --------
    >>> prism_params = prime.PrismParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            stair_step: PrismStairStep,
            no_imprint_zonelets: Iterable[int]):
        self._stair_step = stair_step
        self._no_imprint_zonelets = no_imprint_zonelets if isinstance(no_imprint_zonelets, np.ndarray) else np.array(no_imprint_zonelets, dtype=np.int32) if no_imprint_zonelets is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            stair_step: PrismStairStep = None,
            no_imprint_zonelets: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``PrismParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``PrismParams`` object with default parameters.
        stair_step: PrismStairStep, optional
            Prism stairstep parameters.
        no_imprint_zonelets: Iterable[int], optional
            Option to specify zonelets to skip prism imprint.
        json_data: dict, optional
            JSON dictionary to create a ``PrismParams`` object with provided parameters.

        Examples
        --------
        >>> prism_params = prime.PrismParams(model = model)
        """
        if json_data:
            self.__initialize(
                PrismStairStep(model = model, json_data = json_data["stairStep"] if "stairStep" in json_data else None),
                json_data["noImprintZonelets"] if "noImprintZonelets" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [stair_step, no_imprint_zonelets])
            if all_field_specified:
                self.__initialize(
                    stair_step,
                    no_imprint_zonelets)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "PrismParams")
                    json_data = param_json["PrismParams"] if "PrismParams" in param_json else {}
                    self.__initialize(
                        stair_step if stair_step is not None else ( PrismParams._default_params["stair_step"] if "stair_step" in PrismParams._default_params else PrismStairStep(model = model, json_data = (json_data["stairStep"] if "stairStep" in json_data else None))),
                        no_imprint_zonelets if no_imprint_zonelets is not None else ( PrismParams._default_params["no_imprint_zonelets"] if "no_imprint_zonelets" in PrismParams._default_params else (json_data["noImprintZonelets"] if "noImprintZonelets" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            stair_step: PrismStairStep = None,
            no_imprint_zonelets: Iterable[int] = None):
        """Set the default values of the ``PrismParams`` object.

        Parameters
        ----------
        stair_step: PrismStairStep, optional
            Prism stairstep parameters.
        no_imprint_zonelets: Iterable[int], optional
            Option to specify zonelets to skip prism imprint.
        """
        args = locals()
        [PrismParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``PrismParams`` object.

        Examples
        --------
        >>> PrismParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PrismParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._stair_step is not None:
            json_data["stairStep"] = self._stair_step._jsonify()
        if self._no_imprint_zonelets is not None:
            json_data["noImprintZonelets"] = self._no_imprint_zonelets
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "stair_step :  %s\nno_imprint_zonelets :  %s" % ('{ ' + str(self._stair_step) + ' }', self._no_imprint_zonelets)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def stair_step(self) -> PrismStairStep:
        """Prism stairstep parameters.
        """
        return self._stair_step

    @stair_step.setter
    def stair_step(self, value: PrismStairStep):
        self._stair_step = value

    @property
    def no_imprint_zonelets(self) -> Iterable[int]:
        """Option to specify zonelets to skip prism imprint.
        """
        return self._no_imprint_zonelets

    @no_imprint_zonelets.setter
    def no_imprint_zonelets(self, value: Iterable[int]):
        self._no_imprint_zonelets = value

class SurfaceMeshSizeScaling(CoreObject):
    """Settings related to scaling of surface mesh size for hexcore refinement.

    Parameters
    ----------
    model: Model
        Model to create a ``SurfaceMeshSizeScaling`` object with default parameters.
    factor: float, optional
        Value by which size should be multiplied when the size falls within a certain range. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
    size_range_min: float, optional
        Minimum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
    size_range_max: float, optional
        Maximum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
    json_data: dict, optional
        JSON dictionary to create a ``SurfaceMeshSizeScaling`` object with provided parameters.

    Examples
    --------
    >>> surface_mesh_size_scaling = prime.SurfaceMeshSizeScaling(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            factor: float,
            size_range_min: float,
            size_range_max: float):
        self._factor = factor
        self._size_range_min = size_range_min
        self._size_range_max = size_range_max

    def __init__(
            self,
            model: CommunicationManager=None,
            factor: float = None,
            size_range_min: float = None,
            size_range_max: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SurfaceMeshSizeScaling`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``SurfaceMeshSizeScaling`` object with default parameters.
        factor: float, optional
            Value by which size should be multiplied when the size falls within a certain range. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        size_range_min: float, optional
            Minimum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        size_range_max: float, optional
            Maximum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        json_data: dict, optional
            JSON dictionary to create a ``SurfaceMeshSizeScaling`` object with provided parameters.

        Examples
        --------
        >>> surface_mesh_size_scaling = prime.SurfaceMeshSizeScaling(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["factor"] if "factor" in json_data else None,
                json_data["sizeRangeMin"] if "sizeRangeMin" in json_data else None,
                json_data["sizeRangeMax"] if "sizeRangeMax" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [factor, size_range_min, size_range_max])
            if all_field_specified:
                self.__initialize(
                    factor,
                    size_range_min,
                    size_range_max)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SurfaceMeshSizeScaling")
                    json_data = param_json["SurfaceMeshSizeScaling"] if "SurfaceMeshSizeScaling" in param_json else {}
                    self.__initialize(
                        factor if factor is not None else ( SurfaceMeshSizeScaling._default_params["factor"] if "factor" in SurfaceMeshSizeScaling._default_params else (json_data["factor"] if "factor" in json_data else None)),
                        size_range_min if size_range_min is not None else ( SurfaceMeshSizeScaling._default_params["size_range_min"] if "size_range_min" in SurfaceMeshSizeScaling._default_params else (json_data["sizeRangeMin"] if "sizeRangeMin" in json_data else None)),
                        size_range_max if size_range_max is not None else ( SurfaceMeshSizeScaling._default_params["size_range_max"] if "size_range_max" in SurfaceMeshSizeScaling._default_params else (json_data["sizeRangeMax"] if "sizeRangeMax" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            factor: float = None,
            size_range_min: float = None,
            size_range_max: float = None):
        """Set the default values of the ``SurfaceMeshSizeScaling`` object.

        Parameters
        ----------
        factor: float, optional
            Value by which size should be multiplied when the size falls within a certain range. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        size_range_min: float, optional
            Minimum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        size_range_max: float, optional
            Maximum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        """
        args = locals()
        [SurfaceMeshSizeScaling._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SurfaceMeshSizeScaling`` object.

        Examples
        --------
        >>> SurfaceMeshSizeScaling.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurfaceMeshSizeScaling._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._factor is not None:
            json_data["factor"] = self._factor
        if self._size_range_min is not None:
            json_data["sizeRangeMin"] = self._size_range_min
        if self._size_range_max is not None:
            json_data["sizeRangeMax"] = self._size_range_max
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "factor :  %s\nsize_range_min :  %s\nsize_range_max :  %s" % (self._factor, self._size_range_min, self._size_range_max)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def factor(self) -> float:
        """Value by which size should be multiplied when the size falls within a certain range. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        """
        return self._factor

    @factor.setter
    def factor(self, value: float):
        self._factor = value

    @property
    def size_range_min(self) -> float:
        """Minimum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        """
        return self._size_range_min

    @size_range_min.setter
    def size_range_min(self, value: float):
        self._size_range_min = value

    @property
    def size_range_max(self) -> float:
        """Maximum size required to apply scaling. Applicable only when size field type is set to Geometric in AutoMeshParams structure.
        """
        return self._size_range_max

    @size_range_max.setter
    def size_range_max(self, value: float):
        self._size_range_max = value

class HexCoreParams(CoreObject):
    """Parameters to control hexahedral mesh generation.

    Parameters
    ----------
    model: Model
        Model to create a ``HexCoreParams`` object with default parameters.
    transition_size_field_type: SizeFieldType, optional
        Size field type to be used for transition volume (volume between hexcore and boundary).
    buffer_layers: int, optional
        Minimum number of cell layers of the same size before the cell size halves or doubles.
    rel_peel_layer_offset: float, optional
        Gap between hexahedral core and geometry surface relative to the surface mesh size.
    transition_layer_type: HexCoreTransitionLayerType, optional
        Handle size transition of hex cells.
    cell_element_type: HexCoreCellElementType, optional
        Cell element type of hex-shaped cells.
    surface_mesh_size_scaling: SurfaceMeshSizeScaling, optional
        Setting for scaling surface mesh size for hexcore refinement.
    enable_region_based_hexcore: bool, optional
        Checks whether to enable region based hexcore or not.
    json_data: dict, optional
        JSON dictionary to create a ``HexCoreParams`` object with provided parameters.

    Examples
    --------
    >>> hex_core_params = prime.HexCoreParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            transition_size_field_type: SizeFieldType,
            buffer_layers: int,
            rel_peel_layer_offset: float,
            transition_layer_type: HexCoreTransitionLayerType,
            cell_element_type: HexCoreCellElementType,
            surface_mesh_size_scaling: SurfaceMeshSizeScaling,
            enable_region_based_hexcore: bool):
        self._transition_size_field_type = SizeFieldType(transition_size_field_type)
        self._buffer_layers = buffer_layers
        self._rel_peel_layer_offset = rel_peel_layer_offset
        self._transition_layer_type = HexCoreTransitionLayerType(transition_layer_type)
        self._cell_element_type = HexCoreCellElementType(cell_element_type)
        self._surface_mesh_size_scaling = surface_mesh_size_scaling
        self._enable_region_based_hexcore = enable_region_based_hexcore

    def __init__(
            self,
            model: CommunicationManager=None,
            transition_size_field_type: SizeFieldType = None,
            buffer_layers: int = None,
            rel_peel_layer_offset: float = None,
            transition_layer_type: HexCoreTransitionLayerType = None,
            cell_element_type: HexCoreCellElementType = None,
            surface_mesh_size_scaling: SurfaceMeshSizeScaling = None,
            enable_region_based_hexcore: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``HexCoreParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``HexCoreParams`` object with default parameters.
        transition_size_field_type: SizeFieldType, optional
            Size field type to be used for transition volume (volume between hexcore and boundary).
        buffer_layers: int, optional
            Minimum number of cell layers of the same size before the cell size halves or doubles.
        rel_peel_layer_offset: float, optional
            Gap between hexahedral core and geometry surface relative to the surface mesh size.
        transition_layer_type: HexCoreTransitionLayerType, optional
            Handle size transition of hex cells.
        cell_element_type: HexCoreCellElementType, optional
            Cell element type of hex-shaped cells.
        surface_mesh_size_scaling: SurfaceMeshSizeScaling, optional
            Setting for scaling surface mesh size for hexcore refinement.
        enable_region_based_hexcore: bool, optional
            Checks whether to enable region based hexcore or not.
        json_data: dict, optional
            JSON dictionary to create a ``HexCoreParams`` object with provided parameters.

        Examples
        --------
        >>> hex_core_params = prime.HexCoreParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["transitionSizeFieldType"] if "transitionSizeFieldType" in json_data else None),
                json_data["bufferLayers"] if "bufferLayers" in json_data else None,
                json_data["relPeelLayerOffset"] if "relPeelLayerOffset" in json_data else None,
                HexCoreTransitionLayerType(json_data["transitionLayerType"] if "transitionLayerType" in json_data else None),
                HexCoreCellElementType(json_data["cellElementType"] if "cellElementType" in json_data else None),
                SurfaceMeshSizeScaling(model = model, json_data = json_data["surfaceMeshSizeScaling"] if "surfaceMeshSizeScaling" in json_data else None),
                json_data["enableRegionBasedHexcore"] if "enableRegionBasedHexcore" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [transition_size_field_type, buffer_layers, rel_peel_layer_offset, transition_layer_type, cell_element_type, surface_mesh_size_scaling, enable_region_based_hexcore])
            if all_field_specified:
                self.__initialize(
                    transition_size_field_type,
                    buffer_layers,
                    rel_peel_layer_offset,
                    transition_layer_type,
                    cell_element_type,
                    surface_mesh_size_scaling,
                    enable_region_based_hexcore)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "HexCoreParams")
                    json_data = param_json["HexCoreParams"] if "HexCoreParams" in param_json else {}
                    self.__initialize(
                        transition_size_field_type if transition_size_field_type is not None else ( HexCoreParams._default_params["transition_size_field_type"] if "transition_size_field_type" in HexCoreParams._default_params else SizeFieldType(json_data["transitionSizeFieldType"] if "transitionSizeFieldType" in json_data else None)),
                        buffer_layers if buffer_layers is not None else ( HexCoreParams._default_params["buffer_layers"] if "buffer_layers" in HexCoreParams._default_params else (json_data["bufferLayers"] if "bufferLayers" in json_data else None)),
                        rel_peel_layer_offset if rel_peel_layer_offset is not None else ( HexCoreParams._default_params["rel_peel_layer_offset"] if "rel_peel_layer_offset" in HexCoreParams._default_params else (json_data["relPeelLayerOffset"] if "relPeelLayerOffset" in json_data else None)),
                        transition_layer_type if transition_layer_type is not None else ( HexCoreParams._default_params["transition_layer_type"] if "transition_layer_type" in HexCoreParams._default_params else HexCoreTransitionLayerType(json_data["transitionLayerType"] if "transitionLayerType" in json_data else None)),
                        cell_element_type if cell_element_type is not None else ( HexCoreParams._default_params["cell_element_type"] if "cell_element_type" in HexCoreParams._default_params else HexCoreCellElementType(json_data["cellElementType"] if "cellElementType" in json_data else None)),
                        surface_mesh_size_scaling if surface_mesh_size_scaling is not None else ( HexCoreParams._default_params["surface_mesh_size_scaling"] if "surface_mesh_size_scaling" in HexCoreParams._default_params else SurfaceMeshSizeScaling(model = model, json_data = (json_data["surfaceMeshSizeScaling"] if "surfaceMeshSizeScaling" in json_data else None))),
                        enable_region_based_hexcore if enable_region_based_hexcore is not None else ( HexCoreParams._default_params["enable_region_based_hexcore"] if "enable_region_based_hexcore" in HexCoreParams._default_params else (json_data["enableRegionBasedHexcore"] if "enableRegionBasedHexcore" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            transition_size_field_type: SizeFieldType = None,
            buffer_layers: int = None,
            rel_peel_layer_offset: float = None,
            transition_layer_type: HexCoreTransitionLayerType = None,
            cell_element_type: HexCoreCellElementType = None,
            surface_mesh_size_scaling: SurfaceMeshSizeScaling = None,
            enable_region_based_hexcore: bool = None):
        """Set the default values of the ``HexCoreParams`` object.

        Parameters
        ----------
        transition_size_field_type: SizeFieldType, optional
            Size field type to be used for transition volume (volume between hexcore and boundary).
        buffer_layers: int, optional
            Minimum number of cell layers of the same size before the cell size halves or doubles.
        rel_peel_layer_offset: float, optional
            Gap between hexahedral core and geometry surface relative to the surface mesh size.
        transition_layer_type: HexCoreTransitionLayerType, optional
            Handle size transition of hex cells.
        cell_element_type: HexCoreCellElementType, optional
            Cell element type of hex-shaped cells.
        surface_mesh_size_scaling: SurfaceMeshSizeScaling, optional
            Setting for scaling surface mesh size for hexcore refinement.
        enable_region_based_hexcore: bool, optional
            Checks whether to enable region based hexcore or not.
        """
        args = locals()
        [HexCoreParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``HexCoreParams`` object.

        Examples
        --------
        >>> HexCoreParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in HexCoreParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._transition_size_field_type is not None:
            json_data["transitionSizeFieldType"] = self._transition_size_field_type
        if self._buffer_layers is not None:
            json_data["bufferLayers"] = self._buffer_layers
        if self._rel_peel_layer_offset is not None:
            json_data["relPeelLayerOffset"] = self._rel_peel_layer_offset
        if self._transition_layer_type is not None:
            json_data["transitionLayerType"] = self._transition_layer_type
        if self._cell_element_type is not None:
            json_data["cellElementType"] = self._cell_element_type
        if self._surface_mesh_size_scaling is not None:
            json_data["surfaceMeshSizeScaling"] = self._surface_mesh_size_scaling._jsonify()
        if self._enable_region_based_hexcore is not None:
            json_data["enableRegionBasedHexcore"] = self._enable_region_based_hexcore
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "transition_size_field_type :  %s\nbuffer_layers :  %s\nrel_peel_layer_offset :  %s\ntransition_layer_type :  %s\ncell_element_type :  %s\nsurface_mesh_size_scaling :  %s\nenable_region_based_hexcore :  %s" % (self._transition_size_field_type, self._buffer_layers, self._rel_peel_layer_offset, self._transition_layer_type, self._cell_element_type, '{ ' + str(self._surface_mesh_size_scaling) + ' }', self._enable_region_based_hexcore)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def transition_size_field_type(self) -> SizeFieldType:
        """Size field type to be used for transition volume (volume between hexcore and boundary).
        """
        return self._transition_size_field_type

    @transition_size_field_type.setter
    def transition_size_field_type(self, value: SizeFieldType):
        self._transition_size_field_type = value

    @property
    def buffer_layers(self) -> int:
        """Minimum number of cell layers of the same size before the cell size halves or doubles.
        """
        return self._buffer_layers

    @buffer_layers.setter
    def buffer_layers(self, value: int):
        self._buffer_layers = value

    @property
    def rel_peel_layer_offset(self) -> float:
        """Gap between hexahedral core and geometry surface relative to the surface mesh size.
        """
        return self._rel_peel_layer_offset

    @rel_peel_layer_offset.setter
    def rel_peel_layer_offset(self, value: float):
        self._rel_peel_layer_offset = value

    @property
    def transition_layer_type(self) -> HexCoreTransitionLayerType:
        """Handle size transition of hex cells.
        """
        return self._transition_layer_type

    @transition_layer_type.setter
    def transition_layer_type(self, value: HexCoreTransitionLayerType):
        self._transition_layer_type = value

    @property
    def cell_element_type(self) -> HexCoreCellElementType:
        """Cell element type of hex-shaped cells.
        """
        return self._cell_element_type

    @cell_element_type.setter
    def cell_element_type(self, value: HexCoreCellElementType):
        self._cell_element_type = value

    @property
    def surface_mesh_size_scaling(self) -> SurfaceMeshSizeScaling:
        """Setting for scaling surface mesh size for hexcore refinement.
        """
        return self._surface_mesh_size_scaling

    @surface_mesh_size_scaling.setter
    def surface_mesh_size_scaling(self, value: SurfaceMeshSizeScaling):
        self._surface_mesh_size_scaling = value

    @property
    def enable_region_based_hexcore(self) -> bool:
        """Checks whether to enable region based hexcore or not.
        """
        return self._enable_region_based_hexcore

    @enable_region_based_hexcore.setter
    def enable_region_based_hexcore(self, value: bool):
        self._enable_region_based_hexcore = value

class TetParams(CoreObject):
    """Parameters to control tetrahedral mesh generation.

    Parameters
    ----------
    model: Model
        Model to create a ``TetParams`` object with default parameters.
    quadratic: bool, optional
        Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
    json_data: dict, optional
        JSON dictionary to create a ``TetParams`` object with provided parameters.

    Examples
    --------
    >>> tet_params = prime.TetParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            quadratic: bool):
        self._quadratic = quadratic

    def __init__(
            self,
            model: CommunicationManager=None,
            quadratic: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``TetParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``TetParams`` object with default parameters.
        quadratic: bool, optional
            Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        json_data: dict, optional
            JSON dictionary to create a ``TetParams`` object with provided parameters.

        Examples
        --------
        >>> tet_params = prime.TetParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["quadratic"] if "quadratic" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [quadratic])
            if all_field_specified:
                self.__initialize(
                    quadratic)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "TetParams")
                    json_data = param_json["TetParams"] if "TetParams" in param_json else {}
                    self.__initialize(
                        quadratic if quadratic is not None else ( TetParams._default_params["quadratic"] if "quadratic" in TetParams._default_params else (json_data["quadratic"] if "quadratic" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            quadratic: bool = None):
        """Set the default values of the ``TetParams`` object.

        Parameters
        ----------
        quadratic: bool, optional
            Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        """
        args = locals()
        [TetParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``TetParams`` object.

        Examples
        --------
        >>> TetParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TetParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._quadratic is not None:
            json_data["quadratic"] = self._quadratic
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "quadratic :  %s" % (self._quadratic)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def quadratic(self) -> bool:
        """Option to generate quadratic tetrahedral mesh. It is not supported with parallel meshing. It is only supported with pure tetrahedral mesh.
        """
        return self._quadratic

    @quadratic.setter
    def quadratic(self, value: bool):
        self._quadratic = value

class AutoMeshParams(CoreObject):
    """Parameters for volume meshing.

    Parameters
    ----------
    model: Model
        Model to create a ``AutoMeshParams`` object with default parameters.
    size_field_type: SizeFieldType, optional
        Type of sizing to be used to generate volume mesh.
    max_size: float, optional
        Maximum cell size.
    prism_control_ids: Iterable[int], optional
        Set prism control ids.
    thin_volume_control_ids: Iterable[int], optional
        Set thin volume control ids.
    multi_zone_control_ids: Iterable[int], optional
        Set MultiZone control ids.
    volume_fill_type: VolumeFillType, optional
        Option to fill volume.
    prism: PrismParams, optional
        Prism control parameters.
    tet: TetParams, optional
        Parameters to control tetrahedral mesh generation.
    hexcore: HexCoreParams, optional
        Parameters to control hexahedral mesh generation.
    volume_control_ids: Iterable[int], optional
        Ids of the volume controls.
    periodic_control_ids: Iterable[int], optional
        Ids of the periodic controls.
    json_data: dict, optional
        JSON dictionary to create a ``AutoMeshParams`` object with provided parameters.

    Examples
    --------
    >>> auto_mesh_params = prime.AutoMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            size_field_type: SizeFieldType,
            max_size: float,
            prism_control_ids: Iterable[int],
            thin_volume_control_ids: Iterable[int],
            multi_zone_control_ids: Iterable[int],
            volume_fill_type: VolumeFillType,
            prism: PrismParams,
            tet: TetParams,
            hexcore: HexCoreParams,
            volume_control_ids: Iterable[int],
            periodic_control_ids: Iterable[int]):
        self._size_field_type = SizeFieldType(size_field_type)
        self._max_size = max_size
        self._prism_control_ids = prism_control_ids if isinstance(prism_control_ids, np.ndarray) else np.array(prism_control_ids, dtype=np.int32) if prism_control_ids is not None else None
        self._thin_volume_control_ids = thin_volume_control_ids if isinstance(thin_volume_control_ids, np.ndarray) else np.array(thin_volume_control_ids, dtype=np.int32) if thin_volume_control_ids is not None else None
        self._multi_zone_control_ids = multi_zone_control_ids if isinstance(multi_zone_control_ids, np.ndarray) else np.array(multi_zone_control_ids, dtype=np.int32) if multi_zone_control_ids is not None else None
        self._volume_fill_type = VolumeFillType(volume_fill_type)
        self._prism = prism
        self._tet = tet
        self._hexcore = hexcore
        self._volume_control_ids = volume_control_ids if isinstance(volume_control_ids, np.ndarray) else np.array(volume_control_ids, dtype=np.int32) if volume_control_ids is not None else None
        self._periodic_control_ids = periodic_control_ids if isinstance(periodic_control_ids, np.ndarray) else np.array(periodic_control_ids, dtype=np.int32) if periodic_control_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            size_field_type: SizeFieldType = None,
            max_size: float = None,
            prism_control_ids: Iterable[int] = None,
            thin_volume_control_ids: Iterable[int] = None,
            multi_zone_control_ids: Iterable[int] = None,
            volume_fill_type: VolumeFillType = None,
            prism: PrismParams = None,
            tet: TetParams = None,
            hexcore: HexCoreParams = None,
            volume_control_ids: Iterable[int] = None,
            periodic_control_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``AutoMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``AutoMeshParams`` object with default parameters.
        size_field_type: SizeFieldType, optional
            Type of sizing to be used to generate volume mesh.
        max_size: float, optional
            Maximum cell size.
        prism_control_ids: Iterable[int], optional
            Set prism control ids.
        thin_volume_control_ids: Iterable[int], optional
            Set thin volume control ids.
        multi_zone_control_ids: Iterable[int], optional
            Set MultiZone control ids.
        volume_fill_type: VolumeFillType, optional
            Option to fill volume.
        prism: PrismParams, optional
            Prism control parameters.
        tet: TetParams, optional
            Parameters to control tetrahedral mesh generation.
        hexcore: HexCoreParams, optional
            Parameters to control hexahedral mesh generation.
        volume_control_ids: Iterable[int], optional
            Ids of the volume controls.
        periodic_control_ids: Iterable[int], optional
            Ids of the periodic controls.
        json_data: dict, optional
            JSON dictionary to create a ``AutoMeshParams`` object with provided parameters.

        Examples
        --------
        >>> auto_mesh_params = prime.AutoMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None),
                json_data["maxSize"] if "maxSize" in json_data else None,
                json_data["prismControlIds"] if "prismControlIds" in json_data else None,
                json_data["thinVolumeControlIds"] if "thinVolumeControlIds" in json_data else None,
                json_data["multiZoneControlIds"] if "multiZoneControlIds" in json_data else None,
                VolumeFillType(json_data["volumeFillType"] if "volumeFillType" in json_data else None),
                PrismParams(model = model, json_data = json_data["prism"] if "prism" in json_data else None),
                TetParams(model = model, json_data = json_data["tet"] if "tet" in json_data else None),
                HexCoreParams(model = model, json_data = json_data["hexcore"] if "hexcore" in json_data else None),
                json_data["volumeControlIds"] if "volumeControlIds" in json_data else None,
                json_data["periodicControlIds"] if "periodicControlIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [size_field_type, max_size, prism_control_ids, thin_volume_control_ids, multi_zone_control_ids, volume_fill_type, prism, tet, hexcore, volume_control_ids, periodic_control_ids])
            if all_field_specified:
                self.__initialize(
                    size_field_type,
                    max_size,
                    prism_control_ids,
                    thin_volume_control_ids,
                    multi_zone_control_ids,
                    volume_fill_type,
                    prism,
                    tet,
                    hexcore,
                    volume_control_ids,
                    periodic_control_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "AutoMeshParams")
                    json_data = param_json["AutoMeshParams"] if "AutoMeshParams" in param_json else {}
                    self.__initialize(
                        size_field_type if size_field_type is not None else ( AutoMeshParams._default_params["size_field_type"] if "size_field_type" in AutoMeshParams._default_params else SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None)),
                        max_size if max_size is not None else ( AutoMeshParams._default_params["max_size"] if "max_size" in AutoMeshParams._default_params else (json_data["maxSize"] if "maxSize" in json_data else None)),
                        prism_control_ids if prism_control_ids is not None else ( AutoMeshParams._default_params["prism_control_ids"] if "prism_control_ids" in AutoMeshParams._default_params else (json_data["prismControlIds"] if "prismControlIds" in json_data else None)),
                        thin_volume_control_ids if thin_volume_control_ids is not None else ( AutoMeshParams._default_params["thin_volume_control_ids"] if "thin_volume_control_ids" in AutoMeshParams._default_params else (json_data["thinVolumeControlIds"] if "thinVolumeControlIds" in json_data else None)),
                        multi_zone_control_ids if multi_zone_control_ids is not None else ( AutoMeshParams._default_params["multi_zone_control_ids"] if "multi_zone_control_ids" in AutoMeshParams._default_params else (json_data["multiZoneControlIds"] if "multiZoneControlIds" in json_data else None)),
                        volume_fill_type if volume_fill_type is not None else ( AutoMeshParams._default_params["volume_fill_type"] if "volume_fill_type" in AutoMeshParams._default_params else VolumeFillType(json_data["volumeFillType"] if "volumeFillType" in json_data else None)),
                        prism if prism is not None else ( AutoMeshParams._default_params["prism"] if "prism" in AutoMeshParams._default_params else PrismParams(model = model, json_data = (json_data["prism"] if "prism" in json_data else None))),
                        tet if tet is not None else ( AutoMeshParams._default_params["tet"] if "tet" in AutoMeshParams._default_params else TetParams(model = model, json_data = (json_data["tet"] if "tet" in json_data else None))),
                        hexcore if hexcore is not None else ( AutoMeshParams._default_params["hexcore"] if "hexcore" in AutoMeshParams._default_params else HexCoreParams(model = model, json_data = (json_data["hexcore"] if "hexcore" in json_data else None))),
                        volume_control_ids if volume_control_ids is not None else ( AutoMeshParams._default_params["volume_control_ids"] if "volume_control_ids" in AutoMeshParams._default_params else (json_data["volumeControlIds"] if "volumeControlIds" in json_data else None)),
                        periodic_control_ids if periodic_control_ids is not None else ( AutoMeshParams._default_params["periodic_control_ids"] if "periodic_control_ids" in AutoMeshParams._default_params else (json_data["periodicControlIds"] if "periodicControlIds" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            size_field_type: SizeFieldType = None,
            max_size: float = None,
            prism_control_ids: Iterable[int] = None,
            thin_volume_control_ids: Iterable[int] = None,
            multi_zone_control_ids: Iterable[int] = None,
            volume_fill_type: VolumeFillType = None,
            prism: PrismParams = None,
            tet: TetParams = None,
            hexcore: HexCoreParams = None,
            volume_control_ids: Iterable[int] = None,
            periodic_control_ids: Iterable[int] = None):
        """Set the default values of the ``AutoMeshParams`` object.

        Parameters
        ----------
        size_field_type: SizeFieldType, optional
            Type of sizing to be used to generate volume mesh.
        max_size: float, optional
            Maximum cell size.
        prism_control_ids: Iterable[int], optional
            Set prism control ids.
        thin_volume_control_ids: Iterable[int], optional
            Set thin volume control ids.
        multi_zone_control_ids: Iterable[int], optional
            Set MultiZone control ids.
        volume_fill_type: VolumeFillType, optional
            Option to fill volume.
        prism: PrismParams, optional
            Prism control parameters.
        tet: TetParams, optional
            Parameters to control tetrahedral mesh generation.
        hexcore: HexCoreParams, optional
            Parameters to control hexahedral mesh generation.
        volume_control_ids: Iterable[int], optional
            Ids of the volume controls.
        periodic_control_ids: Iterable[int], optional
            Ids of the periodic controls.
        """
        args = locals()
        [AutoMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``AutoMeshParams`` object.

        Examples
        --------
        >>> AutoMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._size_field_type is not None:
            json_data["sizeFieldType"] = self._size_field_type
        if self._max_size is not None:
            json_data["maxSize"] = self._max_size
        if self._prism_control_ids is not None:
            json_data["prismControlIds"] = self._prism_control_ids
        if self._thin_volume_control_ids is not None:
            json_data["thinVolumeControlIds"] = self._thin_volume_control_ids
        if self._multi_zone_control_ids is not None:
            json_data["multiZoneControlIds"] = self._multi_zone_control_ids
        if self._volume_fill_type is not None:
            json_data["volumeFillType"] = self._volume_fill_type
        if self._prism is not None:
            json_data["prism"] = self._prism._jsonify()
        if self._tet is not None:
            json_data["tet"] = self._tet._jsonify()
        if self._hexcore is not None:
            json_data["hexcore"] = self._hexcore._jsonify()
        if self._volume_control_ids is not None:
            json_data["volumeControlIds"] = self._volume_control_ids
        if self._periodic_control_ids is not None:
            json_data["periodicControlIds"] = self._periodic_control_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "size_field_type :  %s\nmax_size :  %s\nprism_control_ids :  %s\nthin_volume_control_ids :  %s\nmulti_zone_control_ids :  %s\nvolume_fill_type :  %s\nprism :  %s\ntet :  %s\nhexcore :  %s\nvolume_control_ids :  %s\nperiodic_control_ids :  %s" % (self._size_field_type, self._max_size, self._prism_control_ids, self._thin_volume_control_ids, self._multi_zone_control_ids, self._volume_fill_type, '{ ' + str(self._prism) + ' }', '{ ' + str(self._tet) + ' }', '{ ' + str(self._hexcore) + ' }', self._volume_control_ids, self._periodic_control_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def size_field_type(self) -> SizeFieldType:
        """Type of sizing to be used to generate volume mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def max_size(self) -> float:
        """Maximum cell size.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def prism_control_ids(self) -> Iterable[int]:
        """Set prism control ids.
        """
        return self._prism_control_ids

    @prism_control_ids.setter
    def prism_control_ids(self, value: Iterable[int]):
        self._prism_control_ids = value

    @property
    def thin_volume_control_ids(self) -> Iterable[int]:
        """Set thin volume control ids.
        """
        return self._thin_volume_control_ids

    @thin_volume_control_ids.setter
    def thin_volume_control_ids(self, value: Iterable[int]):
        self._thin_volume_control_ids = value

    @property
    def multi_zone_control_ids(self) -> Iterable[int]:
        """Set MultiZone control ids.
        """
        return self._multi_zone_control_ids

    @multi_zone_control_ids.setter
    def multi_zone_control_ids(self, value: Iterable[int]):
        self._multi_zone_control_ids = value

    @property
    def volume_fill_type(self) -> VolumeFillType:
        """Option to fill volume.
        """
        return self._volume_fill_type

    @volume_fill_type.setter
    def volume_fill_type(self, value: VolumeFillType):
        self._volume_fill_type = value

    @property
    def prism(self) -> PrismParams:
        """Prism control parameters.
        """
        return self._prism

    @prism.setter
    def prism(self, value: PrismParams):
        self._prism = value

    @property
    def tet(self) -> TetParams:
        """Parameters to control tetrahedral mesh generation.
        """
        return self._tet

    @tet.setter
    def tet(self, value: TetParams):
        self._tet = value

    @property
    def hexcore(self) -> HexCoreParams:
        """Parameters to control hexahedral mesh generation.
        """
        return self._hexcore

    @hexcore.setter
    def hexcore(self, value: HexCoreParams):
        self._hexcore = value

    @property
    def volume_control_ids(self) -> Iterable[int]:
        """Ids of the volume controls.
        """
        return self._volume_control_ids

    @volume_control_ids.setter
    def volume_control_ids(self, value: Iterable[int]):
        self._volume_control_ids = value

    @property
    def periodic_control_ids(self) -> Iterable[int]:
        """Ids of the periodic controls.
        """
        return self._periodic_control_ids

    @periodic_control_ids.setter
    def periodic_control_ids(self, value: Iterable[int]):
        self._periodic_control_ids = value
