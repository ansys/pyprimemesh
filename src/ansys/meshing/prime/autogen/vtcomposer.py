""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class VTComposer(CoreObject):
    """VTComposer is used for fix topology corrections like separate, pinch.

    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize VTComposer  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::VTComposer/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for VTComposer. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for VTComposer. """
        command_name = "PrimeMesh::VTComposer/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def separate_faces_with_interior_edges(self, topo_faces : Iterable[int], params : VTComposerParams) -> VTComposerResults:
        """ Separates the given topofaces having interior edges using the given VT Composer parameters.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of input topofaces.
        params : VTComposerParams
            VT composer parameters.

        Returns
        -------
        VTComposerResults
            Return results in VTComposerResults.


        Notes
        -----
        This API is a Beta. API Behavior and implementation may change in future.

        Examples
        --------
        >>> results = vtcomposer.separate_faces_with_interior_edges([1,2,3,4,5], params)

        """
        if not isinstance(topo_faces, Iterable):
            raise TypeError("Invalid argument type passed for topo_faces, valid argument type is Iterable[int].")
        if not isinstance(params, VTComposerParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is VTComposerParams.")
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VTComposer/SeparateFacesWithInteriorEdges"
        self._model._print_beta_api_warning("separate_faces_with_interior_edges")
        self._model._print_logs_before_command("separate_faces_with_interior_edges", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("separate_faces_with_interior_edges", VTComposerResults(model = self._model, json_data = result))
        return VTComposerResults(model = self._model, json_data = result)
