""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class WrapperControl(CoreObject):
    """Wrapper Control to describe all parameters and controls used for wrapping.

    """

    def __init__(self, model: CommunicationManager, id: int, object_id: int, name: str):
        """ Initialize WrapperControl """
        self._model = model
        self._comm = model._communicator
        self._id = id
        self._object_id = object_id
        self._name = name
        self._freeze()

    def set_geometry_scope(self, scope : ScopeDefinition):
        """ Sets geometry scope to given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            ScopeDefinition to scope entities for wrapping.

        Examples
        --------
        >>> wrapper_control.set_geometry_scope(scope)

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::WrapperControl/SetGeometryScope"
        self._model._print_logs_before_command("set_geometry_scope", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_geometry_scope")

    def set_leak_preventions(self, params : List[LeakPreventionParams]) -> SetLeakPreventionsResults:
        """ Set leak preventions to the wrapper control.


        Parameters
        ----------
        params : LeakPreventionParamsArray
            List of leak prevention parameters.

        Returns
        -------
        SetLeakPreventionsResults
            Return the set leak prevention results.

        Examples
        --------
        >>> set_leak_prev_results = wrapper_control.set_leak_preventions([params])

        """
        args = {"params" : [p._jsonify() for p in params]}
        command_name = "PrimeMesh::WrapperControl/SetLeakPreventions"
        self._model._print_logs_before_command("set_leak_preventions", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_leak_preventions", SetLeakPreventionsResults(model = self._model, json_data = result))
        return SetLeakPreventionsResults(model = self._model, json_data = result)

    def set_contact_preventions(self, params : List[ContactPreventionParams]) -> SetContactPreventionsResults:
        """ Set contact preventions to the wrapper control.


        Parameters
        ----------
        params : ContactPreventionParamsArray
            List of contact prevention parameters.

        Returns
        -------
        SetContactPreventionsResults
            Return the set contact prevention results.

        Examples
        --------
        >>> set_cont_prev_results = wrapper_control.set_contact_preventions([params])

        """
        args = {"params" : [p._jsonify() for p in params]}
        command_name = "PrimeMesh::WrapperControl/SetContactPreventions"
        self._model._print_logs_before_command("set_contact_preventions", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_contact_preventions", SetContactPreventionsResults(model = self._model, json_data = result))
        return SetContactPreventionsResults(model = self._model, json_data = result)

    def set_live_material_points(self, material_point_names : List[str]):
        """ Set live material points to the wrapper control.


        Parameters
        ----------
        material_point_names : List[str]
            List of live material points.

        Examples
        --------
        >>> wrapper_control.set_live_material_points(["Fluid1"])

        """
        args = {"material_point_names" : material_point_names}
        command_name = "PrimeMesh::WrapperControl/SetLiveMaterialPoints"
        self._model._print_logs_before_command("set_live_material_points", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_live_material_points")

    def set_feature_recoveries(self, params : List[FeatureRecoveryParams]) -> SetFeatureRecoveriesResults:
        """ Set feature recoveries to the wrapper control.


        Parameters
        ----------
        params : FeatureRecoveryParamsArray
            List of feature recovery parameters.

        Returns
        -------
        SetFeatureRecoveriesResults
            Return the set feature recoveries results.

        Examples
        --------
        >>> set_feat_rec_results = wrapper_control.set_feature_recoveries([params])

        """
        args = {"params" : [p._jsonify() for p in params]}
        command_name = "PrimeMesh::WrapperControl/SetFeatureRecoveries"
        self._model._print_logs_before_command("set_feature_recoveries", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_feature_recoveries", SetFeatureRecoveriesResults(model = self._model, json_data = result))
        return SetFeatureRecoveriesResults(model = self._model, json_data = result)

    def set_suggested_wrapper_part_name(self, name : str):
        """ Sets the given name for the created wrapper part  after wrapping with the wrapper control.


        Parameters
        ----------
        name : str
            Suggested name of the wrapper part to be created.

        Examples
        --------
        >>> wrapper_control.set_suggested_wrapper_part_name("wrap")

        """
        args = {"name" : name}
        command_name = "PrimeMesh::WrapperControl/SetSuggestedWrapperPartName"
        self._model._print_logs_before_command("set_suggested_wrapper_part_name", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_wrapper_part_name")

    def set_suggested_name(self, name : str) -> SetNameResults:
        """ Sets the unique name for the wrapper control based on the given suggested name.


        Parameters
        ----------
        name : str
            Suggested name for the wrapper control.

        Returns
        -------
        SetNameResults
            Returns the results with assigned name of the wrapper control.


        Examples
        --------
        >>> wrapper_control.set_suggested_name("wrapper_control1")

        """
        args = {"name" : name}
        command_name = "PrimeMesh::WrapperControl/SetSuggestedName"
        self._model._print_logs_before_command("set_suggested_name", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_suggested_name", SetNameResults(model = self._model, json_data = result))
        return SetNameResults(model = self._model, json_data = result)

    def get_geometry_scope(self) -> ScopeDefinition:
        """ Gets geometry scope of wrapper control.


        Returns
        -------
        ScopeDefinition
            Returns ScopeDefinition to scope entities from wrapper control.


        Examples
        --------
        >>> geom_scope = wrapper_control.get_geometry_scope()

        """
        args = {}
        command_name = "PrimeMesh::WrapperControl/GetGeometryScope"
        self._model._print_logs_before_command("get_geometry_scope", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_geometry_scope", ScopeDefinition(model = self._model, json_data = result))
        return ScopeDefinition(model = self._model, json_data = result)

    def get_live_material_points(self) -> List[str]:
        """ Gets list of material point names.


        Returns
        -------
        List[str]
            Returns the list of material point names.


        Examples
        --------
        >>> live_material_point_names = wrapper_control.get_live_material_points()

        """
        args = {}
        command_name = "PrimeMesh::WrapperControl/GetLiveMaterialPoints"
        self._model._print_logs_before_command("get_live_material_points", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_live_material_points")
        return result

    def set_shadow_geometry_scope(self, scope : ScopeDefinition):
        """ Sets shadow geometry scope to given scope.


        Parameters
        ----------
        scope : ScopeDefinition
            ScopeDefinition to scope shadow entities for wrapping.

        Examples
        --------
        >>> wrapper_control.set_shadow_geometry_scope(scope)

        """
        args = {"scope" : scope._jsonify()}
        command_name = "PrimeMesh::WrapperControl/SetShadowGeometryScope"
        self._model._print_logs_before_command("set_shadow_geometry_scope", args)
        self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("set_shadow_geometry_scope")

    @property
    def id(self):
        """ Get the id of WrapperControl."""
        return self._id

    @property
    def name(self):
        """ Get the name of WrapperControl."""
        return self._name
