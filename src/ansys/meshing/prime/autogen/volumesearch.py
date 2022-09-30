""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class VolumeSearch(CoreObject):
    """VolumeSearch allows you to check volume mesh quality.

    VolumeSearch performs volume mesh quality check based on different cell quality measures.
    """

    def __init__(self, model: CommunicationManager):
        """ Initialize VolumeSearch """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::VolumeSearch/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for VolumeSearch. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for VolumeSearch. """
        command_name = "PrimeMesh::VolumeSearch/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def get_volume_quality_summary(self, params : VolumeQualitySummaryParams) -> VolumeQualitySummaryResults:
        """ Gets the volume quality summary.

        Diagnose volume quality for the given scope and cell quality measures provided in the VolumeQualitySummaryParams structure.
        Use default quality limit if the parameters are not specified.

        Parameters
        ----------
        params : VolumeQualitySummaryParams
            Volume quality summary parameters.

        Returns
        -------
        VolumeQualitySummaryResults
            Returns the VolumeQualitySummaryResults.

        Examples
        --------
        >>> vol_search = VolumeSearch(model=model)
        >>> results = vol_search.get_volume_quality_summary(VolumeQualitySummaryParams(model=model))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::VolumeSearch/GetVolumeQualitySummary"
        self._model._print_logs_before_command("get_volume_quality_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_volume_quality_summary", VolumeQualitySummaryResults(model = self._model, json_data = result))
        return VolumeQualitySummaryResults(model = self._model, json_data = result)
