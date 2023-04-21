""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class QuadToSpline(CoreObject):
    """Converts all-quad mesh to spline.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize QuadToSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::QuadToSpline/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for QuadToSpline. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for QuadToSpline. """
        command_name = "PrimeMesh::QuadToSpline/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def convert_quad_to_spline__beta(self, part_id : int, quad_mesh_face_zonelet_ids : Iterable[int], topo_face_ids : Iterable[int], topo_edge_ids : Iterable[int], quad_to_spline_params : QuadToSplineParams) -> IGAResults:
        """ Converts fully quad mesh with topology to spline with the given conversion parameters.


        Parameters
        ----------
        part_id : int
            Id of the Part.
        quad_mesh_face_zonelet_ids : Iterable[int]
            Ids of the face zonelets of quad mesh.
        topo_face_ids : Iterable[int]
            Ids of topofaces.
        topo_edge_ids : Iterable[int]
            Ids of topoedges.
        quad_to_spline_params : QuadToSplineParams
            Parameters to convert quad to spline.

        Returns
        -------
        IGAResults
            Returns the IGAResults structure.


        Examples
        --------
        >>> results = quadToSpline.ConvertQuadToSpline(part_id, quad_mesh_face_zonelet_ids, geometric_face_zonelet_ids, geometric_edge_zonelet_ids, quad_to_spline_params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(quad_mesh_face_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for quad_mesh_face_zonelet_ids, valid argument type is Iterable[int].")
        if not isinstance(topo_face_ids, Iterable):
            raise TypeError("Invalid argument type passed for topo_face_ids, valid argument type is Iterable[int].")
        if not isinstance(topo_edge_ids, Iterable):
            raise TypeError("Invalid argument type passed for topo_edge_ids, valid argument type is Iterable[int].")
        if not isinstance(quad_to_spline_params, QuadToSplineParams):
            raise TypeError("Invalid argument type passed for quad_to_spline_params, valid argument type is QuadToSplineParams.")
        args = {"part_id" : part_id,
        "quad_mesh_face_zonelet_ids" : quad_mesh_face_zonelet_ids,
        "topo_face_ids" : topo_face_ids,
        "topo_edge_ids" : topo_edge_ids,
        "quad_to_spline_params" : quad_to_spline_params._jsonify()}
        command_name = "PrimeMesh::QuadToSpline/ConvertQuadToSpline_Beta"
        self._model._print_logs_before_command("convert_quad_to_spline__beta", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("convert_quad_to_spline__beta", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)
