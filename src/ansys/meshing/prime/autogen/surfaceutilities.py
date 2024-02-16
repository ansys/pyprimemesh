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
        """ Get bounding box of given zonelets.


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
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for zonelets, valid argument type is Iterable[int].")
        args = {"zonelets" : zonelets}
        command_name = "PrimeMesh::SurfaceUtilities/GetBoundingBoxOfZonelets"
        self._model._print_logs_before_command("get_bounding_box_of_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("get_bounding_box_of_zonelets", BoundingBox(model = self._model, json_data = result))
        return BoundingBox(model = self._model, json_data = result)

    def fix_invalid_normal_nodes_of_face_zonelets(self, part_id : int, face_zonelets : Iterable[int], params : FixInvalidNormalNodeParams) -> FixInvalidNormalNodeResults:
        """ Create nuggets to fix invalid normal at nodes of the given face zonelets.


        Parameters
        ----------
        part_id : int
            Part id of the given face zonelets. Nuggets created are associated to the given part.
        face_zonelets : Iterable[int]
            Ids of face zonelets used to find invalid normal nodes.
        params : FixInvalidNormalNodeParams
            Parameters to find invalid normal nodes and fix them.

        Returns
        -------
        FixInvalidNormalNodeResults
            Returns the FixInvalidNormalNodeResults.


        Examples
        --------
        >>> params = prime.FixInvalidNormalNodeParams(model = model)
        >>> results = surface_utils.fix_invalid_normal_nodes_of_face_zonelets(part_id, face_zonelets, params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, FixInvalidNormalNodeParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is FixInvalidNormalNodeParams.")
        args = {"part_id" : part_id,
        "face_zonelets" : face_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/FixInvalidNormalNodesOfFaceZonelets"
        self._model._print_logs_before_command("fix_invalid_normal_nodes_of_face_zonelets", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("fix_invalid_normal_nodes_of_face_zonelets", FixInvalidNormalNodeResults(model = self._model, json_data = result))
        return FixInvalidNormalNodeResults(model = self._model, json_data = result)

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
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(target_part_id, int):
            raise TypeError("Invalid argument type passed for target_part_id, valid argument type is int.")
        if not isinstance(params, CopyZoneletsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CopyZoneletsParams.")
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
            Returns the FillHolesAtPlaneResults.


        Examples
        --------
        >>> params = prime.FillHolesAtPlaneParams(model = model)
        >>> results = surface_utils.fill_holes_at_plane(part_id, face_zonelets, plane_points, params)

        """
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(plane_points, Iterable):
            raise TypeError("Invalid argument type passed for plane_points, valid argument type is Iterable[float].")
        if not isinstance(params, FillHolesAtPlaneParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is FillHolesAtPlaneParams.")
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
        if not isinstance(part_id, int):
            raise TypeError("Invalid argument type passed for part_id, valid argument type is int.")
        if not isinstance(face_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, CreateCapParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CreateCapParams.")
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
            Returns a DeleteUnwettedResult.


        Examples
        --------
        >>> result = surf_utils.delete_unwetted_surfaces(zonelets, live_mpt_names, prime.DeleteUnwettedParams(model))

        """
        if not isinstance(face_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelet_ids, valid argument type is Iterable[int].")
        if not isinstance(live_material_point_names, List):
            raise TypeError("Invalid argument type passed for live_material_point_names, valid argument type is List[str].")
        if not isinstance(params, DeleteUnwettedParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is DeleteUnwettedParams.")
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
            Returns a ResolveIntersectionResult.


        Examples
        --------
        >>> result = surf_utils.resolve_intersections(zonelets, prime.ResolveIntersectionsParams(model))

        """
        if not isinstance(face_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelet_ids, valid argument type is Iterable[int].")
        if not isinstance(params, ResolveIntersectionsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is ResolveIntersectionsParams.")
        args = {"face_zonelet_ids" : face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/ResolveIntersections"
        self._model._print_logs_before_command("resolve_intersections", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("resolve_intersections", ResolveIntersectionResult(model = self._model, json_data = result))
        return ResolveIntersectionResult(model = self._model, json_data = result)

    def smooth_dihedral_face_nodes(self, zonelets : Iterable[int], params : SmoothDihedralFaceNodesParams) -> SmoothDihedralFaceNodesResults:
        """ Perform a smoothing operation to eliminate sharp corners at locations where the input face zonelets intersect.


        Parameters
        ----------
        zonelets : Iterable[int]
            List of input face zonelet ids.
        params : SmoothDihedralFaceNodesParams
            Parameters to control the smoothing operation.

        Returns
        -------
        SmoothDihedralFaceNodesResults
            Returns a SmoothDihedralFaceNodesResults.


        Examples
        --------
        >>> result = surf_utils.smooth_dihedral_face_nodes(zonelets, params)

        """
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, SmoothDihedralFaceNodesParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is SmoothDihedralFaceNodesParams.")
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
        if not isinstance(part_ids, Iterable):
            raise TypeError("Invalid argument type passed for part_ids, valid argument type is Iterable[int].")
        if not isinstance(params, RefineAtContactsParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is RefineAtContactsParams.")
        args = {"part_ids" : part_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/RefineAtContacts"
        self._model._print_logs_before_command("refine_at_contacts", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("refine_at_contacts", RefineAtContactsResults(model = self._model, json_data = result))
        return RefineAtContactsResults(model = self._model, json_data = result)

    def add_thickness(self, zonelets : Iterable[int], params : AddThicknessParams) -> AddThicknessResults:
        """ Add thickness to the selected list of face zonelet ids.


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
        if not isinstance(zonelets, Iterable):
            raise TypeError("Invalid argument type passed for zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, AddThicknessParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is AddThicknessParams.")
        args = {"zonelets" : zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/AddThickness"
        self._model._print_logs_before_command("add_thickness", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("add_thickness", AddThicknessResults(model = self._model, json_data = result))
        return AddThicknessResults(model = self._model, json_data = result)

    def create_boi(self, face_zonelet_ids : Iterable[int], params : CreateBOIParams) -> CreateBOIResults:
        """ Create BOI to the selected list of face zonelet ids.


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            List of input face zonelet ids.
        params : CreateBOIParams
            Parameters to control the BOI creation operation.

        Returns
        -------
        CreateBOIResults
            Returns the BOIResults.


        Examples
        --------
        >>> result = surf_utils.create_boi(zonelets, params)

        """
        if not isinstance(face_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelet_ids, valid argument type is Iterable[int].")
        if not isinstance(params, CreateBOIParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CreateBOIParams.")
        args = {"face_zonelet_ids" : face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/CreateBOI"
        self._model._print_logs_before_command("create_boi", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_boi", CreateBOIResults(model = self._model, json_data = result))
        return CreateBOIResults(model = self._model, json_data = result)

    def create_contact_patch(self, source_zonelets : Iterable[int], target_zonelets : Iterable[int], params : CreateContactPatchParams) -> CreateContactPatchResults:
        """ Create contact patch by offsetting the target zonelets.


        Parameters
        ----------
        source_zonelets : Iterable[int]
            Source face zonelet ids.
        target_zonelets : Iterable[int]
            Target face zonelet ids.
        params : CreateContactPatchParams
            Parameters to control the contact patch creation operation.

        Returns
        -------
        CreateContactPatchResults
            Returns the CreateContactPatchResults.


        Examples
        --------
        >>> result = surf_utils.create_contact_patch(zonelets, params)

        """
        if not isinstance(source_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for source_zonelets, valid argument type is Iterable[int].")
        if not isinstance(target_zonelets, Iterable):
            raise TypeError("Invalid argument type passed for target_zonelets, valid argument type is Iterable[int].")
        if not isinstance(params, CreateContactPatchParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is CreateContactPatchParams.")
        args = {"source_zonelets" : source_zonelets,
        "target_zonelets" : target_zonelets,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/CreateContactPatch"
        self._model._print_logs_before_command("create_contact_patch", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("create_contact_patch", CreateContactPatchResults(model = self._model, json_data = result))
        return CreateContactPatchResults(model = self._model, json_data = result)

    def stretch_free_boundaries(self, face_zonelet_ids : Iterable[int], params : StretchFreeBoundariesParams) -> StretchFreeBoundariesResults:
        """ Stretch free boundaries of each zonelet.


        Parameters
        ----------
        face_zonelet_ids : Iterable[int]
            Ids of face zonelets.
        params : StretchFreeBoundariesParams
            Parameters to control stretch free boundaries operation.

        Returns
        -------
        StretchFreeBoundariesResults
            Returns the StretchFreeBoundariesResults.


        Examples
        --------
        >>> result = surf_utils.stretch_free_boundaries(face_zonelet_ids, params)

        """
        if not isinstance(face_zonelet_ids, Iterable):
            raise TypeError("Invalid argument type passed for face_zonelet_ids, valid argument type is Iterable[int].")
        if not isinstance(params, StretchFreeBoundariesParams):
            raise TypeError("Invalid argument type passed for params, valid argument type is StretchFreeBoundariesParams.")
        args = {"face_zonelet_ids" : face_zonelet_ids,
        "params" : params._jsonify()}
        command_name = "PrimeMesh::SurfaceUtilities/StretchFreeBoundaries"
        self._model._print_logs_before_command("stretch_free_boundaries", args)
        result = self._comm.serve(self._model, command_name, self._object_id, args=args)
        self._model._print_logs_after_command("stretch_free_boundaries", StretchFreeBoundariesResults(model = self._model, json_data = result))
        return StretchFreeBoundariesResults(model = self._model, json_data = result)
