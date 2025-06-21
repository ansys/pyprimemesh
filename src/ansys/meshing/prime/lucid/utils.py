# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Util functions for lucid modules."""
import re
import ansys.meshing.prime as prime


def match_pattern(pattern: str, name: str) -> bool:
    """Pattern matching function for strings.

    Parameters
    ----------
    pattern : str
        Pattern you are looking for in the string.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if the pattern is found.
    """
    pattern = "^" + pattern.replace("*", ".*").replace("?", ".") + "$"
    x = re.search(pattern, name)
    if x:
        return True
    else:
        return False


def check_name_pattern(name_patterns: str, name: str) -> bool:
    """Check several patterns in one string.

    Parameters
    ----------
    name_patterns : str
        Patterns to check, separated by commas.
        If pattern starts with !, it shouldn't be found.
    name : str
        String where you look for patterns.

    Returns
    -------
    bool
        True if all found.
    """
    patterns = []
    a = name_patterns.split(",")
    for aa in a:
        patterns.append(aa)

    for pattern in patterns:
        bb = pattern.split("!")
        if match_pattern(bb[0].strip(), name):
            if len(bb) > 1:
                nv = False
                for nvbb in bb[1:]:
                    if match_pattern(nvbb.strip(), name):
                        nv = True
                        break
                if not nv:
                    return True
            else:
                return True

    return False

class SummaryResults():
    def __init__(self,
                 summary: prime.PartSummaryResults=None,
                 vol_quality: prime.VolumeQualitySummaryResults=None,
                 surf_quality: prime.SurfaceQualitySummaryResults=None):
        self._summary = summary
        self._vol_quality_result = vol_quality.quality_results_part[0]
        self._surf_quality_result = surf_quality.quality_results[0]

