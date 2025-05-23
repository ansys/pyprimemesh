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

class DeleteMeshResults(CoreObject):
    """Results structure associated with delete mesh on topofaces.

    Parameters
    ----------
    model: Model
        Model to create a ``DeleteMeshResults`` object with default parameters.
    error_code: ErrorCode, optional
        Error code associated with the failure of operation.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DeleteMeshResults`` object with provided parameters.

    Examples
    --------
    >>> delete_mesh_results = prime.DeleteMeshResults(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            error_code: ErrorCode):
        self._error_code = ErrorCode(error_code)

    def __init__(
            self,
            model: CommunicationManager=None,
            error_code: ErrorCode = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DeleteMeshResults`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DeleteMeshResults`` object with default parameters.
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DeleteMeshResults`` object with provided parameters.

        Examples
        --------
        >>> delete_mesh_results = prime.DeleteMeshResults(model = model)
        """
        if json_data:
            self.__initialize(
                ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None))
        else:
            all_field_specified = all(arg is not None for arg in [error_code])
            if all_field_specified:
                self.__initialize(
                    error_code)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteMeshResults")
                    json_data = param_json["DeleteMeshResults"] if "DeleteMeshResults" in param_json else {}
                    self.__initialize(
                        error_code if error_code is not None else ( DeleteMeshResults._default_params["error_code"] if "error_code" in DeleteMeshResults._default_params else ErrorCode(json_data["errorCode"] if "errorCode" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            error_code: ErrorCode = None):
        """Set the default values of the ``DeleteMeshResults`` object.

        Parameters
        ----------
        error_code: ErrorCode, optional
            Error code associated with the failure of operation.
        """
        args = locals()
        [DeleteMeshResults._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DeleteMeshResults`` object.

        Examples
        --------
        >>> DeleteMeshResults.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteMeshResults._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._error_code is not None:
            json_data["errorCode"] = self._error_code
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "error_code :  %s" % (self._error_code)
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

class DeleteMeshParams(CoreObject):
    """Parameters to delete mesh on topoentities.

    Parameters
    ----------
    model: Model
        Model to create a ``DeleteMeshParams`` object with default parameters.
    delete_mesh_on_connected_topo_edges: bool, optional
        Option to delete mesh on topoedges connected only to provided topoentities.

        **This is a beta parameter**. **The behavior and name may change in the future**.
    json_data: dict, optional
        JSON dictionary to create a ``DeleteMeshParams`` object with provided parameters.

    Examples
    --------
    >>> delete_mesh_params = prime.DeleteMeshParams(model = model)
    """
    _default_params = {}

    def __initialize(
            self,
            delete_mesh_on_connected_topo_edges: bool):
        self._delete_mesh_on_connected_topo_edges = delete_mesh_on_connected_topo_edges

    def __init__(
            self,
            model: CommunicationManager=None,
            delete_mesh_on_connected_topo_edges: bool = None,
            json_data : dict = None,
             **kwargs):
        """Initialize a ``DeleteMeshParams`` object.

        Parameters
        ----------
        model: Model
            Model to create a ``DeleteMeshParams`` object with default parameters.
        delete_mesh_on_connected_topo_edges: bool, optional
            Option to delete mesh on topoedges connected only to provided topoentities.

            **This is a beta parameter**. **The behavior and name may change in the future**.
        json_data: dict, optional
            JSON dictionary to create a ``DeleteMeshParams`` object with provided parameters.

        Examples
        --------
        >>> delete_mesh_params = prime.DeleteMeshParams(model = model)
        """
        if json_data:
            self.__initialize(
                json_data["deleteMeshOnConnectedTopoEdges"] if "deleteMeshOnConnectedTopoEdges" in json_data else None)
        else:
            all_field_specified = all(arg is not None for arg in [delete_mesh_on_connected_topo_edges])
            if all_field_specified:
                self.__initialize(
                    delete_mesh_on_connected_topo_edges)
            else:
                if model is None:
                    raise ValueError("Invalid assignment. Either pass a model or specify all properties.")
                else:
                    param_json = model._communicator.initialize_params(model, "DeleteMeshParams")
                    json_data = param_json["DeleteMeshParams"] if "DeleteMeshParams" in param_json else {}
                    self.__initialize(
                        delete_mesh_on_connected_topo_edges if delete_mesh_on_connected_topo_edges is not None else ( DeleteMeshParams._default_params["delete_mesh_on_connected_topo_edges"] if "delete_mesh_on_connected_topo_edges" in DeleteMeshParams._default_params else (json_data["deleteMeshOnConnectedTopoEdges"] if "deleteMeshOnConnectedTopoEdges" in json_data else None)))
        self._custom_params = kwargs
        if model is not None:
            [ model._logger.warning(f'Unsupported argument : {key}') for key in kwargs ]
        [setattr(type(self), key, property(lambda self, key = key:  self._custom_params[key] if key in self._custom_params else None,
        lambda self, value, key = key : self._custom_params.update({ key: value }))) for key in kwargs]
        self._freeze()

    @staticmethod
    def set_default(
            delete_mesh_on_connected_topo_edges: bool = None):
        """Set the default values of the ``DeleteMeshParams`` object.

        Parameters
        ----------
        delete_mesh_on_connected_topo_edges: bool, optional
            Option to delete mesh on topoedges connected only to provided topoentities.
        """
        args = locals()
        [DeleteMeshParams._default_params.update({ key: value }) for key, value in args.items() if value is not None]

    @staticmethod
    def print_default():
        """Print the default values of ``DeleteMeshParams`` object.

        Examples
        --------
        >>> DeleteMeshParams.print_default()
        """
        message = ""
        message += ''.join(str(key) + ' : ' + str(value) + '\n' for key, value in DeleteMeshParams._default_params.items())
        print(message)

    def _jsonify(self) -> Dict[str, Any]:
        json_data = {}
        if self._delete_mesh_on_connected_topo_edges is not None:
            json_data["deleteMeshOnConnectedTopoEdges"] = self._delete_mesh_on_connected_topo_edges
        [ json_data.update({ utils.to_camel_case(key) : value }) for key, value in self._custom_params.items()]
        return json_data

    def __str__(self) -> str:
        message = "delete_mesh_on_connected_topo_edges :  %s" % (self._delete_mesh_on_connected_topo_edges)
        message += ''.join('\n' + str(key) + ' : ' + str(value) for key, value in self._custom_params.items())
        return message

    @property
    def delete_mesh_on_connected_topo_edges(self) -> bool:
        """Option to delete mesh on topoedges connected only to provided topoentities.

        **This is a beta parameter**. **The behavior and name may change in the future**.
        """
        return self._delete_mesh_on_connected_topo_edges

    @delete_mesh_on_connected_topo_edges.setter
    def delete_mesh_on_connected_topo_edges(self, value: bool):
        self._delete_mesh_on_connected_topo_edges = value
