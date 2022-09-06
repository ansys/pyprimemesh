""" Auto-generated file. DO NOT MODIFY """
# Copyright 2023 ANSYS, Inc.
# Unauthorized use, distribution, or duplication is prohibited.
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class VolumeMeshTool(CoreObject):
    """VolumeMeshTool allows you to check grid and improve volume mesh quality.

    VolumeMeshTool provides various volume mesh improvement algorithms.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize VolumeMeshTool """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::VolumeMeshTool/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for VolumeMeshTool. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for VolumeMeshTool. """
        command_name = "PrimeMesh::VolumeMeshTool/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def improve_by_auto_node_move(self, part_id : int, cell_zonelets : Iterable[int], boundary_zonelets : Iterable[int], params : AutoNodeMoveParams) -> VolumeMeshToolResults:
        """ Improve volume mesh by auto node move.


        Parameters
        ----------
        part_id : int
            Id of a part.
        cell_zonelets : Iterable[int]
            Ids of cell zonelets to be improved.
        boundary_zonelets : Iterable[int]
            Ids of boundary face zonelets.
        params : AutoNodeMoveParams
            Auto node move parameters.

        Returns
        -------
        VolumeMeshToolResults
            Return the VolumeMeshToolResults.


        Examples
        --------
        >>> results = volume_mesh_tool.improve_by_auto_node_move(part_id,
        >>>                                cell_zonelets,
        >>>                                boundary_zonelets,
        >>>                                prime.AutoNodeMoveParams(model =model))

        """
        args = {"part_id" : part_id,
        "cell_zonelets" : cell_zonelets,
        "boundary_zonelets" : boundary_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/ImproveByAutoNodeMove"
        self._model._print_logs_before_command("improve_by_auto_node_move", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("improve_by_auto_node_move", VolumeMeshToolResults(model = self._model, json_data = result))
        return VolumeMeshToolResults(model = self._model, json_data = result)

    def check_mesh(self, part_id : int, params : CheckMeshParams) -> CheckMeshResults:
        """ Checks mesh of a part.


        Parameters
        ----------
        part_id : int
            Id of a part.
        params : CheckMeshParams
            Parameters to check mesh.

        Returns
        -------
        CheckMeshResults
            Returns the CheckMeshResults.


        Examples
        --------
        >>> results = volume_mesh_tool.check_mesh(part_id,
        >>>                                prime.CheckMeshParams(model =model))

        """
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CheckMesh"
        self._model._print_logs_before_command("check_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_mesh", CheckMeshResults(model = self._model, json_data = result))
        return CheckMeshResults(model = self._model, json_data = result)

    def subtract_volumes(self, part_id : int, target_face_zonelets : Iterable[int], cutter_face_zonelets : Iterable[int], ignore_face_zonelets : Iterable[int], params : SubtractVolumesParams) -> SubtractVolumesResults:
        """ Subtract closed volumes represented by cutter face zonelets from target face zonelets. You need to ensure that both the cutter and the target do not share face zonelets or contain duplicates face zonelets. Note that the cutter and target can form multiple, overlapping closed volumes.


        Parameters
        ----------
        part_id : int
            Id of a part.
        target_face_zonelets : Iterable[int]
            Ids of face zonelets that form target volumes.
        cutter_face_zonelets : Iterable[int]
            Ids of face zonelets that form cutter volumes.
        ignore_face_zonelets : Iterable[int]
            Ids of face zonelets that should not be modified.
        params : SubtractVolumesParams
            Parameters to control subtraction of volumes.

        Returns
        -------
        SubtractVolumesResults
            Returns the SubtractVolumesResults.


        Examples
        --------
        >>> results = volume_mesh_tool.subtract_volumes(part_id, target_face_zonelets, cutter_face_zonelets, ignore_face_zonelets, params)

        """
        args = {"part_id" : part_id,
        "target_face_zonelets" : target_face_zonelets,
        "cutter_face_zonelets" : cutter_face_zonelets,
        "ignore_face_zonelets" : ignore_face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/SubtractVolumes"
        self._model._print_logs_before_command("subtract_volumes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("subtract_volumes", SubtractVolumesResults(model = self._model, json_data = result))
        return SubtractVolumesResults(model = self._model, json_data = result)
