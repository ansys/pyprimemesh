""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class MaterialPointManager(CoreObject):
    """Provides functions for material point creation, deletion and queries.

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
            A name suggestion for material point.
        coords : Iterable[float]
            Coordinates of material point.
        params : CreateMaterialPointParams
            Parameters to material point.

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
        >>> model = prime.local_model()
        >>> results = model.material_point_data.delete_material_point("fluid")

        """
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
