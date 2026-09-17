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

"""Tests for USD mesh functionality."""


def test_mesh_usd_import():
    """Test that MeshUSD class can be imported."""
    from ansys.meshing.prime.core.mesh import MeshUSD

    assert MeshUSD is not None


def test_geometry_dto_creation():
    """Test that geometry DTO classes can be created."""
    import numpy as np

    from ansys.meshing.prime.core.mesh import (
        DisplayMeshType,
        EdgeGeometry,
        FaceGeometry,
        SplineGeometry,
    )

    # Test FaceGeometry
    points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]], dtype=np.float32)
    face_geom = FaceGeometry(
        points=points,
        face_vertex_indices=np.array([0, 1, 2], dtype=np.uint32),
        face_vertex_counts=np.array([3], dtype=np.uint32),
        color=[255, 0, 0],
        part_id=1,
        zone_id=0,
        zone_name="Zone1",
        mesh_id=1,
        display_mesh_type=DisplayMeshType.FACEZONELET,
        has_mesh=True,
    )
    assert face_geom.points.shape == (3, 3)
    assert face_geom.color == [255, 0, 0]

    # Test EdgeGeometry
    edge_geom = EdgeGeometry(
        points=points,
        edge_vertex_indices=np.array([0, 1, 1, 2], dtype=np.uint32),
        edge_vertex_counts=np.array([2, 2], dtype=np.uint32),
        color=[0, 255, 0],
        part_id=1,
        mesh_id=2,
        display_mesh_type=DisplayMeshType.EDGEZONELET,
    )
    assert edge_geom.mesh_id == 2

    # Test SplineGeometry
    spline_geom = SplineGeometry(
        points=points,
        color=[0, 0, 255],
        part_id=1,
        spline_id=1,
        geom_type=DisplayMeshType.SPLINECONTROLPOINTS,
    )
    assert spline_geom.spline_id == 1


def test_mesh_usd_io_normalize_color():
    """Test color normalization."""
    from ansys.meshing.prime.core.mesh_usd_io import normalize_color

    # Test normalization
    normalized = normalize_color([255, 128, 0])
    assert abs(normalized[0] - 1.0) < 1e-6
    assert abs(normalized[1] - (128 / 255.0)) < 1e-6
    assert abs(normalized[2] - 0.0) < 1e-6


if __name__ == "__main__":
    test_mesh_usd_import()
    test_geometry_dto_creation()
    test_mesh_usd_io_normalize_color()
    print("All tests passed!")
