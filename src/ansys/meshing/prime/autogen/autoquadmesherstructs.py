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

class EdgeConnectType(enum.IntEnum):
    """Edge connect type to define the type of connection between edges .
    """
    NONE = 0
    """Perform no connection.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    ALLTOALL = 1
    """Perform connections between any type of edges or faces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FREETOALL = 2
    """Perform connections between free edges and any type of edges or faces.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FREETOFREE = 3
    """Perform connections between free edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class DetectHolesParams(CoreObject):
    """Parameters for detect holes operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectHolesParams`` object with default parameters.
    max_radius_circular_holes: float, optional
        Maximum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    min_radius_circular_holes: float, optional
        Minimum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    max_hole_length: float, optional
        Maximum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    min_hole_length: float, optional
        Minimum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    allow_curved_topo_faces: bool, optional
        Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectHolesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_holes_params = prime.DetectHolesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            max_radius_circular_holes: float,
            min_radius_circular_holes: float,
            max_hole_length: float,
            min_hole_length: float,
            allow_curved_topo_faces: bool):
        self._max_radius_circular_holes = max_radius_circular_holes
        self._min_radius_circular_holes = min_radius_circular_holes
        self._max_hole_length = max_hole_length
        self._min_hole_length = min_hole_length
        self._allow_curved_topo_faces = allow_curved_topo_faces

    def __init__(
            self,
            model: CommunicationManager=None,
            max_radius_circular_holes: float = None,
            min_radius_circular_holes: float = None,
            max_hole_length: float = None,
            min_hole_length: float = None,
            allow_curved_topo_faces: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectHolesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectHolesParams`` object with default parameters.
        max_radius_circular_holes: float, optional
            Maximum radius of circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        min_radius_circular_holes: float, optional
            Minimum radius of circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        max_hole_length: float, optional
            Maximum length of holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        min_hole_length: float, optional
            Minimum length of holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectHolesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_holes_params = prime.DetectHolesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["maxRadiusCircularHoles"] if "maxRadiusCircularHoles" in json_data else None,
                json_data["minRadiusCircularHoles"] if "minRadiusCircularHoles" in json_data else None,
                json_data["maxHoleLength"] if "maxHoleLength" in json_data else None,
                json_data["minHoleLength"] if "minHoleLength" in json_data else None,
                json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [max_radius_circular_holes, min_radius_circular_holes, max_hole_length, min_hole_length, allow_curved_topo_faces])
            if all_field_specified:
                self.__initialize(
                    max_radius_circular_holes,
                    min_radius_circular_holes,
                    max_hole_length,
                    min_hole_length,
                    allow_curved_topo_faces)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectHolesParams")
                    json_data = param_json["DetectHolesParams"] if "DetectHolesParams" in param_json else {}
                    self.__initialize(
                        max_radius_circular_holes if max_radius_circular_holes is not None else ( DetectHolesParams._default_params["max_radius_circular_holes"] if "max_radius_circular_holes" in DetectHolesParams._default_params else (json_data["maxRadiusCircularHoles"] if "maxRadiusCircularHoles" in json_data else None)),
                        min_radius_circular_holes if min_radius_circular_holes is not None else ( DetectHolesParams._default_params["min_radius_circular_holes"] if "min_radius_circular_holes" in DetectHolesParams._default_params else (json_data["minRadiusCircularHoles"] if "minRadiusCircularHoles" in json_data else None)),
                        max_hole_length if max_hole_length is not None else ( DetectHolesParams._default_params["max_hole_length"] if "max_hole_length" in DetectHolesParams._default_params else (json_data["maxHoleLength"] if "maxHoleLength" in json_data else None)),
                        min_hole_length if min_hole_length is not None else ( DetectHolesParams._default_params["min_hole_length"] if "min_hole_length" in DetectHolesParams._default_params else (json_data["minHoleLength"] if "minHoleLength" in json_data else None)),
                        allow_curved_topo_faces if allow_curved_topo_faces is not None else ( DetectHolesParams._default_params["allow_curved_topo_faces"] if "allow_curved_topo_faces" in DetectHolesParams._default_params else (json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            max_radius_circular_holes: float = None,
            min_radius_circular_holes: float = None,
            max_hole_length: float = None,
            min_hole_length: float = None,
            allow_curved_topo_faces: bool = None):
        """Set the default values of the ``DetectHolesParams`` object.

        Parameters
        ----------
        max_radius_circular_holes: float, optional
            Maximum radius of circular holes.
        min_radius_circular_holes: float, optional
            Minimum radius of circular holes.
        max_hole_length: float, optional
            Maximum length of holes.
        min_hole_length: float, optional
            Minimum length of holes.
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.
        """
        args = locals()
        [DetectHolesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectHolesParams`` object.

        Examples
        --------
        >>> DetectHolesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectHolesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._max_radius_circular_holes is not None:
            json_data["maxRadiusCircularHoles"] = self._max_radius_circular_holes
        if self._min_radius_circular_holes is not None:
            json_data["minRadiusCircularHoles"] = self._min_radius_circular_holes
        if self._max_hole_length is not None:
            json_data["maxHoleLength"] = self._max_hole_length
        if self._min_hole_length is not None:
            json_data["minHoleLength"] = self._min_hole_length
        if self._allow_curved_topo_faces is not None:
            json_data["allowCurvedTopoFaces"] = self._allow_curved_topo_faces
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "max_radius_circular_holes :  %s\nmin_radius_circular_holes :  %s\nmax_hole_length :  %s\nmin_hole_length :  %s\nallow_curved_topo_faces :  %s" % (self._max_radius_circular_holes, self._min_radius_circular_holes, self._max_hole_length, self._min_hole_length, self._allow_curved_topo_faces)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def max_radius_circular_holes(self) -> float:
        """Maximum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._max_radius_circular_holes

    @max_radius_circular_holes.setter
    def max_radius_circular_holes(self, value: float):
        self._max_radius_circular_holes = value

    @property
    def min_radius_circular_holes(self) -> float:
        """Minimum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._min_radius_circular_holes

    @min_radius_circular_holes.setter
    def min_radius_circular_holes(self, value: float):
        self._min_radius_circular_holes = value

    @property
    def max_hole_length(self) -> float:
        """Maximum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._max_hole_length

    @max_hole_length.setter
    def max_hole_length(self, value: float):
        self._max_hole_length = value

    @property
    def min_hole_length(self) -> float:
        """Minimum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._min_hole_length

    @min_hole_length.setter
    def min_hole_length(self, value: float):
        self._min_hole_length = value

    @property
    def allow_curved_topo_faces(self) -> bool:
        """Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._allow_curved_topo_faces

    @allow_curved_topo_faces.setter
    def allow_curved_topo_faces(self, value: bool):
        self._allow_curved_topo_faces = value

class DetectCircularHolesParams(CoreObject):
    """Parameters for detect circular holes operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectCircularHolesParams`` object with default parameters.
    allow_curved_topo_faces: bool, optional
        Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    max_radius_circular_holes: float, optional
        Maximum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    min_radius_circular_holes: float, optional
        Minimum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectCircularHolesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_circular_holes_params = prime.DetectCircularHolesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            allow_curved_topo_faces: bool,
            max_radius_circular_holes: float,
            min_radius_circular_holes: float,
            merge_edge_allow_self_close: bool):
        self._allow_curved_topo_faces = allow_curved_topo_faces
        self._max_radius_circular_holes = max_radius_circular_holes
        self._min_radius_circular_holes = min_radius_circular_holes
        self._merge_edge_allow_self_close = merge_edge_allow_self_close

    def __init__(
            self,
            model: CommunicationManager=None,
            allow_curved_topo_faces: bool = None,
            max_radius_circular_holes: float = None,
            min_radius_circular_holes: float = None,
            merge_edge_allow_self_close: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectCircularHolesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectCircularHolesParams`` object with default parameters.
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        max_radius_circular_holes: float, optional
            Maximum radius of circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        min_radius_circular_holes: float, optional
            Minimum radius of circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectCircularHolesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_circular_holes_params = prime.DetectCircularHolesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None,
                json_data["maxRadiusCircularHoles"] if "maxRadiusCircularHoles" in json_data else None,
                json_data["minRadiusCircularHoles"] if "minRadiusCircularHoles" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [allow_curved_topo_faces, max_radius_circular_holes, min_radius_circular_holes, merge_edge_allow_self_close])
            if all_field_specified:
                self.__initialize(
                    allow_curved_topo_faces,
                    max_radius_circular_holes,
                    min_radius_circular_holes,
                    merge_edge_allow_self_close)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectCircularHolesParams")
                    json_data = param_json["DetectCircularHolesParams"] if "DetectCircularHolesParams" in param_json else {}
                    self.__initialize(
                        allow_curved_topo_faces if allow_curved_topo_faces is not None else ( DetectCircularHolesParams._default_params["allow_curved_topo_faces"] if "allow_curved_topo_faces" in DetectCircularHolesParams._default_params else (json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None)),
                        max_radius_circular_holes if max_radius_circular_holes is not None else ( DetectCircularHolesParams._default_params["max_radius_circular_holes"] if "max_radius_circular_holes" in DetectCircularHolesParams._default_params else (json_data["maxRadiusCircularHoles"] if "maxRadiusCircularHoles" in json_data else None)),
                        min_radius_circular_holes if min_radius_circular_holes is not None else ( DetectCircularHolesParams._default_params["min_radius_circular_holes"] if "min_radius_circular_holes" in DetectCircularHolesParams._default_params else (json_data["minRadiusCircularHoles"] if "minRadiusCircularHoles" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( DetectCircularHolesParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in DetectCircularHolesParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            allow_curved_topo_faces: bool = None,
            max_radius_circular_holes: float = None,
            min_radius_circular_holes: float = None,
            merge_edge_allow_self_close: bool = None):
        """Set the default values of the ``DetectCircularHolesParams`` object.

        Parameters
        ----------
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.
        max_radius_circular_holes: float, optional
            Maximum radius of circular holes.
        min_radius_circular_holes: float, optional
            Minimum radius of circular holes.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        """
        args = locals()
        [DetectCircularHolesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectCircularHolesParams`` object.

        Examples
        --------
        >>> DetectCircularHolesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectCircularHolesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._allow_curved_topo_faces is not None:
            json_data["allowCurvedTopoFaces"] = self._allow_curved_topo_faces
        if self._max_radius_circular_holes is not None:
            json_data["maxRadiusCircularHoles"] = self._max_radius_circular_holes
        if self._min_radius_circular_holes is not None:
            json_data["minRadiusCircularHoles"] = self._min_radius_circular_holes
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "allow_curved_topo_faces :  %s\nmax_radius_circular_holes :  %s\nmin_radius_circular_holes :  %s\nmerge_edge_allow_self_close :  %s" % (self._allow_curved_topo_faces, self._max_radius_circular_holes, self._min_radius_circular_holes, self._merge_edge_allow_self_close)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def allow_curved_topo_faces(self) -> bool:
        """Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._allow_curved_topo_faces

    @allow_curved_topo_faces.setter
    def allow_curved_topo_faces(self, value: bool):
        self._allow_curved_topo_faces = value

    @property
    def max_radius_circular_holes(self) -> float:
        """Maximum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._max_radius_circular_holes

    @max_radius_circular_holes.setter
    def max_radius_circular_holes(self, value: float):
        self._max_radius_circular_holes = value

    @property
    def min_radius_circular_holes(self) -> float:
        """Minimum radius of circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._min_radius_circular_holes

    @min_radius_circular_holes.setter
    def min_radius_circular_holes(self, value: float):
        self._min_radius_circular_holes = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

