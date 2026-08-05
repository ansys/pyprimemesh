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

import numpy as np
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
    display.plot(model, update=True)
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


def _curved_quadratic_elbow(model, elbow_fmd):
    """Coarse quadratic tet mesh whose mid-side nodes follow the CAD surface.

    Meshing the faceted PMDAT leaves mid-side nodes on straight edges, so the
    result is indistinguishable from a linear mesh. Reading the CAD and
    projecting onto it is what actually bulges the elements out.
    """
    if model.parts:
        model.delete_parts([part.id for part in model.parts])
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(file_name=elbow_fmd)
    # coarse enough that a single element spans a visible amount of curvature
    mesh_util.surface_mesh(min_size=25, max_size=60)
    mesh_util.volume_mesh(quadratic=True, volume_fill_type=prime.VolumeFillType.TET)
    part = model.parts[0]
    prime.SurfaceUtilities(model).project_topo_faces_on_geometry(
        part.get_topo_faces(),
        prime.ProjectOnGeometryParams(
            model, project_on_facets_if_cadnot_found=True, project_only_mid_nodes=False
        ),
    )


def test_quadratic_edge_zonelets_follow_mid_nodes(get_remote_client, get_examples):
    """Edge zonelets are drawn through their mid-side node, not across it.

    A quadratic edge arrives as ``(start, mid, end)``. Drawing it as one segment
    leaves the mid node sitting in the point array without any line referencing
    it, and the line cuts the chord of the curve the node was projected onto.
    """
    model = get_remote_client.model
    _curved_quadratic_elbow(model, get_examples["elbow_fmd"])
    model_pd = model.as_polydata(update=True)

    checked = 0
    for part_pd in model_pd.values():
        for edge_mesh_part in part_pd["edges"]:
            edge = edge_mesh_part.mesh
            if edge.n_cells == 0:
                continue
            lines = edge.lines.reshape(-1, 3)
            assert (lines[:, 0] == 2).all()
            referenced = set(lines[:, 1]) | set(lines[:, 2])
            assert len(referenced) == edge.n_points
            checked += 1
    assert checked > 0


def test_quadratic_tet_plotter(get_remote_client, get_examples, verify_image_cache):
    """Visual regression for quadratic tet outlines on a curved model.

    Framed at a grazing angle on the pipe wall, where the curved element edges
    and the mid-side subdivision within each facet are most obvious.
    """
    model = get_remote_client.model
    _curved_quadratic_elbow(model, get_examples["elbow_fmd"])

    display = PrimePlotter()
    # update, or the polydata another test already cached for this model is reused
    display.plot(model, update=True)

    scene = display.scene
    bounds = np.array(scene.bounds).reshape(3, 2)
    span = float((bounds[:, 1] - bounds[:, 0]).max())
    target = bounds.mean(axis=1) + np.array([-0.10, -0.10, 0.0]) * span
    azimuth, elevation = np.radians(72), np.radians(12)
    direction = np.array(
        [
            np.cos(elevation) * np.cos(azimuth),
            np.cos(elevation) * np.sin(azimuth),
            np.sin(elevation),
        ]
    )
    scene.camera_position = [tuple(target + direction * span * 1.6), tuple(target), (0, 0, 1)]
    scene.camera.zoom(2.4)
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
