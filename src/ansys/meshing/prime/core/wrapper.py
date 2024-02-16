"""Module for the wrapper class."""
from typing import List

import numpy as np

# isort: split
from ansys.meshing.prime.autogen.wrapper import Wrapper as _Wrapper

# isort: split
from ansys.meshing.prime.autogen.connect import Connect
from ansys.meshing.prime.autogen.connectstructs import IntersectParams
from ansys.meshing.prime.autogen.controlstructs import (
    ScopeDefinition as ScopeDefinition,
)
from ansys.meshing.prime.autogen.modelstructs import MergePartsParams
from ansys.meshing.prime.autogen.partstructs import NamePatternParams
from ansys.meshing.prime.autogen.surfaceutilities import SurfaceUtilities
from ansys.meshing.prime.autogen.surfaceutilitystructs import ResolveIntersectionsParams
from ansys.meshing.prime.autogen.wrapperstructs import WrapParams as WrapParams
from ansys.meshing.prime.autogen.wrapperstructs import (
    WrapperCloseGapsParams,
    WrapperCloseGapsResult,
    WrapperPatchFlowRegionsParams,
    WrapperPatchFlowRegionsResult,
)
from ansys.meshing.prime.autogen.wrapperstructs import WrapResult as WrapResult
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode


class Wrapper(_Wrapper):
    """Provides operations for generating a surface mesh using wrapper technology.

    Parameters
    ----------
    model : Model
        Model to apply wrapping to.
    """

    def __init__(self, model: Model):
        """Initialize the wrapper and model."""
        _Wrapper.__init__(self, model)
        self._model = model

    def wrap(self, wrapper_control_id: int, params: WrapParams) -> WrapResult:
        """Perform wrapping with specified controls and given parameters.

        This method performs wrapping with specified controls in the wrapper control
        and with given parameters.


        Parameters
        ----------
        wrapper_control_id : int
            ID of the wrapper control.
        params : WrapParams
            Wrap parameters.

        Returns
        -------
        WrapResult
            Wrap results.


        Examples
        --------
        >>> results = wrapper.wrap(wrapper_control_id, params)

        """
        result = _Wrapper.wrap(self, wrapper_control_id, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._add_part(result.id)
        return result

    def connect(
        self,
        wrapper_part: Part,
        target_labels: List[str],
        source_parts: List[Part],
        source_labels: List[str],
    ):
        """Perform a label-controlled connection.

        This method performs a label-controlled connection of wrapper part face zonelets to
        face zonelets of source parts.


        Parameters
        ----------
        wrapper_part : Part
            Wrapper part.
        target_labels : List[str]
            List of target zonelet labels to connect.
        source_parts : List[Part]
           List of source parts to connect with.
        source_labels : List[Part]
           List of source zonelet labels to connect.


        Examples
        --------
        >>> wrapper.connect(wrapper_part, target_labels, source_parts, source_labels)

        """
        for i in range(0, len(source_parts)):
            source_parts[i].add_labels_on_zonelets(
                [source_parts[i].get_name()], source_parts[i].get_face_zonelets()
            )
        name_pattern_params = NamePatternParams(self._model)
        face_zonelet_ids = [
            fz
            for label in target_labels
            for fz in wrapper_part.get_face_zonelets_of_label_name_pattern(
                label, name_pattern_params=name_pattern_params
            )
        ]
        with_face_zonelet_ids = [
            fz
            for i in range(0, len(source_parts))
            for fz in source_parts[i].get_face_zonelets_of_label_name_pattern(
                source_labels[i], name_pattern_params=name_pattern_params
            )
        ]

        part_ids = [part.id for part in source_parts]
        part_ids.append(wrapper_part.id)
        merged_part_res = self._model.merge_parts(
            part_ids=part_ids,
            params=MergePartsParams(
                model=self._model, merged_part_suggested_name=wrapper_part.name
            ),
        )

        modified_zonelets = np.array([], dtype=np.int32)
        if len(with_face_zonelet_ids) > 0 and len(face_zonelet_ids) > 0:
            # intersect
            connect = Connect(self._model)
            params = IntersectParams(model=self._model)
            params.collapse_feature_angle = 179
            params.collapse_target_skewness = 0.9
            res = connect.intersect_face_zonelets(
                part_id=merged_part_res.merged_part_id,
                face_zonelet_ids=face_zonelet_ids,
                with_face_zonelet_ids=with_face_zonelet_ids,
                params=params,
            )
            modified_zonelets = np.append(modified_zonelets, face_zonelet_ids)
            modified_zonelets = np.append(modified_zonelets, with_face_zonelet_ids)
        surf_utils = SurfaceUtilities(self._model)
        surf_utils.resolve_intersections(
            face_zonelet_ids=modified_zonelets, params=ResolveIntersectionsParams(model=self._model)
        )

    def close_gaps(
        self, scope: ScopeDefinition, params: WrapperCloseGapsParams
    ) -> WrapperCloseGapsResult:
        """Close gaps.

        Closing gaps creates patching surfaces within the face zonelets specified
        by scope using gap size.


        Parameters
        ----------
        scope : ScopeDefinition
            Scope definition of the face zonelets.
        params : WrapperCloseGapsParams
            Wrapper providing close gap parameters.

        Returns
        -------
        WrapperCloseGapsResult
            Results from the wrapper for closing gaps.


        Examples
        --------
        >>> result = wrapper.close_gaps(scope, params)

        """
        result = _Wrapper.close_gaps(self, scope, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result

    def patch_flow_regions(
        self, live_material_point: str, params: WrapperPatchFlowRegionsParams
    ) -> WrapperPatchFlowRegionsResult:
        """Patch flow regions.

        Patch flow regions create patching surfaces for regions identified
        by dead regions from wrapper patch holes parameters.


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
        result = _Wrapper.patch_flow_regions(self, live_material_point, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._add_part(result.id)
        return result
