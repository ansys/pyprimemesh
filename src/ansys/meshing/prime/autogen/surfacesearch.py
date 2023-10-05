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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchByQualityParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchByQualityParams.")
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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchBySelfIntersectionParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchBySelfIntersectionParams.")
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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchBySpikeParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchBySpikeParams.")
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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchByFoldsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchByFoldsParams.")
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByFolds"
        self._model._print_logs_before_command("search_zonelets_by_folds", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_folds", SearchByFoldsResults(model = self._model, json_data = result))
        return SearchByFoldsResults(model = self._model, json_data = result)

    def search_zonelets_by_invalid_normals(self, part_id : int, face_zonelets : Iterable[int], register_id : int) -> SearchByInvalidNormalsResults:
        """ Search face zonelets to identify faces with invalid normals.

        Search face zonelets to identify faces with invalid normals.

        Parameters
        ----------
        part_id : int
            Id of part.
        face_zonelets : Iterable[int]
            Ids of face zonelets.
        register_id : int
            Id of register.

        Returns
        -------
        SearchByInvalidNormalsResults
            Returns the SearchByInvalidNormalsResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> results = surf_search.search_zonelets_by_invalid_normals(part_id, face_zonelets, register_id)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "register_id" : register_id}
        command_name = "PrimeMesh::SurfaceSearch/SearchZoneletsByInvalidNormals"
        self._model._print_logs_before_command("search_zonelets_by_invalid_normals", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("search_zonelets_by_invalid_normals", SearchByInvalidNormalsResults(model = self._model, json_data = result))
        return SearchByInvalidNormalsResults(model = self._model, json_data = result)

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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchByThinStripParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchByThinStripParams.")
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
        if not isinstance(params, SurfaceQualitySummaryParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SurfaceQualitySummaryParams.")
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
        if not isinstance(params, SurfaceDiagnosticSummaryParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SurfaceDiagnosticSummaryParams.")
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
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(register_id, int):
            raise TypeError("Invalid argument type passed for register_id, valid argument type is int.")
        if not isinstance(params, SearchInfoByRegisterIdParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SearchInfoByRegisterIdParams.")
        args = {"face_zonelets" : face_zonelets,
        "register_id" : register_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/GetSearchInfoByRegisterId"
        self._model._print_logs_before_command("get_search_info_by_register_id", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_search_info_by_register_id", SearchInfoByRegisterIdResults(model = self._model, json_data = result))
        return SearchInfoByRegisterIdResults(model = self._model, json_data = result)

    def check_face_deviation(self, source_face_zonelets : Iterable[int], target_face_zonelets : Iterable[int], params : CheckFaceDeviationParams) -> CheckFaceDeviationResults:
        """ Gets information regarding the number of faces with a deviation higher than the tolerance.


        Parameters
        ----------
        source_face_zonelets : Iterable[int]
            Scope of reference zonelets from which the deviation is checked.
        target_face_zonelets : Iterable[int]
            Scope of target zonelets for which the deviation is checked.
        params : CheckFaceDeviationParams
            Parameters for retrieving information while performing check face deviation operation.

        Returns
        -------
        CheckFaceDeviationResults
            Returns the CheckFaceDeviationResults.

        Examples
        --------
        >>> surf_search = SurfaceSearch(model=model)
        >>> params = prime.CheckFaceDeviationParams()
        >>> results = surf_search.check_face_deviation(source_scope, reference_scope, params)

        """
        if not isinstance(source_face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for source_face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(target_face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for target_face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, CheckFaceDeviationParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CheckFaceDeviationParams.")
        args = {"source_face_zonelets" : source_face_zonelets,
        "target_face_zonelets" : target_face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceSearch/CheckFaceDeviation"
        self._model._print_logs_before_command("check_face_deviation", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("check_face_deviation", CheckFaceDeviationResults(model = self._model, json_data = result))
        return CheckFaceDeviationResults(model = self._model, json_data = result)
