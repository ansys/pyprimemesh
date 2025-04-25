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

class AdvancedSurferSetup(enum.IntEnum):
    """Define advanced settings for remeshing operation.
    """
    NONE = 0
    """Option to define no advanced settings."""
    WRAPPER = 1
    """Option to define advanced settings for wrapper surfaces."""

class SurferParams(CoreObject):
    """Parameters used to generate surface mesh.

    Parameters
    ----------
    model: Model
        Model to create a ``SurferParams`` object with default parameters.
    max_angle: float, optional
        Maximum feature angle limit to be used to identify and preserve features.
    size_field_type: SizeFieldType, optional
        Size field type used to generate surface mesh.
    min_size: float, optional
        Minimum size to be used in sizing for the surfer.
    max_size: float, optional
        Maximum size to be used in sizing for the surfer.
    growth_rate: float, optional
        Growth rate to be used to propagate sizes.
    constant_size: float, optional
        Size used in constant size surface meshing.
    generate_quads: bool, optional
        Option to generate quadrilateral surface mesh.
    check_non_manifolds: bool, optional
        Option to avoid new non-manifolds(multi-connection) if generated in surface mesh.
    avoid_corner_triangles: bool, optional
        Option to avoid corner triangles(with all three boundary nodes) generated.
    smooth_size_transition: bool, optional
        Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.
    advanced_surfer_setup: AdvancedSurferSetup, optional
        Option to define advanced settings for remeshing operation.
    project_on_geometry: bool, optional
        Option to project on CAD geometry when meshing.
    enable_multi_threading: bool, optional
        Option to perform surface meshing in parallel using multithreads.
    json_data: dict, optional
        JSON dictionary to create a ``SurferParams`` object with provided parameters.

    Examples
    --------
    >>> surfer_params = prime.SurferParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            max_angle: float,
            size_field_type: SizeFieldType,
            min_size: float,
            max_size: float,
            growth_rate: float,
            constant_size: float,
            generate_quads: bool,
            check_non_manifolds: bool,
            avoid_corner_triangles: bool,
            smooth_size_transition: bool,
            advanced_surfer_setup: AdvancedSurferSetup,
            project_on_geometry: bool,
            enable_multi_threading: bool):
        self._max_angle = max_angle
        self._size_field_type = SizeFieldType(size_field_type)
        self._min_size = min_size
        self._max_size = max_size
        self._growth_rate = growth_rate
        self._constant_size = constant_size
        self._generate_quads = generate_quads
        self._check_non_manifolds = check_non_manifolds
        self._avoid_corner_triangles = avoid_corner_triangles
        self._smooth_size_transition = smooth_size_transition
        self._advanced_surfer_setup = AdvancedSurferSetup(advanced_surfer_setup)
        self._project_on_geometry = project_on_geometry
        self._enable_multi_threading = enable_multi_threading

    def __init__(
            self,
            model: CommunicationManager=None,
            max_angle: float = None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            generate_quads: bool = None,
            check_non_manifolds: bool = None,
            avoid_corner_triangles: bool = None,
            smooth_size_transition: bool = None,
            advanced_surfer_setup: AdvancedSurferSetup = None,
            project_on_geometry: bool = None,
            enable_multi_threading: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SurferParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``SurferParams`` object with default parameters.
        max_angle: float, optional
            Maximum feature angle limit to be used to identify and preserve features.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        check_non_manifolds: bool, optional
            Option to avoid new non-manifolds(multi-connection) if generated in surface mesh.
        avoid_corner_triangles: bool, optional
            Option to avoid corner triangles(with all three boundary nodes) generated.
        smooth_size_transition: bool, optional
            Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.
        advanced_surfer_setup: AdvancedSurferSetup, optional
            Option to define advanced settings for remeshing operation.
        project_on_geometry: bool, optional
            Option to project on CAD geometry when meshing.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multithreads.
        json_data: dict, optional
            JSON dictionary to create a ``SurferParams`` object with provided parameters.

        Examples
        --------
        >>> surfer_params = prime.SurferParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["maxAngle"] if "maxAngle" in json_data else None,
                SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None),
                json_data["minSize"] if "minSize" in json_data else None,
                json_data["maxSize"] if "maxSize" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["constantSize"] if "constantSize" in json_data else None,
                json_data["generateQuads"] if "generateQuads" in json_data else None,
                json_data["checkNonManifolds"] if "checkNonManifolds" in json_data else None,
                json_data["avoidCornerTriangles"] if "avoidCornerTriangles" in json_data else None,
                json_data["smoothSizeTransition"] if "smoothSizeTransition" in json_data else None,
                AdvancedSurferSetup(json_data["advancedSurferSetup"] if "advancedSurferSetup" in json_data else None),
                json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None,
                json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [max_angle, size_field_type, min_size, max_size, growth_rate, constant_size, generate_quads, check_non_manifolds, avoid_corner_triangles, smooth_size_transition, advanced_surfer_setup, project_on_geometry, enable_multi_threading])
            if all_field_specified:
                self.__initialize(
                    max_angle,
                    size_field_type,
                    min_size,
                    max_size,
                    growth_rate,
                    constant_size,
                    generate_quads,
                    check_non_manifolds,
                    avoid_corner_triangles,
                    smooth_size_transition,
                    advanced_surfer_setup,
                    project_on_geometry,
                    enable_multi_threading)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SurferParams")
                    json_data = param_json["SurferParams"] if "SurferParams" in param_json else {}
                    self.__initialize(
                        max_angle if max_angle is not None else ( SurferParams._default_params["max_angle"] if "max_angle" in SurferParams._default_params else (json_data["maxAngle"] if "maxAngle" in json_data else None)),
                        size_field_type if size_field_type is not None else ( SurferParams._default_params["size_field_type"] if "size_field_type" in SurferParams._default_params else SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None)),
                        min_size if min_size is not None else ( SurferParams._default_params["min_size"] if "min_size" in SurferParams._default_params else (json_data["minSize"] if "minSize" in json_data else None)),
                        max_size if max_size is not None else ( SurferParams._default_params["max_size"] if "max_size" in SurferParams._default_params else (json_data["maxSize"] if "maxSize" in json_data else None)),
                        growth_rate if growth_rate is not None else ( SurferParams._default_params["growth_rate"] if "growth_rate" in SurferParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        constant_size if constant_size is not None else ( SurferParams._default_params["constant_size"] if "constant_size" in SurferParams._default_params else (json_data["constantSize"] if "constantSize" in json_data else None)),
                        generate_quads if generate_quads is not None else ( SurferParams._default_params["generate_quads"] if "generate_quads" in SurferParams._default_params else (json_data["generateQuads"] if "generateQuads" in json_data else None)),
                        check_non_manifolds if check_non_manifolds is not None else ( SurferParams._default_params["check_non_manifolds"] if "check_non_manifolds" in SurferParams._default_params else (json_data["checkNonManifolds"] if "checkNonManifolds" in json_data else None)),
                        avoid_corner_triangles if avoid_corner_triangles is not None else ( SurferParams._default_params["avoid_corner_triangles"] if "avoid_corner_triangles" in SurferParams._default_params else (json_data["avoidCornerTriangles"] if "avoidCornerTriangles" in json_data else None)),
                        smooth_size_transition if smooth_size_transition is not None else ( SurferParams._default_params["smooth_size_transition"] if "smooth_size_transition" in SurferParams._default_params else (json_data["smoothSizeTransition"] if "smoothSizeTransition" in json_data else None)),
                        advanced_surfer_setup if advanced_surfer_setup is not None else ( SurferParams._default_params["advanced_surfer_setup"] if "advanced_surfer_setup" in SurferParams._default_params else AdvancedSurferSetup(json_data["advancedSurferSetup"] if "advancedSurferSetup" in json_data else None)),
                        project_on_geometry if project_on_geometry is not None else ( SurferParams._default_params["project_on_geometry"] if "project_on_geometry" in SurferParams._default_params else (json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None)),
                        enable_multi_threading if enable_multi_threading is not None else ( SurferParams._default_params["enable_multi_threading"] if "enable_multi_threading" in SurferParams._default_params else (json_data["enableMultiThreading"] if "enableMultiThreading" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            max_angle: float = None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            generate_quads: bool = None,
            check_non_manifolds: bool = None,
            avoid_corner_triangles: bool = None,
            smooth_size_transition: bool = None,
            advanced_surfer_setup: AdvancedSurferSetup = None,
            project_on_geometry: bool = None,
            enable_multi_threading: bool = None):
        """Set the default values of the ``SurferParams`` object.

        Parameters
        ----------
        max_angle: float, optional
            Maximum feature angle limit to be used to identify and preserve features.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Size used in constant size surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        check_non_manifolds: bool, optional
            Option to avoid new non-manifolds(multi-connection) if generated in surface mesh.
        avoid_corner_triangles: bool, optional
            Option to avoid corner triangles(with all three boundary nodes) generated.
        smooth_size_transition: bool, optional
            Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.
        advanced_surfer_setup: AdvancedSurferSetup, optional
            Option to define advanced settings for remeshing operation.
        project_on_geometry: bool, optional
            Option to project on CAD geometry when meshing.
        enable_multi_threading: bool, optional
            Option to perform surface meshing in parallel using multithreads.
        """
        args = locals()
        [SurferParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SurferParams`` object.

        Examples
        --------
        >>> SurferParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._max_angle is not None:
            json_data["maxAngle"] = self._max_angle
        if self._size_field_type is not None:
            json_data["sizeFieldType"] = self._size_field_type
        if self._min_size is not None:
            json_data["minSize"] = self._min_size
        if self._max_size is not None:
            json_data["maxSize"] = self._max_size
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._constant_size is not None:
            json_data["constantSize"] = self._constant_size
        if self._generate_quads is not None:
            json_data["generateQuads"] = self._generate_quads
        if self._check_non_manifolds is not None:
            json_data["checkNonManifolds"] = self._check_non_manifolds
        if self._avoid_corner_triangles is not None:
            json_data["avoidCornerTriangles"] = self._avoid_corner_triangles
        if self._smooth_size_transition is not None:
            json_data["smoothSizeTransition"] = self._smooth_size_transition
        if self._advanced_surfer_setup is not None:
            json_data["advancedSurferSetup"] = self._advanced_surfer_setup
        if self._project_on_geometry is not None:
            json_data["projectOnGeometry"] = self._project_on_geometry
        if self._enable_multi_threading is not None:
            json_data["enableMultiThreading"] = self._enable_multi_threading
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "max_angle :  %s\nsize_field_type :  %s\nmin_size :  %s\nmax_size :  %s\ngrowth_rate :  %s\nconstant_size :  %s\ngenerate_quads :  %s\ncheck_non_manifolds :  %s\navoid_corner_triangles :  %s\nsmooth_size_transition :  %s\nadvanced_surfer_setup :  %s\nproject_on_geometry :  %s\nenable_multi_threading :  %s" % (self._max_angle, self._size_field_type, self._min_size, self._max_size, self._growth_rate, self._constant_size, self._generate_quads, self._check_non_manifolds, self._avoid_corner_triangles, self._smooth_size_transition, self._advanced_surfer_setup, self._project_on_geometry, self._enable_multi_threading)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def max_angle(self) -> float:
        """Maximum feature angle limit to be used to identify and preserve features.
        """
        return self._max_angle

    @max_angle.setter
    def max_angle(self, value: float):
        self._max_angle = value

    @property
    def size_field_type(self) -> SizeFieldType:
        """Size field type used to generate surface mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def min_size(self) -> float:
        """Minimum size to be used in sizing for the surfer.
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        self._min_size = value

    @property
    def max_size(self) -> float:
        """Maximum size to be used in sizing for the surfer.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def growth_rate(self) -> float:
        """Growth rate to be used to propagate sizes.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def constant_size(self) -> float:
        """Size used in constant size surface meshing.
        """
        return self._constant_size

    @constant_size.setter
    def constant_size(self, value: float):
        self._constant_size = value

    @property
    def generate_quads(self) -> bool:
        """Option to generate quadrilateral surface mesh.
        """
        return self._generate_quads

    @generate_quads.setter
    def generate_quads(self, value: bool):
        self._generate_quads = value

    @property
    def check_non_manifolds(self) -> bool:
        """Option to avoid new non-manifolds(multi-connection) if generated in surface mesh.
        """
        return self._check_non_manifolds

    @check_non_manifolds.setter
    def check_non_manifolds(self, value: bool):
        self._check_non_manifolds = value

    @property
    def avoid_corner_triangles(self) -> bool:
        """Option to avoid corner triangles(with all three boundary nodes) generated.
        """
        return self._avoid_corner_triangles

    @avoid_corner_triangles.setter
    def avoid_corner_triangles(self, value: bool):
        self._avoid_corner_triangles = value

    @property
    def smooth_size_transition(self) -> bool:
        """Option to generate mesh with smooth size transition from neighbors of selected surfaces. This includes neighboring face edge sizes in sizing provided for surface meshing to achieve smooth size transition.

        Notes
         -----
          - Input facets or mesh with finer sizes compared to neighboring face edge sizes are required for this option to work.
          - Valid min, max sizes and growth rate are required to include the neighboring face edges sizes in sizing.
        """
        return self._smooth_size_transition

    @smooth_size_transition.setter
    def smooth_size_transition(self, value: bool):
        self._smooth_size_transition = value

    @property
    def advanced_surfer_setup(self) -> AdvancedSurferSetup:
        """Option to define advanced settings for remeshing operation.
        """
        return self._advanced_surfer_setup

    @advanced_surfer_setup.setter
    def advanced_surfer_setup(self, value: AdvancedSurferSetup):
        self._advanced_surfer_setup = value

    @property
    def project_on_geometry(self) -> bool:
        """Option to project on CAD geometry when meshing.
        """
        return self._project_on_geometry

    @project_on_geometry.setter
    def project_on_geometry(self, value: bool):
        self._project_on_geometry = value

    @property
    def enable_multi_threading(self) -> bool:
        """Option to perform surface meshing in parallel using multithreads.
        """
        return self._enable_multi_threading

    @enable_multi_threading.setter
    def enable_multi_threading(self, value: bool):
        self._enable_multi_threading = value

class SurferResults(CoreObject):
    """Results associated with the surface mesh.

    Parameters
    ----------
    model: Model
        Model to create a ``SurferResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.
    topofaces_not_projected_on_geometry: Iterable[int], optional
        Ids of topofaces projected to facets instead of CAD geometry, when projectOnGeometry is enabled.
    json_data: dict, optional
        JSON dictionary to create a ``SurferResults`` object with provided parameters.

    Examples
    --------
    >>> surfer_results = prime.SurferResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            topofaces_not_projected_on_geometry: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._topofaces_not_projected_on_geometry = topofaces_not_projected_on_geometry if isinstance(topofaces_not_projected_on_geometry, np.ndarray) else np.array(topofaces_not_projected_on_geometry, dtype=np.int32) if topofaces_not_projected_on_geometry is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            topofaces_not_projected_on_geometry: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``SurferResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``SurferResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        topofaces_not_projected_on_geometry: Iterable[int], optional
            Ids of topofaces projected to facets instead of CAD geometry, when projectOnGeometry is enabled.
        json_data: dict, optional
            JSON dictionary to create a ``SurferResults`` object with provided parameters.

        Examples
        --------
        >>> surfer_results = prime.SurferResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["topofacesNotProjectedOnGeometry"] if "topofacesNotProjectedOnGeometry" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, topofaces_not_projected_on_geometry])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    topofaces_not_projected_on_geometry)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "SurferResults")
                    json_data = param_json["SurferResults"] if "SurferResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( SurferResults._default_params["error_code"] if "error_code" in SurferResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        topofaces_not_projected_on_geometry if topofaces_not_projected_on_geometry is not None else ( SurferResults._default_params["topofaces_not_projected_on_geometry"] if "topofaces_not_projected_on_geometry" in SurferResults._default_params else (json_data["topofacesNotProjectedOnGeometry"] if "topofacesNotProjectedOnGeometry" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            topofaces_not_projected_on_geometry: Iterable[int] = None):
        """Set the default values of the ``SurferResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        topofaces_not_projected_on_geometry: Iterable[int], optional
            Ids of topofaces projected to facets instead of CAD geometry, when projectOnGeometry is enabled.
        """
        args = locals()
        [SurferResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``SurferResults`` object.

        Examples
        --------
        >>> SurferResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in SurferResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._topofaces_not_projected_on_geometry is not None:
            json_data["topofacesNotProjectedOnGeometry"] = self._topofaces_not_projected_on_geometry
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\ntopofaces_not_projected_on_geometry :  %s" % (self._error_code, self._topofaces_not_projected_on_geometry)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def topofaces_not_projected_on_geometry(self) -> Iterable[int]:
        """Ids of topofaces projected to facets instead of CAD geometry, when projectOnGeometry is enabled.
        """
        return self._topofaces_not_projected_on_geometry

    @topofaces_not_projected_on_geometry.setter
    def topofaces_not_projected_on_geometry(self, value: Iterable[int]):
        self._topofaces_not_projected_on_geometry = value

class LocalSurferParams(CoreObject):
    """Parameters to perform local surface remeshing.

    Parameters
    ----------
    model: Model
        Model to create a ``LocalSurferParams`` object with default parameters.
    min_angle: float, optional
        Minimum feature angle limit used to identify and preserve features.
    max_angle: float, optional
        Maximum feature angle limit used to identify and preserve features.
    size_field_type: SizeFieldType, optional
        Size field type used to generate surface mesh.
    min_size: float, optional
        Minimum size to be used in sizing for the surfer.
    max_size: float, optional
        Maximum size to be used in sizing for the surfer.
    growth_rate: float, optional
        Growth rate to be used to propagate sizes.
    constant_size: float, optional
        Constant size to be used in case of constant size field.
    smooth_boundary: bool, optional
        Option to extend local selection to get smooth boundary of selected elements.
    n_rings: int, optional
        Number of rings to extend the registered face selection for remeshing.
    json_data: dict, optional
        JSON dictionary to create a ``LocalSurferParams`` object with provided parameters.

    Examples
    --------
    >>> local_surfer_params = prime.LocalSurferParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            min_angle: float,
            max_angle: float,
            size_field_type: SizeFieldType,
            min_size: float,
            max_size: float,
            growth_rate: float,
            constant_size: float,
            smooth_boundary: bool,
            n_rings: int):
        self._min_angle = min_angle
        self._max_angle = max_angle
        self._size_field_type = SizeFieldType(size_field_type)
        self._min_size = min_size
        self._max_size = max_size
        self._growth_rate = growth_rate
        self._constant_size = constant_size
        self._smooth_boundary = smooth_boundary
        self._n_rings = n_rings

    def __init__(
            self,
            model: CommunicationManager=None,
            min_angle: float = None,
            max_angle: float = None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            smooth_boundary: bool = None,
            n_rings: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``LocalSurferParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``LocalSurferParams`` object with default parameters.
        min_angle: float, optional
            Minimum feature angle limit used to identify and preserve features.
        max_angle: float, optional
            Maximum feature angle limit used to identify and preserve features.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Constant size to be used in case of constant size field.
        smooth_boundary: bool, optional
            Option to extend local selection to get smooth boundary of selected elements.
        n_rings: int, optional
            Number of rings to extend the registered face selection for remeshing.
        json_data: dict, optional
            JSON dictionary to create a ``LocalSurferParams`` object with provided parameters.

        Examples
        --------
        >>> local_surfer_params = prime.LocalSurferParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["minAngle"] if "minAngle" in json_data else None,
                json_data["maxAngle"] if "maxAngle" in json_data else None,
                SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None),
                json_data["minSize"] if "minSize" in json_data else None,
                json_data["maxSize"] if "maxSize" in json_data else None,
                json_data["growthRate"] if "growthRate" in json_data else None,
                json_data["constantSize"] if "constantSize" in json_data else None,
                json_data["smoothBoundary"] if "smoothBoundary" in json_data else None,
                json_data["nRings"] if "nRings" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [min_angle, max_angle, size_field_type, min_size, max_size, growth_rate, constant_size, smooth_boundary, n_rings])
            if all_field_specified:
                self.__initialize(
                    min_angle,
                    max_angle,
                    size_field_type,
                    min_size,
                    max_size,
                    growth_rate,
                    constant_size,
                    smooth_boundary,
                    n_rings)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "LocalSurferParams")
                    json_data = param_json["LocalSurferParams"] if "LocalSurferParams" in param_json else {}
                    self.__initialize(
                        min_angle if min_angle is not None else ( LocalSurferParams._default_params["min_angle"] if "min_angle" in LocalSurferParams._default_params else (json_data["minAngle"] if "minAngle" in json_data else None)),
                        max_angle if max_angle is not None else ( LocalSurferParams._default_params["max_angle"] if "max_angle" in LocalSurferParams._default_params else (json_data["maxAngle"] if "maxAngle" in json_data else None)),
                        size_field_type if size_field_type is not None else ( LocalSurferParams._default_params["size_field_type"] if "size_field_type" in LocalSurferParams._default_params else SizeFieldType(json_data["sizeFieldType"] if "sizeFieldType" in json_data else None)),
                        min_size if min_size is not None else ( LocalSurferParams._default_params["min_size"] if "min_size" in LocalSurferParams._default_params else (json_data["minSize"] if "minSize" in json_data else None)),
                        max_size if max_size is not None else ( LocalSurferParams._default_params["max_size"] if "max_size" in LocalSurferParams._default_params else (json_data["maxSize"] if "maxSize" in json_data else None)),
                        growth_rate if growth_rate is not None else ( LocalSurferParams._default_params["growth_rate"] if "growth_rate" in LocalSurferParams._default_params else (json_data["growthRate"] if "growthRate" in json_data else None)),
                        constant_size if constant_size is not None else ( LocalSurferParams._default_params["constant_size"] if "constant_size" in LocalSurferParams._default_params else (json_data["constantSize"] if "constantSize" in json_data else None)),
                        smooth_boundary if smooth_boundary is not None else ( LocalSurferParams._default_params["smooth_boundary"] if "smooth_boundary" in LocalSurferParams._default_params else (json_data["smoothBoundary"] if "smoothBoundary" in json_data else None)),
                        n_rings if n_rings is not None else ( LocalSurferParams._default_params["n_rings"] if "n_rings" in LocalSurferParams._default_params else (json_data["nRings"] if "nRings" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            min_angle: float = None,
            max_angle: float = None,
            size_field_type: SizeFieldType = None,
            min_size: float = None,
            max_size: float = None,
            growth_rate: float = None,
            constant_size: float = None,
            smooth_boundary: bool = None,
            n_rings: int = None):
        """Set the default values of the ``LocalSurferParams`` object.

        Parameters
        ----------
        min_angle: float, optional
            Minimum feature angle limit used to identify and preserve features.
        max_angle: float, optional
            Maximum feature angle limit used to identify and preserve features.
        size_field_type: SizeFieldType, optional
            Size field type used to generate surface mesh.
        min_size: float, optional
            Minimum size to be used in sizing for the surfer.
        max_size: float, optional
            Maximum size to be used in sizing for the surfer.
        growth_rate: float, optional
            Growth rate to be used to propagate sizes.
        constant_size: float, optional
            Constant size to be used in case of constant size field.
        smooth_boundary: bool, optional
            Option to extend local selection to get smooth boundary of selected elements.
        n_rings: int, optional
            Number of rings to extend the registered face selection for remeshing.
        """
        args = locals()
        [LocalSurferParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``LocalSurferParams`` object.

        Examples
        --------
        >>> LocalSurferParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LocalSurferParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._min_angle is not None:
            json_data["minAngle"] = self._min_angle
        if self._max_angle is not None:
            json_data["maxAngle"] = self._max_angle
        if self._size_field_type is not None:
            json_data["sizeFieldType"] = self._size_field_type
        if self._min_size is not None:
            json_data["minSize"] = self._min_size
        if self._max_size is not None:
            json_data["maxSize"] = self._max_size
        if self._growth_rate is not None:
            json_data["growthRate"] = self._growth_rate
        if self._constant_size is not None:
            json_data["constantSize"] = self._constant_size
        if self._smooth_boundary is not None:
            json_data["smoothBoundary"] = self._smooth_boundary
        if self._n_rings is not None:
            json_data["nRings"] = self._n_rings
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "min_angle :  %s\nmax_angle :  %s\nsize_field_type :  %s\nmin_size :  %s\nmax_size :  %s\ngrowth_rate :  %s\nconstant_size :  %s\nsmooth_boundary :  %s\nn_rings :  %s" % (self._min_angle, self._max_angle, self._size_field_type, self._min_size, self._max_size, self._growth_rate, self._constant_size, self._smooth_boundary, self._n_rings)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def min_angle(self) -> float:
        """Minimum feature angle limit used to identify and preserve features.
        """
        return self._min_angle

    @min_angle.setter
    def min_angle(self, value: float):
        self._min_angle = value

    @property
    def max_angle(self) -> float:
        """Maximum feature angle limit used to identify and preserve features.
        """
        return self._max_angle

    @max_angle.setter
    def max_angle(self, value: float):
        self._max_angle = value

    @property
    def size_field_type(self) -> SizeFieldType:
        """Size field type used to generate surface mesh.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: SizeFieldType):
        self._size_field_type = value

    @property
    def min_size(self) -> float:
        """Minimum size to be used in sizing for the surfer.
        """
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        self._min_size = value

    @property
    def max_size(self) -> float:
        """Maximum size to be used in sizing for the surfer.
        """
        return self._max_size

    @max_size.setter
    def max_size(self, value: float):
        self._max_size = value

    @property
    def growth_rate(self) -> float:
        """Growth rate to be used to propagate sizes.
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, value: float):
        self._growth_rate = value

    @property
    def constant_size(self) -> float:
        """Constant size to be used in case of constant size field.
        """
        return self._constant_size

    @constant_size.setter
    def constant_size(self, value: float):
        self._constant_size = value

    @property
    def smooth_boundary(self) -> bool:
        """Option to extend local selection to get smooth boundary of selected elements.
        """
        return self._smooth_boundary

    @smooth_boundary.setter
    def smooth_boundary(self, value: bool):
        self._smooth_boundary = value

    @property
    def n_rings(self) -> int:
        """Number of rings to extend the registered face selection for remeshing.
        """
        return self._n_rings

    @n_rings.setter
    def n_rings(self, value: int):
        self._n_rings = value

class LocalSurferResults(CoreObject):
    """Results associated with the local surface mesh.

    Parameters
    ----------
    model: Model
        Model to create a ``LocalSurferResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.
    json_data: dict, optional
        JSON dictionary to create a ``LocalSurferResults`` object with provided parameters.

    Examples
    --------
    >>> local_surfer_results = prime.LocalSurferResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``LocalSurferResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``LocalSurferResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        json_data: dict, optional
            JSON dictionary to create a ``LocalSurferResults`` object with provided parameters.

        Examples
        --------
        >>> local_surfer_results = prime.LocalSurferResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "LocalSurferResults")
                    json_data = param_json["LocalSurferResults"] if "LocalSurferResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( LocalSurferResults._default_params["error_code"] if "error_code" in LocalSurferResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( LocalSurferResults._default_params["warning_codes"] if "warning_codes" in LocalSurferResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``LocalSurferResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [LocalSurferResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``LocalSurferResults`` object.

        Examples
        --------
        >>> LocalSurferResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in LocalSurferResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.
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

