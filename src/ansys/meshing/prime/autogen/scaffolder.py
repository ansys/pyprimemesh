""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Scaffolder(CoreObject):
    """Scaffolder is used for achieving connections in structures made of sheets and beams. Solid bodies should be suppressed before applying scaffolding.

    """

    def __init__(self, model: CommunicationManager, part_id: int):
        """ Initialize Scaffolder  """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Scaffolder/Construct"
        args = {"ModelID" : model._object_id , "PartID" : part_id, "MaxID" : -1}
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Scaffolder. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Scaffolder. """
        command_name = "PrimeMesh::Scaffolder/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def scaffold_topo_faces_and_beams(self, topo_faces : Iterable[int], topo_beams : Iterable[int], params : ScaffolderParams) -> ScaffolderResults:
        """ Scaffold faces and beams with provided parameters.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topology faces.
        topo_beams : Iterable[int]
            Ids of topology edges for beams.
        params : ScaffolderParams
            Scaffolding parameters.

        Returns
        -------
        ScaffolderResults
            Return results in ScaffolderResults structure.


        Examples
        --------
        >>> results = scaffolder.ScaffoldTopoFacesAndBeams([1,2], [7,8], params)

        """
        args = {"topo_faces" : topo_faces,
        "topo_beams" : topo_beams,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Scaffolder/ScaffoldTopoFacesAndBeams"
        self._model._print_logs_before_command("scaffold_topo_faces_and_beams", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("scaffold_topo_faces_and_beams", ScaffolderResults(model = self._model, json_data = result))
        return ScaffolderResults(model = self._model, json_data = result)

    def split_topo_faces_by_mesh_region(self, topo_faces : Iterable[int]) -> ScaffolderSplitResults:
        """ Split input topofaces by mesh region.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topology faces.

        Returns
        -------
        ScaffolderSplitResults
            Return results in ScaffolderSplitResults type.


        Examples
        --------
        >>> results = scaffolder.split_topo_faces_by_mesh_region([1,2,7,8])

        """
        args = {"topo_faces" : topo_faces}
        command_name = "PrimeMesh::Scaffolder/SplitTopoFacesByMeshRegion"
        self._model._print_logs_before_command("split_topo_faces_by_mesh_region", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("split_topo_faces_by_mesh_region", ScaffolderSplitResults(model = self._model, json_data = result))
        return ScaffolderSplitResults(model = self._model, json_data = result)

    def merge_overlapping_topo_faces(self, topo_faces : Iterable[int], params : ScaffolderParams) -> ScaffolderMergeResults:
        """ Merge overlapping topofaces.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of topology faces.
        params : ScaffolderParams
            Scaffolder parameters.

        Returns
        -------
        ScaffolderMergeResults
            Return results in ScaffolderMergeResults.


        Examples
        --------
        >>> results = scaffolder.MergeOverlappingTopoFaces([1,2,7,8], params)

        """
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Scaffolder/MergeOverlappingTopoFaces"
        self._model._print_logs_before_command("merge_overlapping_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("merge_overlapping_topo_faces", ScaffolderMergeResults(model = self._model, json_data = result))
        return ScaffolderMergeResults(model = self._model, json_data = result)

    def delete_shadowed_topo_faces(self, topo_faces : Iterable[int], params : VolumetricScaffolderParams) -> ScaffolderMergeResults:
        """ Delete fully shadowed topofaces.


        Parameters
        ----------
        topo_faces : Iterable[int]
            Ids of input topofaces.
        params : VolumetricScaffolderParams
            Volumetric scaffolder parameters.

        Returns
        -------
        ScaffolderMergeResults
            Return results in ScaffolderMergeResults.


        Examples
        --------
        >>> results = scaffolder.delete_shadowed_topo_faces([1,2,3,4,5], params)

        """
        args = {"topo_faces" : topo_faces,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Scaffolder/DeleteShadowedTopoFaces"
        self._model._print_logs_before_command("delete_shadowed_topo_faces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_shadowed_topo_faces", ScaffolderMergeResults(model = self._model, json_data = result))
        return ScaffolderMergeResults(model = self._model, json_data = result)
