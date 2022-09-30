""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class SizeControl(CoreObject):
    """Size control is used to compute the size field.

    The size field is computed based on the size control defined.
    Different type of size controls provide control over how the mesh size is distributed on a surface or within the volume.
    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize SizeControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_curvature_sizing_params(self, params : CurvatureSizingParams) -> SetSizingResults:
        """ Set the curvature sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : CurvatureSizingParams
            Parameters that enables you to set the normal angle as the maximum allowable angle at which one element edge may span.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_curvature_sizing_params(
        >>>                  prime.CurvatureSizingParams(model=model,
        >>>                  min = 0.1, max = 1.0, growth_rate = 1.2,
        >>>                  normal_angle = 18))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetCurvatureSizingParams"
        self._model._print_logs_before_command("set_curvature_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_curvature_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def set_soft_sizing_params(self, params : SoftSizingParams) -> SetSizingResults:
        """ Set the soft sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : SoftSizingParams
            Parameters that enables you to set the maximum size on scoped face zonelets.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_soft_sizing_params(
        >>>                  prime.SoftSizingParams(model=model,
        >>>                  max = 1.0, growth_rate = 1.2))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetSoftSizingParams"
        self._model._print_logs_before_command("set_soft_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_soft_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def set_proximity_sizing_params(self, params : ProximitySizingParams) -> SetSizingResults:
        """ Set the proximity sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : ProximitySizingParams
            Parameters that enables you to specify number of elements in the gaps.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_proximity_sizing_params(
        >>>                  prime.ProximitySizingParams(model=model,
        >>>                  min = 0.1, max = 1.0, growth_rate = 1.2))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetProximitySizingParams"
        self._model._print_logs_before_command("set_proximity_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_proximity_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def set_hard_sizing_params(self, params : HardSizingParams) -> SetSizingResults:
        """ Set the hard sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : HardSizingParams
            Parameters that enables you to set uniform size based on the specified size.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_hard_sizing_params(
        >>>                  prime.HardSizingParams(model=model,
        >>>                  min = 0.1, growth_rate = 1.2))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetHardSizingParams"
        self._model._print_logs_before_command("set_hard_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_hard_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def set_meshed_sizing_params(self, params : MeshedSizingParams) -> SetSizingResults:
        """ Set the meshed sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : MeshedSizingParams
            Parameters that enables you to set the sizes based on existing sizes.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_meshed_sizing_params(
        >>>                  prime.MeshedSizingParams(model=model,
        >>>                  growth_rate = 1.2))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetMeshedSizingParams"
        self._model._print_logs_before_command("set_meshed_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_meshed_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def set_boi_sizing_params(self, params : BoiSizingParams) -> SetSizingResults:
        """ Set the body of influence sizing parameters to compute volumetric size field.


        Parameters
        ----------
        params : BoiSizingParams
            Parameters that enables you to set sizing on the body of influence region.

        Returns
        -------
        SetSizingResults
            Return the SetSizingResults.


        Examples
        --------
        >>> size_control.set_boi_sizing_params(
        >>>                  prime.BoiSizingParams(model=model,
        >>>                  max = 0.1, growth_rate = 1.2))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetBoiSizingParams"
        self._model._print_logs_before_command("set_boi_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_boi_sizing_params", SetSizingResults(model = self._model, json_data = result))
        return SetSizingResults(model = self._model, json_data = result)

    def get_curvature_sizing_params(self) -> CurvatureSizingParams:
        """ Get the curvature sizing parameters of size control.


        Returns
        -------
        CurvatureSizingParams
            Return the CurvatureSizingParams.


        Examples
        --------
        >>> params = size_control.get_curvature_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetCurvatureSizingParams"
        self._model._print_logs_before_command("get_curvature_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_curvature_sizing_params", CurvatureSizingParams(model = self._model, json_data = result))
        return CurvatureSizingParams(model = self._model, json_data = result)

    def get_soft_sizing_params(self) -> SoftSizingParams:
        """ Get the soft sizing parameters of size control.


        Returns
        -------
        SoftSizingParams
            Return the SoftSizingParams.


        Examples
        --------
        >>> params = size_control.get_soft_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetSoftSizingParams"
        self._model._print_logs_before_command("get_soft_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_soft_sizing_params", SoftSizingParams(model = self._model, json_data = result))
        return SoftSizingParams(model = self._model, json_data = result)

    def get_proximity_sizing_params(self) -> ProximitySizingParams:
        """ Get the proximity sizing parameters of size control.


        Returns
        -------
        ProximitySizingParams
            Return the ProximitySizingParams.


        Examples
        --------
        >>> params = size_control.get_proximity_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetProximitySizingParams"
        self._model._print_logs_before_command("get_proximity_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_proximity_sizing_params", ProximitySizingParams(model = self._model, json_data = result))
        return ProximitySizingParams(model = self._model, json_data = result)

    def get_hard_sizing_params(self) -> HardSizingParams:
        """ Get the hard sizing parameters of size control.


        Returns
        -------
        HardSizingParams
            Return the HardSizingParams.


        Examples
        --------
        >>> params = size_control.get_hard_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetHardSizingParams"
        self._model._print_logs_before_command("get_hard_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_hard_sizing_params", HardSizingParams(model = self._model, json_data = result))
        return HardSizingParams(model = self._model, json_data = result)

    def get_meshed_sizing_params(self) -> MeshedSizingParams:
        """ Get the meshed sizing parameters of size control.


        Returns
        -------
        MeshedSizingParams
            Return the MeshedSizingParams.


        Examples
        --------
        >>> params = size_control.get_meshed_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetMeshedSizingParams"
        self._model._print_logs_before_command("get_meshed_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_meshed_sizing_params", MeshedSizingParams(model = self._model, json_data = result))
        return MeshedSizingParams(model = self._model, json_data = result)

    def get_boi_sizing_params(self) -> BoiSizingParams:
        """ Get the body of influence sizing parameters of size control.


        Returns
        -------
        BoiSizingParams
            Return the BoiSizingParams.


        Examples
        --------
        >>> params = size_control.get_boi_sizing_params()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetBoiSizingParams"
        self._model._print_logs_before_command("get_boi_sizing_params", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_boi_sizing_params", BoiSizingParams(model = self._model, json_data = result))
        return BoiSizingParams(model = self._model, json_data = result)

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Set the unique name for the size control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the size control.

        Returns
        -------
        SetNameResults
            Return a name of the size control.


        Examples
        --------
        >>> size_control.set_suggested_name("control1")

        """
        args = {"name" : name}
        command_name = "PrimeMesh::SizeControl/SetSuggestedName"
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    def set_scope(self, scope : ScopeDefinition) -> SetScopeResults:
        """ Set the scope for size control to evaluate.

        Size control uses scope to evaluate entities for which size field needs to be computed.

        Parameters
        ----------
        scope : ScopeDefinition
            ScopeDefinition to scope entities for size field computation.

        Returns
        -------
        SetScopeResults
            Return a SetScopeResults.


        Examples
        --------
        >>> size_control.set_scope(prime.ScopeDefinition(model=model,
        >>>                        entity_type = ScopeEntity.FACEZONELETS,
        >>>                        evaluation_type = ScopeEvaluationType.LABELS,
        >>>                        label_expression = "inlet"))

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::SizeControl/SetScope"
        self._model._print_logs_before_command("set_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_scope", SetScopeResults(model = self._model, json_data = result))
        return SetScopeResults(model = self._model, json_data = result)

    def get_scope(self) -> ScopeDefinition:
        """ Get the scope used by size control to evaluate entities.


        Returns
        -------
        ScopeDefinition
            Return the ScopeDefinition.


        Examples
        --------
        >>> scope = size_control.get_scope()

        """
        args = {}
        command_name = "PrimeMesh::SizeControl/GetScope"
        self._model._print_logs_before_command("get_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_summary(self, params : SizeControlSummaryParams) -> SizeControlSummaryResult:
        """ Get the size control summary along with the evaluated scope for the provided parameters..


        Parameters
        ----------
        params : SizeControlSummaryParams
            Size control summary parameters.

        Returns
        -------
        SizeControlSummaryResult
            Return the SizeControlSummaryResult.

        Examples
        --------
        >>> results = size_control.get_summary(prime.SizeControlSummaryParams(model=model))

        """
        args = {"params" : params._jsonify()}
        command_name = "PrimeMesh::SizeControl/GetSummary"
        self._model._print_logs_before_command("get_summary", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_summary", SizeControlSummaryResult(model = self._model, json_data = result))
        return SizeControlSummaryResult(model = self._model, json_data = result)

    @property
    def id(self):
        """ Get the id of SizeControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of SizeControl."""
        return self._name
