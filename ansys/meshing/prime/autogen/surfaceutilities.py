""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any

class SurfaceUtilities(CoreObject):
    """Performs various general surface utilities algorithms. For example, copy zonelets, resolve surface intersections.

    """

    def __init__(self, model: CommunicationManager):
        """ Initialize SurfaceUtilities """
        self._model = model
        self._comm = model._communicator
        command_name = "PrimeMesh::SurfaceUtilities/Construct"
        args = {"ModelID" : model._object_id , "MaxID" : -1 }
        result = self._comm.serve(model, command_name, args=args)
        self._object_id = result["ObjectIndex"]
        self._freeze()

    def __enter__(self):
        """ Enter context for SurfaceUtilities. """
        return self

    def __exit__(self, type, value, traceback) :
        """ Exit context for SurfaceUtilities. """
        command_name = "PrimeMesh::SurfaceUtilities/Destruct"
        self._comm.serve(self._model, command_name, self._object_id, args={})

    def get_bounding_box_of_zonelets(self, zonelets : Iterable[int]) -> BoundingBox:
        """ Gets bounding box of given zonelets.


        Parameters
        ----------
        zonelets : Iterable[int]
            Ids of zonelets.

        Returns
        -------
        BoundingBox
            Returns bounding of box of given zonelets.


        Examples
        --------
        >>> zonelets = part.get_face_zonelets() + part.get_edge_zonelets()
        >>> bounding_box = surface_utilities.get_bounding_box_of_zonelets(zonelets)

        """
        args = {"zonelets" : zonelets}
        command_name = "PrimeMesh::SurfaceUtilities/GetBoundingBoxOfZonelets"
        self._model._print_logs_before_command("get_bounding_box_of_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_bounding_box_of_zonelets", BoundingBox(model = self._model, json_data = result))
        return BoundingBox(model = self._model, json_data = result)

    def fill_holes_at_plane(self, part_id : int, face_zonelets : Iterable[int], plane_points : Iterable[float], params : FillHolesAtPlaneParams) -> FillHolesAtPlaneResults:
        """ Fills holes in given face zonelets at given plane.


        Parameters
        ----------
        part_id : int
            Id of part to associate face zonelets created to fill hole.
        face_zonelets : Iterable[int]
            Ids of face zonelets to be used to find holes.
        plane_points : Iterable[float]
            Coordinates of three points to define plane.
        params : FillHolesAtPlaneParams
            Parameters to fill holes.

        Returns
        -------
        FillHolesAtPlaneResults
            Returns the FillHolesAtPlaneResults.


        Examples
        --------
        >>> params = prime.FillHolesAtPlaneParams(model = model)
        >>> results = surface_utils.fill_holes_at_plane(part_id, face_zonelets, plane_points, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "plane_points" : plane_points,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/FillHolesAtPlane"
        self._model._print_logs_before_command("fill_holes_at_plane", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("fill_holes_at_plane", FillHolesAtPlaneResults(model = self._model, json_data = result))
        return FillHolesAtPlaneResults(model = self._model, json_data = result)

    def delete_unwetted_surfaces(self, face_zonelet_ids : Iterable[int], live_material_point_names : List[str], params : DeleteUnwettedParams) -> DeleteUnwettedResult:
        """ Deletes unwetted surfaces based on material point list.


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            Ids of face zonelets.
        live_material_point_names : List[str]
            Names of material points.
        params : DeleteUnwettedParams
            DeleteUnwettedParams to define material points.

        Returns
        -------
        DeleteUnwettedResult
            Returns a DeleteUnwettedResult.


        Examples
        --------
        >>> result = surf_utils.delete_unwetted_surfaces(zonelets, live_mpt_names, prime.DeleteUnwettedParams(model))

        """
        args = {"face_zonelet_ids" : face_zonelet_ids,
        "live_material_point_names" : live_material_point_names,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/DeleteUnwettedSurfaces"
        self._model._print_logs_before_command("delete_unwetted_surfaces", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("delete_unwetted_surfaces", DeleteUnwettedResult(model = self._model, json_data = result))
        return DeleteUnwettedResult(model = self._model, json_data = result)

    def resolve_intersections(self, face_zonelet_ids : Iterable[int], params : ResolveIntersectionsParams) -> ResolveIntersectionResult:
        """ Resolves facezonelets intersections


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            Ids of face zonelets.
        params : ResolveIntersectionsParams
            ResolveIntersectionsParams for resolve intersection.

        Returns
        -------
        ResolveIntersectionResult
            Returns a ResolveIntersectionResult.


        Examples
        --------
        >>> result = surf_utils.resolve_intersections(zonelets, prime.ResolveIntersectionsParams(model))

        """
        args = {"face_zonelet_ids" : face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/ResolveIntersections"
        self._model._print_logs_before_command("resolve_intersections", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("resolve_intersections", ResolveIntersectionResult(model = self._model, json_data = result))
        return ResolveIntersectionResult(model = self._model, json_data = result)

    def subtract_zonelets(self, part_id : int, zonelets : Iterable[int], cutters : List[PartZonelets], params : SubtractZoneletsParams) -> SubtractZoneletsResults:
        """ Does a boolean subtract operation of cutter zonelets from specified input face zonelets. It is expected that input zonelets form a non-self intersecting, watertight volume. Each set of cutter zonelets should be non self-intersecting. If the cutters are also watertight, this function will always succeed.


        Parameters
        ----------
        part_id : int
            Id of input part.
        zonelets : Iterable[int]
            List of input face zonelet ids.
        cutters : PartZoneletsArray
            Collection of face zonelet ids used to remove material from the input zonelets.
        params : SubtractZoneletsParams
            Parameters to control the subtract operation.

        Returns
        -------
        SubtractZoneletsResults
            Returns a SubtractZoneletsResults.


        Examples
        --------
        >>> result = surf_utils.subtract_zonelets(part_id, zonelet_id, cutters, params)

        """
        args = {"part_id" : part_id,
        "zonelets" : zonelets,
        "cutters" : [p._jsonify() for p in cutters],
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/SubtractZonelets"
        self._model._print_logs_before_command("subtract_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("subtract_zonelets", SubtractZoneletsResults(model = self._model, json_data = result))
        return SubtractZoneletsResults(model = self._model, json_data = result)
