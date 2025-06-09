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

class MeshStackerResults(CoreObject):
    """Results associated with the mesh stacker operations.

    Parameters
    ----------
    model: Model
        Model to create a ``MeshStackerResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the operation.
    error_codes_per_topo_volume: Iterable[int], optional
        Error codes associated with the topovolume-by-topovolume stacking.
    non_stackable_faces: Iterable[int], optional
        List of non-stackable faces. Note: Under-resolved faceting can also create non-stackable geometry.
    non_stackable_edges: Iterable[int], optional
        List of non-stackable edges. Note: Under-resolved faceting can also create non-stackable geometry.
    small_features: Iterable[int], optional
        List of features edges smaller than input tolerance.
    base_face_ids: Iterable[int], optional
        List of base face ids after base creation.
    size_control_ids: Iterable[int], optional
        List of ids of newly created size controls.
    json_data: dict, optional
        JSON dictionary to create a ``MeshStackerResults`` object with provided parameters.

    Examples
    --------
    >>> mesh_stacker_results = prime.MeshStackerResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            error_codes_per_topo_volume: Iterable[int],
            non_stackable_faces: Iterable[int],
            non_stackable_edges: Iterable[int],
            small_features: Iterable[int],
            base_face_ids: Iterable[int],
            size_control_ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._error_codes_per_topo_volume = error_codes_per_topo_volume if isinstance(error_codes_per_topo_volume, np.ndarray) else np.array(error_codes_per_topo_volume, dtype=np.int32) if error_codes_per_topo_volume is not None else None
        self._non_stackable_faces = non_stackable_faces if isinstance(non_stackable_faces, np.ndarray) else np.array(non_stackable_faces, dtype=np.int32) if non_stackable_faces is not None else None
        self._non_stackable_edges = non_stackable_edges if isinstance(non_stackable_edges, np.ndarray) else np.array(non_stackable_edges, dtype=np.int32) if non_stackable_edges is not None else None
        self._small_features = small_features if isinstance(small_features, np.ndarray) else np.array(small_features, dtype=np.int32) if small_features is not None else None
        self._base_face_ids = base_face_ids if isinstance(base_face_ids, np.ndarray) else np.array(base_face_ids, dtype=np.int32) if base_face_ids is not None else None
        self._size_control_ids = size_control_ids if isinstance(size_control_ids, np.ndarray) else np.array(size_control_ids, dtype=np.int32) if size_control_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            error_codes_per_topo_volume: Iterable[int] = None,
            non_stackable_faces: Iterable[int] = None,
            non_stackable_edges: Iterable[int] = None,
            small_features: Iterable[int] = None,
            base_face_ids: Iterable[int] = None,
            size_control_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MeshStackerResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``MeshStackerResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the operation.
        error_codes_per_topo_volume: Iterable[int], optional
            Error codes associated with the topovolume-by-topovolume stacking.
        non_stackable_faces: Iterable[int], optional
            List of non-stackable faces. Note: Under-resolved faceting can also create non-stackable geometry.
        non_stackable_edges: Iterable[int], optional
            List of non-stackable edges. Note: Under-resolved faceting can also create non-stackable geometry.
        small_features: Iterable[int], optional
            List of features edges smaller than input tolerance.
        base_face_ids: Iterable[int], optional
            List of base face ids after base creation.
        size_control_ids: Iterable[int], optional
            List of ids of newly created size controls.
        json_data: dict, optional
            JSON dictionary to create a ``MeshStackerResults`` object with provided parameters.

        Examples
        --------
        >>> mesh_stacker_results = prime.MeshStackerResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["errorCodesPerTopoVolume"] if "errorCodesPerTopoVolume" in json_data else None,
                json_data["nonStackableFaces"] if "nonStackableFaces" in json_data else None,
                json_data["nonStackableEdges"] if "nonStackableEdges" in json_data else None,
                json_data["smallFeatures"] if "smallFeatures" in json_data else None,
                json_data["baseFaceIds"] if "baseFaceIds" in json_data else None,
                json_data["sizeControlIds"] if "sizeControlIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, error_codes_per_topo_volume, non_stackable_faces, non_stackable_edges, small_features, base_face_ids, size_control_ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    error_codes_per_topo_volume,
                    non_stackable_faces,
                    non_stackable_edges,
                    small_features,
                    base_face_ids,
                    size_control_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MeshStackerResults")
                    json_data = param_json["MeshStackerResults"] if "MeshStackerResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( MeshStackerResults._default_params["error_code"] if "error_code" in MeshStackerResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        error_codes_per_topo_volume if error_codes_per_topo_volume is not None else ( MeshStackerResults._default_params["error_codes_per_topo_volume"] if "error_codes_per_topo_volume" in MeshStackerResults._default_params else (json_data["errorCodesPerTopoVolume"] if "errorCodesPerTopoVolume" in json_data else None)),
                        non_stackable_faces if non_stackable_faces is not None else ( MeshStackerResults._default_params["non_stackable_faces"] if "non_stackable_faces" in MeshStackerResults._default_params else (json_data["nonStackableFaces"] if "nonStackableFaces" in json_data else None)),
                        non_stackable_edges if non_stackable_edges is not None else ( MeshStackerResults._default_params["non_stackable_edges"] if "non_stackable_edges" in MeshStackerResults._default_params else (json_data["nonStackableEdges"] if "nonStackableEdges" in json_data else None)),
                        small_features if small_features is not None else ( MeshStackerResults._default_params["small_features"] if "small_features" in MeshStackerResults._default_params else (json_data["smallFeatures"] if "smallFeatures" in json_data else None)),
                        base_face_ids if base_face_ids is not None else ( MeshStackerResults._default_params["base_face_ids"] if "base_face_ids" in MeshStackerResults._default_params else (json_data["baseFaceIds"] if "baseFaceIds" in json_data else None)),
                        size_control_ids if size_control_ids is not None else ( MeshStackerResults._default_params["size_control_ids"] if "size_control_ids" in MeshStackerResults._default_params else (json_data["sizeControlIds"] if "sizeControlIds" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            error_codes_per_topo_volume: Iterable[int] = None,
            non_stackable_faces: Iterable[int] = None,
            non_stackable_edges: Iterable[int] = None,
            small_features: Iterable[int] = None,
            base_face_ids: Iterable[int] = None,
            size_control_ids: Iterable[int] = None):
        """Set the default values of the ``MeshStackerResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the operation.
        error_codes_per_topo_volume: Iterable[int], optional
            Error codes associated with the topovolume-by-topovolume stacking.
        non_stackable_faces: Iterable[int], optional
            List of non-stackable faces. Note: Under-resolved faceting can also create non-stackable geometry.
        non_stackable_edges: Iterable[int], optional
            List of non-stackable edges. Note: Under-resolved faceting can also create non-stackable geometry.
        small_features: Iterable[int], optional
            List of features edges smaller than input tolerance.
        base_face_ids: Iterable[int], optional
            List of base face ids after base creation.
        size_control_ids: Iterable[int], optional
            List of ids of newly created size controls.
        """
        args = locals()
        [MeshStackerResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MeshStackerResults`` object.

        Examples
        --------
        >>> MeshStackerResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MeshStackerResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._error_codes_per_topo_volume is not None:
            json_data["errorCodesPerTopoVolume"] = self._error_codes_per_topo_volume
        if self._non_stackable_faces is not None:
            json_data["nonStackableFaces"] = self._non_stackable_faces
        if self._non_stackable_edges is not None:
            json_data["nonStackableEdges"] = self._non_stackable_edges
        if self._small_features is not None:
            json_data["smallFeatures"] = self._small_features
        if self._base_face_ids is not None:
            json_data["baseFaceIds"] = self._base_face_ids
        if self._size_control_ids is not None:
            json_data["sizeControlIds"] = self._size_control_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nerror_codes_per_topo_volume :  %s\nnon_stackable_faces :  %s\nnon_stackable_edges :  %s\nsmall_features :  %s\nbase_face_ids :  %s\nsize_control_ids :  %s" % (self._error_code, self._error_codes_per_topo_volume, self._non_stackable_faces, self._non_stackable_edges, self._small_features, self._base_face_ids, self._size_control_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with the operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def error_codes_per_topo_volume(self) -> Iterable[int]:
        """Error codes associated with the topovolume-by-topovolume stacking.
        """
        return self._error_codes_per_topo_volume

    @error_codes_per_topo_volume.setter
    def error_codes_per_topo_volume(self, value: Iterable[int]):
        self._error_codes_per_topo_volume = value

    @property
    def non_stackable_faces(self) -> Iterable[int]:
        """List of non-stackable faces. Note: Under-resolved faceting can also create non-stackable geometry.
        """
        return self._non_stackable_faces

    @non_stackable_faces.setter
    def non_stackable_faces(self, value: Iterable[int]):
        self._non_stackable_faces = value

    @property
    def non_stackable_edges(self) -> Iterable[int]:
        """List of non-stackable edges. Note: Under-resolved faceting can also create non-stackable geometry.
        """
        return self._non_stackable_edges

    @non_stackable_edges.setter
    def non_stackable_edges(self, value: Iterable[int]):
        self._non_stackable_edges = value

    @property
    def small_features(self) -> Iterable[int]:
        """List of features edges smaller than input tolerance.
        """
        return self._small_features

    @small_features.setter
    def small_features(self, value: Iterable[int]):
        self._small_features = value

    @property
    def base_face_ids(self) -> Iterable[int]:
        """List of base face ids after base creation.
        """
        return self._base_face_ids

    @base_face_ids.setter
    def base_face_ids(self, value: Iterable[int]):
        self._base_face_ids = value

    @property
    def size_control_ids(self) -> Iterable[int]:
        """List of ids of newly created size controls.
        """
        return self._size_control_ids

    @size_control_ids.setter
    def size_control_ids(self, value: Iterable[int]):
        self._size_control_ids = value

class MeshStackerParams(CoreObject):
    """Input parameters associated with the mesh stacker operations.

    Parameters
    ----------
    model: Model
        Model to create a ``MeshStackerParams`` object with default parameters.
    origin: Iterable[float], optional
        Origin coordinate list of stacker.
    direction: Iterable[float], optional
        Direction vector of stacker.
    lateral_defeature_tolerance: float, optional
        Absolute lateral distance tolerance for stacker. If the lateral distance tolerance is not specified, a default tolerance value is calculated by stacker.
    stacking_defeature_tolerance: float, optional
        Absolute stacking distance tolerance for stacker. If the stacking distance tolerance is not specified, a default tolerance value is calculated by stacker.
    max_offset_size: float, optional
        Maximum stack size allowed during stacking. If the maximum stack size is not specified, it is set to global max size.
    size_control_ids: Iterable[int], optional
        List of size control ids to be respected by stacker. Stacker respects all supported controls by default.
    seed_faces: Iterable[int], optional
        List of faces whose edges need to be imprinted on the base face. If the faces are meshed, the mesh will be transferred to the base face.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    delete_base: bool, optional
        Option to delete base face at the end of stacking. The default is false.
    json_data: dict, optional
        JSON dictionary to create a ``MeshStackerParams`` object with provided parameters.

    Examples
    --------
    >>> mesh_stacker_params = prime.MeshStackerParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            origin: Iterable[float],
            direction: Iterable[float],
            lateral_defeature_tolerance: float,
            stacking_defeature_tolerance: float,
            max_offset_size: float,
            size_control_ids: Iterable[int],
            seed_faces: Iterable[int],
            delete_base: bool):
        self._origin = origin if isinstance(origin, np.ndarray) else np.array(origin, dtype=np.double) if origin is not None else None
        self._direction = direction if isinstance(direction, np.ndarray) else np.array(direction, dtype=np.double) if direction is not None else None
        self._lateral_defeature_tolerance = lateral_defeature_tolerance
        self._stacking_defeature_tolerance = stacking_defeature_tolerance
        self._max_offset_size = max_offset_size
        self._size_control_ids = size_control_ids if isinstance(size_control_ids, np.ndarray) else np.array(size_control_ids, dtype=np.int32) if size_control_ids is not None else None
        self._seed_faces = seed_faces if isinstance(seed_faces, np.ndarray) else np.array(seed_faces, dtype=np.int32) if seed_faces is not None else None
        self._delete_base = delete_base

    def __init__(
            self,
            model: CommunicationManager=None,
            origin: Iterable[float] = None,
            direction: Iterable[float] = None,
            lateral_defeature_tolerance: float = None,
            stacking_defeature_tolerance: float = None,
            max_offset_size: float = None,
            size_control_ids: Iterable[int] = None,
            seed_faces: Iterable[int] = None,
            delete_base: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``MeshStackerParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``MeshStackerParams`` object with default parameters.
        origin: Iterable[float], optional
            Origin coordinate list of stacker.
        direction: Iterable[float], optional
            Direction vector of stacker.
        lateral_defeature_tolerance: float, optional
            Absolute lateral distance tolerance for stacker. If the lateral distance tolerance is not specified, a default tolerance value is calculated by stacker.
        stacking_defeature_tolerance: float, optional
            Absolute stacking distance tolerance for stacker. If the stacking distance tolerance is not specified, a default tolerance value is calculated by stacker.
        max_offset_size: float, optional
            Maximum stack size allowed during stacking. If the maximum stack size is not specified, it is set to global max size.
        size_control_ids: Iterable[int], optional
            List of size control ids to be respected by stacker. Stacker respects all supported controls by default.
        seed_faces: Iterable[int], optional
            List of faces whose edges need to be imprinted on the base face. If the faces are meshed, the mesh will be transferred to the base face.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        delete_base: bool, optional
            Option to delete base face at the end of stacking. The default is false.
        json_data: dict, optional
            JSON dictionary to create a ``MeshStackerParams`` object with provided parameters.

        Examples
        --------
        >>> mesh_stacker_params = prime.MeshStackerParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["origin"] if "origin" in json_data else None,
                json_data["direction"] if "direction" in json_data else None,
                json_data["lateralDefeatureTolerance"] if "lateralDefeatureTolerance" in json_data else None,
                json_data["stackingDefeatureTolerance"] if "stackingDefeatureTolerance" in json_data else None,
                json_data["maxOffsetSize"] if "maxOffsetSize" in json_data else None,
                json_data["sizeControlIds"] if "sizeControlIds" in json_data else None,
                json_data["seedFaces"] if "seedFaces" in json_data else None,
                json_data["deleteBase"] if "deleteBase" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [origin, direction, lateral_defeature_tolerance, stacking_defeature_tolerance, max_offset_size, size_control_ids, seed_faces, delete_base])
            if all_field_specified:
                self.__initialize(
                    origin,
                    direction,
                    lateral_defeature_tolerance,
                    stacking_defeature_tolerance,
                    max_offset_size,
                    size_control_ids,
                    seed_faces,
                    delete_base)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "MeshStackerParams")
                    json_data = param_json["MeshStackerParams"] if "MeshStackerParams" in param_json else {}
                    self.__initialize(
                        origin if origin is not None else ( MeshStackerParams._default_params["origin"] if "origin" in MeshStackerParams._default_params else (json_data["origin"] if "origin" in json_data else None)),
                        direction if direction is not None else ( MeshStackerParams._default_params["direction"] if "direction" in MeshStackerParams._default_params else (json_data["direction"] if "direction" in json_data else None)),
                        lateral_defeature_tolerance if lateral_defeature_tolerance is not None else ( MeshStackerParams._default_params["lateral_defeature_tolerance"] if "lateral_defeature_tolerance" in MeshStackerParams._default_params else (json_data["lateralDefeatureTolerance"] if "lateralDefeatureTolerance" in json_data else None)),
                        stacking_defeature_tolerance if stacking_defeature_tolerance is not None else ( MeshStackerParams._default_params["stacking_defeature_tolerance"] if "stacking_defeature_tolerance" in MeshStackerParams._default_params else (json_data["stackingDefeatureTolerance"] if "stackingDefeatureTolerance" in json_data else None)),
                        max_offset_size if max_offset_size is not None else ( MeshStackerParams._default_params["max_offset_size"] if "max_offset_size" in MeshStackerParams._default_params else (json_data["maxOffsetSize"] if "maxOffsetSize" in json_data else None)),
                        size_control_ids if size_control_ids is not None else ( MeshStackerParams._default_params["size_control_ids"] if "size_control_ids" in MeshStackerParams._default_params else (json_data["sizeControlIds"] if "sizeControlIds" in json_data else None)),
                        seed_faces if seed_faces is not None else ( MeshStackerParams._default_params["seed_faces"] if "seed_faces" in MeshStackerParams._default_params else (json_data["seedFaces"] if "seedFaces" in json_data else None)),
                        delete_base if delete_base is not None else ( MeshStackerParams._default_params["delete_base"] if "delete_base" in MeshStackerParams._default_params else (json_data["deleteBase"] if "deleteBase" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            origin: Iterable[float] = None,
            direction: Iterable[float] = None,
            lateral_defeature_tolerance: float = None,
            stacking_defeature_tolerance: float = None,
            max_offset_size: float = None,
            size_control_ids: Iterable[int] = None,
            seed_faces: Iterable[int] = None,
            delete_base: bool = None):
        """Set the default values of the ``MeshStackerParams`` object.

        Parameters
        ----------
        origin: Iterable[float], optional
            Origin coordinate list of stacker.
        direction: Iterable[float], optional
            Direction vector of stacker.
        lateral_defeature_tolerance: float, optional
            Absolute lateral distance tolerance for stacker. If the lateral distance tolerance is not specified, a default tolerance value is calculated by stacker.
        stacking_defeature_tolerance: float, optional
            Absolute stacking distance tolerance for stacker. If the stacking distance tolerance is not specified, a default tolerance value is calculated by stacker.
        max_offset_size: float, optional
            Maximum stack size allowed during stacking. If the maximum stack size is not specified, it is set to global max size.
        size_control_ids: Iterable[int], optional
            List of size control ids to be respected by stacker. Stacker respects all supported controls by default.
        seed_faces: Iterable[int], optional
            List of faces whose edges need to be imprinted on the base face. If the faces are meshed, the mesh will be transferred to the base face.
        delete_base: bool, optional
            Option to delete base face at the end of stacking. The default is false.
        """
        args = locals()
        [MeshStackerParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``MeshStackerParams`` object.

        Examples
        --------
        >>> MeshStackerParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in MeshStackerParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._origin is not None:
            json_data["origin"] = self._origin
        if self._direction is not None:
            json_data["direction"] = self._direction
        if self._lateral_defeature_tolerance is not None:
            json_data["lateralDefeatureTolerance"] = self._lateral_defeature_tolerance
        if self._stacking_defeature_tolerance is not None:
            json_data["stackingDefeatureTolerance"] = self._stacking_defeature_tolerance
        if self._max_offset_size is not None:
            json_data["maxOffsetSize"] = self._max_offset_size
        if self._size_control_ids is not None:
            json_data["sizeControlIds"] = self._size_control_ids
        if self._seed_faces is not None:
            json_data["seedFaces"] = self._seed_faces
        if self._delete_base is not None:
            json_data["deleteBase"] = self._delete_base
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "origin :  %s\ndirection :  %s\nlateral_defeature_tolerance :  %s\nstacking_defeature_tolerance :  %s\nmax_offset_size :  %s\nsize_control_ids :  %s\nseed_faces :  %s\ndelete_base :  %s" % (self._origin, self._direction, self._lateral_defeature_tolerance, self._stacking_defeature_tolerance, self._max_offset_size, self._size_control_ids, self._seed_faces, self._delete_base)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def origin(self) -> Iterable[float]:
        """Origin coordinate list of stacker.
        """
        return self._origin

    @origin.setter
    def origin(self, value: Iterable[float]):
        self._origin = value

    @property
    def direction(self) -> Iterable[float]:
        """Direction vector of stacker.
        """
        return self._direction

    @direction.setter
    def direction(self, value: Iterable[float]):
        self._direction = value

    @property
    def lateral_defeature_tolerance(self) -> float:
        """Absolute lateral distance tolerance for stacker. If the lateral distance tolerance is not specified, a default tolerance value is calculated by stacker.
        """
        return self._lateral_defeature_tolerance

    @lateral_defeature_tolerance.setter
    def lateral_defeature_tolerance(self, value: float):
        self._lateral_defeature_tolerance = value

    @property
    def stacking_defeature_tolerance(self) -> float:
        """Absolute stacking distance tolerance for stacker. If the stacking distance tolerance is not specified, a default tolerance value is calculated by stacker.
        """
        return self._stacking_defeature_tolerance

    @stacking_defeature_tolerance.setter
    def stacking_defeature_tolerance(self, value: float):
        self._stacking_defeature_tolerance = value

    @property
    def max_offset_size(self) -> float:
        """Maximum stack size allowed during stacking. If the maximum stack size is not specified, it is set to global max size.
        """
        return self._max_offset_size

    @max_offset_size.setter
    def max_offset_size(self, value: float):
        self._max_offset_size = value

    @property
    def size_control_ids(self) -> Iterable[int]:
        """List of size control ids to be respected by stacker. Stacker respects all supported controls by default.
        """
        return self._size_control_ids

    @size_control_ids.setter
    def size_control_ids(self, value: Iterable[int]):
        self._size_control_ids = value

    @property
    def seed_faces(self) -> Iterable[int]:
        """List of faces whose edges need to be imprinted on the base face. If the faces are meshed, the mesh will be transferred to the base face.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._seed_faces

    @seed_faces.setter
    def seed_faces(self, value: Iterable[int]):
        self._seed_faces = value

    @property
    def delete_base(self) -> bool:
        """Option to delete base face at the end of stacking. The default is false.
        """
        return self._delete_base

    @delete_base.setter
    def delete_base(self, value: bool):
        self._delete_base = value