class DetectNonCircularHolesParams(CoreObject):
    """Parameters for detect non circular holes operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectNonCircularHolesParams`` object with default parameters.
    allow_curved_topo_faces: bool, optional
        Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    max_hole_length: float, optional
        Maximum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    min_hole_length: float, optional
        Minimum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectNonCircularHolesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_non_circular_holes_params = prime.DetectNonCircularHolesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            allow_curved_topo_faces: bool,
            max_hole_length: float,
            min_hole_length: float,
            merge_edge_allow_self_close: bool):
        self._allow_curved_topo_faces = allow_curved_topo_faces
        self._max_hole_length = max_hole_length
        self._min_hole_length = min_hole_length
        self._merge_edge_allow_self_close = merge_edge_allow_self_close

    def __init__(
            self,
            model: CommunicationManager=None,
            allow_curved_topo_faces: bool = None,
            max_hole_length: float = None,
            min_hole_length: float = None,
            merge_edge_allow_self_close: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectNonCircularHolesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectNonCircularHolesParams`` object with default parameters.
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        max_hole_length: float, optional
            Maximum length of holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        min_hole_length: float, optional
            Minimum length of holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectNonCircularHolesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_non_circular_holes_params = prime.DetectNonCircularHolesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None,
                json_data["maxHoleLength"] if "maxHoleLength" in json_data else None,
                json_data["minHoleLength"] if "minHoleLength" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [allow_curved_topo_faces, max_hole_length, min_hole_length, merge_edge_allow_self_close])
            if all_field_specified:
                self.__initialize(
                    allow_curved_topo_faces,
                    max_hole_length,
                    min_hole_length,
                    merge_edge_allow_self_close)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectNonCircularHolesParams")
                    json_data = param_json["DetectNonCircularHolesParams"] if "DetectNonCircularHolesParams" in param_json else {}
                    self.__initialize(
                        allow_curved_topo_faces if allow_curved_topo_faces is not None else ( DetectNonCircularHolesParams._default_params["allow_curved_topo_faces"] if "allow_curved_topo_faces" in DetectNonCircularHolesParams._default_params else (json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None)),
                        max_hole_length if max_hole_length is not None else ( DetectNonCircularHolesParams._default_params["max_hole_length"] if "max_hole_length" in DetectNonCircularHolesParams._default_params else (json_data["maxHoleLength"] if "maxHoleLength" in json_data else None)),
                        min_hole_length if min_hole_length is not None else ( DetectNonCircularHolesParams._default_params["min_hole_length"] if "min_hole_length" in DetectNonCircularHolesParams._default_params else (json_data["minHoleLength"] if "minHoleLength" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( DetectNonCircularHolesParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in DetectNonCircularHolesParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            allow_curved_topo_faces: bool = None,
            max_hole_length: float = None,
            min_hole_length: float = None,
            merge_edge_allow_self_close: bool = None):
        """Set the default values of the ``DetectNonCircularHolesParams`` object.

        Parameters
        ----------
        allow_curved_topo_faces: bool, optional
            Option to allow holes in curved topoface.
        max_hole_length: float, optional
            Maximum length of holes.
        min_hole_length: float, optional
            Minimum length of holes.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        """
        args = locals()
        [DetectNonCircularHolesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectNonCircularHolesParams`` object.

        Examples
        --------
        >>> DetectNonCircularHolesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectNonCircularHolesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._allow_curved_topo_faces is not None:
            json_data["allowCurvedTopoFaces"] = self._allow_curved_topo_faces
        if self._max_hole_length is not None:
            json_data["maxHoleLength"] = self._max_hole_length
        if self._min_hole_length is not None:
            json_data["minHoleLength"] = self._min_hole_length
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "allow_curved_topo_faces :  %s\nmax_hole_length :  %s\nmin_hole_length :  %s\nmerge_edge_allow_self_close :  %s" % (self._allow_curved_topo_faces, self._max_hole_length, self._min_hole_length, self._merge_edge_allow_self_close)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def allow_curved_topo_faces(self) -> bool:
        """Option to allow holes in curved topoface.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._allow_curved_topo_faces

    @allow_curved_topo_faces.setter
    def allow_curved_topo_faces(self, value: bool):
        self._allow_curved_topo_faces = value

    @property
    def max_hole_length(self) -> float:
        """Maximum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._max_hole_length

    @max_hole_length.setter
    def max_hole_length(self, value: float):
        self._max_hole_length = value

    @property
    def min_hole_length(self) -> float:
        """Minimum length of holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._min_hole_length

    @min_hole_length.setter
    def min_hole_length(self, value: float):
        self._min_hole_length = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

class DetectAndTreatCircularFacesParams(CoreObject):
    """Parameters for detect and treat circular faces operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectAndTreatCircularFacesParams`` object with default parameters.
    edge_mesh_constant_size: float, optional
        Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    surface_mesh_constant_size: float, optional
        Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_face_normals_angle: float, optional
        Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectAndTreatCircularFacesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_and_treat_circular_faces_params = prime.DetectAndTreatCircularFacesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            edge_mesh_constant_size: float,
            surface_mesh_constant_size: float,
            merge_edge_allow_self_close: bool,
            merge_face_normals_angle: float):
        self._edge_mesh_constant_size = edge_mesh_constant_size
        self._surface_mesh_constant_size = surface_mesh_constant_size
        self._merge_edge_allow_self_close = merge_edge_allow_self_close
        self._merge_face_normals_angle = merge_face_normals_angle

    def __init__(
            self,
            model: CommunicationManager=None,
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None,
            merge_edge_allow_self_close: bool = None,
            merge_face_normals_angle: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectAndTreatCircularFacesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectAndTreatCircularFacesParams`` object with default parameters.
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectAndTreatCircularFacesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_and_treat_circular_faces_params = prime.DetectAndTreatCircularFacesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None,
                json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None,
                json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [edge_mesh_constant_size, surface_mesh_constant_size, merge_edge_allow_self_close, merge_face_normals_angle])
            if all_field_specified:
                self.__initialize(
                    edge_mesh_constant_size,
                    surface_mesh_constant_size,
                    merge_edge_allow_self_close,
                    merge_face_normals_angle)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectAndTreatCircularFacesParams")
                    json_data = param_json["DetectAndTreatCircularFacesParams"] if "DetectAndTreatCircularFacesParams" in param_json else {}
                    self.__initialize(
                        edge_mesh_constant_size if edge_mesh_constant_size is not None else ( DetectAndTreatCircularFacesParams._default_params["edge_mesh_constant_size"] if "edge_mesh_constant_size" in DetectAndTreatCircularFacesParams._default_params else (json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None)),
                        surface_mesh_constant_size if surface_mesh_constant_size is not None else ( DetectAndTreatCircularFacesParams._default_params["surface_mesh_constant_size"] if "surface_mesh_constant_size" in DetectAndTreatCircularFacesParams._default_params else (json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( DetectAndTreatCircularFacesParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in DetectAndTreatCircularFacesParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)),
                        merge_face_normals_angle if merge_face_normals_angle is not None else ( DetectAndTreatCircularFacesParams._default_params["merge_face_normals_angle"] if "merge_face_normals_angle" in DetectAndTreatCircularFacesParams._default_params else (json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None,
            merge_edge_allow_self_close: bool = None,
            merge_face_normals_angle: float = None):
        """Set the default values of the ``DetectAndTreatCircularFacesParams`` object.

        Parameters
        ----------
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.
        """
        args = locals()
        [DetectAndTreatCircularFacesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectAndTreatCircularFacesParams`` object.

        Examples
        --------
        >>> DetectAndTreatCircularFacesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectAndTreatCircularFacesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._edge_mesh_constant_size is not None:
            json_data["edgeMeshConstantSize"] = self._edge_mesh_constant_size
        if self._surface_mesh_constant_size is not None:
            json_data["surfaceMeshConstantSize"] = self._surface_mesh_constant_size
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        if self._merge_face_normals_angle is not None:
            json_data["mergeFaceNormalsAngle"] = self._merge_face_normals_angle
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "edge_mesh_constant_size :  %s\nsurface_mesh_constant_size :  %s\nmerge_edge_allow_self_close :  %s\nmerge_face_normals_angle :  %s" % (self._edge_mesh_constant_size, self._surface_mesh_constant_size, self._merge_edge_allow_self_close, self._merge_face_normals_angle)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def edge_mesh_constant_size(self) -> float:
        """Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_mesh_constant_size

    @edge_mesh_constant_size.setter
    def edge_mesh_constant_size(self, value: float):
        self._edge_mesh_constant_size = value

    @property
    def surface_mesh_constant_size(self) -> float:
        """Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._surface_mesh_constant_size

    @surface_mesh_constant_size.setter
    def surface_mesh_constant_size(self, value: float):
        self._surface_mesh_constant_size = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

    @property
    def merge_face_normals_angle(self) -> float:
        """Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_face_normals_angle

    @merge_face_normals_angle.setter
    def merge_face_normals_angle(self, value: float):
        self._merge_face_normals_angle = value

