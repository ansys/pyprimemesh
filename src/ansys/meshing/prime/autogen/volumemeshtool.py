""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(cell_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for cell_zonelets, valid argument type is Iterable[int].")
        if not isinstance(boundary_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for boundary_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, AutoNodeMoveParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is AutoNodeMoveParams.")
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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(params, CheckMeshParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CheckMeshParams.")
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CheckMesh"
        self._model._print_logs_before_command("check_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_mesh", CheckMeshResults(model = self._model, json_data = result))
        return CheckMeshResults(model = self._model, json_data = result)

    def copy_cell_zonelets(self, cell_zonelets : Iterable[int], target_part_id : int, params : CopyZoneletsParams) -> CopyZoneletsResults:
        """ Copy cell zonelets and face zonelets connected to the cell zonelets.


        Parameters
        ----------
        cell_zonelets : Iterable[int]
            Ids of cell zonelets to be copied.
        target_part_id : int
            Part id used to move the copied zonelets.
        params : CopyZoneletsParams
            Parameters to copy cell zonelets.

        Returns
        -------
        CopyZoneletsResults
            Returns the CopyZoneletsResults.


        Notes
        -----
        This API is a Beta. API Behavior and implementation may change in future.

        Examples
        --------
        >>>> results = volume_mesh_tool.copy_cell_zonelets(cell_zonelets, target_part_id = new_part.id, prime.CopyZoneletsParams(model = model))

        """
        if not isinstance(cell_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for cell_zonelets, valid argument type is Iterable[int].")
        if not isinstance(target_part_id, int):
            raise TypeError("Invalid argument type passed for target_part_id, valid argument type is int.")
        if not isinstance(params, CopyZoneletsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CopyZoneletsParams.")
        args = {"cell_zonelets" : cell_zonelets,
        "target_part_id" : target_part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CopyCellZonelets"
        self._model._print_beta_api_warning("copy_cell_zonelets")
        self._model._print_logs_before_command("copy_cell_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("copy_cell_zonelets", CopyZoneletsResults(model = self._model, json_data = result))
        return CopyZoneletsResults(model = self._model, json_data = result)
