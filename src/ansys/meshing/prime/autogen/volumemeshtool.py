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

class VolumeMeshTool(CoreObject):
    """VolumeMeshTool allows you to check grid and improve volume mesh quality.

    VolumeMeshTool provides various volume mesh improvement algorithms.


    Parameters
    ----------
    model : Model
        Server model to create VolumeMeshTool object.
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

    def assign_mesh_regions(self, target_part_id : int, target_cell_zonelets : Iterable[int], source_part_ids : Iterable[int], small_regions_volume_fraction : float) -> VolumeMeshToolResults:
        """ Assigns a region id to the cells in target cell zonelets of target part id. The region id is based on their location within source part ids.


        Parameters
        ----------
        target_part_id : int
            Id of the target part.
        target_cell_zonelets : Iterable[int]
            Ids of cell zonelets to be split into regions.
        source_part_ids : Iterable[int]
            Ids of solids used as a reference for assigning regions.
        small_regions_volume_fraction : float
            Regions with volumes smaller than a specified fraction of the total volume are merged into their largest adjacent region.
            This helps to eliminate isolated cells and thin regions from the output.

        Returns
        -------
        VolumeMeshToolResults
            Returns the VolumeMeshToolResults.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = volume_mesh_tool.AssignMeshRegions(target_part_id, target_cell_zonelets, source_part_ids, small_regions_volume_fraction)

        """
        if not isinstance(target_part_id, int):
            raise TypeError("Invalid argument type passed for 'target_part_id'. Valid argument type is int.")
        if not isinstance(target_cell_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'target_cell_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(source_part_ids, Iterable):
            raise TypeError("Invalid argument type passed for 'source_part_ids'. Valid argument type is Iterable[int].")
        if not isinstance(small_regions_volume_fraction, float):
            raise TypeError("Invalid argument type passed for 'small_regions_volume_fraction'. Valid argument type is float.")
        args = {"target_part_id" : target_part_id,
        "target_cell_zonelets" : target_cell_zonelets,
        "source_part_ids" : source_part_ids,
        "small_regions_volume_fraction" : small_regions_volume_fraction}
        command_name = "PrimeMesh::VolumeMeshTool/AssignMeshRegions"
        self._model._print_beta_api_warning("assign_mesh_regions")
        self._model._print_logs_before_command("assign_mesh_regions", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("assign_mesh_regions", VolumeMeshToolResults(model = self._model, json_data = result))
        return VolumeMeshToolResults(model = self._model, json_data = result)

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
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(cell_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'cell_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(boundary_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'boundary_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(params, AutoNodeMoveParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is AutoNodeMoveParams.")
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
            raise TypeError("Invalid argument type passed for 'part_id'. Valid argument type is int.")
        if not isinstance(params, CheckMeshParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is CheckMeshParams.")
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CheckMesh"
        self._model._print_logs_before_command("check_mesh", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_mesh", CheckMeshResults(model = self._model, json_data = result))
        return CheckMeshResults(model = self._model, json_data = result)

    def get_parts_for_points(self, points : Iterable[float], params : PartsForPointsParams) -> Iterable[int]:
        """ Finds parts enclosing the given list of points.


        Parameters
        ----------
        points : Iterable[float]
            Coordinates of points for which parts need to be found.
        params : PartsForPointsParams
            Parameters for searching parts.

        Returns
        -------
        Iterable[int]
            Returns array containing information about parts enclosing the points.


        Notes
        -----
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>> results = volume_mesh_tool.get_parts_for_points([0., 0., 0.], params)

        """
        if not isinstance(points, Iterable):
            raise TypeError("Invalid argument type passed for 'points'. Valid argument type is Iterable[float].")
        if not isinstance(params, PartsForPointsParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is PartsForPointsParams.")
        args = {"points" : points,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/GetPartsForPoints"
        self._model._print_beta_api_warning("get_parts_for_points")
        self._model._print_logs_before_command("get_parts_for_points", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_parts_for_points")
        return result

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
        **This is a beta API**. **The behavior and implementation may change in future**.

        Examples
        --------
        >>>> results = volume_mesh_tool.copy_cell_zonelets(cell_zonelets, target_part_id = new_part.id, prime.CopyZoneletsParams(model = model))

        """
        if not isinstance(cell_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for 'cell_zonelets'. Valid argument type is Iterable[int].")
        if not isinstance(target_part_id, int):
            raise TypeError("Invalid argument type passed for 'target_part_id'. Valid argument type is int.")
        if not isinstance(params, CopyZoneletsParams):
            raise TypeError("Invalid argument type passed for 'params'. Valid argument type is CopyZoneletsParams.")
        args = {"cell_zonelets" : cell_zonelets,
        "target_part_id" : target_part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeMeshTool/CopyCellZonelets"
        self._model._print_beta_api_warning("copy_cell_zonelets")
        self._model._print_logs_before_command("copy_cell_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("copy_cell_zonelets", CopyZoneletsResults(model = self._model, json_data = result))
        return CopyZoneletsResults(model = self._model, json_data = result)
