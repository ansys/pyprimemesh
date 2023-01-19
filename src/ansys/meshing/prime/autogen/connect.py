""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Connect(CoreObject):
    """Connect face zonelets.

    Perform surface connection using various connect algorithms on face zonelets.

    Notes
    -----
    Connect operations like Join, Stitch and Intersect supports only computational mesh
    (mesh with reasonable size). Faceted mesh is not supported.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Connect """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Connect/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Connect. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Connect. """
        command_name = "PrimeMesh::Connect/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def intersect_face_zonelets(self, part_id : int, face_zonelet_ids : Iterable[int], with_face_zonelet_ids : Iterable[int], params : IntersectParams) -> ConnectResults:
        """ Perform intersection between specified face zonelets of the part with the given intersect parameters.


        Parameters
        ----------
        part_id : int
            Id of the part.
        face_zonelet_ids : Iterable[int]
            Face zonelets to be intersected.
        with_face_zonelet_ids : Iterable[int]
            Face zonelets to be intersected with.
        params : IntersectParams
            Parameters for intersection.

        Returns
        -------
        ConnectResults
            Returns the ConnectResults.


        Examples
        --------
        >>> connect = Connect(model = model)
        >>> results = connect.intersect_face_zonelets (part_id, face_zonelet_ids, with_face_zonelet_ids, params)

        """
        args = {"part_id" : part_id,
        "face_zonelet_ids" : face_zonelet_ids,
        "with_face_zonelet_ids" : with_face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Connect/IntersectFaceZonelets"
        self._model._print_logs_before_command("intersect_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("intersect_face_zonelets", ConnectResults(model = self._model, json_data = result))
        return ConnectResults(model = self._model, json_data = result)

    def join_face_zonelets(self, part_id : int, face_zonelet_ids : Iterable[int], with_face_zonelet_ids : Iterable[int], params : JoinParams) -> ConnectResults:
        """ Joins a set of face zones with another set of face zones.


        Parameters
        ----------
        part_id : int
            Id of the part.
        face_zonelet_ids : Iterable[int]
            Face zonelets to be joined.
        with_face_zonelet_ids : Iterable[int]
            Face zonelets to be joined with.
        params : JoinParams
            Parameters for join.

        Returns
        -------
        ConnectResults
            Returns the ConnectResults.


        Examples
        --------
        >>> connect = Connect(model = model)
        >>> results = connect.join_face_zonelets (part_id, face_zonelet_ids, with_face_zonelet_ids, params)

        """
        args = {"part_id" : part_id,
        "face_zonelet_ids" : face_zonelet_ids,
        "with_face_zonelet_ids" : with_face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Connect/JoinFaceZonelets"
        self._model._print_logs_before_command("join_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("join_face_zonelets", ConnectResults(model = self._model, json_data = result))
        return ConnectResults(model = self._model, json_data = result)

    def subtract_volumes(self, part_id : int, target_volumes : Iterable[int], cutter_volumes : Iterable[int], params : SubtractVolumesParams) -> SubtractVolumesResults:
        """ Subtract cutter volumes from target volumes.


        Parameters
        ----------
        part_id : int
            Id of a part.
        target_volumes : Iterable[int]
            Ids of target volumes.
        cutter_volumes : Iterable[int]
            Ids of cutter volumes.
        params : SubtractVolumesParams
            Parameters to control subtraction of volumes.

        Returns
        -------
        SubtractVolumesResults
            Returns the SubtractVolumesResults.


        Examples
        --------
        >>> results = connect.subtract_volumes(part_id, target_volumes, cutter_volumes, params)

        """
        args = {"part_id" : part_id,
        "target_volumes" : target_volumes,
        "cutter_volumes" : cutter_volumes,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Connect/SubtractVolumes"
        self._model._print_logs_before_command("subtract_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("subtract_volumes", SubtractVolumesResults(model = self._model, json_data = result))
        return SubtractVolumesResults(model = self._model, json_data = result)

    def stitch_face_zonelets(self, part_id : int, face_zonelet_ids : Iterable[int], with_face_zonelet_ids : Iterable[int], params : StitchParams) -> ConnectResults:
        """ Stitches a set of face zonelets with another set of face zones.


        Parameters
        ----------
        part_id : int
            Id of the part.
        face_zonelet_ids : Iterable[int]
            Face zonelets to be stitched.
        with_face_zonelet_ids : Iterable[int]
            Face zonelets to be stitched with.
        params : StitchParams
            Parameters for stitch.

        Returns
        -------
        ConnectResults
            Returns the ConnectResults.


        Examples
        --------
        >>> connect = Connect(model = model)
        >>> results = connect.stitch_face_zonelets (part_id, face_zonelet_ids, with_face_zonelet_ids, stitch_params)

        """
        args = {"part_id" : part_id,
        "face_zonelet_ids" : face_zonelet_ids,
        "with_face_zonelet_ids" : with_face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Connect/StitchFaceZonelets"
        self._model._print_logs_before_command("stitch_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("stitch_face_zonelets", ConnectResults(model = self._model, json_data = result))
        return ConnectResults(model = self._model, json_data = result)
