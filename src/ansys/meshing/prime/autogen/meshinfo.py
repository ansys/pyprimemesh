""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class MeshInfo(CoreObject):
    """MeshInfo provides information about the mesh connectivity and more.

    Mesh connectivity information is used in graphics rendering.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize MeshInfo """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::MeshInfo/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for MeshInfo. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for MeshInfo. """
        command_name = "PrimeMesh::MeshInfo/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def get_face_and_edge_connectivity(self, part_ids : Iterable[int], params : FaceAndEdgeConnectivityParams) -> FaceAndEdgeConnectivityResults:
        """ Gets the connectivity of face and edge zonelets of the given part ids.

        Connectivity result is used in graphics rendering.

        Parameters
        ----------
        part_ids : Iterable[int]
            Ids of the part.
        params : FaceAndEdgeConnectivityParams
            Parameters to get connectivity of face zonelets and edge zonelets.

        Returns
        -------
        FaceAndEdgeConnectivityResults
            Returns the FaceAndEdgeConnectivityResults.


        Examples
        --------
        >>> mesh_info = prime.MeshInfo(model)
        >>> part_ids = [part.id for part in model.parts]
        >>> result = mesh_info.get_face_and_edge_connectivity(part_ids,
        >>>                  prime.FaceAndEdgeConnectivityParams(model =model))

        """
        args = {"part_ids" : part_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::MeshInfo/GetFaceAndEdgeConnectivity"
        self._model._print_logs_before_command("get_face_and_edge_connectivity", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_face_and_edge_connectivity", FaceAndEdgeConnectivityResults(model = self._model, json_data = result))
        return FaceAndEdgeConnectivityResults(model = self._model, json_data = result)

    def get_statistics_of_cell_zonelets(self, cell_zonelets : Iterable[int], params : CellStatisticsParams) -> CellStatisticsResults:
        """ Gets cell statistics of given cell zonelets using provided cell statistics parameters.


        Parameters
        ----------
        cell_zonelets : Iterable[int]
            Ids of cell zonelets for which statistics are calculated.
        params : CellStatisticsParams
            Parameters to get cells statistics.

        Returns
        -------
        CellStatisticsResults
            Returns the CellStatisticsResults.


        Examples
        --------
        >>> mesh_info = prime.MeshInfo(model)
        >>> part = model.get_part_by_name("part_name")
        >>> result = mesh_info.get_statistics_of_cell_zonelets(part.get_cell_zonelets(),
        >>>                  prime.CellStatisticsParams(model=model))

        """
        args = {"cell_zonelets" : cell_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::MeshInfo/GetStatisticsOfCellZonelets"
        self._model._print_logs_before_command("get_statistics_of_cell_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_statistics_of_cell_zonelets", CellStatisticsResults(model = self._model, json_data = result))
        return CellStatisticsResults(model = self._model, json_data = result)
