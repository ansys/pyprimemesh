""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class SurfaceSearch(CoreObject):
    """SurfaceSearch allows you to check surface mesh quality.

    SurfaceSearch performs surface mesh quality check based on different face quality measures.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize SurfaceSearch """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::SurfaceSearch/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for SurfaceSearch. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for SurfaceSearch. """
        command_name = "PrimeMesh::SurfaceSearch/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def search_zonelets_by_quality(self, part_id : int, face_zonelets : Iterable[int], register_id : int, params : SearchByQualityParams) -> SearchByQualityResults:
        """ Search face zonelets with the provided quality parameters and applies register id on face elements found.


        Parameters
        ----------
        part_id : int
            Id of the part.
        face_zonelets : Iterable[int]
            Ids of the face zonelets whose element search is performed.
        register_id : int
            Id used to register face elements found by the search.
        params : SearchByQualityParams
            Quality parameters used to search face elements.

        Returns
        -------
        SearchByQualityResults
            Returns the SearchByQualityResults.

        Examples
        --------
        >>> surf_search = prime.SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_quality(part_id, face_zonelets, register_id, prime.SearchByQualityParams(model=model))

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByQuality"
        self._model._print_logs_before_command("search_zonelets_by_quality", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_quality", SearchByQualityResults(model = self._model, json_data = result))
        return SearchByQualityResults(model = self._model, json_data = result)

    def search_zonelets_by_self_intersections(self, part_id : int, face_zonelets : Iterable[int], register_id : int, params : SearchBySelfIntersectionParams) -> SearchByIntersectionResults:
        """ Search face zonelets to identify face elements intersecting with each other.


        Parameters
        ----------
        part_id : int
            Id of part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id of register.
        params : SearchBySelfIntersectionParams
            Parameters used to identify face elements by self intersection.

        Returns
        -------
        SearchByIntersectionResults
            Returns the SearchByIntersectionResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_self_intersections(part_id, face_zonelets, register_id, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsBySelfIntersections"
        self._model._print_logs_before_command("search_zonelets_by_self_intersections", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_self_intersections", SearchByIntersectionResults(model = self._model, json_data = result))
        return SearchByIntersectionResults(model = self._model, json_data = result)

    def search_zonelets_by_spikes(self, part_id : int, face_zonelets : Iterable[int], register_id : int, params : SearchBySpikeParams) -> SearchBySpikeResults:
        """ Search face zonelets to identify spikes.

        Search face zonelets to identify spikes with provided spike parameters

        Parameters
        ----------
        part_id : int
            Id of part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id of register.
        params : SearchBySpikeParams
            Parameters used to identify spikes.

        Returns
        -------
        SearchBySpikeResults
            Returns the SearchBySpikeResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_spikes(part_id, face_zonelets, register_id, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsBySpikes"
        self._model._print_logs_before_command("search_zonelets_by_spikes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_spikes", SearchBySpikeResults(model = self._model, json_data = result))
        return SearchBySpikeResults(model = self._model, json_data = result)

    def search_zonelets_by_folds(self, part_id : int, face_zonelets : Iterable[int], register_id : int, params : SearchByFoldsParams) -> SearchByFoldsResults:
        """ Search face zonelets to identify folds.

        Search face zonelets to identify folds with provided folds parameters.

        Parameters
        ----------
        part_id : int
            Id of part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id of register.
        params : SearchByFoldsParams
            Parameters used to identify folds.

        Returns
        -------
        SearchByFoldsResults
            Returns the SearchByFoldsResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_folds(part_id, face_zonelets, register_id, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByFolds"
        self._model._print_logs_before_command("search_zonelets_by_folds", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_folds", SearchByFoldsResults(model = self._model, json_data = result))
        return SearchByFoldsResults(model = self._model, json_data = result)

    def search_zonelets_by_thin_strips(self, part_id : int, face_zonelets : Iterable[int], register_id : int, params : SearchByThinStripParams) -> SearchByThinStripResults:
        """ Search face zonelets to identify face element of thin strips(single layer of triangles between features).


        Parameters
        ----------
        part_id : int
            Id of part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id of register.
        params : SearchByThinStripParams
            Parameters used to identify face elements of thin strips.

        Returns
        -------
        SearchByThinStripResults
            Returns the SearchByThinStripResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_thin_strips(part_id, face_zonelets, register_id, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByThinStrips"
        self._model._print_logs_before_command("search_zonelets_by_thin_strips", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_thin_strips", SearchByThinStripResults(model = self._model, json_data = result))
        return SearchByThinStripResults(model = self._model, json_data = result)

    def get_surface_quality_summary(self, params : SurfaceQualitySummaryParams) -> SurfaceQualitySummaryResults:
        """ Gets the surface quality summary.

        Diagnose surface quality for the given scope and face quality measures provided by the surface quality summary parameters.
        Uses default quality limit if not specified with params.

        Parameters
        ----------
        params : SurfaceQualitySummaryParams
            Surface quality summary parameters.

        Returns
        -------
        SurfaceQualitySummaryResults
            Returns the SurfaceQualitySummaryResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.get_surface_quality_summary(SurfaceQualitySummaryParams(model=model))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/GetSurfaceQualitySummary"
        self._model._print_logs_before_command("get_surface_quality_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_surface_quality_summary", SurfaceQualitySummaryResults(model = self._model, json_data = result))
        return SurfaceQualitySummaryResults(model = self._model, json_data = result)

    def get_surface_diagnostic_summary(self, params : SurfaceDiagnosticSummaryParams) -> SurfaceDiagnosticSummaryResults:
        """ Gets the surface diagnostic summary.

        Diagnose surface connectivity for the given scope and controls provided by the surface diagnostic summary parameters.

        Parameters
        ----------
        params : SurfaceDiagnosticSummaryParams
            Surface diagnostic summary parameters.

        Returns
        -------
        SurfaceDiagnosticSummaryResults
            Returns the SurfaceDiagnosticSummaryResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.get_surface_diagnostics_summary(SurfaceDiagnosticSummaryParams(model=model))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/GetSurfaceDiagnosticSummary"
        self._model._print_logs_before_command("get_surface_diagnostic_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_surface_diagnostic_summary", SurfaceDiagnosticSummaryResults(model = self._model, json_data = result))
        return SurfaceDiagnosticSummaryResults(model = self._model, json_data = result)

    def get_search_info_by_register_id(self, face_zonelets : Iterable[int], register_id : int, params : SearchInfoByRegisterIdParams) -> SearchInfoByRegisterIdResults:
        """ Gets search information regarding registered face elements of provided zonelets using a register id.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of the face zonelets to search in.
        register_id : int
            An integer register id.
        params : SearchInfoByRegisterIdParams
            Parameters for retrieveing information on registered faces.

        Returns
        -------
        SearchInfoByRegisterIdResults
            Returns the SearchInfoByRegisterIdResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> params = prime.SearchInfoByRegisterIdParams(model=model)
        >>> results = surf_search.get_search_info_by_register_id(face_zonelets, register_id, params)

        """
        args = {"face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/GetSearchInfoByRegisterId"
        self._model._print_logs_before_command("get_search_info_by_register_id", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_search_info_by_register_id", SearchInfoByRegisterIdResults(model = self._model, json_data = result))
        return SearchInfoByRegisterIdResults(model = self._model, json_data = result)
