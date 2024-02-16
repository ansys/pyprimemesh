""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class Wrapper(CoreObject):
    """Provide operations to generate surface mesh using wrapper technology.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize Wrapper """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::Wrapper/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for Wrapper. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for Wrapper. """
        command_name = "PrimeMesh::Wrapper/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def wrap(self, wrapper_control_id : int, params : WrapParams) -> WrapResult:
        """ Performs wrapping with specified controls in wrapper control and with provided parameters.


        Parameters
        ----------
        wrapper_control_id : int
            Id of wrapper control.
        params : WrapParams
            Wrap Parameters.

        Returns
        -------
        WrapResult
            Returns the WrapResult.


        Examples
        --------
        >>> results = wrapper.wrap(wrapper_control_id, params)

        """
        if not isinstance(wrapper_control_id, int):
            raise TypeError("Invalid argument type passed for wrapper_control_id, valid argument type is int.")
        if not isinstance(params, WrapParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is WrapParams.")
        args = {"wrapper_control_id" : wrapper_control_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/Wrap"
        self._model._print_logs_before_command("wrap", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("wrap", WrapResult(model = self._model, json_data = result))
        return WrapResult(model = self._model, json_data = result)

    def improve_quality(self, part_id : int, params : WrapperImproveQualityParams) -> WrapperImproveResult:
        """ Improve the surface quality and resolve connectivity issues like intersections, multi, free, spikes, point contacts and so on.


        Parameters
        ----------
        part_id : int
            Id of the part.
        params : WrapperImproveQualityParams
            Wrapper improve quality parameters.

        Returns
        -------
        WrapperImproveResult
            Return the Wrapper improve result.


        Examples
        --------
        >>> result = wrapper.improve_quality(part_id, params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(params, WrapperImproveQualityParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is WrapperImproveQualityParams.")
        args = {"part_id" : part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/ImproveQuality"
        self._model._print_logs_before_command("improve_quality", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("improve_quality", WrapperImproveResult(model = self._model, json_data = result))
        return WrapperImproveResult(model = self._model, json_data = result)

    def close_gaps(self, scope : ScopeDefinition, params : WrapperCloseGapsParams) -> WrapperCloseGapsResult:
        """ Close gaps create patching surfaces within the face zonelets specified by scope using gap size.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition of face zonelets.
        params : WrapperCloseGapsParams
            Wrapper close gaps parameters.

        Returns
        -------
        WrapperCloseGapsResult
            Returns the WrapperCloseGapsResult.


        Examples
        --------
        >>> result = wrapper.close_gaps(scope, params)

        """
        if not isinstance(scope, ScopeDefinition):
            raise TypeError("Invalid argument type passed for scope, valid argument type is ScopeDefinition.")
        if not isinstance(params, WrapperCloseGapsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is WrapperCloseGapsParams.")
        args = {"scope" : scope._jsonify(),
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/CloseGaps"
        self._model._print_logs_before_command("close_gaps", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("close_gaps", WrapperCloseGapsResult(model = self._model, json_data = result))
        return WrapperCloseGapsResult(model = self._model, json_data = result)

    def patch_flow_regions(self, live_material_point : str, params : WrapperPatchFlowRegionsParams) -> WrapperPatchFlowRegionsResult:
        """ Patch flow regions create patching surfaces for regions identified by dead regions from wrapper patch holes parameters.


        Parameters
        ----------
        live_material_point : str
            Name of live material point.
        params : WrapperPatchFlowRegionsParams
            Parameters to define patch flow regions operation.

        Returns
        -------
        WrapperPatchFlowRegionsResult
            Returns the WrapperPatchFlowRegionsResult.


        Notes
        -----
        This API is a Beta. API Behavior and implementation may change in future.

        Examples
        --------
        >>> results = wrapper.PatchFlowRegions(live_material_point, params)

        """
        if not isinstance(live_material_point, str):
            raise TypeError("Invalid argument type passed for live_material_point, valid argument type is str.")
        if not isinstance(params, WrapperPatchFlowRegionsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is WrapperPatchFlowRegionsParams.")
        args = {"live_material_point" : live_material_point,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::Wrapper/PatchFlowRegions"
        self._model._print_beta_api_warning("patch_flow_regions")
        self._model._print_logs_before_command("patch_flow_regions", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("patch_flow_regions", WrapperPatchFlowRegionsResult(model = self._model, json_data = result))
        return WrapperPatchFlowRegionsResult(model = self._model, json_data = result)