class ConnectFacesParams(CoreObject):
    """Parameters for connect faces operation.

    Parameters
    ----------
    model: Model
        Model to create a ``ConnectFacesParams`` object with default parameters.
    constant_mesh_size: float, optional
        Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    absolute_tolerance: float, optional
        Absolute distance tolerance between edges or faces for connect faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ConnectFacesParams`` object with provided parameters.

    Examples
    --------
    >>> connect_faces_params = prime.ConnectFacesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            constant_mesh_size: float,
            absolute_tolerance: float):
        self._constant_mesh_size = constant_mesh_size
        self._absolute_tolerance = absolute_tolerance

    def __init__(
            self,
            model: CommunicationManager=None,
            constant_mesh_size: float = None,
            absolute_tolerance: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ConnectFacesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ConnectFacesParams`` object with default parameters.
        constant_mesh_size: float, optional
            Constant size used for surface meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        absolute_tolerance: float, optional
            Absolute distance tolerance between edges or faces for connect faces operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ConnectFacesParams`` object with provided parameters.

        Examples
        --------
        >>> connect_faces_params = prime.ConnectFacesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["constantMeshSize"] if "constantMeshSize" in json_data else None,
                json_data["absoluteTolerance"] if "absoluteTolerance" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [constant_mesh_size, absolute_tolerance])
            if all_field_specified:
                self.__initialize(
                    constant_mesh_size,
                    absolute_tolerance)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ConnectFacesParams")
                    json_data = param_json["ConnectFacesParams"] if "ConnectFacesParams" in param_json else {}
                    self.__initialize(
                        constant_mesh_size if constant_mesh_size is not None else ( ConnectFacesParams._default_params["constant_mesh_size"] if "constant_mesh_size" in ConnectFacesParams._default_params else (json_data["constantMeshSize"] if "constantMeshSize" in json_data else None)),
                        absolute_tolerance if absolute_tolerance is not None else ( ConnectFacesParams._default_params["absolute_tolerance"] if "absolute_tolerance" in ConnectFacesParams._default_params else (json_data["absoluteTolerance"] if "absoluteTolerance" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            constant_mesh_size: float = None,
            absolute_tolerance: float = None):
        """Set the default values of the ``ConnectFacesParams`` object.

        Parameters
        ----------
        constant_mesh_size: float, optional
            Constant size used for surface meshing.
        absolute_tolerance: float, optional
            Absolute distance tolerance between edges or faces for connect faces operation.
        """
        args = locals()
        [ConnectFacesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ConnectFacesParams`` object.

        Examples
        --------
        >>> ConnectFacesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ConnectFacesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._constant_mesh_size is not None:
            json_data["constantMeshSize"] = self._constant_mesh_size
        if self._absolute_tolerance is not None:
            json_data["absoluteTolerance"] = self._absolute_tolerance
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "constant_mesh_size :  %s\nabsolute_tolerance :  %s" % (self._constant_mesh_size, self._absolute_tolerance)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def constant_mesh_size(self) -> float:
        """Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._constant_mesh_size

    @constant_mesh_size.setter
    def constant_mesh_size(self, value: float):
        self._constant_mesh_size = value

    @property
    def absolute_tolerance(self) -> float:
        """Absolute distance tolerance between edges or faces for connect faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._absolute_tolerance

    @absolute_tolerance.setter
    def absolute_tolerance(self, value: float):
        self._absolute_tolerance = value

class RepairEdgesParams(CoreObject):
    """Parameters for repair edges operation.

    Parameters
    ----------
    model: Model
        Model to create a ``RepairEdgesParams`` object with default parameters.
    constant_mesh_size: float, optional
        Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    absolute_tolerance: float, optional
        Absolute distance tolerance between nodes or edges for repair edges operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``RepairEdgesParams`` object with provided parameters.

    Examples
    --------
    >>> repair_edges_params = prime.RepairEdgesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            constant_mesh_size: float,
            absolute_tolerance: float):
        self._constant_mesh_size = constant_mesh_size
        self._absolute_tolerance = absolute_tolerance

    def __init__(
            self,
            model: CommunicationManager=None,
            constant_mesh_size: float = None,
            absolute_tolerance: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``RepairEdgesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``RepairEdgesParams`` object with default parameters.
        constant_mesh_size: float, optional
            Constant size used for surface meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        absolute_tolerance: float, optional
            Absolute distance tolerance between nodes or edges for repair edges operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``RepairEdgesParams`` object with provided parameters.

        Examples
        --------
        >>> repair_edges_params = prime.RepairEdgesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["constantMeshSize"] if "constantMeshSize" in json_data else None,
                json_data["absoluteTolerance"] if "absoluteTolerance" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [constant_mesh_size, absolute_tolerance])
            if all_field_specified:
                self.__initialize(
                    constant_mesh_size,
                    absolute_tolerance)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "RepairEdgesParams")
                    json_data = param_json["RepairEdgesParams"] if "RepairEdgesParams" in param_json else {}
                    self.__initialize(
                        constant_mesh_size if constant_mesh_size is not None else ( RepairEdgesParams._default_params["constant_mesh_size"] if "constant_mesh_size" in RepairEdgesParams._default_params else (json_data["constantMeshSize"] if "constantMeshSize" in json_data else None)),
                        absolute_tolerance if absolute_tolerance is not None else ( RepairEdgesParams._default_params["absolute_tolerance"] if "absolute_tolerance" in RepairEdgesParams._default_params else (json_data["absoluteTolerance"] if "absoluteTolerance" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            constant_mesh_size: float = None,
            absolute_tolerance: float = None):
        """Set the default values of the ``RepairEdgesParams`` object.

        Parameters
        ----------
        constant_mesh_size: float, optional
            Constant size used for surface meshing.
        absolute_tolerance: float, optional
            Absolute distance tolerance between nodes or edges for repair edges operation.
        """
        args = locals()
        [RepairEdgesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``RepairEdgesParams`` object.

        Examples
        --------
        >>> RepairEdgesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RepairEdgesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._constant_mesh_size is not None:
            json_data["constantMeshSize"] = self._constant_mesh_size
        if self._absolute_tolerance is not None:
            json_data["absoluteTolerance"] = self._absolute_tolerance
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "constant_mesh_size :  %s\nabsolute_tolerance :  %s" % (self._constant_mesh_size, self._absolute_tolerance)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def constant_mesh_size(self) -> float:
        """Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._constant_mesh_size

    @constant_mesh_size.setter
    def constant_mesh_size(self, value: float):
        self._constant_mesh_size = value

    @property
    def absolute_tolerance(self) -> float:
        """Absolute distance tolerance between nodes or edges for repair edges operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._absolute_tolerance

    @absolute_tolerance.setter
    def absolute_tolerance(self, value: float):
        self._absolute_tolerance = value

class PartialDefeatureParams(CoreObject):
    """Parameters for partial defeature operation.

    Parameters
    ----------
    model: Model
        Model to create a ``PartialDefeatureParams`` object with default parameters.
    edge_sharp_corner_angle: float, optional
        Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_face_normals_angle: float, optional
        Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``PartialDefeatureParams`` object with provided parameters.

    Examples
    --------
    >>> partial_defeature_params = prime.PartialDefeatureParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            edge_sharp_corner_angle: float,
            merge_face_normals_angle: float,
            merge_edge_allow_self_close: bool):
        self._edge_sharp_corner_angle = edge_sharp_corner_angle
        self._merge_face_normals_angle = merge_face_normals_angle
        self._merge_edge_allow_self_close = merge_edge_allow_self_close

    def __init__(
            self,
            model: CommunicationManager=None,
            edge_sharp_corner_angle: float = None,
            merge_face_normals_angle: float = None,
            merge_edge_allow_self_close: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``PartialDefeatureParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``PartialDefeatureParams`` object with default parameters.
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``PartialDefeatureParams`` object with provided parameters.

        Examples
        --------
        >>> partial_defeature_params = prime.PartialDefeatureParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None,
                json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [edge_sharp_corner_angle, merge_face_normals_angle, merge_edge_allow_self_close])
            if all_field_specified:
                self.__initialize(
                    edge_sharp_corner_angle,
                    merge_face_normals_angle,
                    merge_edge_allow_self_close)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "PartialDefeatureParams")
                    json_data = param_json["PartialDefeatureParams"] if "PartialDefeatureParams" in param_json else {}
                    self.__initialize(
                        edge_sharp_corner_angle if edge_sharp_corner_angle is not None else ( PartialDefeatureParams._default_params["edge_sharp_corner_angle"] if "edge_sharp_corner_angle" in PartialDefeatureParams._default_params else (json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None)),
                        merge_face_normals_angle if merge_face_normals_angle is not None else ( PartialDefeatureParams._default_params["merge_face_normals_angle"] if "merge_face_normals_angle" in PartialDefeatureParams._default_params else (json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( PartialDefeatureParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in PartialDefeatureParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            edge_sharp_corner_angle: float = None,
            merge_face_normals_angle: float = None,
            merge_edge_allow_self_close: bool = None):
        """Set the default values of the ``PartialDefeatureParams`` object.

        Parameters
        ----------
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        """
        args = locals()
        [PartialDefeatureParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``PartialDefeatureParams`` object.

        Examples
        --------
        >>> PartialDefeatureParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in PartialDefeatureParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._edge_sharp_corner_angle is not None:
            json_data["edgeSharpCornerAngle"] = self._edge_sharp_corner_angle
        if self._merge_face_normals_angle is not None:
            json_data["mergeFaceNormalsAngle"] = self._merge_face_normals_angle
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "edge_sharp_corner_angle :  %s\nmerge_face_normals_angle :  %s\nmerge_edge_allow_self_close :  %s" % (self._edge_sharp_corner_angle, self._merge_face_normals_angle, self._merge_edge_allow_self_close)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def edge_sharp_corner_angle(self) -> float:
        """Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_sharp_corner_angle

    @edge_sharp_corner_angle.setter
    def edge_sharp_corner_angle(self, value: float):
        self._edge_sharp_corner_angle = value

    @property
    def merge_face_normals_angle(self) -> float:
        """Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_face_normals_angle

    @merge_face_normals_angle.setter
    def merge_face_normals_angle(self, value: float):
        self._merge_face_normals_angle = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

class DeleteInteriorNodesParams(CoreObject):
    """Parameters for delete interior nodes operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DeleteInteriorNodesParams`` object with default parameters.
    merge_face_normals_angle: float, optional
        Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_sharp_corner_angle: float, optional
        Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DeleteInteriorNodesParams`` object with provided parameters.

    Examples
    --------
    >>> delete_interior_nodes_params = prime.DeleteInteriorNodesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            merge_face_normals_angle: float,
            merge_edge_allow_self_close: bool,
            edge_sharp_corner_angle: float):
        self._merge_face_normals_angle = merge_face_normals_angle
        self._merge_edge_allow_self_close = merge_edge_allow_self_close
        self._edge_sharp_corner_angle = edge_sharp_corner_angle

    def __init__(
            self,
            model: CommunicationManager=None,
            merge_face_normals_angle: float = None,
            merge_edge_allow_self_close: bool = None,
            edge_sharp_corner_angle: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DeleteInteriorNodesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DeleteInteriorNodesParams`` object with default parameters.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DeleteInteriorNodesParams`` object with provided parameters.

        Examples
        --------
        >>> delete_interior_nodes_params = prime.DeleteInteriorNodesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None,
                json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [merge_face_normals_angle, merge_edge_allow_self_close, edge_sharp_corner_angle])
            if all_field_specified:
                self.__initialize(
                    merge_face_normals_angle,
                    merge_edge_allow_self_close,
                    edge_sharp_corner_angle)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteInteriorNodesParams")
                    json_data = param_json["DeleteInteriorNodesParams"] if "DeleteInteriorNodesParams" in param_json else {}
                    self.__initialize(
                        merge_face_normals_angle if merge_face_normals_angle is not None else ( DeleteInteriorNodesParams._default_params["merge_face_normals_angle"] if "merge_face_normals_angle" in DeleteInteriorNodesParams._default_params else (json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( DeleteInteriorNodesParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in DeleteInteriorNodesParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)),
                        edge_sharp_corner_angle if edge_sharp_corner_angle is not None else ( DeleteInteriorNodesParams._default_params["edge_sharp_corner_angle"] if "edge_sharp_corner_angle" in DeleteInteriorNodesParams._default_params else (json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            merge_face_normals_angle: float = None,
            merge_edge_allow_self_close: bool = None,
            edge_sharp_corner_angle: float = None):
        """Set the default values of the ``DeleteInteriorNodesParams`` object.

        Parameters
        ----------
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.
        """
        args = locals()
        [DeleteInteriorNodesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DeleteInteriorNodesParams`` object.

        Examples
        --------
        >>> DeleteInteriorNodesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteInteriorNodesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._merge_face_normals_angle is not None:
            json_data["mergeFaceNormalsAngle"] = self._merge_face_normals_angle
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        if self._edge_sharp_corner_angle is not None:
            json_data["edgeSharpCornerAngle"] = self._edge_sharp_corner_angle
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "merge_face_normals_angle :  %s\nmerge_edge_allow_self_close :  %s\nedge_sharp_corner_angle :  %s" % (self._merge_face_normals_angle, self._merge_edge_allow_self_close, self._edge_sharp_corner_angle)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def merge_face_normals_angle(self) -> float:
        """Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_face_normals_angle

    @merge_face_normals_angle.setter
    def merge_face_normals_angle(self, value: float):
        self._merge_face_normals_angle = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

    @property
    def edge_sharp_corner_angle(self) -> float:
        """Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_sharp_corner_angle

    @edge_sharp_corner_angle.setter
    def edge_sharp_corner_angle(self, value: float):
        self._edge_sharp_corner_angle = value

class DetectAndTreatHolesParams(CoreObject):
    """Parameters for detect and treat holes operation.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectAndTreatHolesParams`` object with default parameters.
    detect_and_defeature_edges_near_holes: bool, optional
        Option to detect and defeature edges near all holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_circular_holes: bool, optional
        Option to detect circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_non_circular_holes: bool, optional
        Option to detect non-circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    offset_holes: bool, optional
        Option to offset holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    mesh_offset_faces: bool, optional
        Option to mesh the offset holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_holes_params: DetectHolesParams, optional
        Parameters for detect holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_circular_holes_params: DetectCircularHolesParams, optional
        Parameters for detect circular holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_non_circular_holes_params: DetectNonCircularHolesParams, optional
        Parameters for detect non circular holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    hole_proximity_tolerance: float, optional
        Edge proximity tolerance for holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_face_normals_angle: float, optional
        Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_sharp_corner_angle: float, optional
        Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    fragmented_edge_tolerance: float, optional
        Fragmented edge length tolerance for merging edges.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    offset_distance: float, optional
        Offset distance for creating offset edge.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_mesh_constant_size: float, optional
        Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    surface_mesh_constant_size: float, optional
        Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectAndTreatHolesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_and_treat_holes_params = prime.DetectAndTreatHolesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            detect_and_defeature_edges_near_holes: bool,
            detect_circular_holes: bool,
            detect_non_circular_holes: bool,
            offset_holes: bool,
            mesh_offset_faces: bool,
            detect_holes_params: DetectHolesParams,
            detect_circular_holes_params: DetectCircularHolesParams,
            detect_non_circular_holes_params: DetectNonCircularHolesParams,
            hole_proximity_tolerance: float,
            merge_face_normals_angle: float,
            edge_sharp_corner_angle: float,
            fragmented_edge_tolerance: float,
            offset_distance: float,
            edge_mesh_constant_size: float,
            surface_mesh_constant_size: float):
        self._detect_and_defeature_edges_near_holes = detect_and_defeature_edges_near_holes
        self._detect_circular_holes = detect_circular_holes
        self._detect_non_circular_holes = detect_non_circular_holes
        self._offset_holes = offset_holes
        self._mesh_offset_faces = mesh_offset_faces
        self._detect_holes_params = detect_holes_params
        self._detect_circular_holes_params = detect_circular_holes_params
        self._detect_non_circular_holes_params = detect_non_circular_holes_params
        self._hole_proximity_tolerance = hole_proximity_tolerance
        self._merge_face_normals_angle = merge_face_normals_angle
        self._edge_sharp_corner_angle = edge_sharp_corner_angle
        self._fragmented_edge_tolerance = fragmented_edge_tolerance
        self._offset_distance = offset_distance
        self._edge_mesh_constant_size = edge_mesh_constant_size
        self._surface_mesh_constant_size = surface_mesh_constant_size

    def __init__(
            self,
            model: CommunicationManager=None,
            detect_and_defeature_edges_near_holes: bool = None,
            detect_circular_holes: bool = None,
            detect_non_circular_holes: bool = None,
            offset_holes: bool = None,
            mesh_offset_faces: bool = None,
            detect_holes_params: DetectHolesParams = None,
            detect_circular_holes_params: DetectCircularHolesParams = None,
            detect_non_circular_holes_params: DetectNonCircularHolesParams = None,
            hole_proximity_tolerance: float = None,
            merge_face_normals_angle: float = None,
            edge_sharp_corner_angle: float = None,
            fragmented_edge_tolerance: float = None,
            offset_distance: float = None,
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectAndTreatHolesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectAndTreatHolesParams`` object with default parameters.
        detect_and_defeature_edges_near_holes: bool, optional
            Option to detect and defeature edges near all holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_circular_holes: bool, optional
            Option to detect circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_non_circular_holes: bool, optional
            Option to detect non-circular holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        offset_holes: bool, optional
            Option to offset holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        mesh_offset_faces: bool, optional
            Option to mesh the offset holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_holes_params: DetectHolesParams, optional
            Parameters for detect holes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_circular_holes_params: DetectCircularHolesParams, optional
            Parameters for detect circular holes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_non_circular_holes_params: DetectNonCircularHolesParams, optional
            Parameters for detect non circular holes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        hole_proximity_tolerance: float, optional
            Edge proximity tolerance for holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        fragmented_edge_tolerance: float, optional
            Fragmented edge length tolerance for merging edges.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        offset_distance: float, optional
            Offset distance for creating offset edge.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectAndTreatHolesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_and_treat_holes_params = prime.DetectAndTreatHolesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["detectAndDefeatureEdgesNearHoles"] if "detectAndDefeatureEdgesNearHoles" in json_data else None,
                json_data["detectCircularHoles"] if "detectCircularHoles" in json_data else None,
                json_data["detectNonCircularHoles"] if "detectNonCircularHoles" in json_data else None,
                json_data["offsetHoles"] if "offsetHoles" in json_data else None,
                json_data["meshOffsetFaces"] if "meshOffsetFaces" in json_data else None,
                DetectHolesParams(model = model, json_data = json_data["detectHolesParams"] if "detectHolesParams" in json_data else None),
                DetectCircularHolesParams(model = model, json_data = json_data["detectCircularHolesParams"] if "detectCircularHolesParams" in json_data else None),
                DetectNonCircularHolesParams(model = model, json_data = json_data["detectNonCircularHolesParams"] if "detectNonCircularHolesParams" in json_data else None),
                json_data["holeProximityTolerance"] if "holeProximityTolerance" in json_data else None,
                json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None,
                json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None,
                json_data["fragmentedEdgeTolerance"] if "fragmentedEdgeTolerance" in json_data else None,
                json_data["offsetDistance"] if "offsetDistance" in json_data else None,
                json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None,
                json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [detect_and_defeature_edges_near_holes, detect_circular_holes, detect_non_circular_holes, offset_holes, mesh_offset_faces, detect_holes_params, detect_circular_holes_params, detect_non_circular_holes_params, hole_proximity_tolerance, merge_face_normals_angle, edge_sharp_corner_angle, fragmented_edge_tolerance, offset_distance, edge_mesh_constant_size, surface_mesh_constant_size])
            if all_field_specified:
                self.__initialize(
                    detect_and_defeature_edges_near_holes,
                    detect_circular_holes,
                    detect_non_circular_holes,
                    offset_holes,
                    mesh_offset_faces,
                    detect_holes_params,
                    detect_circular_holes_params,
                    detect_non_circular_holes_params,
                    hole_proximity_tolerance,
                    merge_face_normals_angle,
                    edge_sharp_corner_angle,
                    fragmented_edge_tolerance,
                    offset_distance,
                    edge_mesh_constant_size,
                    surface_mesh_constant_size)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectAndTreatHolesParams")
                    json_data = param_json["DetectAndTreatHolesParams"] if "DetectAndTreatHolesParams" in param_json else {}
                    self.__initialize(
                        detect_and_defeature_edges_near_holes if detect_and_defeature_edges_near_holes is not None else ( DetectAndTreatHolesParams._default_params["detect_and_defeature_edges_near_holes"] if "detect_and_defeature_edges_near_holes" in DetectAndTreatHolesParams._default_params else (json_data["detectAndDefeatureEdgesNearHoles"] if "detectAndDefeatureEdgesNearHoles" in json_data else None)),
                        detect_circular_holes if detect_circular_holes is not None else ( DetectAndTreatHolesParams._default_params["detect_circular_holes"] if "detect_circular_holes" in DetectAndTreatHolesParams._default_params else (json_data["detectCircularHoles"] if "detectCircularHoles" in json_data else None)),
                        detect_non_circular_holes if detect_non_circular_holes is not None else ( DetectAndTreatHolesParams._default_params["detect_non_circular_holes"] if "detect_non_circular_holes" in DetectAndTreatHolesParams._default_params else (json_data["detectNonCircularHoles"] if "detectNonCircularHoles" in json_data else None)),
                        offset_holes if offset_holes is not None else ( DetectAndTreatHolesParams._default_params["offset_holes"] if "offset_holes" in DetectAndTreatHolesParams._default_params else (json_data["offsetHoles"] if "offsetHoles" in json_data else None)),
                        mesh_offset_faces if mesh_offset_faces is not None else ( DetectAndTreatHolesParams._default_params["mesh_offset_faces"] if "mesh_offset_faces" in DetectAndTreatHolesParams._default_params else (json_data["meshOffsetFaces"] if "meshOffsetFaces" in json_data else None)),
                        detect_holes_params if detect_holes_params is not None else ( DetectAndTreatHolesParams._default_params["detect_holes_params"] if "detect_holes_params" in DetectAndTreatHolesParams._default_params else DetectHolesParams(model = model, json_data = (json_data["detectHolesParams"] if "detectHolesParams" in json_data else None))),
                        detect_circular_holes_params if detect_circular_holes_params is not None else ( DetectAndTreatHolesParams._default_params["detect_circular_holes_params"] if "detect_circular_holes_params" in DetectAndTreatHolesParams._default_params else DetectCircularHolesParams(model = model, json_data = (json_data["detectCircularHolesParams"] if "detectCircularHolesParams" in json_data else None))),
                        detect_non_circular_holes_params if detect_non_circular_holes_params is not None else ( DetectAndTreatHolesParams._default_params["detect_non_circular_holes_params"] if "detect_non_circular_holes_params" in DetectAndTreatHolesParams._default_params else DetectNonCircularHolesParams(model = model, json_data = (json_data["detectNonCircularHolesParams"] if "detectNonCircularHolesParams" in json_data else None))),
                        hole_proximity_tolerance if hole_proximity_tolerance is not None else ( DetectAndTreatHolesParams._default_params["hole_proximity_tolerance"] if "hole_proximity_tolerance" in DetectAndTreatHolesParams._default_params else (json_data["holeProximityTolerance"] if "holeProximityTolerance" in json_data else None)),
                        merge_face_normals_angle if merge_face_normals_angle is not None else ( DetectAndTreatHolesParams._default_params["merge_face_normals_angle"] if "merge_face_normals_angle" in DetectAndTreatHolesParams._default_params else (json_data["mergeFaceNormalsAngle"] if "mergeFaceNormalsAngle" in json_data else None)),
                        edge_sharp_corner_angle if edge_sharp_corner_angle is not None else ( DetectAndTreatHolesParams._default_params["edge_sharp_corner_angle"] if "edge_sharp_corner_angle" in DetectAndTreatHolesParams._default_params else (json_data["edgeSharpCornerAngle"] if "edgeSharpCornerAngle" in json_data else None)),
                        fragmented_edge_tolerance if fragmented_edge_tolerance is not None else ( DetectAndTreatHolesParams._default_params["fragmented_edge_tolerance"] if "fragmented_edge_tolerance" in DetectAndTreatHolesParams._default_params else (json_data["fragmentedEdgeTolerance"] if "fragmentedEdgeTolerance" in json_data else None)),
                        offset_distance if offset_distance is not None else ( DetectAndTreatHolesParams._default_params["offset_distance"] if "offset_distance" in DetectAndTreatHolesParams._default_params else (json_data["offsetDistance"] if "offsetDistance" in json_data else None)),
                        edge_mesh_constant_size if edge_mesh_constant_size is not None else ( DetectAndTreatHolesParams._default_params["edge_mesh_constant_size"] if "edge_mesh_constant_size" in DetectAndTreatHolesParams._default_params else (json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None)),
                        surface_mesh_constant_size if surface_mesh_constant_size is not None else ( DetectAndTreatHolesParams._default_params["surface_mesh_constant_size"] if "surface_mesh_constant_size" in DetectAndTreatHolesParams._default_params else (json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            detect_and_defeature_edges_near_holes: bool = None,
            detect_circular_holes: bool = None,
            detect_non_circular_holes: bool = None,
            offset_holes: bool = None,
            mesh_offset_faces: bool = None,
            detect_holes_params: DetectHolesParams = None,
            detect_circular_holes_params: DetectCircularHolesParams = None,
            detect_non_circular_holes_params: DetectNonCircularHolesParams = None,
            hole_proximity_tolerance: float = None,
            merge_face_normals_angle: float = None,
            edge_sharp_corner_angle: float = None,
            fragmented_edge_tolerance: float = None,
            offset_distance: float = None,
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None):
        """Set the default values of the ``DetectAndTreatHolesParams`` object.

        Parameters
        ----------
        detect_and_defeature_edges_near_holes: bool, optional
            Option to detect and defeature edges near all holes.
        detect_circular_holes: bool, optional
            Option to detect circular holes.
        detect_non_circular_holes: bool, optional
            Option to detect non-circular holes.
        offset_holes: bool, optional
            Option to offset holes.
        mesh_offset_faces: bool, optional
            Option to mesh the offset holes.
        detect_holes_params: DetectHolesParams, optional
            Parameters for detect holes operation.
        detect_circular_holes_params: DetectCircularHolesParams, optional
            Parameters for detect circular holes operation.
        detect_non_circular_holes_params: DetectNonCircularHolesParams, optional
            Parameters for detect non circular holes operation.
        hole_proximity_tolerance: float, optional
            Edge proximity tolerance for holes.
        merge_face_normals_angle: float, optional
            Merge faces when the normal angle between the faces is below the provided value.
        edge_sharp_corner_angle: float, optional
            Merge edges when the angle between the edges are below the provided value.
        fragmented_edge_tolerance: float, optional
            Fragmented edge length tolerance for merging edges.
        offset_distance: float, optional
            Offset distance for creating offset edge.
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.
        """
        args = locals()
        [DetectAndTreatHolesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectAndTreatHolesParams`` object.

        Examples
        --------
        >>> DetectAndTreatHolesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectAndTreatHolesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._detect_and_defeature_edges_near_holes is not None:
            json_data["detectAndDefeatureEdgesNearHoles"] = self._detect_and_defeature_edges_near_holes
        if self._detect_circular_holes is not None:
            json_data["detectCircularHoles"] = self._detect_circular_holes
        if self._detect_non_circular_holes is not None:
            json_data["detectNonCircularHoles"] = self._detect_non_circular_holes
        if self._offset_holes is not None:
            json_data["offsetHoles"] = self._offset_holes
        if self._mesh_offset_faces is not None:
            json_data["meshOffsetFaces"] = self._mesh_offset_faces
        if self._detect_holes_params is not None:
            json_data["detectHolesParams"] = self._detect_holes_params._jsonify()
        if self._detect_circular_holes_params is not None:
            json_data["detectCircularHolesParams"] = self._detect_circular_holes_params._jsonify()
        if self._detect_non_circular_holes_params is not None:
            json_data["detectNonCircularHolesParams"] = self._detect_non_circular_holes_params._jsonify()
        if self._hole_proximity_tolerance is not None:
            json_data["holeProximityTolerance"] = self._hole_proximity_tolerance
        if self._merge_face_normals_angle is not None:
            json_data["mergeFaceNormalsAngle"] = self._merge_face_normals_angle
        if self._edge_sharp_corner_angle is not None:
            json_data["edgeSharpCornerAngle"] = self._edge_sharp_corner_angle
        if self._fragmented_edge_tolerance is not None:
            json_data["fragmentedEdgeTolerance"] = self._fragmented_edge_tolerance
        if self._offset_distance is not None:
            json_data["offsetDistance"] = self._offset_distance
        if self._edge_mesh_constant_size is not None:
            json_data["edgeMeshConstantSize"] = self._edge_mesh_constant_size
        if self._surface_mesh_constant_size is not None:
            json_data["surfaceMeshConstantSize"] = self._surface_mesh_constant_size
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "detect_and_defeature_edges_near_holes :  %s\ndetect_circular_holes :  %s\ndetect_non_circular_holes :  %s\noffset_holes :  %s\nmesh_offset_faces :  %s\ndetect_holes_params :  %s\ndetect_circular_holes_params :  %s\ndetect_non_circular_holes_params :  %s\nhole_proximity_tolerance :  %s\nmerge_face_normals_angle :  %s\nedge_sharp_corner_angle :  %s\nfragmented_edge_tolerance :  %s\noffset_distance :  %s\nedge_mesh_constant_size :  %s\nsurface_mesh_constant_size :  %s" % (self._detect_and_defeature_edges_near_holes, self._detect_circular_holes, self._detect_non_circular_holes, self._offset_holes, self._mesh_offset_faces, '{ ' + str(self._detect_holes_params) + ' }', '{ ' + str(self._detect_circular_holes_params) + ' }', '{ ' + str(self._detect_non_circular_holes_params) + ' }', self._hole_proximity_tolerance, self._merge_face_normals_angle, self._edge_sharp_corner_angle, self._fragmented_edge_tolerance, self._offset_distance, self._edge_mesh_constant_size, self._surface_mesh_constant_size)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def detect_and_defeature_edges_near_holes(self) -> bool:
        """Option to detect and defeature edges near all holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_and_defeature_edges_near_holes

    @detect_and_defeature_edges_near_holes.setter
    def detect_and_defeature_edges_near_holes(self, value: bool):
        self._detect_and_defeature_edges_near_holes = value

    @property
    def detect_circular_holes(self) -> bool:
        """Option to detect circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_circular_holes

    @detect_circular_holes.setter
    def detect_circular_holes(self, value: bool):
        self._detect_circular_holes = value

    @property
    def detect_non_circular_holes(self) -> bool:
        """Option to detect non-circular holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_non_circular_holes

    @detect_non_circular_holes.setter
    def detect_non_circular_holes(self, value: bool):
        self._detect_non_circular_holes = value

    @property
    def offset_holes(self) -> bool:
        """Option to offset holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._offset_holes

    @offset_holes.setter
    def offset_holes(self, value: bool):
        self._offset_holes = value

    @property
    def mesh_offset_faces(self) -> bool:
        """Option to mesh the offset holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._mesh_offset_faces

    @mesh_offset_faces.setter
    def mesh_offset_faces(self, value: bool):
        self._mesh_offset_faces = value

    @property
    def detect_holes_params(self) -> DetectHolesParams:
        """Parameters for detect holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_holes_params

    @detect_holes_params.setter
    def detect_holes_params(self, value: DetectHolesParams):
        self._detect_holes_params = value

    @property
    def detect_circular_holes_params(self) -> DetectCircularHolesParams:
        """Parameters for detect circular holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_circular_holes_params

    @detect_circular_holes_params.setter
    def detect_circular_holes_params(self, value: DetectCircularHolesParams):
        self._detect_circular_holes_params = value

    @property
    def detect_non_circular_holes_params(self) -> DetectNonCircularHolesParams:
        """Parameters for detect non circular holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_non_circular_holes_params

    @detect_non_circular_holes_params.setter
    def detect_non_circular_holes_params(self, value: DetectNonCircularHolesParams):
        self._detect_non_circular_holes_params = value

    @property
    def hole_proximity_tolerance(self) -> float:
        """Edge proximity tolerance for holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._hole_proximity_tolerance

    @hole_proximity_tolerance.setter
    def hole_proximity_tolerance(self, value: float):
        self._hole_proximity_tolerance = value

    @property
    def merge_face_normals_angle(self) -> float:
        """Merge faces when the normal angle between the faces is below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_face_normals_angle

    @merge_face_normals_angle.setter
    def merge_face_normals_angle(self, value: float):
        self._merge_face_normals_angle = value

    @property
    def edge_sharp_corner_angle(self) -> float:
        """Merge edges when the angle between the edges are below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_sharp_corner_angle

    @edge_sharp_corner_angle.setter
    def edge_sharp_corner_angle(self, value: float):
        self._edge_sharp_corner_angle = value

    @property
    def fragmented_edge_tolerance(self) -> float:
        """Fragmented edge length tolerance for merging edges.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._fragmented_edge_tolerance

    @fragmented_edge_tolerance.setter
    def fragmented_edge_tolerance(self, value: float):
        self._fragmented_edge_tolerance = value

    @property
    def offset_distance(self) -> float:
        """Offset distance for creating offset edge.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._offset_distance

    @offset_distance.setter
    def offset_distance(self, value: float):
        self._offset_distance = value

    @property
    def edge_mesh_constant_size(self) -> float:
        """Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_mesh_constant_size

    @edge_mesh_constant_size.setter
    def edge_mesh_constant_size(self, value: float):
        self._edge_mesh_constant_size = value

    @property
    def surface_mesh_constant_size(self) -> float:
        """Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._surface_mesh_constant_size

    @surface_mesh_constant_size.setter
    def surface_mesh_constant_size(self, value: float):
        self._surface_mesh_constant_size = value

class DetectAndTreatFeaturesParams(CoreObject):
    """Parameters for detect and treat features operations.

    Parameters
    ----------
    model: Model
        Model to create a ``DetectAndTreatFeaturesParams`` object with default parameters.
    detect_and_treat_holes: bool, optional
        Option to detect and treat holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    detect_and_treat_circular_faces: bool, optional
        Option to detect and treat circular faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    treat_holes_params: DetectAndTreatHolesParams, optional
        Parameters for detect and treat holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    treat_circular_faces_params: DetectAndTreatCircularFacesParams, optional
        Parameters for detect and treat circular faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DetectAndTreatFeaturesParams`` object with provided parameters.

    Examples
    --------
    >>> detect_and_treat_features_params = prime.DetectAndTreatFeaturesParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            detect_and_treat_holes: bool,
            detect_and_treat_circular_faces: bool,
            treat_holes_params: DetectAndTreatHolesParams,
            treat_circular_faces_params: DetectAndTreatCircularFacesParams):
        self._detect_and_treat_holes = detect_and_treat_holes
        self._detect_and_treat_circular_faces = detect_and_treat_circular_faces
        self._treat_holes_params = treat_holes_params
        self._treat_circular_faces_params = treat_circular_faces_params

    def __init__(
            self,
            model: CommunicationManager=None,
            detect_and_treat_holes: bool = None,
            detect_and_treat_circular_faces: bool = None,
            treat_holes_params: DetectAndTreatHolesParams = None,
            treat_circular_faces_params: DetectAndTreatCircularFacesParams = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DetectAndTreatFeaturesParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DetectAndTreatFeaturesParams`` object with default parameters.
        detect_and_treat_holes: bool, optional
            Option to detect and treat holes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        detect_and_treat_circular_faces: bool, optional
            Option to detect and treat circular faces.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        treat_holes_params: DetectAndTreatHolesParams, optional
            Parameters for detect and treat holes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        treat_circular_faces_params: DetectAndTreatCircularFacesParams, optional
            Parameters for detect and treat circular faces operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DetectAndTreatFeaturesParams`` object with provided parameters.

        Examples
        --------
        >>> detect_and_treat_features_params = prime.DetectAndTreatFeaturesParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["detectAndTreatHoles"] if "detectAndTreatHoles" in json_data else None,
                json_data["detectAndTreatCircularFaces"] if "detectAndTreatCircularFaces" in json_data else None,
                DetectAndTreatHolesParams(model = model, json_data = json_data["treatHolesParams"] if "treatHolesParams" in json_data else None),
                DetectAndTreatCircularFacesParams(model = model, json_data = json_data["treatCircularFacesParams"] if "treatCircularFacesParams" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [detect_and_treat_holes, detect_and_treat_circular_faces, treat_holes_params, treat_circular_faces_params])
            if all_field_specified:
                self.__initialize(
                    detect_and_treat_holes,
                    detect_and_treat_circular_faces,
                    treat_holes_params,
                    treat_circular_faces_params)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DetectAndTreatFeaturesParams")
                    json_data = param_json["DetectAndTreatFeaturesParams"] if "DetectAndTreatFeaturesParams" in param_json else {}
                    self.__initialize(
                        detect_and_treat_holes if detect_and_treat_holes is not None else ( DetectAndTreatFeaturesParams._default_params["detect_and_treat_holes"] if "detect_and_treat_holes" in DetectAndTreatFeaturesParams._default_params else (json_data["detectAndTreatHoles"] if "detectAndTreatHoles" in json_data else None)),
                        detect_and_treat_circular_faces if detect_and_treat_circular_faces is not None else ( DetectAndTreatFeaturesParams._default_params["detect_and_treat_circular_faces"] if "detect_and_treat_circular_faces" in DetectAndTreatFeaturesParams._default_params else (json_data["detectAndTreatCircularFaces"] if "detectAndTreatCircularFaces" in json_data else None)),
                        treat_holes_params if treat_holes_params is not None else ( DetectAndTreatFeaturesParams._default_params["treat_holes_params"] if "treat_holes_params" in DetectAndTreatFeaturesParams._default_params else DetectAndTreatHolesParams(model = model, json_data = (json_data["treatHolesParams"] if "treatHolesParams" in json_data else None))),
                        treat_circular_faces_params if treat_circular_faces_params is not None else ( DetectAndTreatFeaturesParams._default_params["treat_circular_faces_params"] if "treat_circular_faces_params" in DetectAndTreatFeaturesParams._default_params else DetectAndTreatCircularFacesParams(model = model, json_data = (json_data["treatCircularFacesParams"] if "treatCircularFacesParams" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            detect_and_treat_holes: bool = None,
            detect_and_treat_circular_faces: bool = None,
            treat_holes_params: DetectAndTreatHolesParams = None,
            treat_circular_faces_params: DetectAndTreatCircularFacesParams = None):
        """Set the default values of the ``DetectAndTreatFeaturesParams`` object.

        Parameters
        ----------
        detect_and_treat_holes: bool, optional
            Option to detect and treat holes.
        detect_and_treat_circular_faces: bool, optional
            Option to detect and treat circular faces.
        treat_holes_params: DetectAndTreatHolesParams, optional
            Parameters for detect and treat holes operation.
        treat_circular_faces_params: DetectAndTreatCircularFacesParams, optional
            Parameters for detect and treat circular faces operation.
        """
        args = locals()
        [DetectAndTreatFeaturesParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DetectAndTreatFeaturesParams`` object.

        Examples
        --------
        >>> DetectAndTreatFeaturesParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DetectAndTreatFeaturesParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._detect_and_treat_holes is not None:
            json_data["detectAndTreatHoles"] = self._detect_and_treat_holes
        if self._detect_and_treat_circular_faces is not None:
            json_data["detectAndTreatCircularFaces"] = self._detect_and_treat_circular_faces
        if self._treat_holes_params is not None:
            json_data["treatHolesParams"] = self._treat_holes_params._jsonify()
        if self._treat_circular_faces_params is not None:
            json_data["treatCircularFacesParams"] = self._treat_circular_faces_params._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "detect_and_treat_holes :  %s\ndetect_and_treat_circular_faces :  %s\ntreat_holes_params :  %s\ntreat_circular_faces_params :  %s" % (self._detect_and_treat_holes, self._detect_and_treat_circular_faces, '{ ' + str(self._treat_holes_params) + ' }', '{ ' + str(self._treat_circular_faces_params) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def detect_and_treat_holes(self) -> bool:
        """Option to detect and treat holes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_and_treat_holes

    @detect_and_treat_holes.setter
    def detect_and_treat_holes(self, value: bool):
        self._detect_and_treat_holes = value

    @property
    def detect_and_treat_circular_faces(self) -> bool:
        """Option to detect and treat circular faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._detect_and_treat_circular_faces

    @detect_and_treat_circular_faces.setter
    def detect_and_treat_circular_faces(self, value: bool):
        self._detect_and_treat_circular_faces = value

    @property
    def treat_holes_params(self) -> DetectAndTreatHolesParams:
        """Parameters for detect and treat holes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._treat_holes_params

    @treat_holes_params.setter
    def treat_holes_params(self, value: DetectAndTreatHolesParams):
        self._treat_holes_params = value

    @property
    def treat_circular_faces_params(self) -> DetectAndTreatCircularFacesParams:
        """Parameters for detect and treat circular faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._treat_circular_faces_params

    @treat_circular_faces_params.setter
    def treat_circular_faces_params(self, value: DetectAndTreatCircularFacesParams):
        self._treat_circular_faces_params = value

class RepairTopologyParams(CoreObject):
    """Parameters for repair topology operations.

    Parameters
    ----------
    model: Model
        Model to create a ``RepairTopologyParams`` object with default parameters.
    connect_faces: bool, optional
        Option to connect faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    repair_edges: bool, optional
        Option to repair edges.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    split_topo_edges_at_apex_point: bool, optional
        Option to split edges at apex point.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    fillet_max_radius: float, optional
        Maximum radius of fillets to be detected.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    smallest_edge_length: float, optional
        Length of smallest edge for which split is applied.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    merge_edge_allow_self_close: bool, optional
        Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    suppress_shared_edges_when_merging: bool, optional
        Option for suppressing shared edges when merging.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_connect_type: int, optional
        Edge connection type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    connect_faces_params: ConnectFacesParams, optional
        Parameters for connect faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    repair_edges_params: RepairEdgesParams, optional
        Parameters for repair edges operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``RepairTopologyParams`` object with provided parameters.

    Examples
    --------
    >>> repair_topology_params = prime.RepairTopologyParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            connect_faces: bool,
            repair_edges: bool,
            split_topo_edges_at_apex_point: bool,
            fillet_max_radius: float,
            smallest_edge_length: float,
            merge_edge_allow_self_close: bool,
            suppress_shared_edges_when_merging: bool,
            edge_connect_type: int,
            connect_faces_params: ConnectFacesParams,
            repair_edges_params: RepairEdgesParams):
        self._connect_faces = connect_faces
        self._repair_edges = repair_edges
        self._split_topo_edges_at_apex_point = split_topo_edges_at_apex_point
        self._fillet_max_radius = fillet_max_radius
        self._smallest_edge_length = smallest_edge_length
        self._merge_edge_allow_self_close = merge_edge_allow_self_close
        self._suppress_shared_edges_when_merging = suppress_shared_edges_when_merging
        self._edge_connect_type = edge_connect_type
        self._connect_faces_params = connect_faces_params
        self._repair_edges_params = repair_edges_params

    def __init__(
            self,
            model: CommunicationManager=None,
            connect_faces: bool = None,
            repair_edges: bool = None,
            split_topo_edges_at_apex_point: bool = None,
            fillet_max_radius: float = None,
            smallest_edge_length: float = None,
            merge_edge_allow_self_close: bool = None,
            suppress_shared_edges_when_merging: bool = None,
            edge_connect_type: int = None,
            connect_faces_params: ConnectFacesParams = None,
            repair_edges_params: RepairEdgesParams = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``RepairTopologyParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``RepairTopologyParams`` object with default parameters.
        connect_faces: bool, optional
            Option to connect faces.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        repair_edges: bool, optional
            Option to repair edges.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        split_topo_edges_at_apex_point: bool, optional
            Option to split edges at apex point.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        fillet_max_radius: float, optional
            Maximum radius of fillets to be detected.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        smallest_edge_length: float, optional
            Length of smallest edge for which split is applied.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        suppress_shared_edges_when_merging: bool, optional
            Option for suppressing shared edges when merging.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_connect_type: int, optional
            Edge connection type.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        connect_faces_params: ConnectFacesParams, optional
            Parameters for connect faces operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        repair_edges_params: RepairEdgesParams, optional
            Parameters for repair edges operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``RepairTopologyParams`` object with provided parameters.

        Examples
        --------
        >>> repair_topology_params = prime.RepairTopologyParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["connectFaces"] if "connectFaces" in json_data else None,
                json_data["repairEdges"] if "repairEdges" in json_data else None,
                json_data["splitTopoEdgesAtApexPoint"] if "splitTopoEdgesAtApexPoint" in json_data else None,
                json_data["filletMaxRadius"] if "filletMaxRadius" in json_data else None,
                json_data["smallestEdgeLength"] if "smallestEdgeLength" in json_data else None,
                json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None,
                json_data["suppressSharedEdgesWhenMerging"] if "suppressSharedEdgesWhenMerging" in json_data else None,
                json_data["edgeConnectType"] if "edgeConnectType" in json_data else None,
                ConnectFacesParams(model = model, json_data = json_data["connectFacesParams"] if "connectFacesParams" in json_data else None),
                RepairEdgesParams(model = model, json_data = json_data["repairEdgesParams"] if "repairEdgesParams" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [connect_faces, repair_edges, split_topo_edges_at_apex_point, fillet_max_radius, smallest_edge_length, merge_edge_allow_self_close, suppress_shared_edges_when_merging, edge_connect_type, connect_faces_params, repair_edges_params])
            if all_field_specified:
                self.__initialize(
                    connect_faces,
                    repair_edges,
                    split_topo_edges_at_apex_point,
                    fillet_max_radius,
                    smallest_edge_length,
                    merge_edge_allow_self_close,
                    suppress_shared_edges_when_merging,
                    edge_connect_type,
                    connect_faces_params,
                    repair_edges_params)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "RepairTopologyParams")
                    json_data = param_json["RepairTopologyParams"] if "RepairTopologyParams" in param_json else {}
                    self.__initialize(
                        connect_faces if connect_faces is not None else ( RepairTopologyParams._default_params["connect_faces"] if "connect_faces" in RepairTopologyParams._default_params else (json_data["connectFaces"] if "connectFaces" in json_data else None)),
                        repair_edges if repair_edges is not None else ( RepairTopologyParams._default_params["repair_edges"] if "repair_edges" in RepairTopologyParams._default_params else (json_data["repairEdges"] if "repairEdges" in json_data else None)),
                        split_topo_edges_at_apex_point if split_topo_edges_at_apex_point is not None else ( RepairTopologyParams._default_params["split_topo_edges_at_apex_point"] if "split_topo_edges_at_apex_point" in RepairTopologyParams._default_params else (json_data["splitTopoEdgesAtApexPoint"] if "splitTopoEdgesAtApexPoint" in json_data else None)),
                        fillet_max_radius if fillet_max_radius is not None else ( RepairTopologyParams._default_params["fillet_max_radius"] if "fillet_max_radius" in RepairTopologyParams._default_params else (json_data["filletMaxRadius"] if "filletMaxRadius" in json_data else None)),
                        smallest_edge_length if smallest_edge_length is not None else ( RepairTopologyParams._default_params["smallest_edge_length"] if "smallest_edge_length" in RepairTopologyParams._default_params else (json_data["smallestEdgeLength"] if "smallestEdgeLength" in json_data else None)),
                        merge_edge_allow_self_close if merge_edge_allow_self_close is not None else ( RepairTopologyParams._default_params["merge_edge_allow_self_close"] if "merge_edge_allow_self_close" in RepairTopologyParams._default_params else (json_data["mergeEdgeAllowSelfClose"] if "mergeEdgeAllowSelfClose" in json_data else None)),
                        suppress_shared_edges_when_merging if suppress_shared_edges_when_merging is not None else ( RepairTopologyParams._default_params["suppress_shared_edges_when_merging"] if "suppress_shared_edges_when_merging" in RepairTopologyParams._default_params else (json_data["suppressSharedEdgesWhenMerging"] if "suppressSharedEdgesWhenMerging" in json_data else None)),
                        edge_connect_type if edge_connect_type is not None else ( RepairTopologyParams._default_params["edge_connect_type"] if "edge_connect_type" in RepairTopologyParams._default_params else (json_data["edgeConnectType"] if "edgeConnectType" in json_data else None)),
                        connect_faces_params if connect_faces_params is not None else ( RepairTopologyParams._default_params["connect_faces_params"] if "connect_faces_params" in RepairTopologyParams._default_params else ConnectFacesParams(model = model, json_data = (json_data["connectFacesParams"] if "connectFacesParams" in json_data else None))),
                        repair_edges_params if repair_edges_params is not None else ( RepairTopologyParams._default_params["repair_edges_params"] if "repair_edges_params" in RepairTopologyParams._default_params else RepairEdgesParams(model = model, json_data = (json_data["repairEdgesParams"] if "repairEdgesParams" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            connect_faces: bool = None,
            repair_edges: bool = None,
            split_topo_edges_at_apex_point: bool = None,
            fillet_max_radius: float = None,
            smallest_edge_length: float = None,
            merge_edge_allow_self_close: bool = None,
            suppress_shared_edges_when_merging: bool = None,
            edge_connect_type: int = None,
            connect_faces_params: ConnectFacesParams = None,
            repair_edges_params: RepairEdgesParams = None):
        """Set the default values of the ``RepairTopologyParams`` object.

        Parameters
        ----------
        connect_faces: bool, optional
            Option to connect faces.
        repair_edges: bool, optional
            Option to repair edges.
        split_topo_edges_at_apex_point: bool, optional
            Option to split edges at apex point.
        fillet_max_radius: float, optional
            Maximum radius of fillets to be detected.
        smallest_edge_length: float, optional
            Length of smallest edge for which split is applied.
        merge_edge_allow_self_close: bool, optional
            Option for merging self-closing edge loops.
        suppress_shared_edges_when_merging: bool, optional
            Option for suppressing shared edges when merging.
        edge_connect_type: int, optional
            Edge connection type.
        connect_faces_params: ConnectFacesParams, optional
            Parameters for connect faces operation.
        repair_edges_params: RepairEdgesParams, optional
            Parameters for repair edges operation.
        """
        args = locals()
        [RepairTopologyParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``RepairTopologyParams`` object.

        Examples
        --------
        >>> RepairTopologyParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in RepairTopologyParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._connect_faces is not None:
            json_data["connectFaces"] = self._connect_faces
        if self._repair_edges is not None:
            json_data["repairEdges"] = self._repair_edges
        if self._split_topo_edges_at_apex_point is not None:
            json_data["splitTopoEdgesAtApexPoint"] = self._split_topo_edges_at_apex_point
        if self._fillet_max_radius is not None:
            json_data["filletMaxRadius"] = self._fillet_max_radius
        if self._smallest_edge_length is not None:
            json_data["smallestEdgeLength"] = self._smallest_edge_length
        if self._merge_edge_allow_self_close is not None:
            json_data["mergeEdgeAllowSelfClose"] = self._merge_edge_allow_self_close
        if self._suppress_shared_edges_when_merging is not None:
            json_data["suppressSharedEdgesWhenMerging"] = self._suppress_shared_edges_when_merging
        if self._edge_connect_type is not None:
            json_data["edgeConnectType"] = self._edge_connect_type
        if self._connect_faces_params is not None:
            json_data["connectFacesParams"] = self._connect_faces_params._jsonify()
        if self._repair_edges_params is not None:
            json_data["repairEdgesParams"] = self._repair_edges_params._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "connect_faces :  %s\nrepair_edges :  %s\nsplit_topo_edges_at_apex_point :  %s\nfillet_max_radius :  %s\nsmallest_edge_length :  %s\nmerge_edge_allow_self_close :  %s\nsuppress_shared_edges_when_merging :  %s\nedge_connect_type :  %s\nconnect_faces_params :  %s\nrepair_edges_params :  %s" % (self._connect_faces, self._repair_edges, self._split_topo_edges_at_apex_point, self._fillet_max_radius, self._smallest_edge_length, self._merge_edge_allow_self_close, self._suppress_shared_edges_when_merging, self._edge_connect_type, '{ ' + str(self._connect_faces_params) + ' }', '{ ' + str(self._repair_edges_params) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def connect_faces(self) -> bool:
        """Option to connect faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._connect_faces

    @connect_faces.setter
    def connect_faces(self, value: bool):
        self._connect_faces = value

    @property
    def repair_edges(self) -> bool:
        """Option to repair edges.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._repair_edges

    @repair_edges.setter
    def repair_edges(self, value: bool):
        self._repair_edges = value

    @property
    def split_topo_edges_at_apex_point(self) -> bool:
        """Option to split edges at apex point.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._split_topo_edges_at_apex_point

    @split_topo_edges_at_apex_point.setter
    def split_topo_edges_at_apex_point(self, value: bool):
        self._split_topo_edges_at_apex_point = value

    @property
    def fillet_max_radius(self) -> float:
        """Maximum radius of fillets to be detected.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._fillet_max_radius

    @fillet_max_radius.setter
    def fillet_max_radius(self, value: float):
        self._fillet_max_radius = value

    @property
    def smallest_edge_length(self) -> float:
        """Length of smallest edge for which split is applied.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._smallest_edge_length

    @smallest_edge_length.setter
    def smallest_edge_length(self, value: float):
        self._smallest_edge_length = value

    @property
    def merge_edge_allow_self_close(self) -> bool:
        """Option for merging self-closing edge loops.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._merge_edge_allow_self_close

    @merge_edge_allow_self_close.setter
    def merge_edge_allow_self_close(self, value: bool):
        self._merge_edge_allow_self_close = value

    @property
    def suppress_shared_edges_when_merging(self) -> bool:
        """Option for suppressing shared edges when merging.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._suppress_shared_edges_when_merging

    @suppress_shared_edges_when_merging.setter
    def suppress_shared_edges_when_merging(self, value: bool):
        self._suppress_shared_edges_when_merging = value

    @property
    def edge_connect_type(self) -> int:
        """Edge connection type.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_connect_type

    @edge_connect_type.setter
    def edge_connect_type(self, value: int):
        self._edge_connect_type = value

    @property
    def connect_faces_params(self) -> ConnectFacesParams:
        """Parameters for connect faces operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._connect_faces_params

    @connect_faces_params.setter
    def connect_faces_params(self, value: ConnectFacesParams):
        self._connect_faces_params = value

    @property
    def repair_edges_params(self) -> RepairEdgesParams:
        """Parameters for repair edges operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._repair_edges_params

    @repair_edges_params.setter
    def repair_edges_params(self, value: RepairEdgesParams):
        self._repair_edges_params = value

class DefeatureTopologyParams(CoreObject):
    """Parameters for defeature topology operations.

    Parameters
    ----------
    model: Model
        Model to create a ``DefeatureTopologyParams`` object with default parameters.
    partial_defeature: bool, optional
        Option to partial defeature.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    delete_interior_nodes: bool, optional
        Option to delete interior nodes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    allow_curved_topo_faces: bool, optional
        Option to allow curved topofaces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    fillet_spanning_angle: float, optional
        Angular threshold for detecting fillets with spanning angles below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    aggressive_edge_merge: bool, optional
        Indicate whether to allow aggressive edge merge while performing partial defeature.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    thin_stripes_tolerance: float, optional
        Topoface width tolerance to detect thin faces below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    partial_defeature_params: PartialDefeatureParams, optional
        Parameters for partial defeature operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    delete_interior_nodes_params: DeleteInteriorNodesParams, optional
        Parameters for delete interior nodes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DefeatureTopologyParams`` object with provided parameters.

    Examples
    --------
    >>> defeature_topology_params = prime.DefeatureTopologyParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            partial_defeature: bool,
            delete_interior_nodes: bool,
            allow_curved_topo_faces: bool,
            fillet_spanning_angle: float,
            aggressive_edge_merge: bool,
            thin_stripes_tolerance: float,
            partial_defeature_params: PartialDefeatureParams,
            delete_interior_nodes_params: DeleteInteriorNodesParams):
        self._partial_defeature = partial_defeature
        self._delete_interior_nodes = delete_interior_nodes
        self._allow_curved_topo_faces = allow_curved_topo_faces
        self._fillet_spanning_angle = fillet_spanning_angle
        self._aggressive_edge_merge = aggressive_edge_merge
        self._thin_stripes_tolerance = thin_stripes_tolerance
        self._partial_defeature_params = partial_defeature_params
        self._delete_interior_nodes_params = delete_interior_nodes_params

    def __init__(
            self,
            model: CommunicationManager=None,
            partial_defeature: bool = None,
            delete_interior_nodes: bool = None,
            allow_curved_topo_faces: bool = None,
            fillet_spanning_angle: float = None,
            aggressive_edge_merge: bool = None,
            thin_stripes_tolerance: float = None,
            partial_defeature_params: PartialDefeatureParams = None,
            delete_interior_nodes_params: DeleteInteriorNodesParams = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DefeatureTopologyParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DefeatureTopologyParams`` object with default parameters.
        partial_defeature: bool, optional
            Option to partial defeature.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        delete_interior_nodes: bool, optional
            Option to delete interior nodes.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        allow_curved_topo_faces: bool, optional
            Option to allow curved topofaces.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        fillet_spanning_angle: float, optional
            Angular threshold for detecting fillets with spanning angles below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        aggressive_edge_merge: bool, optional
            Indicate whether to allow aggressive edge merge while performing partial defeature.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        thin_stripes_tolerance: float, optional
            Topoface width tolerance to detect thin faces below the provided value.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        partial_defeature_params: PartialDefeatureParams, optional
            Parameters for partial defeature operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        delete_interior_nodes_params: DeleteInteriorNodesParams, optional
            Parameters for delete interior nodes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DefeatureTopologyParams`` object with provided parameters.

        Examples
        --------
        >>> defeature_topology_params = prime.DefeatureTopologyParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["partialDefeature"] if "partialDefeature" in json_data else None,
                json_data["deleteInteriorNodes"] if "deleteInteriorNodes" in json_data else None,
                json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None,
                json_data["filletSpanningAngle"] if "filletSpanningAngle" in json_data else None,
                json_data["aggressiveEdgeMerge"] if "aggressiveEdgeMerge" in json_data else None,
                json_data["thinStripesTolerance"] if "thinStripesTolerance" in json_data else None,
                PartialDefeatureParams(model = model, json_data = json_data["partialDefeatureParams"] if "partialDefeatureParams" in json_data else None),
                DeleteInteriorNodesParams(model = model, json_data = json_data["deleteInteriorNodesParams"] if "deleteInteriorNodesParams" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [partial_defeature, delete_interior_nodes, allow_curved_topo_faces, fillet_spanning_angle, aggressive_edge_merge, thin_stripes_tolerance, partial_defeature_params, delete_interior_nodes_params])
            if all_field_specified:
                self.__initialize(
                    partial_defeature,
                    delete_interior_nodes,
                    allow_curved_topo_faces,
                    fillet_spanning_angle,
                    aggressive_edge_merge,
                    thin_stripes_tolerance,
                    partial_defeature_params,
                    delete_interior_nodes_params)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DefeatureTopologyParams")
                    json_data = param_json["DefeatureTopologyParams"] if "DefeatureTopologyParams" in param_json else {}
                    self.__initialize(
                        partial_defeature if partial_defeature is not None else ( DefeatureTopologyParams._default_params["partial_defeature"] if "partial_defeature" in DefeatureTopologyParams._default_params else (json_data["partialDefeature"] if "partialDefeature" in json_data else None)),
                        delete_interior_nodes if delete_interior_nodes is not None else ( DefeatureTopologyParams._default_params["delete_interior_nodes"] if "delete_interior_nodes" in DefeatureTopologyParams._default_params else (json_data["deleteInteriorNodes"] if "deleteInteriorNodes" in json_data else None)),
                        allow_curved_topo_faces if allow_curved_topo_faces is not None else ( DefeatureTopologyParams._default_params["allow_curved_topo_faces"] if "allow_curved_topo_faces" in DefeatureTopologyParams._default_params else (json_data["allowCurvedTopoFaces"] if "allowCurvedTopoFaces" in json_data else None)),
                        fillet_spanning_angle if fillet_spanning_angle is not None else ( DefeatureTopologyParams._default_params["fillet_spanning_angle"] if "fillet_spanning_angle" in DefeatureTopologyParams._default_params else (json_data["filletSpanningAngle"] if "filletSpanningAngle" in json_data else None)),
                        aggressive_edge_merge if aggressive_edge_merge is not None else ( DefeatureTopologyParams._default_params["aggressive_edge_merge"] if "aggressive_edge_merge" in DefeatureTopologyParams._default_params else (json_data["aggressiveEdgeMerge"] if "aggressiveEdgeMerge" in json_data else None)),
                        thin_stripes_tolerance if thin_stripes_tolerance is not None else ( DefeatureTopologyParams._default_params["thin_stripes_tolerance"] if "thin_stripes_tolerance" in DefeatureTopologyParams._default_params else (json_data["thinStripesTolerance"] if "thinStripesTolerance" in json_data else None)),
                        partial_defeature_params if partial_defeature_params is not None else ( DefeatureTopologyParams._default_params["partial_defeature_params"] if "partial_defeature_params" in DefeatureTopologyParams._default_params else PartialDefeatureParams(model = model, json_data = (json_data["partialDefeatureParams"] if "partialDefeatureParams" in json_data else None))),
                        delete_interior_nodes_params if delete_interior_nodes_params is not None else ( DefeatureTopologyParams._default_params["delete_interior_nodes_params"] if "delete_interior_nodes_params" in DefeatureTopologyParams._default_params else DeleteInteriorNodesParams(model = model, json_data = (json_data["deleteInteriorNodesParams"] if "deleteInteriorNodesParams" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            partial_defeature: bool = None,
            delete_interior_nodes: bool = None,
            allow_curved_topo_faces: bool = None,
            fillet_spanning_angle: float = None,
            aggressive_edge_merge: bool = None,
            thin_stripes_tolerance: float = None,
            partial_defeature_params: PartialDefeatureParams = None,
            delete_interior_nodes_params: DeleteInteriorNodesParams = None):
        """Set the default values of the ``DefeatureTopologyParams`` object.

        Parameters
        ----------
        partial_defeature: bool, optional
            Option to partial defeature.
        delete_interior_nodes: bool, optional
            Option to delete interior nodes.
        allow_curved_topo_faces: bool, optional
            Option to allow curved topofaces.
        fillet_spanning_angle: float, optional
            Angular threshold for detecting fillets with spanning angles below the provided value.
        aggressive_edge_merge: bool, optional
            Indicate whether to allow aggressive edge merge while performing partial defeature.
        thin_stripes_tolerance: float, optional
            Topoface width tolerance to detect thin faces below the provided value.
        partial_defeature_params: PartialDefeatureParams, optional
            Parameters for partial defeature operation.
        delete_interior_nodes_params: DeleteInteriorNodesParams, optional
            Parameters for delete interior nodes operation.
        """
        args = locals()
        [DefeatureTopologyParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DefeatureTopologyParams`` object.

        Examples
        --------
        >>> DefeatureTopologyParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DefeatureTopologyParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._partial_defeature is not None:
            json_data["partialDefeature"] = self._partial_defeature
        if self._delete_interior_nodes is not None:
            json_data["deleteInteriorNodes"] = self._delete_interior_nodes
        if self._allow_curved_topo_faces is not None:
            json_data["allowCurvedTopoFaces"] = self._allow_curved_topo_faces
        if self._fillet_spanning_angle is not None:
            json_data["filletSpanningAngle"] = self._fillet_spanning_angle
        if self._aggressive_edge_merge is not None:
            json_data["aggressiveEdgeMerge"] = self._aggressive_edge_merge
        if self._thin_stripes_tolerance is not None:
            json_data["thinStripesTolerance"] = self._thin_stripes_tolerance
        if self._partial_defeature_params is not None:
            json_data["partialDefeatureParams"] = self._partial_defeature_params._jsonify()
        if self._delete_interior_nodes_params is not None:
            json_data["deleteInteriorNodesParams"] = self._delete_interior_nodes_params._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "partial_defeature :  %s\ndelete_interior_nodes :  %s\nallow_curved_topo_faces :  %s\nfillet_spanning_angle :  %s\naggressive_edge_merge :  %s\nthin_stripes_tolerance :  %s\npartial_defeature_params :  %s\ndelete_interior_nodes_params :  %s" % (self._partial_defeature, self._delete_interior_nodes, self._allow_curved_topo_faces, self._fillet_spanning_angle, self._aggressive_edge_merge, self._thin_stripes_tolerance, '{ ' + str(self._partial_defeature_params) + ' }', '{ ' + str(self._delete_interior_nodes_params) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def partial_defeature(self) -> bool:
        """Option to partial defeature.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._partial_defeature

    @partial_defeature.setter
    def partial_defeature(self, value: bool):
        self._partial_defeature = value

    @property
    def delete_interior_nodes(self) -> bool:
        """Option to delete interior nodes.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._delete_interior_nodes

    @delete_interior_nodes.setter
    def delete_interior_nodes(self, value: bool):
        self._delete_interior_nodes = value

    @property
    def allow_curved_topo_faces(self) -> bool:
        """Option to allow curved topofaces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._allow_curved_topo_faces

    @allow_curved_topo_faces.setter
    def allow_curved_topo_faces(self, value: bool):
        self._allow_curved_topo_faces = value

    @property
    def fillet_spanning_angle(self) -> float:
        """Angular threshold for detecting fillets with spanning angles below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._fillet_spanning_angle

    @fillet_spanning_angle.setter
    def fillet_spanning_angle(self, value: float):
        self._fillet_spanning_angle = value

    @property
    def aggressive_edge_merge(self) -> bool:
        """Indicate whether to allow aggressive edge merge while performing partial defeature.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._aggressive_edge_merge

    @aggressive_edge_merge.setter
    def aggressive_edge_merge(self, value: bool):
        self._aggressive_edge_merge = value

    @property
    def thin_stripes_tolerance(self) -> float:
        """Topoface width tolerance to detect thin faces below the provided value.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._thin_stripes_tolerance

    @thin_stripes_tolerance.setter
    def thin_stripes_tolerance(self, value: float):
        self._thin_stripes_tolerance = value

    @property
    def partial_defeature_params(self) -> PartialDefeatureParams:
        """Parameters for partial defeature operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._partial_defeature_params

    @partial_defeature_params.setter
    def partial_defeature_params(self, value: PartialDefeatureParams):
        self._partial_defeature_params = value

    @property
    def delete_interior_nodes_params(self) -> DeleteInteriorNodesParams:
        """Parameters for delete interior nodes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._delete_interior_nodes_params

    @delete_interior_nodes_params.setter
    def delete_interior_nodes_params(self, value: DeleteInteriorNodesParams):
        self._delete_interior_nodes_params = value

class OptimizeQuadMeshParams(CoreObject):
    """Parameters for optimize quad mesh operations.

    Parameters
    ----------
    model: Model
        Model to create a ``OptimizeQuadMeshParams`` object with default parameters.
    suppress_topo_edge_and_mesh_cleanup: bool, optional
        Option to suppress topoedges and clean up mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    edge_mesh_constant_size: float, optional
        Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    surface_mesh_constant_size: float, optional
        Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    generate_quads: bool, optional
        Option to generate quadrilateral surface mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    project_on_geometry: bool, optional
        Option to project on geometry when meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    delete_interior_nodes_params: DeleteInteriorNodesParams, optional
        Parameters to control delete interior nodes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``OptimizeQuadMeshParams`` object with provided parameters.

    Examples
    --------
    >>> optimize_quad_mesh_params = prime.OptimizeQuadMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            suppress_topo_edge_and_mesh_cleanup: bool,
            edge_mesh_constant_size: float,
            surface_mesh_constant_size: float,
            generate_quads: bool,
            project_on_geometry: bool,
            delete_interior_nodes_params: DeleteInteriorNodesParams):
        self._suppress_topo_edge_and_mesh_cleanup = suppress_topo_edge_and_mesh_cleanup
        self._edge_mesh_constant_size = edge_mesh_constant_size
        self._surface_mesh_constant_size = surface_mesh_constant_size
        self._generate_quads = generate_quads
        self._project_on_geometry = project_on_geometry
        self._delete_interior_nodes_params = delete_interior_nodes_params

    def __init__(
            self,
            model: CommunicationManager=None,
            suppress_topo_edge_and_mesh_cleanup: bool = None,
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None,
            generate_quads: bool = None,
            project_on_geometry: bool = None,
            delete_interior_nodes_params: DeleteInteriorNodesParams = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``OptimizeQuadMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``OptimizeQuadMeshParams`` object with default parameters.
        suppress_topo_edge_and_mesh_cleanup: bool, optional
            Option to suppress topoedges and clean up mesh.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        project_on_geometry: bool, optional
            Option to project on geometry when meshing.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        delete_interior_nodes_params: DeleteInteriorNodesParams, optional
            Parameters to control delete interior nodes operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``OptimizeQuadMeshParams`` object with provided parameters.

        Examples
        --------
        >>> optimize_quad_mesh_params = prime.OptimizeQuadMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["suppressTopoEdgeAndMeshCleanup"] if "suppressTopoEdgeAndMeshCleanup" in json_data else None,
                json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None,
                json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None,
                json_data["generateQuads"] if "generateQuads" in json_data else None,
                json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None,
                DeleteInteriorNodesParams(model = model, json_data = json_data["deleteInteriorNodesParams"] if "deleteInteriorNodesParams" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [suppress_topo_edge_and_mesh_cleanup, edge_mesh_constant_size, surface_mesh_constant_size, generate_quads, project_on_geometry, delete_interior_nodes_params])
            if all_field_specified:
                self.__initialize(
                    suppress_topo_edge_and_mesh_cleanup,
                    edge_mesh_constant_size,
                    surface_mesh_constant_size,
                    generate_quads,
                    project_on_geometry,
                    delete_interior_nodes_params)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "OptimizeQuadMeshParams")
                    json_data = param_json["OptimizeQuadMeshParams"] if "OptimizeQuadMeshParams" in param_json else {}
                    self.__initialize(
                        suppress_topo_edge_and_mesh_cleanup if suppress_topo_edge_and_mesh_cleanup is not None else ( OptimizeQuadMeshParams._default_params["suppress_topo_edge_and_mesh_cleanup"] if "suppress_topo_edge_and_mesh_cleanup" in OptimizeQuadMeshParams._default_params else (json_data["suppressTopoEdgeAndMeshCleanup"] if "suppressTopoEdgeAndMeshCleanup" in json_data else None)),
                        edge_mesh_constant_size if edge_mesh_constant_size is not None else ( OptimizeQuadMeshParams._default_params["edge_mesh_constant_size"] if "edge_mesh_constant_size" in OptimizeQuadMeshParams._default_params else (json_data["edgeMeshConstantSize"] if "edgeMeshConstantSize" in json_data else None)),
                        surface_mesh_constant_size if surface_mesh_constant_size is not None else ( OptimizeQuadMeshParams._default_params["surface_mesh_constant_size"] if "surface_mesh_constant_size" in OptimizeQuadMeshParams._default_params else (json_data["surfaceMeshConstantSize"] if "surfaceMeshConstantSize" in json_data else None)),
                        generate_quads if generate_quads is not None else ( OptimizeQuadMeshParams._default_params["generate_quads"] if "generate_quads" in OptimizeQuadMeshParams._default_params else (json_data["generateQuads"] if "generateQuads" in json_data else None)),
                        project_on_geometry if project_on_geometry is not None else ( OptimizeQuadMeshParams._default_params["project_on_geometry"] if "project_on_geometry" in OptimizeQuadMeshParams._default_params else (json_data["projectOnGeometry"] if "projectOnGeometry" in json_data else None)),
                        delete_interior_nodes_params if delete_interior_nodes_params is not None else ( OptimizeQuadMeshParams._default_params["delete_interior_nodes_params"] if "delete_interior_nodes_params" in OptimizeQuadMeshParams._default_params else DeleteInteriorNodesParams(model = model, json_data = (json_data["deleteInteriorNodesParams"] if "deleteInteriorNodesParams" in json_data else None))))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            suppress_topo_edge_and_mesh_cleanup: bool = None,
            edge_mesh_constant_size: float = None,
            surface_mesh_constant_size: float = None,
            generate_quads: bool = None,
            project_on_geometry: bool = None,
            delete_interior_nodes_params: DeleteInteriorNodesParams = None):
        """Set the default values of the ``OptimizeQuadMeshParams`` object.

        Parameters
        ----------
        suppress_topo_edge_and_mesh_cleanup: bool, optional
            Option to suppress topoedges and clean up mesh.
        edge_mesh_constant_size: float, optional
            Constant size used for edge meshing.
        surface_mesh_constant_size: float, optional
            Constant size used for surface meshing.
        generate_quads: bool, optional
            Option to generate quadrilateral surface mesh.
        project_on_geometry: bool, optional
            Option to project on geometry when meshing.
        delete_interior_nodes_params: DeleteInteriorNodesParams, optional
            Parameters to control delete interior nodes operation.
        """
        args = locals()
        [OptimizeQuadMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``OptimizeQuadMeshParams`` object.

        Examples
        --------
        >>> OptimizeQuadMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in OptimizeQuadMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._suppress_topo_edge_and_mesh_cleanup is not None:
            json_data["suppressTopoEdgeAndMeshCleanup"] = self._suppress_topo_edge_and_mesh_cleanup
        if self._edge_mesh_constant_size is not None:
            json_data["edgeMeshConstantSize"] = self._edge_mesh_constant_size
        if self._surface_mesh_constant_size is not None:
            json_data["surfaceMeshConstantSize"] = self._surface_mesh_constant_size
        if self._generate_quads is not None:
            json_data["generateQuads"] = self._generate_quads
        if self._project_on_geometry is not None:
            json_data["projectOnGeometry"] = self._project_on_geometry
        if self._delete_interior_nodes_params is not None:
            json_data["deleteInteriorNodesParams"] = self._delete_interior_nodes_params._jsonify()
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "suppress_topo_edge_and_mesh_cleanup :  %s\nedge_mesh_constant_size :  %s\nsurface_mesh_constant_size :  %s\ngenerate_quads :  %s\nproject_on_geometry :  %s\ndelete_interior_nodes_params :  %s" % (self._suppress_topo_edge_and_mesh_cleanup, self._edge_mesh_constant_size, self._surface_mesh_constant_size, self._generate_quads, self._project_on_geometry, '{ ' + str(self._delete_interior_nodes_params) + ' }')
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def suppress_topo_edge_and_mesh_cleanup(self) -> bool:
        """Option to suppress topoedges and clean up mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._suppress_topo_edge_and_mesh_cleanup

    @suppress_topo_edge_and_mesh_cleanup.setter
    def suppress_topo_edge_and_mesh_cleanup(self, value: bool):
        self._suppress_topo_edge_and_mesh_cleanup = value

    @property
    def edge_mesh_constant_size(self) -> float:
        """Constant size used for edge meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_mesh_constant_size

    @edge_mesh_constant_size.setter
    def edge_mesh_constant_size(self, value: float):
        self._edge_mesh_constant_size = value

    @property
    def surface_mesh_constant_size(self) -> float:
        """Constant size used for surface meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._surface_mesh_constant_size

    @surface_mesh_constant_size.setter
    def surface_mesh_constant_size(self, value: float):
        self._surface_mesh_constant_size = value

    @property
    def generate_quads(self) -> bool:
        """Option to generate quadrilateral surface mesh.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._generate_quads

    @generate_quads.setter
    def generate_quads(self, value: bool):
        self._generate_quads = value

    @property
    def project_on_geometry(self) -> bool:
        """Option to project on geometry when meshing.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._project_on_geometry

    @project_on_geometry.setter
    def project_on_geometry(self, value: bool):
        self._project_on_geometry = value

    @property
    def delete_interior_nodes_params(self) -> DeleteInteriorNodesParams:
        """Parameters to control delete interior nodes operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._delete_interior_nodes_params

    @delete_interior_nodes_params.setter
    def delete_interior_nodes_params(self, value: DeleteInteriorNodesParams):
        self._delete_interior_nodes_params = value

class CheckTopologyParams(CoreObject):
    """Parameters for check topology operations.

    Parameters
    ----------
    model: Model
        Model to create a ``CheckTopologyParams`` object with default parameters.
    topo_search_field_mask: int, optional
        Toposearch field option for topology check.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``CheckTopologyParams`` object with provided parameters.

    Examples
    --------
    >>> check_topology_params = prime.CheckTopologyParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            topo_search_field_mask: int):
        self._topo_search_field_mask = topo_search_field_mask

    def __init__(
            self,
            model: CommunicationManager=None,
            topo_search_field_mask: int = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``CheckTopologyParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``CheckTopologyParams`` object with default parameters.
        topo_search_field_mask: int, optional
            Toposearch field option for topology check.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``CheckTopologyParams`` object with provided parameters.

        Examples
        --------
        >>> check_topology_params = prime.CheckTopologyParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["topoSearchFieldMask"] if "topoSearchFieldMask" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [topo_search_field_mask])
            if all_field_specified:
                self.__initialize(
                    topo_search_field_mask)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "CheckTopologyParams")
                    json_data = param_json["CheckTopologyParams"] if "CheckTopologyParams" in param_json else {}
                    self.__initialize(
                        topo_search_field_mask if topo_search_field_mask is not None else ( CheckTopologyParams._default_params["topo_search_field_mask"] if "topo_search_field_mask" in CheckTopologyParams._default_params else (json_data["topoSearchFieldMask"] if "topoSearchFieldMask" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            topo_search_field_mask: int = None):
        """Set the default values of the ``CheckTopologyParams`` object.

        Parameters
        ----------
        topo_search_field_mask: int, optional
            Toposearch field option for topology check.
        """
        args = locals()
        [CheckTopologyParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``CheckTopologyParams`` object.

        Examples
        --------
        >>> CheckTopologyParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in CheckTopologyParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._topo_search_field_mask is not None:
            json_data["topoSearchFieldMask"] = self._topo_search_field_mask
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "topo_search_field_mask :  %s" % (self._topo_search_field_mask)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def topo_search_field_mask(self) -> int:
        """Toposearch field option for topology check.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._topo_search_field_mask

    @topo_search_field_mask.setter
    def topo_search_field_mask(self, value: int):
        self._topo_search_field_mask = value

class AutoQuadMesherResults(CoreObject):
    """Results of auto quad mesher.

    Parameters
    ----------
    model: Model
        Model to create a ``AutoQuadMesherResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code if AutoQuadMesher operation is unsuccessful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    warning_codes: List[WarningCode], optional
        Warning code if AutoQuadMesher operation is partially successful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    failed_topo_face_ids: Iterable[int], optional
        Ids of the failed topofaces during topology check.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``AutoQuadMesherResults`` object with provided parameters.

    Examples
    --------
    >>> auto_quad_mesher_results = prime.AutoQuadMesherResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            warning_codes: List[WarningCode],
            failed_topo_face_ids: Iterable[int]):
        self._error_code = ErrorCode(error_code)
        self._warning_codes = warning_codes
        self._failed_topo_face_ids = failed_topo_face_ids if isinstance(failed_topo_face_ids, np.ndarray) else np.array(failed_topo_face_ids, dtype=np.int32) if failed_topo_face_ids is not None else None

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            warning_codes: List[WarningCode] = None,
            failed_topo_face_ids: Iterable[int] = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``AutoQuadMesherResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``AutoQuadMesherResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code if AutoQuadMesher operation is unsuccessful.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        warning_codes: List[WarningCode], optional
            Warning code if AutoQuadMesher operation is partially successful.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        failed_topo_face_ids: Iterable[int], optional
            Ids of the failed topofaces during topology check.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``AutoQuadMesherResults`` object with provided parameters.

        Examples
        --------
        >>> auto_quad_mesher_results = prime.AutoQuadMesherResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                [WarningCode(data) for data in json_data["warningCodes"]] if "warningCodes" in json_data else None,
                json_data["failedTopoFaceIds"] if "failedTopoFaceIds" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, warning_codes, failed_topo_face_ids])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    warning_codes,
                    failed_topo_face_ids)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "AutoQuadMesherResults")
                    json_data = param_json["AutoQuadMesherResults"] if "AutoQuadMesherResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( AutoQuadMesherResults._default_params["error_code"] if "error_code" in AutoQuadMesherResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        warning_codes if warning_codes is not None else ( AutoQuadMesherResults._default_params["warning_codes"] if "warning_codes" in AutoQuadMesherResults._default_params else [WarningCode(data) for data in (json_data["warningCodes"] if "warningCodes" in json_data else None)]),
                        failed_topo_face_ids if failed_topo_face_ids is not None else ( AutoQuadMesherResults._default_params["failed_topo_face_ids"] if "failed_topo_face_ids" in AutoQuadMesherResults._default_params else (json_data["failedTopoFaceIds"] if "failedTopoFaceIds" in json_data else None)))
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
            failed_topo_face_ids: Iterable[int] = None):
        """Set the default values of the ``AutoQuadMesherResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code if AutoQuadMesher operation is unsuccessful.
        warning_codes: List[WarningCode], optional
            Warning code if AutoQuadMesher operation is partially successful.
        failed_topo_face_ids: Iterable[int], optional
            Ids of the failed topofaces during topology check.
        """
        args = locals()
        [AutoQuadMesherResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``AutoQuadMesherResults`` object.

        Examples
        --------
        >>> AutoQuadMesherResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in AutoQuadMesherResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._warning_codes is not None:
            json_data["warningCodes"] = [data for data in self._warning_codes]
        if self._failed_topo_face_ids is not None:
            json_data["failedTopoFaceIds"] = self._failed_topo_face_ids
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nwarning_codes :  %s\nfailed_topo_face_ids :  %s" % (self._error_code, '[' + ''.join('\n' + str(data) for data in self._warning_codes) + ']', self._failed_topo_face_ids)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def error_code(self) -> ErrorCode:
        """Error code if AutoQuadMesher operation is unsuccessful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

    @property
    def warning_codes(self) -> List[WarningCode]:
        """Warning code if AutoQuadMesher operation is partially successful.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._warning_codes

    @warning_codes.setter
    def warning_codes(self, value: List[WarningCode]):
        self._warning_codes = value

    @property
    def failed_topo_face_ids(self) -> Iterable[int]:
        """Ids of the failed topofaces during topology check.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._failed_topo_face_ids

    @failed_topo_face_ids.setter
    def failed_topo_face_ids(self, value: Iterable[int]):
        self._failed_topo_face_ids = value
