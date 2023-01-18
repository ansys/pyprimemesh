""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class IntersectionMask(enum.IntEnum):
    """Scaffold parameters use intersection mask to define nature of intersection computation.
    """
    EDGEEDGE = 1
    """Performs edge to edge intersection."""
    FACEFACE = 2
    """Performs face to face intersection."""
    FACEFACEANDEDGEEDGE = 3
    """Perform face to face and edge to edge intersections."""

class ScaffolderParams(CoreObject):
    """Parameters to control scaffold operation.
    """
    _default_params = {}

    def __initialize(
            self,
            absolute_dist_tol: float,
            intersection_control_mask: IntersectionMask,
            constant_mesh_size: float):
        self._absolute_dist_tol = absolute_dist_tol
        self._intersection_control_mask = IntersectionMask(intersection_control_mask)
        self._constant_mesh_size = constant_mesh_size

    def __init__(
            self,
            model: CommunicationManager=None,
            absolute_dist_tol: float = None,
            intersection_control_mask: IntersectionMask = None,
            constant_mesh_size: float = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the ScaffolderParams.

        Parameters
        ----------
        model: Model
            Model to create a ScaffolderParams object with default parameters.
        absolute_dist_tol: float, optional
            Defines the maximum gap to connect.
        intersection_control_mask: IntersectionMask, optional
            Specifies the nature of intersection to be computed.
        constant_mesh_size: float, optional
            Defines the constant edge mesh size to check connection.
        json_data: dict, optional
            JSON dictionary to create a ScaffolderParams object with provided parameters.

        Examples
        --------
        >>> scaffolder_params = prime.ScaffolderParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None,
                IntersectionMask(json_data["intersectionControlMask"] if "intersectionControlMask" in json_data else None),
                json_data["constantMeshSize"] if "constantMeshSize" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [absolute_dist_tol, intersection_control_mask, constant_mesh_size])
            if all_field_specified:
                self.__initialize(
                    absolute_dist_tol,
                    intersection_control_mask,
                    constant_mesh_size)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "ScaffolderParams")
                    json_data = param_json["ScaffolderParams"] if "ScaffolderParams" in param_json else {}
                    self.__initialize(
                        absolute_dist_tol if absolute_dist_tol is not None else ( ScaffolderParams._default_params["absolute_dist_tol"] if "absolute_dist_tol" in ScaffolderParams._default_params else (json_data["absoluteDistTol"] if "absoluteDistTol" in json_data else None)),
                        intersection_control_mask if intersection_control_mask is not None else ( ScaffolderParams._default_params["intersection_control_mask"] if "intersection_control_mask" in ScaffolderParams._default_params else IntersectionMask(json_data["intersectionControlMask"] if "intersectionControlMask" in json_data else None)),
                        constant_mesh_size if constant_mesh_size is not None else ( ScaffolderParams._default_params["constant_mesh_size"] if "constant_mesh_size" in ScaffolderParams._default_params else (json_data["constantMeshSize"] if "constantMeshSize" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            absolute_dist_tol: float = None,
            intersection_control_mask: IntersectionMask = None,
            constant_mesh_size: float = None):
        """Set the default values of ScaffolderParams.

        Parameters
        ----------
        absolute_dist_tol: float, optional
            Defines the maximum gap to connect.
        intersection_control_mask: IntersectionMask, optional
            Specifies the nature of intersection to be computed.
        constant_mesh_size: float, optional
            Defines the constant edge mesh size to check connection.
        """
        args = locals()
        [ScaffolderParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ScaffolderParams.

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
        if self._intersection_control_mask is not None:
            json_data["intersectionControlMask"] = self._intersection_control_mask
        if self._constant_mesh_size is not None:
            json_data["constantMeshSize"] = self._constant_mesh_size
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "absolute_dist_tol :  %s\nintersection_control_mask :  %s\nconstant_mesh_size :  %s" % (self._absolute_dist_tol, self._intersection_control_mask, self._constant_mesh_size)
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
    def intersection_control_mask(self) -> IntersectionMask:
        """Specifies the nature of intersection to be computed.
        """
        return self._intersection_control_mask

    @intersection_control_mask.setter
    def intersection_control_mask(self, value: IntersectionMask):
        self._intersection_control_mask = value

    @property
    def constant_mesh_size(self) -> float:
        """Defines the constant edge mesh size to check connection.
        """
        return self._constant_mesh_size

    @constant_mesh_size.setter
    def constant_mesh_size(self, value: float):
        self._constant_mesh_size = value

class VolumetricScaffolderParams(CoreObject):
    """Parameters to control delete shadowed topofaces operation.
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
        """Initializes the VolumetricScaffolderParams.

        Parameters
        ----------
        model: Model
            Model to create a VolumetricScaffolderParams object with default parameters.
        absolute_dist_tol: float, optional
            Specify distance tolerance between overlapping faces.
        only_check_exact_overlaps: bool, optional
            Check only for fully overlapping topofaces when true.
        json_data: dict, optional
            JSON dictionary to create a VolumetricScaffolderParams object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
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
        """Set the default values of VolumetricScaffolderParams.

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
        """Print the default values of VolumetricScaffolderParams.

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
        """Initializes the ScaffolderResults.

        Parameters
        ----------
        model: Model
            Model to create a ScaffolderResults object with default parameters.
        n_incomplete_topo_faces: int, optional
            Number of topofaces failed in scaffold operation.
        error_code: ErrorCode, optional
            Error code associated with scaffold operation.
        json_data: dict, optional
            JSON dictionary to create a ScaffolderResults object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
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
        """Set the default values of ScaffolderResults.

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
        """Print the default values of ScaffolderResults.

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
        """Initializes the ScaffolderSplitResults.

        Parameters
        ----------
        model: Model
            Model to create a ScaffolderSplitResults object with default parameters.
        new_faces: Iterable[int], optional
            Topofaces created after split operation.
        error_code: ErrorCode, optional
            Error code associated with split topofaces operation.
        json_data: dict, optional
            JSON dictionary to create a ScaffolderSplitResults object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
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
        """Set the default values of ScaffolderSplitResults.

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
        """Print the default values of ScaffolderSplitResults.

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
        """Initializes the ScaffolderMergeResults.

        Parameters
        ----------
        model: Model
            Model to create a ScaffolderMergeResults object with default parameters.
        n_merged: int, optional
            Number of merged topofaces.
        error_code: ErrorCode, optional
            Error code associated with merge overlapping topofaces operation.
        json_data: dict, optional
            JSON dictionary to create a ScaffolderMergeResults object with provided parameters.

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
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
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
        """Set the default values of ScaffolderMergeResults.

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
        """Print the default values of ScaffolderMergeResults.

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
