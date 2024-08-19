# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

"""Module for helper macros."""

import re

from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.communicator import call_method


def _get_part_ids(model: prime.Model, part_scope):
    args = {"part_name_pattern": part_scope, "name_pattern_params": {}}
    command_name = "PrimeMesh::Model/GetPartIdsOfNamePattern"
    part_ids = call_method(model, command_name, model._object_id, args=args)
    return part_ids


def _get_topo_faces(model: prime.Model):
    topo_data = model.topo_data
    return call_method(model, "PrimeMesh::TopoData/GetTopoFaces", topo_data._object_id, {})


def _get_topo_nodes(model: prime.Model):
    topo_data = model.topo_data
    return call_method(model, "PrimeMesh::TopoData/GetTopoNodes", topo_data._object_id, {})


def _get_interior_topoedges_of_topoface(model: prime.Model, topo_face: int):
    topo_data = model.topo_data
    args = {"topo_face": topo_face}
    command_name = "PrimeMesh::TopoData/GetInteriorTopoEdgesOfTopoFace"
    return call_method(model, command_name, topo_data._object_id, args)


def _check_size_control_scope(
    model: prime.Model,
    part_id: int,
    entity_type: str,
    entity_scope: str,
    scope_evaluation_type: str,
):
    if entity_scope == "*":
        return True
    part = model.get_part(part_id)
    name_pattern_params = prime.NamePatternParams(model)
    face_zonelets = []
    edge_zonelets = []
    if entity_type == "face" or entity_type == "face_and_edge":
        if scope_evaluation_type == "labels":
            face_zonelets = part.get_face_zonelets_of_label_name_pattern(
                entity_scope, name_pattern_params
            )
        elif scope_evaluation_type == "zones":
            face_zonelets = part.get_face_zonelets_of_zone_name_pattern(
                entity_scope, name_pattern_params
            )
    if entity_type == "edge" or entity_type == "face_and_edge":
        if scope_evaluation_type == "labels":
            edge_zonelets = part.get_edge_zonelets_of_label_name_pattern(
                entity_scope, name_pattern_params
            )
    if len(face_zonelets) > 0 or len(edge_zonelets) > 0:
        return True

    return False


def _check_pattern(val: str, pattern: str):
    pattern = "^" + pattern.replace("*", ".*") + "$"
    x = re.search(pattern, val)
    if x:
        return True
    else:
        return False


def check_name_pattern(name: str, name_pattern: str):
    """Checks name pattern."""
    name_pattern = name_pattern.replace(",", " ")
    patterns = name_pattern.split(" ")
    found = False
    for pattern in patterns:
        if pattern.startswith("!"):
            if _check_pattern(name, pattern[1:]):
                return False
            else:
                found = True
        elif not found:
            found = _check_pattern(name, pattern)
    return found
