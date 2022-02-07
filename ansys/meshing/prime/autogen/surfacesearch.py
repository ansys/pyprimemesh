""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

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
        result = self._comm.serve(command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for SurfaceSearch. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for SurfaceSearch. """
        command_name = "PrimeMesh::SurfaceSearch/Destruct"
        self._comm.serve(command_name, self._object_id, args={})

    def get_surface_quality_summary(self, params : SurfaceQualitySummaryParams) -> SurfaceQualitySummaryResults:
        """ Gets the surface quality summary.

        Diagnose surface quality for the given scope and face quality measures provided in params.
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
        result = self._comm.serve(command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_surface_quality_summary", SurfaceQualitySummaryResults(model = self._model, json_data = result))
        return SurfaceQualitySummaryResults(model = self._model, json_data = result)