class CreateShellBLResults(CoreObject):
    """Results associated with the ShellBL mesh.

    Parameters
    ----------
    model: Model
        Model to create a ``CreateShellBLResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    warning_codes: List[WarningCode], optional
        Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``CreateShellBLResults`` object with provided parameters.

    Examples
    --------
    >>> create_shell_blresults = prime.CreateShellBLResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CreateShellBLResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``CreateShellBLResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``CreateShellBLResults`` object with provided parameters.

        Examples
        --------
        >>> create_shell_blresults = prime.CreateShellBLResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CreateShellBLResults")
                    json_data = param_json["CreateShellBLResults"] if "CreateShellBLResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( CreateShellBLResults._default_params["error_code"] if "error_code" in CreateShellBLResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( CreateShellBLResults._default_params["warning_codes"] if "warning_codes" in CreateShellBLResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None):
        """Set the default values of the ``CreateShellBLResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        warning_codes: List[WarningCode], optional
            Warning codes associated with the operation.
        """
        args = locals()
        [CreateShellBLResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CreateShellBLResults`` object.

        Examples
        --------
        >>> CreateShellBLResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CreateShellBLResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning codes associated with the operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

class ShellBLParams(CoreObject):
    """Parameters used to generate ShellBL.

    Parameters
    ----------
    model: Model
        Model to create a ``ShellBLParams`` object with default parameters.
    json_data: dict, optional
        JSON dictionary to create a ``ShellBLParams`` object with provided parameters.

    Examples
    --------
    >>> shell_blparams = prime.ShellBLParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self):
        pass

    def __init__(
            self,
            model: CommunicationManager=None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ShellBLParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ShellBLParams`` object with default parameters.
        json_data: dict, optional
            JSON dictionary to create a ``ShellBLParams`` object with provided parameters.

        Examples
        --------
        >>> shell_blparams = prime.ShellBLParams(model = model)
        """
        if json_data:
            self.__initialize()
        else:
            all_field_specified = all(arg is not None for arg in [])
            if all_field_specified:
                self.__initialize()
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ShellBLParams")
                    json_data = param_json["ShellBLParams"] if "ShellBLParams" in param_json else {}
                    self.__initialize()
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default():
        """Set the default values of the ``ShellBLParams`` object.

        """
        args = locals()
        [ShellBLParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ShellBLParams`` object.

        Examples
        --------
        >>> ShellBLParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ShellBLParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "" % ()
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        if len(message) == 0:
            message = 'The object has no parameters to print.'
        return message
