# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Module for testing plotter related functions."""
from pathlib import Path

import pyvista as pv

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    compute_distance,
    compute_face_list_from_structured_nodes,
)
from ansys.meshing.prime.graphics import PrimePlotter

pv.OFF_SCREEN = True
IMAGE_RESULTS_DIR = Path(Path(__file__).parent, "image_cache", "results")


def test_plotter(get_remote_client, get_examples, verify_image_cache):
    """Test the basic functionality of the plotter."""
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(mixing_elbow)

    mesh_util.surface_mesh(min_size=5, max_size=20)
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    display = PrimePlotter()
    display.plot(model)
    display.show()


def _check_element_outlines(model_pd):
    """Check outlines are held for the zonelets the face actor cannot draw itself.

    Returns the number of zonelets that hold outlines.
    """
    count = 0
    for part_pd in model_pd.values():
        for mesh_object, info in part_pd["faces"]:
            higher_order = mesh_object.mesh.GetPolys().GetMaxCellSize() > 4
            expected = info.has_mesh and higher_order
            assert (info.element_edges is not None) == expected
            assert (info.render_mesh is not None) == expected
            if expected:
                assert info.element_edges.n_cells > 0
                # shaded with an explicit triangulation, outlined with the real facets
                assert info.render_mesh.GetPolys().GetMaxCellSize() == 3
                assert info.render_mesh.n_cells > mesh_object.mesh.n_cells
                count += 1
    return count


def _mesh_elbow(model, mixing_elbow, quadratic):
    """Volume mesh the mixing elbow in an empty model and return its polydata."""
    model.delete_parts([part.id for part in model.parts])
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(mixing_elbow)
    mesh_util.surface_mesh(min_size=5, max_size=20)
    mesh_util.volume_mesh(quadratic=quadratic, volume_fill_type=prime.VolumeFillType.TET)
    return model.as_polydata(update=True)


def test_quadratic_element_outlines(get_remote_client, get_examples):
    """Quadratic facets get their outlines drawn as separate line geometry."""
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model

    # linear facets are drawn by the face actor itself, as they always have been
    linear_pd = _mesh_elbow(model, mixing_elbow, quadratic=False)
    assert _check_element_outlines(linear_pd) == 0

    linear_display = PrimePlotter()
    try:
        linear_display.add_model_pd(linear_pd)
        assert linear_display.element_edge_actors == {}
    finally:
        linear_display.scene.close()

    quadratic_pd = _mesh_elbow(model, mixing_elbow, quadratic=True)
    expected = _check_element_outlines(quadratic_pd)
    assert expected > 0

    display = PrimePlotter()
    try:
        display.add_model_pd(quadratic_pd)
        outlines = display.element_edge_actors
        assert len(outlines) == expected
        assert all(actor.visibility for actor in outlines.values())
        # every outline is keyed by the face actor it belongs to, so that hiding a
        # zonelet hides its outlines too
        face_actors = [actor for actor in display.info_actor_map if actor in outlines]
        assert len(face_actors) == expected
    finally:
        display.scene.close()


def test_quadratic_tet_plotter(get_remote_client, get_examples, verify_image_cache):
    """Visual regression for quadratic tet outlines on a curved model.

    Uses an oblique camera so mid-side node edges on the bend are visible in the
    cached screenshot (downloadable from the CI artifact).
    """
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model
    _mesh_elbow(model, mixing_elbow, quadratic=True)

    display = PrimePlotter()
    display.plot(model)
    display.scene.view_isometric()
    display.scene.camera.elevation = 25
    display.scene.camera.azimuth = 35
    display.show()


def test_compute_distance():
    point1 = [1, 1, 3]
    point2 = [1, 1, 1]
    assert compute_distance(point1=point1, point2=point2) == 2.0


def test_compute_face_list():
    dim = []
    dim.append(2)
    dim.append(2)
    dim.append(2)
    flist = compute_face_list_from_structured_nodes(dim)
    assert len(flist) == 30
