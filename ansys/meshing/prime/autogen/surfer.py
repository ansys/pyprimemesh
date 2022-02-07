""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class Surfer(CoreObject):
    """Generates surface mesh.

    Performs surface meshing using various surface meshing algorithms on topofaces or face zonelets.
    For example, constant size or volumetric size surface meshing.
    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize Surfer  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Surfer/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Surfer. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Surfer. """
        command_name = "PrimeMesh::Surfer/Destruct"
        self._comm.serve(command_name, self._object_id, args={})

    def remesh_face_zonelets(self, face_zonelets : List[int], edge_zonelets : List[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given face zonelets with provided parameters.


        Parameters
        ----------
        face_zonelets : List[int]
            Ids of face zonelets.
        edge_zonelets : List[int]
            Ids of edge zonelets.
        params : SurferParams
            Surfer parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.remesh_face_zonelets(face_zonelets, edge_zonelets, params)

        """
        args = {"face_zonelets" : face_zonelets,
        "edge_zonelets" : edge_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/RemeshFaceZonelets"
        self._model._print_logs_before_command("remesh_face_zonelets", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("remesh_face_zonelets", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)

    def mesh_topo_faces(self, topo_faces : List[int], params : SurferParams) -> SurferResults:
        """ Performs meshing on the given topofaces with provided parameters.


        Parameters
        ----------
        topo_faces : List[int]
            Ids of topofaces.
        params : SurferParams
            Surfer Parameters.

        Returns
        -------
        SurferResults
            Returns the SurferResults.


        Examples
        --------
        >>> results = surfer.mesh_topo_faces(topo_faces, params)

        """
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Surfer/MeshTopoFaces"
        self._model._print_logs_before_command("mesh_topo_faces", args)
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("mesh_topo_faces", SurferResults(model = self._model, json_data = result))
        return SurferResults(model = self._model, json_data = result)
