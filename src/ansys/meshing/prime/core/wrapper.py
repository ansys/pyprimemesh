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
)
from ansys.meshing.prime.autogen.wrapperstructs import WrapResult as WrapResult
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode


class Wrapper(_Wrapper):
    """Provides operations to generate surface mesh using wrapper technology."""

    def __init__(self, model: Model):
        """__init__(Model self, int id, int object_id, char* name)"""
        _Wrapper.__init__(self, model)
        self._model = model

    def wrap(self, wrapper_control_id: int, params: WrapParams) -> WrapResult:
        """Performs wrapping with specified controls in wrapper control and with provided
            parameters.


        Parameters
        ----------
        wrapper_control_id : int
            Id of wrapper control.
        params : WrapParams
            Wrap Parameters.

        Returns
        -------
        WrapResult
            Returns the Wrap Results.


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
        """Performs label controlled connection of wrapper part face zonelets to face zonelets of
            source parts.


        Parameters
        ----------
        wrapper_part : Part
            wrapper part.
        target_labels : List[str]
            target zonelet labels to be connected.
        source_parts : List[Part]
           source parts to be connected with.
        source_labels : List[Part]
           source zonelet labels to be connected.


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
            res = connect.intersect_face_zonelets(
                part_id=merged_part_res.merged_part_id,
                face_zonelet_ids=face_zonelet_ids,
                with_face_zonelet_ids=with_face_zonelet_ids,
                params=params,
            )
            np.append(modified_zonelets, face_zonelet_ids)
            np.append(modified_zonelets, with_face_zonelet_ids)
        surf_utils = SurfaceUtilities(self._model)
        surf_utils.resolve_intersections(
            face_zonelet_ids=modified_zonelets, params=ResolveIntersectionsParams(model=self._model)
        )

    def close_gaps(
        self, scope: ScopeDefinition, params: WrapperCloseGapsParams
    ) -> WrapperCloseGapsResult:
        """Close gaps create patching surfaces within the face zonelets specified
            by scope using gap size.


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
        result = _Wrapper.close_gaps(self, scope, params)
        if result.error_code == ErrorCode.NOERROR:
            self._model._sync_up_model()
        return result
