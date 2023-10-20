""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

class QuadToSpline(CoreObject):
    """Converts all-quad mesh to spline.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize QuadToSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::QuadToSpline/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for QuadToSpline. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for QuadToSpline. """
        command_name = "PrimeMesh::QuadToSpline/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def convert_quad_to_spline(self, input_scope : ScopeDefinition, quad_to_spline_params : QuadToSplineParams) -> IGAResults:
        """ Converts fully quad mesh with topology to spline with the given conversion parameters.


        Parameters
        ----------
        input_scope : ScopeDefinition
            Scope definition for input quad mesh.
        quad_to_spline_params : QuadToSplineParams
            Parameters to convert quad to spline.

        Returns
        -------
        IGAResults
            Returns the IGAResults structure.


        Notes
        -----
        This API is a Beta. API Behavior and implementation may change in future.

        Examples
        --------
        >>> results = quadToSpline.convert_quad_to_spline(input_scope, quad_to_spline_params)

        """
        if not isinstance(input_scope, ScopeDefinition):
            raise TypeError("Invalid argument type passed for input_scope, valid argument type is ScopeDefinition.")
        if not isinstance(quad_to_spline_params, QuadToSplineParams):
            raise TypeError("Invalid argument type passed for quad_to_spline_params, valid argument type is QuadToSplineParams.")
        args = {"input_scope" : input_scope._jsonify(),
        "quad_to_spline_params" : quad_to_spline_params._jsonify()}
        command_name = "PrimeMesh::QuadToSpline/ConvertQuadToSpline"
        self._model._print_beta_api_warning("convert_quad_to_spline")
        self._model._print_logs_before_command("convert_quad_to_spline", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("convert_quad_to_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)
