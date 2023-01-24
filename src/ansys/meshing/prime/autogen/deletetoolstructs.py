""" Auto-generated file. DO NOT MODIFY """
import enum
from typing import Dict, Any, Union, List, Iterable
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.internals import utils
from ansys.meshing.prime.autogen.coreobject import *
import numpy as np

from ansys.meshing.prime.params.primestructs import *

class DeleteFringesAndOverlapsParams(CoreObject):
    """Parameters to delete fringes and overlapping faces.
    """
    _default_params = {}

    def __initialize(
            self,
            fringe_element_count: int,
            overlap_element_count: int,
            delete_fringes: bool,
            delete_overlaps: bool):
        self._fringe_element_count = fringe_element_count
        self._overlap_element_count = overlap_element_count
        self._delete_fringes = delete_fringes
        self._delete_overlaps = delete_overlaps

    def __init__(
            self,
            model: CommunicationManager=None,
            fringe_element_count: int = None,
            overlap_element_count: int = None,
            delete_fringes: bool = None,
            delete_overlaps: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteFringesAndOverlapsParams.

        Parameters
        ----------
        model: Model
            Model to create a DeleteFringesAndOverlapsParams object with default parameters.
        fringe_element_count: int, optional
            Maximum count of free face elements identified as fringe to be deleted.
        overlap_element_count: int, optional
            Maximum count of overlapping face elements identified as overlap to be deleted.
        delete_fringes: bool, optional
            Option to delete fringes. The default is true.
        delete_overlaps: bool, optional
            Option to delete overlaps. The default is false.
        json_data: dict, optional
            JSON dictionary to create a DeleteFringesAndOverlapsParams object with provided parameters.

        Examples
        --------
        >>> delete_fringes_and_overlaps_params = prime.DeleteFringesAndOverlapsParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["fringeElementCount"] if "fringeElementCount" in json_data else None,
                json_data["overlapElementCount"] if "overlapElementCount" in json_data else None,
                json_data["deleteFringes"] if "deleteFringes" in json_data else None,
                json_data["deleteOverlaps"] if "deleteOverlaps" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [fringe_element_count, overlap_element_count, delete_fringes, delete_overlaps])
            if all_field_specified:
                self.__initialize(
                    fringe_element_count,
                    overlap_element_count,
                    delete_fringes,
                    delete_overlaps)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteFringesAndOverlapsParams")
                    json_data = param_json["DeleteFringesAndOverlapsParams"] if "DeleteFringesAndOverlapsParams" in param_json else {}
                    self.__initialize(
                        fringe_element_count if fringe_element_count is not None else ( DeleteFringesAndOverlapsParams._default_params["fringe_element_count"] if "fringe_element_count" in DeleteFringesAndOverlapsParams._default_params else (json_data["fringeElementCount"] if "fringeElementCount" in json_data else None)),
                        overlap_element_count if overlap_element_count is not None else ( DeleteFringesAndOverlapsParams._default_params["overlap_element_count"] if "overlap_element_count" in DeleteFringesAndOverlapsParams._default_params else (json_data["overlapElementCount"] if "overlapElementCount" in json_data else None)),
                        delete_fringes if delete_fringes is not None else ( DeleteFringesAndOverlapsParams._default_params["delete_fringes"] if "delete_fringes" in DeleteFringesAndOverlapsParams._default_params else (json_data["deleteFringes"] if "deleteFringes" in json_data else None)),
                        delete_overlaps if delete_overlaps is not None else ( DeleteFringesAndOverlapsParams._default_params["delete_overlaps"] if "delete_overlaps" in DeleteFringesAndOverlapsParams._default_params else (json_data["deleteOverlaps"] if "deleteOverlaps" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            fringe_element_count: int = None,
            overlap_element_count: int = None,
            delete_fringes: bool = None,
            delete_overlaps: bool = None):
        """Set the default values of DeleteFringesAndOverlapsParams.

        Parameters
        ----------
        fringe_element_count: int, optional
            Maximum count of free face elements identified as fringe to be deleted.
        overlap_element_count: int, optional
            Maximum count of overlapping face elements identified as overlap to be deleted.
        delete_fringes: bool, optional
            Option to delete fringes. The default is true.
        delete_overlaps: bool, optional
            Option to delete overlaps. The default is false.
        """
        args = locals()
        [DeleteFringesAndOverlapsParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteFringesAndOverlapsParams.

        Examples
        --------
        >>> DeleteFringesAndOverlapsParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteFringesAndOverlapsParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._fringe_element_count is not None:
            json_data["fringeElementCount"] = self._fringe_element_count
        if self._overlap_element_count is not None:
            json_data["overlapElementCount"] = self._overlap_element_count
        if self._delete_fringes is not None:
            json_data["deleteFringes"] = self._delete_fringes
        if self._delete_overlaps is not None:
            json_data["deleteOverlaps"] = self._delete_overlaps
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "fringe_element_count :  %s\noverlap_element_count :  %s\ndelete_fringes :  %s\ndelete_overlaps :  %s" % (self._fringe_element_count, self._overlap_element_count, self._delete_fringes, self._delete_overlaps)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def fringe_element_count(self) -> int:
        """Maximum count of free face elements identified as fringe to be deleted.
        """
        return self._fringe_element_count

    @fringe_element_count.setter
    def fringe_element_count(self, value: int):
        self._fringe_element_count = value

    @property
    def overlap_element_count(self) -> int:
        """Maximum count of overlapping face elements identified as overlap to be deleted.
        """
        return self._overlap_element_count

    @overlap_element_count.setter
    def overlap_element_count(self, value: int):
        self._overlap_element_count = value

    @property
    def delete_fringes(self) -> bool:
        """Option to delete fringes. The default is true.
        """
        return self._delete_fringes

    @delete_fringes.setter
    def delete_fringes(self, value: bool):
        self._delete_fringes = value

    @property
    def delete_overlaps(self) -> bool:
        """Option to delete overlaps. The default is false.
        """
        return self._delete_overlaps

    @delete_overlaps.setter
    def delete_overlaps(self, value: bool):
        self._delete_overlaps = value

class DeleteFringesAndOverlapsResults(CoreObject):
    """Results associated with the delete fringes and overlapping faces operation.
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode,
            n_deleted: int):
        self._error_code = ErrorCode(error_code)
        self._n_deleted = n_deleted

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            n_deleted: int = None,
            json_data : dict = None,
             **kwargs):
        """Initializes the DeleteFringesAndOverlapsResults.

        Parameters
        ----------
        model: Model
            Model to create a DeleteFringesAndOverlapsResults object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        n_deleted: int, optional
            Number of face elements deleted.
        json_data: dict, optional
            JSON dictionary to create a DeleteFringesAndOverlapsResults object with provided parameters.

        Examples
        --------
        >>> delete_fringes_and_overlaps_results = prime.DeleteFringesAndOverlapsResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None),
                json_data["nDeleted"] if "nDeleted" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [error_code, n_deleted])
            if all_field_specified:
                self.__initialize(
                    error_code,
                    n_deleted)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass model or specify all properties")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteFringesAndOverlapsResults")
                    json_data = param_json["DeleteFringesAndOverlapsResults"] if "DeleteFringesAndOverlapsResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteFringesAndOverlapsResults._default_params["error_code"] if "error_code" in DeleteFringesAndOverlapsResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)),
                        n_deleted if n_deleted is not None else ( DeleteFringesAndOverlapsResults._default_params["n_deleted"] if "n_deleted" in DeleteFringesAndOverlapsResults._default_params else (json_data["nDeleted"] if "nDeleted" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None,
            n_deleted: int = None):
        """Set the default values of DeleteFringesAndOverlapsResults.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        n_deleted: int, optional
            Number of face elements deleted.
        """
        args = locals()
        [DeleteFringesAndOverlapsResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of DeleteFringesAndOverlapsResults.

        Examples
        --------
        >>> DeleteFringesAndOverlapsResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteFringesAndOverlapsResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        if self._n_deleted is not None:
            json_data["nDeleted"] = self._n_deleted
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s\nn_deleted :  %s" % (self._error_code, self._n_deleted)
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
    def n_deleted(self) -> int:
        """Number of face elements deleted.
        """
        return self._n_deleted

    @n_deleted.setter
    def n_deleted(self, value: int):
        self._n_deleted = value
