# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
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

"""Tests for the fast render-data build path."""

from types import SimpleNamespace

import numpy as np

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    CONNECTIVITY_PART_CHUNK_SIZE,
    _facet_edge_lines,
    _get_face_and_edge_connectivity,
    _triangulate_wide_cells,
    build_edge_render_batches,
    build_element_edge_batches,
    build_face_render_batches,
)


def test_wide_cells_are_triangulated_without_vtk_objects():
    """Wide polygons are fan-triangulated while quads remain unchanged."""
    block = np.array([5, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8], dtype=np.int64)

    triangulated, n_cells = _triangulate_wide_cells(block, 2)

    assert n_cells == 4
    assert triangulated.tolist() == [
        3,
        0,
        1,
        2,
        3,
        0,
        2,
        3,
        3,
        0,
        3,
        4,
        4,
        5,
        6,
        7,
        8,
    ]
    lines, n_lines = _facet_edge_lines(block, 2, 9)
    assert n_lines == 9
    assert lines.shape == (9, 3)


def test_connectivity_requests_are_chunked_and_combined():
    """Large part lists use bounded RPCs while preserving result order."""

    class FakeMesh:
        def __init__(self):
            self.calls = []

        def get_face_and_edge_connectivity(self, part_ids, params):
            self.calls.append((part_ids, params))
            return SimpleNamespace(
                part_ids=part_ids,
                face_connectivity_result_per_part=[f"face-{part_id}" for part_id in part_ids],
                edge_connectivity_result_per_part=[f"edge-{part_id}" for part_id in part_ids],
            )

    fake = FakeMesh()
    params = object()
    part_ids = list(range(CONNECTIVITY_PART_CHUNK_SIZE + 1))

    result = _get_face_and_edge_connectivity(fake, part_ids, params)

    assert [len(call[0]) for call in fake.calls] == [CONNECTIVITY_PART_CHUNK_SIZE, 1]
    assert all(call[1] is params for call in fake.calls)
    assert result.part_ids == part_ids
    assert result.face_connectivity_result_per_part[-1] == f"face-{part_ids[-1]}"
    assert result.edge_connectivity_result_per_part[-1] == f"edge-{part_ids[-1]}"


def _legacy_model_batches(model_pd):
    """Build legacy merged geometry across all parts."""
    face_entries = []
    edge_entries = []
    for part_data in model_pd.values():
        face_entries.extend(entry for entry in part_data.get("faces", []) if entry is not None)
        edge_entries.extend(entry for entry in part_data.get("edges", []) if entry is not None)
    return {
        "faces": build_face_render_batches(face_entries),
        "edges": build_edge_render_batches(edge_entries),
        "element_edges": build_element_edge_batches(face_entries),
    }


def test_build_render_data_matches_legacy_merge(get_remote_client):
    """The fast path produces the same merged geometry as the per-entity path."""
    model = get_remote_client.model
    mesh_util = prime.lucid.Mesh(model)
    mesh_util.read(prime.examples.download_wheel_ground_fmd())

    model_pd = model.as_polydata(update=True)
    render_data = model.build_render_data(update=True)
    legacy = _legacy_model_batches(model_pd)

    for key in ("faces", "edges", "element_edges"):
        legacy_cells = sum(batch.mesh.n_cells for batch in legacy[key].values())
        fast_cells = sum(batch.mesh.n_cells for batch in render_data.batches[key].values())
        assert legacy_cells == fast_cells
