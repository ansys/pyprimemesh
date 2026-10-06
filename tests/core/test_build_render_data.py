# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Tests for the fast render-data build path."""

from types import SimpleNamespace

import numpy as np
import pytest
import pyvista as pv

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    CONNECTIVITY_PART_CHUNK_SIZE,
    _facet_edge_lines,
    _get_face_and_edge_connectivity,
    _triangulate_polygon_block,
    build_edge_render_batches,
    build_element_edge_batches,
    build_face_render_batches,
)


def test_facet_edges_follow_polygon_sides_without_vtk_objects():
    """Outlines come from the polygon sides themselves, deduplicated."""
    block = np.array([5, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8], dtype=np.int64)

    lines, n_lines = _facet_edge_lines(block, 2, 9)

    assert n_lines == 9
    assert lines.shape == (9, 3)
    assert set(map(tuple, lines[:, 1:].tolist())) == {
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (0, 4),
        (5, 6),
        (6, 7),
        (7, 8),
        (5, 8),
    }


def _quadratic_triangle(bulge):
    """Return the six nodes of a quadratic triangle, in polygon loop order.

    Each mid-side node is displaced from the straight edge by ``bulge`` times its
    distance from the centre, so a negative bulge gives the inward curve that a
    quadratic facet takes on a concave surface.
    """
    corners = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.5, 0.9, 0.0]])
    centre = corners.mean(axis=0)
    nodes = []
    for first, second in ((0, 1), (1, 2), (2, 0)):
        middle = (corners[first] + corners[second]) / 2.0
        nodes.append(corners[first])
        nodes.append(middle + bulge * (middle - centre))
    return np.array(nodes, dtype=float)


def _shoelace_area(points):
    """Return the area of a simple polygon lying in the xy-plane.

    VTK reports the area of a polygon cell by fanning it from its first node, which
    is the very thing under test here, so the reference is computed directly.
    """
    x, y = points[:, 0], points[:, 1]
    return float(abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) / 2.0)


@pytest.mark.parametrize("bulge", [0.0, 0.35, -0.35, -0.6])
def test_wide_cells_keep_the_area_of_the_polygon_they_replace(bulge):
    """Quadratic facets shade their true area whichever way they curve.

    A fan from the first node double-covers a facet that curves inwards and leaves
    the rest of it bare, so the shaded area is checked against the polygon itself.
    """
    points = _quadratic_triangle(bulge)
    block = np.array([6, 0, 1, 2, 3, 4, 5], dtype=np.int64)

    render_points, triangulated, n_cells = _triangulate_polygon_block(points, block)
    shaded = pv.PolyData(render_points, triangulated)

    assert shaded.n_cells == n_cells
    assert n_cells == 4
    assert shaded.area == pytest.approx(_shoelace_area(points), rel=1.0e-6)


def test_triangle_and_quad_blocks_are_left_for_the_array_path():
    """Only blocks holding wider polygons need VTK, and they keep their points."""
    points = np.array(
        [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 1.0, 0.0], [0.0, 1.0, 0.0]],
        dtype=float,
    )
    block = np.array([4, 0, 1, 2, 3], dtype=np.int64)

    render_points, triangulated, n_cells = _triangulate_polygon_block(points, block)

    assert n_cells == 2
    assert np.array_equal(render_points, points)
    assert pv.PolyData(render_points, triangulated).area == pytest.approx(1.0)


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
