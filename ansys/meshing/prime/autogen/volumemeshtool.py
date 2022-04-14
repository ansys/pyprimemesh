""" Auto-generated file. DO NOT MODIFY """
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
        """ Improves volme mesh by auto node move.


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
            Returns the VolumeMeshToolResults.


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

    def check_grid(self, part_id : int, params : CheckGridParams) -> CheckGridResults:
        """ Checks grid of a part.


        Parameters
        ----------
        part_id : int
            Id of a part.
        params : CheckGridParams
            Parameters to check grid.

        Returns
        -------
        CheckGridResults
            Returns the CheckGridResults.


        Examples
        --------
        >>> results = volume_mesh_tool.check_grid(part_id,
        >>>                                prime.CheckGridParams(model =model))

        """
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CheckGrid"
        self._model._print_logs_before_command("check_grid", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_grid", CheckGridResults(model = self._model, json_data = result))
        return CheckGridResults(model = self._model, json_data = result)
