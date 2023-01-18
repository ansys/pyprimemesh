""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class TopoFillHoleParams(CoreObject):
    """Parameters used to fill holes in topology.
    """
    _default_params = {}

    def __initialize(
            self,
            edges_to_exclude: Iterable[int],
            suppress_boundary_after_hole_fill: bool,
            fill_annular_hole: bool):
        self._edges_to_exclude = edges_to_exclude if isinstance(edges_to_exclude, np.ndarray) else np.array(edges_to_exclude, dtype=np.int32) if edges_to_exclude is not None else None
        self._suppress_boundary_after_hole_fill = suppress_boundary_after_hole_fill
        self._fill_annular_hole = fill_annular_hole

    def __init__(
            self,
            model: CommunicationManager=None,
            edges_to_exclude: Iterable[int] = None,
            suppress_boundary_after_hole_fill: bool = None,
            fill_annular_hole: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the TopoFillHoleParams.

        Parameters
        ----------
        model: Model
            Model to create a TopoFillHoleParams object with default parameters.
        edges_to_exclude: Iterable[int], optional
            TopoEdges to be excluded for cap creation.
        suppress_boundary_after_hole_fill: bool, optional
            Option to preserve or suppress hole-boundary after filling holes.
        fill_annular_hole: bool, optional
            Option for filling holes with annular bounding loops.
        json_data: dict, optional
            JSON dictionary to create a TopoFillHoleParams object with provided parameters.

        Examples
        --------
        >>> topo_fill_hole_params = prime.TopoFillHoleParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["edgesToExclude"] if "edgesToExclude" in json_data else None,
                json_data["suppressBoundaryAfterHoleFill"] if "suppressBoundaryAfterHoleFill" in json_data else None,
                json_data["fillAnnularHole"] if "fillAnnularHole" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [edges_to_exclude, suppress_boundary_after_hole_fill, fill_annular_hole])
            if all_field_specified:
                self.__initialize(
                    edges_to_exclude,
                    suppress_boundary_after_hole_fill,
                    fill_annular_hole)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "TopoFillHoleParams")
                    json_data = param_json["TopoFillHoleParams"] if "TopoFillHoleParams" in param_json else {}
                    self.__initialize(
                        edges_to_exclude if edges_to_exclude is not None else ( TopoFillHoleParams._default_params["edges_to_exclude"] if "edges_to_exclude" in TopoFillHoleParams._default_params else (json_data["edgesToExclude"] if "edgesToExclude" in json_data else None)),
                        suppress_boundary_after_hole_fill if suppress_boundary_after_hole_fill is not None else ( TopoFillHoleParams._default_params["suppress_boundary_after_hole_fill"] if "suppress_boundary_after_hole_fill" in TopoFillHoleParams._default_params else (json_data["suppressBoundaryAfterHoleFill"] if "suppressBoundaryAfterHoleFill" in json_data else None)),
                        fill_annular_hole if fill_annular_hole is not None else ( TopoFillHoleParams._default_params["fill_annular_hole"] if "fill_annular_hole" in TopoFillHoleParams._default_params else (json_data["fillAnnularHole"] if "fillAnnularHole" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            edges_to_exclude: Iterable[int] = None,
            suppress_boundary_after_hole_fill: bool = None,
            fill_annular_hole: bool = None):
        """Set the default values of TopoFillHoleParams.

        Parameters
        ----------
        edges_to_exclude: Iterable[int], optional
            TopoEdges to be excluded for cap creation.
        suppress_boundary_after_hole_fill: bool, optional
            Option to preserve or suppress hole-boundary after filling holes.
        fill_annular_hole: bool, optional
            Option for filling holes with annular bounding loops.
        """
        args = locals()
        [TopoFillHoleParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of TopoFillHoleParams.

        Examples
        --------
        >>> TopoFillHoleParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TopoFillHoleParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._edges_to_exclude is not None:
            json_data["edgesToExclude"] = self._edges_to_exclude
        if self._suppress_boundary_after_hole_fill is not None:
            json_data["suppressBoundaryAfterHoleFill"] = self._suppress_boundary_after_hole_fill
        if self._fill_annular_hole is not None:
            json_data["fillAnnularHole"] = self._fill_annular_hole
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "edges_to_exclude :  %s\nsuppress_boundary_after_hole_fill :  %s\nfill_annular_hole :  %s" % (self._edges_to_exclude, self._suppress_boundary_after_hole_fill, self._fill_annular_hole)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def edges_to_exclude(self) -> Iterable[int]:
        """TopoEdges to be excluded for cap creation.
        """
        return self._edges_to_exclude

    @edges_to_exclude.setter
    def edges_to_exclude(self, value: Iterable[int]):
        self._edges_to_exclude = value

    @property
    def suppress_boundary_after_hole_fill(self) -> bool:
        """Option to preserve or suppress hole-boundary after filling holes.
        """
        return self._suppress_boundary_after_hole_fill

    @suppress_boundary_after_hole_fill.setter
    def suppress_boundary_after_hole_fill(self, value: bool):
        self._suppress_boundary_after_hole_fill = value

    @property
    def fill_annular_hole(self) -> bool:
        """Option for filling holes with annular bounding loops.
        """
        return self._fill_annular_hole

    @fill_annular_hole.setter
    def fill_annular_hole(self, value: bool):
        self._fill_annular_hole = value

class TopoFillHoleResult(CoreObject):
    """Results associated with fill holes in topology operations.
    """
    _default_params = {}

    def __initialize(
            self,
            new_topo_faces_created: Iterable[int],
            error_code: ErrorCode):
        self._new_topo_faces_created = new_topo_faces_created if isinstance(new_topo_faces_created, np.ndarray) else np.array(new_topo_faces_created, dtype=np.int32) if new_topo_faces_created is not None else None
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            new_topo_faces_created: Iterable[int] = None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the TopoFillHoleResult.

        Parameters
        ----------
        model: Model
            Model to create a TopoFillHoleResult object with default parameters.
        new_topo_faces_created: Iterable[int], optional
            Ids of new topofaces created.
        error_code: ErrorCode, optional
            Error code associated with a wrap operation.
        json_data: dict, optional
            JSON dictionary to create a TopoFillHoleResult object with provided parameters.

        Examples
        --------
        >>> topo_fill_hole_result = prime.TopoFillHoleResult(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["newTopoFacesCreated"] if "newTopoFacesCreated" in json_data else None,
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [new_topo_faces_created, error_code])
            if all_field_specified:
                self.__initialize(
                    new_topo_faces_created,
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "TopoFillHoleResult")
                    json_data = param_json["TopoFillHoleResult"] if "TopoFillHoleResult" in param_json else {}
                    self.__initialize(
                        new_topo_faces_created if new_topo_faces_created is not None else ( TopoFillHoleResult._default_params["new_topo_faces_created"] if "new_topo_faces_created" in TopoFillHoleResult._default_params else (json_data["newTopoFacesCreated"] if "newTopoFacesCreated" in json_data else None)),
                        error_code if error_code is not None else ( TopoFillHoleResult._default_params["error_code"] if "error_code" in TopoFillHoleResult._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            new_topo_faces_created: Iterable[int] = None,
            error_code: ErrorCode = None):
        """Set the default values of TopoFillHoleResult.

        Parameters
        ----------
        new_topo_faces_created: Iterable[int], optional
            Ids of new topofaces created.
        error_code: ErrorCode, optional
            Error code associated with a wrap operation.
        """
        args = locals()
        [TopoFillHoleResult._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of TopoFillHoleResult.

        Examples
        --------
        >>> TopoFillHoleResult.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in TopoFillHoleResult._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._new_topo_faces_created is not None:
            json_data["newTopoFacesCreated"] = self._new_topo_faces_created
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "new_topo_faces_created :  %s\nerror_code :  %s" % (self._new_topo_faces_created, self._error_code)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def new_topo_faces_created(self) -> Iterable[int]:
        """Ids of new topofaces created.
        """
        return self._new_topo_faces_created

    @new_topo_faces_created.setter
    def new_topo_faces_created(self, value: Iterable[int]):
        self._new_topo_faces_created = value

    @property
    def error_code(self) -> ErrorCode:
        """Error code associated with a wrap operation.
        """
        return self._error_code

    @error_code.setter
    def error_code(self, value: ErrorCode):
        self._error_code = value