class Utility():
    def __init__(self, model: prime.Model):
        self._model = model
    
    def print_topology(self, part_name: str, indent=''):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            print(indent + "Invalid part - " + part_name)
        else:
            summary = part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))
            print(indent + 'Topology')
            print(indent + '\tn_topo_edges         : %d' % summary.n_topo_edges)
            print(indent + '\tn_topo_faces         : %d' % summary.n_topo_faces)
            print(indent + '\tn_topo_volumes       : %d' % summary.n_topo_volumes)
            print(indent + '\tn_unmeshed_topo_faces: %d' % summary.n_unmeshed_topo_faces)
    
    def print_zones(self, part_name: str, indent=''):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            print(indent + "Invalid part - " + part_name)
        else:
            summary = part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))
            print(indent + 'Zones\n')
            print(indent + '\tn_edge_zones  : %d' % summary.n_edge_zones)
            print(indent + '\tn_face_zones  : %d' % summary.n_face_zones)
            faceZone_ids = part.get_face_zones()
            for id in faceZone_ids:
                print(indent + '\t\t%s' % self._model.get_zone_name(id))
            print(indent + '\tn_volume_zones: %d' % summary.n_volume_zones)
            volZone_ids = part.get_volume_zones()
            for id in volZone_ids:
                print(indent + '\t\t%s' % self._model.get_zone_name(id))
    
    def print_zonelets(self, part_name: str, indent=''):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            print(indent + "Invalid part - " + part_name)
        else:
            summary = part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))
            print(indent + 'Zonelets\n')
            print(indent + '\tn_edge_zonelets: %d' % summary.n_edge_zonelets)
            print(indent + '\tn_face_zonelets: %d' % summary.n_face_zonelets)
            print(indent + '\tn_cell_zonelets: %d' % summary.n_cell_zonelets)

    def print_mesh_summary(self, part_name: str, indent=''):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            print(indent + "Invalid part - " + part_name)
        else:
            summary = part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))
            print(indent + 'Mesh summary')
            print(indent + '\tn_nodes: %d' % summary.n_nodes)
            print(indent + '\tn_faces: %d' % summary.n_faces)
            print(indent + '\t\tn_tri_faces  : %d' % summary.n_tri_faces)
            print(indent + '\t\tn_quad_faces : %d' % summary.n_quad_faces)
            print(indent + '\t\tn_poly_faces : %d' % summary.n_poly_faces)
            print(indent + '\tn_cells: %d' % summary.n_cells)
            print(indent + '\t\tn_poly_cells : %d' % summary.n_poly_cells)
            print(indent + '\t\tn_hex_cells  : %d' % summary.n_hex_cells)
            print(indent + '\t\tn_prism_cells: %d' % summary.n_prism_cells)
            print(indent + '\t\tn_pyra_cells : %d' % summary.n_pyra_cells)
            print(indent + '\t\tn_tet_cells  : %d' % summary.n_tet_cells)

    def get_labels(self, part_name: str):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            return []
        else:
            return part.get_labels()

    def print_labels(self, part_name: str, indent=''):
        labels = self.get_labels(part_name)
        if len(labels) > 0:
            print(indent + 'Labels: %d' % len(labels))
            for label in labels:
                print(indent + '\t%s' % label)

    def get_summary(self, part_name: str, print_summary=True):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            return None
        else:
            if print_summary is True:
                self.print_summary(part_name)
            return part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))

    def get_all_parts_summary(self, printSummary=True):
        parts = self._model.parts
        for part in parts:
            if printSummary is True:
                self.print_summary(part.get_name())
            return part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))

    def print_summary(self, part_name: str):
        part = self._model.get_part_by_name(part_name)
        if part is None:
            print("Invalid part - " + part_name)
        else:
            self.print_topology(part_name)
            self.print_zones(part_name)
            self.print_zonelets(part_name)
            self.print_labels(part_name)
            self.print_mesh_summary(part_name)

    def get_volume_quality_summary(self, cell_quality_measure: prime.CellQualityMeasure, quality_limit: float):
        vol_quality = prime.VolumeSearch(self._model)
        vol_quality_summary_params = prime.VolumeQualitySummaryParams(self._model)
        vol_quality_summary_params.cell_quality_measures = [cell_quality_measure]
        vol_quality_summary_params.quality_limit = [quality_limit]
        return vol_quality.get_volume_quality_summary(vol_quality_summary_params)

    def get_surface_quality_summary(self, part_name: str, face_quality_measure: prime.FaceQualityMeasure, quality_limit: float):
        surf_quality = prime.SurfaceSearch(self._model)
        surf_quality_summary_params = prime.SurfaceQualitySummaryParams(self._model)
        surf_quality_summary_params.face_quality_measures = [face_quality_measure]
        surf_quality_summary_params.quality_limit = [quality_limit]
        if part_name is not None:
            surf_quality_summary_params.scope = prime.ScopeDefinition(model=self._model, part_expression=part_name)
        else:
            surf_quality_summary_params.scope = prime.ScopeDefinition(model=self._model, part_expression="*")
        return surf_quality.get_surface_quality_summary(surf_quality_summary_params)

    def get_all_summary_for_part(self,
                                 part_name: str,
                                 cell_quality_measure=prime.CellQualityMeasure.SKEWNESS,
                                 cell_quality_limit=0.6, face_quality_measure=prime.FaceQualityMeasure.SKEWNESS,
                                 face_quality_limit=0.9,
                                 print_summary=True) -> SummaryResults:
        part_summary = self.get_summary(part_name, print_summary=print_summary)
        vol_summary = self.get_volume_quality_summary(cell_quality_measure=cell_quality_measure, quality_limit=cell_quality_limit)
        surf_summary = self.get_surface_quality_summary(part_name=part_name, face_quality_measure=face_quality_measure, quality_limit=face_quality_limit)
        all_summary = SummaryResults(part_summary, vol_summary, surf_summary)
        if print_summary is True:
            print('Volume quality')
            if all_summary._vol_quality_result.n_found > 0:
                print('\tn_found    : %d' % all_summary._vol_quality_result.n_found)
            print('\tmin_quality: %f' % all_summary._vol_quality_result.min_quality)
            print('\tmax_quality: %f' % all_summary._vol_quality_result.max_quality)
            print('Surface quality')
            if all_summary._surf_quality_result.n_found > 0:
                print('\tn_found    : %d' % all_summary._surf_quality_result.n_found)
            print('\tmin_quality: %f' % all_summary._surf_quality_result.min_quality)
            print('\tmax_quality: %f' % all_summary._surf_quality_result.max_quality)
        return all_summary
'''
class PartValidator():
    def __init__(self, model: prime.Model, part_name: str):
        self._model = model
        self._part = model.get_part_by_name(part_name)
        self._partSummary = self._part.get_summary(prime.PartSummaryParams(model = self._model, print_id = False, print_mesh = True))
    
    def ValidateTopology(self, n_topo_edges: int, n_topo_faces: int, n_topo_volumes):
        TestScenario.validateNumber("No. of topo edges", self._partSummary.n_topo_edges, n_topo_edges, 0)
        TestScenario.validateNumber("No. of topo faces", self._partSummary.n_topo_faces, n_topo_faces, 0)
        TestScenario.validateNumber("No. of topo volumes", self._partSummary.n_topo_volumes, n_topo_volumes, 0)

    def ValidateMesh(self, n_nodes: int, n_faces: int, n_cells: int):
        TestScenario.validateNumber("No. of nodes", self._partSummary.n_nodes, n_nodes, 0)
        TestScenario.validateNumber("No. of faces", self._partSummary.n_faces, n_faces, 0)
        TestScenario.validateNumber("No. of cells", self._partSummary.n_cells, n_cells, 0)
'''