""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class BoundaryFittedSpline(CoreObject):
    """

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize BoundaryFittedSpline """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::BoundaryFittedSpline/Construct"
        args = {"ModelID" : model.object_id , "MaxID" : -1 }
        result = self._comm.serve(command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for BoundaryFittedSpline """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for BoundaryFittedSpline """
        command_name = "PrimeMesh::BoundaryFittedSpline/Destruct"
        self._comm.serve(command_name, self.object_id, args={})

    def create_boundary_fitted_spline(self, part_id : int, cell_zonelet_ids : List[int], boundary_fitted_spline_params : BoundaryFittedSplineParams) -> IGAResults:
        """ Create boundary fitted spline for structured hex-mesh.

        Create boundary fitted spline for structured hex-mesh.
        The hex-mesh could be structured in blocks but must be conformally connected i.e. each block must be six sided volume and must be connected to other blocks via a unique face.
        The degree and number of control points of the spline can be set in the fitting parameter structure.

        Parameters
        ----------
        part_id : int
            Id of the part.
        cell_zonelet_ids : List[int]
            Ids of the cell zonelets on which spline will be fit.
        boundary_fitted_spline_params : BoundaryFittedSplineParams
            Structure containing spline fitting parameters.

        Returns
        -------
        IGAResults
            Returns the IGAResults Structure.


        Examples
        --------
        >>> from ansys.meshing.prime import BoundaryFittedSpline
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> boundary_fitted_spline = BoundaryFittedSpline(model = model)
        >>> results = boundary_fitted_spline.create_boundary_fitted_spline(part_id, cell_zonelet_ids, boundary_fitted_spline_params)

        """
        args = {"part_id" : part_id,
        "cell_zonelet_ids" : cell_zonelet_ids,
        "boundary_fitted_spline_params" : boundary_fitted_spline_params.jsonify()}
        command_name = "PrimeMesh::BoundaryFittedSpline/CreateBoundaryFittedSpline"
        self._model._print_logs_before_command("create_boundary_fitted_spline", args)
        result = self._comm.serve(command_name, self.object_id, args=args)
        self._model._print_logs_after_command("create_boundary_fitted_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)

    def refine_spline(self, part_id : int, spline_ids : List[int], refine_spline_params : RefineSplineParams) -> IGAResults:
        """ Refine boundary fitted splines.

        Refine boundary fitted splines. Currently h and p refinement are supported.
        Refinement along one or more dimension can be suppressed using refinement parameters in the input.

        Parameters
        ----------
        part_id : int
            Id of the part.
        spline_ids : List[int]
            Ids of the splines on which refinement will be done.
        refine_spline_params : RefineSplineParams
            Structure containing parameters for spline refinement.

        Returns
        -------
        IGAResults
            Returns the IGAResults Structure.


        Examples
        --------
        >>> from ansys.meshing.prime import BoundaryFittedSpline
        >>> #connect client to server and get model from it
        >>> client = Client(ip="localhost", port=50060)
        >>> model = client.model
        >>> boundary_fitted_spline = BoundaryFittedSpline(model = model)
        >>> results = boundary_fitted_spline.refine_spline(part_id, spline_ids, refine_spline_params)

        """
        args = {"part_id" : part_id,
        "spline_ids" : spline_ids,
        "refine_spline_params" : refine_spline_params.jsonify()}
        command_name = "PrimeMesh::BoundaryFittedSpline/RefineSpline"
        self._model._print_logs_before_command("refine_spline", args)
        result = self._comm.serve(command_name, self.object_id, args=args)
        self._model._print_logs_after_command("refine_spline", IGAResults(model = self._model, json_data = result))
        return IGAResults(model = self._model, json_data = result)

    @property
    def object_id(self):
        """ Object id of BoundaryFittedSpline """
        return self._object_id
