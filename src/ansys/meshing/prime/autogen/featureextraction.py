""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class FeatureExtraction(CoreObject):
    """Provide functions for all feature extraction operations like extracting edges zonlelets, tracing node paths.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize FeatureExtraction """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::FeatureExtraction/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for FeatureExtraction. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for FeatureExtraction. """
        command_name = "PrimeMesh::FeatureExtraction/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def extract_features_on_face_zonelets(self, part_id : int, face_zonelets : Iterable[int], params : ExtractFeatureParams) -> ExtractFeatureResults:
        """ Extract edges by angle and face zonelet boundary using given extract feature parameters.


        Parameters
        ----------
        part_id : int
            Id of input part.
        face_zonelets : Iterable[int]
            Ids of input face zonelets.
        params : ExtractFeatureParams
            Parameters used to extract edges.

        Returns
        -------
        ExtractFeatureResults
            Returns a ExtractFeatureResults.


        Examples
        --------
        >>> results = feature_extraction.extract_features_on_face_zonelets(part_id, face_zonelets, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FeatureExtraction/ExtractFeaturesOnFaceZonelets"
        self._model._print_logs_before_command("extract_features_on_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("extract_features_on_face_zonelets", ExtractFeatureResults(model = self._model, json_data = result))
        return ExtractFeatureResults(model = self._model, json_data = result)

    def create_intersection_edge_loops(self, part_face_zonelets : List[PartZonelets], intersecting_part_face_zonelets : List[PartZonelets], params : CreateIntersectionEdgeLoopsParams) -> CreateIntersectionEdgeLoopsResults:
        """ Finds the edge zonelets formed by intersection of two face zonelets. Performs n to n intersection of face zonelets present in part face zonelets with those in intersecting part face zonelets depending on the input parameters. Order of input does not matter.


        Parameters
        ----------
        part_face_zonelets : PartZoneletsArray
            List of part zonelets to be intersected.
        intersecting_part_face_zonelets : PartZoneletsArray
            List of part zonelets to intersect with.
        params : CreateIntersectionEdgeLoopsParams
            Parameter to control edge extraction.

        Returns
        -------
        CreateIntersectionEdgeLoopsResults
            Returns the CreateIntersectionEdgeLoopsResults.


        Examples
        --------
        >>> results = feature_extraction.create_intersection_edge_loops(part_face_zonelets, intersecting_part_face_zonelets, params)

        """
        args = {"part_face_zonelets" : [p._jsonify() for p in part_face_zonelets],
        "intersecting_part_face_zonelets" : [p._jsonify() for p in intersecting_part_face_zonelets],
        "params" : params._jsonify()}
        command_name = "PrimeMesh::FeatureExtraction/CreateIntersectionEdgeLoops"
        self._model._print_logs_before_command("create_intersection_edge_loops", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_intersection_edge_loops", CreateIntersectionEdgeLoopsResults(model = self._model, json_data = result))
        return CreateIntersectionEdgeLoopsResults(model = self._model, json_data = result)
