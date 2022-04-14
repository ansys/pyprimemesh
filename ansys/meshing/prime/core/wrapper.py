from ansys.meshing.prime.autogen.wrapper import Wrapper as _Wrapper
from ansys.meshing.prime.autogen.wrapperstructs import WrapParams as WrapParams
from ansys.meshing.prime.autogen.wrapperstructs import WrapResult as WrapResult
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.core.part import Part
from ansys.meshing.prime.autogen.partstructs import NamePatternParams
from ansys.meshing.prime.autogen.connectstructs import IntersectParams
from ansys.meshing.prime.autogen.connect import Connect
from ansys.meshing.prime.autogen.surfaceutilities import SurfaceUtilities
from ansys.meshing.prime.autogen.surfaceutilitystructs import ResolveIntersectionsParams
from ansys.meshing.prime.params.primestructs import ErrorCode as ErrorCode
from typing import List
import numpy as np

class Wrapper(_Wrapper):
    """Provides operations to generate surface mesh using wrapper technology.

    """
    def __init__(self, model: Model):
        """ __init__(Model self, int id, int object_id, char* name)"""
        _Wrapper.__init__(self, model)
        self._model = model

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
            Returns the Wrap Results.


        Examples
        --------
        >>> results = wrapper.wrap(wrapper_control_id, params)

        """
        result = _Wrapper.wrap(self, wrapper_control_id, params)
        if (result.error_code == ErrorCode.NOERROR):
            self._model._sync_up_model()
        return result

    def connect(self, wrapper_part : Part, target_labels : List[str], source_parts : List[Part],
                source_labels : List[str]):
        """ Performs label controlled connection of wrapper part face zonelets to face zonelets of
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
        modified_zonelets = np.array([], dtype=np.int32)
        for i in range(0, len(source_parts)):
            face_zonelet_ids = wrapper_part.get_face_zonelets_of_label_name_pattern(
                                 target_labels[i],
                                 name_pattern_params=NamePatternParams(self._model))
            with_face_zonelet_ids = source_parts[i].get_face_zonelets_of_label_name_pattern(
                                     source_labels[i],
                                     name_pattern_params=NamePatternParams(self._model))
            #merge the box and wrap and then use below
            source_parts[i].add_labels_on_zonelets([source_parts[i].get_name()],
                                                  source_parts[i].get_face_zonelets())
            wrapper_part.merge_into([source_parts[i].id])
            if len(with_face_zonelet_ids) > 0 and len(face_zonelet_ids) > 0 :
                #intersect
                connect = Connect(self._model)
                params = IntersectParams(model = self._model)
                res = connect.intersect_face_zonelets(part_id=wrapper_part.id,
                                                      face_zonelet_ids=face_zonelet_ids,
                                                      with_face_zonelet_ids=with_face_zonelet_ids,
                                                      params=params)
                np.append(modified_zonelets, face_zonelet_ids)
                np.append(modified_zonelets, with_face_zonelet_ids)
        surf_utils = SurfaceUtilities(self._model)
        surf_utils.resolve_intersections(face_zonelet_ids=modified_zonelets,
                                         params=ResolveIntersectionsParams(model=self._model))
