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

class ScaffolderRepairMode(enum.IntEnum):
    """Mode of Scaffolder repair to be used.
    """
    DEFAULT = 0
    """Repairs edges using the distance tolerance parameter.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    CONSERVATIVE = 1
    """Repairs edges without considering the distance tolerance parameter.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class IntersectionMask(enum.IntEnum):
    """Scaffold parameters use intersection mask to define nature of intersection computation.
    """
    EDGEEDGE = 1
    """Performs edge to edge intersection."""
    FACEFACE = 2
    """Performs face to face intersection."""
    FACEFACEANDEDGEEDGE = 3
    """Perform face to face and edge to edge intersections."""

class EdgeMergeControl(enum.IntEnum):
    """Specifies type of edge pairs to be merged during scaffold operation.
    """
    ALLTOALL = 1
    """Allows to merge all types of edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FREETOALL = 2
    """Allows to merge only free edges into all edges.

    **This is a beta parameter**. **The behavior and name may change in the future**."""
    FREETOFREE = 3
    """Allows to merge free edge into other free edge only.

    **This is a beta parameter**. **The behavior and name may change in the future**."""

class ScaffolderParams(CoreObject):
    """Parameters to control scaffold operation.

    Parameters
    ----------
    model: Model
        Model to create a ``ScaffolderParams`` object with default parameters.
    absolute_dist_tol: float, optional
        Defines the maximum gap to connect.
    repair_mode: ScaffolderRepairMode, optional
        Defines the mode to be used during repair or connect.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    size_field_type: int, optional
        Specifies the type of size field used for scaffolding.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    intersection_control_mask: IntersectionMask, optional
        Specifies the nature of intersection to be computed.
    edge_merge_control: int, optional
        Specifies type of edge pairs to be merged during scaffold operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    constant_mesh_size: float, optional
        Defines the constant edge mesh size to check connection.
    remove_holes_critical_radius: float, optional
        Defines the maximum radius of holes to be removed.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    remove_slivers_abs_dist_tol_ratio: float, optional
        Defines the maximum aspect ratio to remove sliver faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    triangles_coplanar_angle_cos: float, optional
        Lower bound for cos angle to consider coplanar faces for scaffolding.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``ScaffolderParams`` object with provided parameters.

    Examples
    --------
    >>> scaffolder_params = prime.ScaffolderParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            absolute_dist_tol: float,
            repair_mode: ScaffolderRepairMode,
            size_field_type: int,
            intersection_control_mask: IntersectionMask,
            edge_merge_control: int,
            constant_mesh_size: float,
            remove_holes_critical_radius: float,
            remove_slivers_abs_dist_tol_ratio: float,
            triangles_coplanar_angle_cos: float):
        self._absolute_dist_tol = absolute_dist_tol
        self._repair_mode = ScaffolderRepairMode(repair_mode)
        self._size_field_type = size_field_type
        self._intersection_control_mask = IntersectionMask(intersection_control_mask)
        self._edge_merge_control = edge_merge_control
        self._constant_mesh_size = constant_mesh_size
        self._remove_holes_critical_radius = remove_holes_critical_radius
        self._remove_slivers_abs_dist_tol_ratio = remove_slivers_abs_dist_tol_ratio
        self._triangles_coplanar_angle_cos = triangles_coplanar_angle_cos

    def __init__(
            self,
            model: CommunicationManager=None,
            absolute_dist_tol: float = None,
            repair_mode: ScaffolderRepairMode = None,
            size_field_type: int = None,
            intersection_control_mask: IntersectionMask = None,
            edge_merge_control: int = None,
            constant_mesh_size: float = None,
            remove_holes_critical_radius: float = None,
            remove_slivers_abs_dist_tol_ratio: float = None,
            triangles_coplanar_angle_cos: float = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ScaffolderParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ScaffolderParams`` object with default parameters.
        absolute_dist_tol: float, optional
            Defines the maximum gap to connect.
        repair_mode: ScaffolderRepairMode, optional
            Defines the mode to be used during repair or connect.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        size_field_type: int, optional
            Specifies the type of size field used for scaffolding.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        intersection_control_mask: IntersectionMask, optional
            Specifies the nature of intersection to be computed.
        edge_merge_control: int, optional
            Specifies type of edge pairs to be merged during scaffold operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        constant_mesh_size: float, optional
            Defines the constant edge mesh size to check connection.
        remove_holes_critical_radius: float, optional
            Defines the maximum radius of holes to be removed.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        remove_slivers_abs_dist_tol_ratio: float, optional
            Defines the maximum aspect ratio to remove sliver faces.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        triangles_coplanar_angle_cos: float, optional
            Lower bound for cos angle to consider coplanar faces for scaffolding.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``ScaffolderParams`` object with provided parameters.

        Examples
        --------
        >>> scaffolder_params = prime.ScaffolderParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None,
                ScaffolderRepairMode(json_data["repairMode"] if "repairMode" in json_data else None),
                json_data["sizeFieldType"] if "sizeFieldType" in json_data else None,
                IntersectionMask(json_data["intersectionControlMask"] if "intersectionControlMask" in json_data else None),
                json_data["edgeMergeControl"] if "edgeMergeControl" in json_data else None,
                json_data["constantMeshSize"] if "constantMeshSize" in json_data else None,
                json_data["removeHolesCriticalRadius"] if "removeHolesCriticalRadius" in json_data else None,
                json_data["removeSliversAbsDistTolRatio"] if "removeSliversAbsDistTolRatio" in json_data else None,
                json_data["trianglesCoplanarAngleCos"] if "trianglesCoplanarAngleCos" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [absolute_dist_tol, repair_mode, size_field_type, intersection_control_mask, edge_merge_control, constant_mesh_size, remove_holes_critical_radius, remove_slivers_abs_dist_tol_ratio, triangles_coplanar_angle_cos])
            if all_field_specified:
                self.__initialize(
                    absolute_dist_tol,
                    repair_mode,
                    size_field_type,
                    intersection_control_mask,
                    edge_merge_control,
                    constant_mesh_size,
                    remove_holes_critical_radius,
                    remove_slivers_abs_dist_tol_ratio,
                    triangles_coplanar_angle_cos)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScaffolderParams")
                    json_data = param_json["ScaffolderParams"] if "ScaffolderParams" in param_json else {}
                    self.__initialize(
                        absolute_dist_tol if absolute_dist_tol is not None else ( ScaffolderParams._default_params["absolute_dist_tol"] if "absolute_dist_tol" in ScaffolderParams._default_params else (json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None)),
                        repair_mode if repair_mode is not None else ( ScaffolderParams._default_params["repair_mode"] if "repair_mode" in ScaffolderParams._default_params else ScaffolderRepairMode(json_data["repairMode"] if "repairMode" in json_data else None)),
                        size_field_type if size_field_type is not None else ( ScaffolderParams._default_params["size_field_type"] if "size_field_type" in ScaffolderParams._default_params else (json_data["sizeFieldType"] if "sizeFieldType" in json_data else None)),
                        intersection_control_mask if intersection_control_mask is not None else ( ScaffolderParams._default_params["intersection_control_mask"] if "intersection_control_mask" in ScaffolderParams._default_params else IntersectionMask(json_data["intersectionControlMask"] if "intersectionControlMask" in json_data else None)),
                        edge_merge_control if edge_merge_control is not None else ( ScaffolderParams._default_params["edge_merge_control"] if "edge_merge_control" in ScaffolderParams._default_params else (json_data["edgeMergeControl"] if "edgeMergeControl" in json_data else None)),
                        constant_mesh_size if constant_mesh_size is not None else ( ScaffolderParams._default_params["constant_mesh_size"] if "constant_mesh_size" in ScaffolderParams._default_params else (json_data["constantMeshSize"] if "constantMeshSize" in json_data else None)),
                        remove_holes_critical_radius if remove_holes_critical_radius is not None else ( ScaffolderParams._default_params["remove_holes_critical_radius"] if "remove_holes_critical_radius" in ScaffolderParams._default_params else (json_data["removeHolesCriticalRadius"] if "removeHolesCriticalRadius" in json_data else None)),
                        remove_slivers_abs_dist_tol_ratio if remove_slivers_abs_dist_tol_ratio is not None else ( ScaffolderParams._default_params["remove_slivers_abs_dist_tol_ratio"] if "remove_slivers_abs_dist_tol_ratio" in ScaffolderParams._default_params else (json_data["removeSliversAbsDistTolRatio"] if "removeSliversAbsDistTolRatio" in json_data else None)),
                        triangles_coplanar_angle_cos if triangles_coplanar_angle_cos is not None else ( ScaffolderParams._default_params["triangles_coplanar_angle_cos"] if "triangles_coplanar_angle_cos" in ScaffolderParams._default_params else (json_data["trianglesCoplanarAngleCos"] if "trianglesCoplanarAngleCos" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            absolute_dist_tol: float = None,
            repair_mode: ScaffolderRepairMode = None,
            size_field_type: int = None,
            intersection_control_mask: IntersectionMask = None,
            edge_merge_control: int = None,
            constant_mesh_size: float = None,
            remove_holes_critical_radius: float = None,
            remove_slivers_abs_dist_tol_ratio: float = None,
            triangles_coplanar_angle_cos: float = None):
        """Set the default values of the ``ScaffolderParams`` object.

        Parameters
        ----------
        absolute_dist_tol: float, optional
            Defines the maximum gap to connect.
        repair_mode: ScaffolderRepairMode, optional
            Defines the mode to be used during repair or connect.
        size_field_type: int, optional
            Specifies the type of size field used for scaffolding.
        intersection_control_mask: IntersectionMask, optional
            Specifies the nature of intersection to be computed.
        edge_merge_control: int, optional
            Specifies type of edge pairs to be merged during scaffold operation.
        constant_mesh_size: float, optional
            Defines the constant edge mesh size to check connection.
        remove_holes_critical_radius: float, optional
            Defines the maximum radius of holes to be removed.
        remove_slivers_abs_dist_tol_ratio: float, optional
            Defines the maximum aspect ratio to remove sliver faces.
        triangles_coplanar_angle_cos: float, optional
            Lower bound for cos angle to consider coplanar faces for scaffolding.
        """
        args = locals()
        [ScaffolderParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScaffolderParams`` object.

        Examples
        --------
        >>> ScaffolderParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScaffolderParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._absolute_dist_tol is not None:
            json_data["absoluteDistTol"] = self._absolute_dist_tol
        if self._repair_mode is not None:
            json_data["repairMode"] = self._repair_mode
        if self._size_field_type is not None:
            json_data["sizeFieldType"] = self._size_field_type
        if self._intersection_control_mask is not None:
            json_data["intersectionControlMask"] = self._intersection_control_mask
        if self._edge_merge_control is not None:
            json_data["edgeMergeControl"] = self._edge_merge_control
        if self._constant_mesh_size is not None:
            json_data["constantMeshSize"] = self._constant_mesh_size
        if self._remove_holes_critical_radius is not None:
            json_data["removeHolesCriticalRadius"] = self._remove_holes_critical_radius
        if self._remove_slivers_abs_dist_tol_ratio is not None:
            json_data["removeSliversAbsDistTolRatio"] = self._remove_slivers_abs_dist_tol_ratio
        if self._triangles_coplanar_angle_cos is not None:
            json_data["trianglesCoplanarAngleCos"] = self._triangles_coplanar_angle_cos
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "absolute_dist_tol :  %s\nrepair_mode :  %s\nsize_field_type :  %s\nintersection_control_mask :  %s\nedge_merge_control :  %s\nconstant_mesh_size :  %s\nremove_holes_critical_radius :  %s\nremove_slivers_abs_dist_tol_ratio :  %s\ntriangles_coplanar_angle_cos :  %s" % (self._absolute_dist_tol, self._repair_mode, self._size_field_type, self._intersection_control_mask, self._edge_merge_control, self._constant_mesh_size, self._remove_holes_critical_radius, self._remove_slivers_abs_dist_tol_ratio, self._triangles_coplanar_angle_cos)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def absolute_dist_tol(self) -> float:
        """Defines the maximum gap to connect.
        """
        return self._absolute_dist_tol

    @absolute_dist_tol.setter
    def absolute_dist_tol(self, value: float):
        self._absolute_dist_tol = value

    @property
    def repair_mode(self) -> ScaffolderRepairMode:
        """Defines the mode to be used during repair or connect.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._repair_mode

    @repair_mode.setter
    def repair_mode(self, value: ScaffolderRepairMode):
        self._repair_mode = value

    @property
    def size_field_type(self) -> int:
        """Specifies the type of size field used for scaffolding.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._size_field_type

    @size_field_type.setter
    def size_field_type(self, value: int):
        self._size_field_type = value

    @property
    def intersection_control_mask(self) -> IntersectionMask:
        """Specifies the nature of intersection to be computed.
        """
        return self._intersection_control_mask

    @intersection_control_mask.setter
    def intersection_control_mask(self, value: IntersectionMask):
        self._intersection_control_mask = value

    @property
    def edge_merge_control(self) -> int:
        """Specifies type of edge pairs to be merged during scaffold operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._edge_merge_control

    @edge_merge_control.setter
    def edge_merge_control(self, value: int):
        self._edge_merge_control = value

    @property
    def constant_mesh_size(self) -> float:
        """Defines the constant edge mesh size to check connection.
        """
        return self._constant_mesh_size

    @constant_mesh_size.setter
    def constant_mesh_size(self, value: float):
        self._constant_mesh_size = value

    @property
    def remove_holes_critical_radius(self) -> float:
        """Defines the maximum radius of holes to be removed.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._remove_holes_critical_radius

    @remove_holes_critical_radius.setter
    def remove_holes_critical_radius(self, value: float):
        self._remove_holes_critical_radius = value

    @property
    def remove_slivers_abs_dist_tol_ratio(self) -> float:
        """Defines the maximum aspect ratio to remove sliver faces.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._remove_slivers_abs_dist_tol_ratio

    @remove_slivers_abs_dist_tol_ratio.setter
    def remove_slivers_abs_dist_tol_ratio(self, value: float):
        self._remove_slivers_abs_dist_tol_ratio = value

    @property
    def triangles_coplanar_angle_cos(self) -> float:
        """Lower bound for cos angle to consider coplanar faces for scaffolding.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._triangles_coplanar_angle_cos

    @triangles_coplanar_angle_cos.setter
    def triangles_coplanar_angle_cos(self, value: float):
        self._triangles_coplanar_angle_cos = value

class VolumetricScaffolderParams(CoreObject):
    """Parameters to control delete shadowed topofaces operation.

    Parameters
    ----------
    model: Model
        Model to create a ``VolumetricScaffolderParams`` object with default parameters.
    absolute_dist_tol: float, optional
        Specify distance tolerance between overlapping faces.
    only_check_exact_overlaps: bool, optional
        Check only for fully overlapping topofaces when true.
    json_data: dict, optional
        JSON dictionary to create a ``VolumetricScaffolderParams`` object with provided parameters.

    Examples
    --------
    >>> volumetric_scaffolder_params = prime.VolumetricScaffolderParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            absolute_dist_tol: float,
            only_check_exact_overlaps: bool):
        self._absolute_dist_tol = absolute_dist_tol
        self._only_check_exact_overlaps = only_check_exact_overlaps

    def __init__(
            self,
            model: CommunicationManager=None,
            absolute_dist_tol: float = None,
            only_check_exact_overlaps: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``VolumetricScaffolderParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``VolumetricScaffolderParams`` object with default parameters.
        absolute_dist_tol: float, optional
            Specify distance tolerance between overlapping faces.
        only_check_exact_overlaps: bool, optional
            Check only for fully overlapping topofaces when true.
        json_data: dict, optional
            JSON dictionary to create a ``VolumetricScaffolderParams`` object with provided parameters.

        Examples
        --------
        >>> volumetric_scaffolder_params = prime.VolumetricScaffolderParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None,
                json_data["onlyCheckExactOverlaps"] if "onlyCheckExactOverlaps" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [absolute_dist_tol, only_check_exact_overlaps])
            if all_field_specified:
                self.__initialize(
                    absolute_dist_tol,
                    only_check_exact_overlaps)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "VolumetricScaffolderParams")
                    json_data = param_json["VolumetricScaffolderParams"] if "VolumetricScaffolderParams" in param_json else {}
                    self.__initialize(
                        absolute_dist_tol if absolute_dist_tol is not None else ( VolumetricScaffolderParams._default_params["absolute_dist_tol"] if "absolute_dist_tol" in VolumetricScaffolderParams._default_params else (json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None)),
                        only_check_exact_overlaps if only_check_exact_overlaps is not None else ( VolumetricScaffolderParams._default_params["only_check_exact_overlaps"] if "only_check_exact_overlaps" in VolumetricScaffolderParams._default_params else (json_data["onlyCheckExactOverlaps"] if "onlyCheckExactOverlaps" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            absolute_dist_tol: float = None,
            only_check_exact_overlaps: bool = None):
        """Set the default values of the ``VolumetricScaffolderParams`` object.

        Parameters
        ----------
        absolute_dist_tol: float, optional
            Specify distance tolerance between overlapping faces.
        only_check_exact_overlaps: bool, optional
            Check only for fully overlapping topofaces when true.
        """
        args = locals()
        [VolumetricScaffolderParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``VolumetricScaffolderParams`` object.

        Examples
        --------
        >>> VolumetricScaffolderParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in VolumetricScaffolderParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._absolute_dist_tol is not None:
            json_data["absoluteDistTol"] = self._absolute_dist_tol
        if self._only_check_exact_overlaps is not None:
            json_data["onlyCheckExactOverlaps"] = self._only_check_exact_overlaps
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "absolute_dist_tol :  %s\nonly_check_exact_overlaps :  %s" % (self._absolute_dist_tol, self._only_check_exact_overlaps)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def absolute_dist_tol(self) -> float:
        """Specify distance tolerance between overlapping faces.
        """
        return self._absolute_dist_tol

    @absolute_dist_tol.setter
    def absolute_dist_tol(self, value: float):
        self._absolute_dist_tol = value

    @property
    def only_check_exact_overlaps(self) -> bool:
        """Check only for fully overlapping topofaces when true.
        """
        return self._only_check_exact_overlaps

    @only_check_exact_overlaps.setter
    def only_check_exact_overlaps(self, value: bool):
        self._only_check_exact_overlaps = value

class ScaffolderResults(CoreObject):
    """Results structure associated to scaffold operation.

    Parameters
    ----------
    model: Model
        Model to create a ``ScaffolderResults`` object with default parameters.
    n_incomplete_topo_faces: int, optional
        Number of topofaces failed in scaffold operation.
    error_code: ErrorCode, optional
        Error code associated with scaffold operation.
    json_data: dict, optional
        JSON dictionary to create a ``ScaffolderResults`` object with provided parameters.

    Examples
    --------
    >>> scaffolder_results = prime.ScaffolderResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            n_incomplete_topo_faces: int,
            error_code: ErrorCode):
        self._n_incomplete_topo_faces = n_incomplete_topo_faces
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_incomplete_topo_faces: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ScaffolderResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ScaffolderResults`` object with default parameters.
        n_incomplete_topo_faces: int, optional
            Number of topofaces failed in scaffold operation.
        error_code: ErrorCode, optional
            Error code associated with scaffold operation.
        json_data: dict, optional
            JSON dictionary to create a ``ScaffolderResults`` object with provided parameters.

        Examples
        --------
        >>> scaffolder_results = prime.ScaffolderResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nIncompleteTopoFaces"] if "nIncompleteTopoFaces" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [n_incomplete_topo_faces, error_code])
            if all_field_specified:
                self.__initialize(
                    n_incomplete_topo_faces,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScaffolderResults")
                    json_data = param_json["ScaffolderResults"] if "ScaffolderResults" in param_json else {}
                    self.__initialize(
                        n_incomplete_topo_faces if n_incomplete_topo_faces is not None else ( ScaffolderResults._default_params["n_incomplete_topo_faces"] if "n_incomplete_topo_faces" in ScaffolderResults._default_params else (json_data["nIncompleteTopoFaces"] if "nIncompleteTopoFaces" in json_data else None)),
                        error_code if error_code is not None else ( ScaffolderResults._default_params["error_code"] if "error_code" in ScaffolderResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_incomplete_topo_faces: int = None,
            error_code: ErrorCode = None):
        """Set the default values of the ``ScaffolderResults`` object.

        Parameters
        ----------
        n_incomplete_topo_faces: int, optional
            Number of topofaces failed in scaffold operation.
        error_code: ErrorCode, optional
            Error code associated with scaffold operation.
        """
        args = locals()
        [ScaffolderResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScaffolderResults`` object.

        Examples
        --------
        >>> ScaffolderResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScaffolderResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_incomplete_topo_faces is not None:
            json_data["nIncompleteTopoFaces"] = self._n_incomplete_topo_faces
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_incomplete_topo_faces :  %s\nerror_code :  %s" % (self._n_incomplete_topo_faces, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_incomplete_topo_faces(self) -> int:
        """Number of topofaces failed in scaffold operation.
        """
        return self._n_incomplete_topo_faces

    @n_incomplete_topo_faces.setter
    def n_incomplete_topo_faces(self, value: int):
        self._n_incomplete_topo_faces = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with scaffold operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ScaffolderSplitResults(CoreObject):
    """Result structure associated to split topofaces operation.

    Parameters
    ----------
    model: Model
        Model to create a ``ScaffolderSplitResults`` object with default parameters.
    new_faces: Iterable[int], optional
        Topofaces created after split operation.
    error_code: ErrorCode, optional
        Error code associated with split topofaces operation.
    json_data: dict, optional
        JSON dictionary to create a ``ScaffolderSplitResults`` object with provided parameters.

    Examples
    --------
    >>> scaffolder_split_results = prime.ScaffolderSplitResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            new_faces: Iterable[int],
            error_code: ErrorCode):
        self._new_faces = new_faces if isinstance(new_faces, np.ndarray) else np.array(new_faces, dtype=np.int32) if new_faces is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            new_faces: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ScaffolderSplitResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ScaffolderSplitResults`` object with default parameters.
        new_faces: Iterable[int], optional
            Topofaces created after split operation.
        error_code: ErrorCode, optional
            Error code associated with split topofaces operation.
        json_data: dict, optional
            JSON dictionary to create a ``ScaffolderSplitResults`` object with provided parameters.

        Examples
        --------
        >>> scaffolder_split_results = prime.ScaffolderSplitResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["newFaces"] if "newFaces" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [new_faces, error_code])
            if all_field_specified:
                self.__initialize(
                    new_faces,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScaffolderSplitResults")
                    json_data = param_json["ScaffolderSplitResults"] if "ScaffolderSplitResults" in param_json else {}
                    self.__initialize(
                        new_faces if new_faces is not None else ( ScaffolderSplitResults._default_params["new_faces"] if "new_faces" in ScaffolderSplitResults._default_params else (json_data["newFaces"] if "newFaces" in json_data else None)),
                        error_code if error_code is not None else ( ScaffolderSplitResults._default_params["error_code"] if "error_code" in ScaffolderSplitResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            new_faces: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of the ``ScaffolderSplitResults`` object.

        Parameters
        ----------
        new_faces: Iterable[int], optional
            Topofaces created after split operation.
        error_code: ErrorCode, optional
            Error code associated with split topofaces operation.
        """
        args = locals()
        [ScaffolderSplitResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScaffolderSplitResults`` object.

        Examples
        --------
        >>> ScaffolderSplitResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScaffolderSplitResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._new_faces is not None:
            json_data["newFaces"] = self._new_faces
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "new_faces :  %s\nerror_code :  %s" % (self._new_faces, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def new_faces(self) -> Iterable[int]:
        """Topofaces created after split operation.
        """
        return self._new_faces

    @new_faces.setter
    def new_faces(self, value: Iterable[int]):
        self._new_faces = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with split topofaces operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value

class ScaffolderMergeResults(CoreObject):
    """Result structure associated with merge overlapping topofaces and delete shadowed topofaces operations.

    Parameters
    ----------
    model: Model
        Model to create a ``ScaffolderMergeResults`` object with default parameters.
    n_merged: int, optional
        Number of merged topofaces.
    error_code: ErrorCode, optional
        Error code associated with merge overlapping topofaces operation.
    json_data: dict, optional
        JSON dictionary to create a ``ScaffolderMergeResults`` object with provided parameters.

    Examples
    --------
    >>> scaffolder_merge_results = prime.ScaffolderMergeResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            n_merged: int,
            error_code: ErrorCode):
        self._n_merged = n_merged
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            n_merged: int = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``ScaffolderMergeResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``ScaffolderMergeResults`` object with default parameters.
        n_merged: int, optional
            Number of merged topofaces.
        error_code: ErrorCode, optional
            Error code associated with merge overlapping topofaces operation.
        json_data: dict, optional
            JSON dictionary to create a ``ScaffolderMergeResults`` object with provided parameters.

        Examples
        --------
        >>> scaffolder_merge_results = prime.ScaffolderMergeResults(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["nMerged"] if "nMerged" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [n_merged, error_code])
            if all_field_specified:
                self.__initialize(
                    n_merged,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "ScaffolderMergeResults")
                    json_data = param_json["ScaffolderMergeResults"] if "ScaffolderMergeResults" in param_json else {}
                    self.__initialize(
                        n_merged if n_merged is not None else ( ScaffolderMergeResults._default_params["n_merged"] if "n_merged" in ScaffolderMergeResults._default_params else (json_data["nMerged"] if "nMerged" in json_data else None)),
                        error_code if error_code is not None else ( ScaffolderMergeResults._default_params["error_code"] if "error_code" in ScaffolderMergeResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            n_merged: int = None,
            error_code: ErrorCode = None):
        """Set the default values of the ``ScaffolderMergeResults`` object.

        Parameters
        ----------
        n_merged: int, optional
            Number of merged topofaces.
        error_code: ErrorCode, optional
            Error code associated with merge overlapping topofaces operation.
        """
        args = locals()
        [ScaffolderMergeResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``ScaffolderMergeResults`` object.

        Examples
        --------
        >>> ScaffolderMergeResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in ScaffolderMergeResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._n_merged is not None:
            json_data["nMerged"] = self._n_merged
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "n_merged :  %s\nerror_code :  %s" % (self._n_merged, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def n_merged(self) -> int:
        """Number of merged topofaces.
        """
        return self._n_merged

    @n_merged.setter
    def n_merged(self, value: int):
        self._n_merged = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with merge overlapping topofaces operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
