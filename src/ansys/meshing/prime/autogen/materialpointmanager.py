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
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class MaterialPointManager(CoreObject):
    """Provide functions for material point creation, deletion and queries.

    Parameters
    ----------
    model : Model
        Server model to create MaterialPointManager object.
    id : int
        Id of the MaterialPointManager.
    object_id : int
        Object id of the MaterialPointManager.
    name : str
        Name of the MaterialPointManager.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize MaterialPointManager """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def create_material_point(self, suggested_name : str, coords : Iterable[float], params : CreateMaterialPointParams) -> CreateMaterialPointResults:
        """ Creates a material point at the given coordinates.


        Parameters
        ----------
        suggested_name : str
            Name suggested for the material point.
        coords : Iterable[float]
            Coordinates of material point.
        params : CreateMaterialPointParams
            Parameters used to create material point.

        Returns
        -------
        CreateMaterialPointResults
            Returns the result with material point name and id.

        Notes
        -----
        A material point is created on calling this API.

        Examples
        --------
        >>> material_point_results = model.control_data.create_material_point("Fluid", [1.0,2,0,3.0], params)

        """
        if not isinstance(suggested_name, str):
            raise TypeError("Invalid argument type passed for 'suggested_name'. Valid argument type is str.")
        if not isinstance(coords, Iterable):
            raise TypeError("Invalid argument type passed for 'coords'. Valid argument type is Iterable[float].")
        if not isinstance(params, CreateMaterialPointParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is CreateMaterialPointParams.")
        args = {"suggested_name" : suggested_name,
        "coords" : coords,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::MaterialPointManager/CreateMaterialPoint"
        self._model._print_logs_before_command("create_material_point", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_material_point", CreateMaterialPointResults(model = self._model, json_data = result))
        return CreateMaterialPointResults(model = self._model, json_data = result)

    def delete_material_point(self, name : str) -> DeleteMaterialPointResults:
        """ Deletes material point identified with the given name.


        Parameters
        ----------
        name : str
            Name of the material point to be deleted.

        Returns
        -------
        DeleteMaterialPointResults
            Returns the DeleteMaterialPointResults.


        Examples
        --------
        >>> client = prime.launch_prime()
        >>> model = client.model
        >>> results = model.material_point_data.delete_material_point("fluid")

        """
        if not isinstance(name, str):
            raise TypeError("Invalid argument type passed for 'name'. Valid argument type is str.")
        args = {"name" : name}
        command_name = "PrimeMesh::MaterialPointManager/DeleteMaterialPoint"
        self._model._print_logs_before_command("delete_material_point", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_material_point", DeleteMaterialPointResults(model = self._model, json_data = result))
        return DeleteMaterialPointResults(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of MaterialPointManager."""
        return self._id

    @property
    def name(self):
        """ Get the name of MaterialPointManager."""
        return self._name
