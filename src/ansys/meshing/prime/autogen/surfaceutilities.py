""" Auto-generated file. DO NOT MODIFY """
from __future__ import annotations
from ansys.meshing.prime.internals.comm_manager import CommunicationManager
from ansys.meshing.prime.params.primestructs import *
from ansys.meshing.prime.autogen.coreobject import *
from typing import List, Any, Union

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

    def copy_face_zonelets(self, face_zonelets : Iterable[int], target_part_id : int, params : CopyZoneletsParams) -> CopyZoneletsResults:
        """ Copy face zonelets.


        Parameters
        ----------
        face_zonelets : Iterable[int]
            Ids of face zonelets to be copied.
        target_part_id : int
            Part id to be used to move the copied zonelets.
        params : CopyZoneletsParams
            Parameters to copy face zonelets.

        Returns
        -------
        CopyZoneletsResults
            Returns the CopyZoneletsResults.


        Examples
        --------
        >>>> surfaceutil = SurfaceUtilities(model = model)
        >>>> surfaceutil = surfaceutil.copy_face_zonelets(face_zonelets, target_part_id = new_part.id, prime.CopyZoneletsParams(model = model))

        """
        args = {"face_zonelets" : face_zonelets,
        "target_part_id" : target_part_id,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/CopyFaceZonelets"
        self._model._print_logs_before_command("copy_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("copy_face_zonelets", CopyZoneletsResults(model = self._model, json_data = result))
        return CopyZoneletsResults(model = self._model, json_data = result)

    def fill_holes_at_plane(self, part_id : int, face_zonelets : Iterable[int], plane_points : Iterable[float], params : FillHolesAtPlaneParams) -> FillHolesAtPlaneResults:
        """ Fill holes in given face zonelets at given plane.


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
            Return the FillHolesAtPlaneResults.


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

    def create_cap_on_face_zonelets(self, part_id : int, face_zonelets : Iterable[int], params : CreateCapParams) -> CreateCapResults:
        """ Create caps on the given face zonelets.


        Parameters
        ----------
        part_id : int
            Id of part to associate face zonelets created to cap.
        face_zonelets : Iterable[int]
            Ids of face zonelets to be used to find caps.
        params : CreateCapParams
            Parameters to create caps.

        Returns
        -------
        CreateCapResults
            Returns the CreateCapResults.


        Examples
        --------
        >>> params = prime.CreateCapParams(model = model)
        >>> results = surface_utils.cap_face_zonelets(part_id, face_zonelets, params)

        """
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/CreateCapOnFaceZonelets"
        self._model._print_logs_before_command("create_cap_on_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_cap_on_face_zonelets", CreateCapResults(model = self._model, json_data = result))
        return CreateCapResults(model = self._model, json_data = result)

    def delete_unwetted_surfaces(self, face_zonelet_ids : Iterable[int], live_material_point_names : List[str], params : DeleteUnwettedParams) -> DeleteUnwettedResult:
        """ Delete unwetted surfaces based on material point list.


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
            Return a DeleteUnwettedResult.


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
        """ Resolve facezonelets intersections.


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            Ids of face zonelets.
        params : ResolveIntersectionsParams
            ResolveIntersectionsParams for resolve intersection.

        Returns
        -------
        ResolveIntersectionResult
            Return a ResolveIntersectionResult.


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

    def smooth_dihedral_face_nodes(self, zonelets : Iterable[int], params : SmoothDihedralFaceNodesParams) -> SmoothDihedralFaceNodesResults:
        """ Performs a smoothing operation to eliminate sharp corners at locations where the input face zonelets intersect.


        Parameters
        ----------
        zonelets : Iterable[int]
            List of input face zonelet ids.
        params : SmoothDihedralFaceNodesParams
            Parameters to control the smoothing operation.

        Returns
        -------
        SmoothDihedralFaceNodesResults
            Return a SmoothDihedralFaceNodesResults.


        Examples
        --------
        >>> result = surf_utils.smooth_dihedral_face_nodes(zonelets, params)

        """
        args = {"zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/SmoothDihedralFaceNodes"
        self._model._print_logs_before_command("smooth_dihedral_face_nodes", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("smooth_dihedral_face_nodes", SmoothDihedralFaceNodesResults(model = self._model, json_data = result))
        return SmoothDihedralFaceNodesResults(model = self._model, json_data = result)

    def refine_at_contacts(self, part_ids : Iterable[int], params : RefineAtContactsParams) -> RefineAtContactsResults:
        """ Refine face elements in contact with other parts.


        Parameters
        ----------
        part_ids : Iterable[int]
            Input part ids.
        params : RefineAtContactsParams
            Parameters to refine at contacts.

        Returns
        -------
        RefineAtContactsResults
            Returns the RefineAtContactsResults.


        Examples
        --------
        >>> params = prime.RefineAtContactsParams(model = model)
        >>> result = surf_utils.refine_at_contacts(part_ids, params)

        """
        args = {"part_ids" : part_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/RefineAtContacts"
        self._model._print_logs_before_command("refine_at_contacts", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("refine_at_contacts", RefineAtContactsResults(model = self._model, json_data = result))
        return RefineAtContactsResults(model = self._model, json_data = result)

    def add_thickness(self, zonelets : Iterable[int], params : AddThicknessParams) -> AddThicknessResults:
        """ Adds thickness to the selected list of face zonelet ids.


        Parameters
        ----------
        zonelets : Iterable[int]
            List of input face zonelet ids.
        params : AddThicknessParams
            Parameters to control the add thickness operation.

        Returns
        -------
        AddThicknessResults
            Returns the AddThicknessResults.


        Examples
        --------
        >>> result = surf_utils.add_thickness(zonelets, params)

        """
        args = {"zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/AddThickness"
        self._model._print_logs_before_command("add_thickness", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_thickness", AddThicknessResults(model = self._model, json_data = result))
        return AddThicknessResults(model = self._model, json_data = result)
