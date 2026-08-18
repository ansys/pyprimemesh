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
    ENTITY_COLOR_ARRAY,
    ENTITY_ID_ARRAY,
    ColorByType,
    compute_distance,
    compute_face_list_from_structured_nodes,
)
from ansys.meshing.prime.graphics import PrimePlotter
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked

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
    part_ids = [part.id for part in model.parts]
    if part_ids:
        model.delete_parts(part_ids)
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
        # the outlines of a part are drawn together, so they are keyed by part
        assert set(outlines) <= set(quadratic_pd)
        assert all(actor.visibility for actor in outlines.values())
        # every zonelet that holds outlines is still identifiable within them
        outlined = set()
        for actor in outlines.values():
            outlined |= set(display._drawn_geometry[actor].cell_data[ENTITY_ID_ARRAY].tolist())
        assert len(outlined) == expected

        # hiding an entity takes its outlines out of the scene together with its faces
        hidden_id = sorted(outlined)[0]
        display.set_entities_visible([hidden_id], False)
        for actor in outlines.values():
            drawn = display._drawn_geometry[actor]
            assert hidden_id not in set(drawn.cell_data[ENTITY_ID_ARRAY].tolist())
        display.set_entities_visible([hidden_id], True)
        for actor in outlines.values():
            drawn = display._drawn_geometry[actor]
            assert hidden_id in set(drawn.cell_data[ENTITY_ID_ARRAY].tolist())
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
    _curved_quadratic_elbow(model, get_examples["elbow_lucid"])
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
    _curved_quadratic_elbow(model, get_examples["elbow_lucid"])

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


def _plot_model(model_pd):
    """Plot polydata and return the plotter."""
    display = PrimePlotter(allow_picking=False)
    display.add_model_pd(model_pd)
    return display


def _drawn_pixels(display):
    """Count the pixels the model is drawn on, from a camera that does not move."""
    image = np.asarray(display.scene.screenshot())
    return int(np.count_nonzero((image != 255).any(axis=2)))


def test_entities_of_a_part_share_actors(get_remote_client, get_examples):
    """A part is drawn with a handful of actors however many entities it holds.

    The cost of a scene, and of exporting one, scales with the number of actors,
    so entity count must not leak into it.
    """
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    # the widget buttons are actors of their own, so only count what the model adds
    empty = PrimePlotter(allow_picking=False)
    baseline = len(empty.scene.actors)
    empty.scene.close()

    display = _plot_model(model_pd)
    try:
        entities = sum(len(part_pd["faces"]) for part_pd in model_pd.values())
        model_actors = len(display.scene.actors) - baseline
        # at most two face batches, one outline actor, and one edge actor per part
        assert model_actors <= 4 * len(model_pd)
        assert model_actors < entities
        # merging must not lose any entity
        assert len(display.entity_infos) == entities
    finally:
        display.scene.close()


def test_pick_resolves_to_the_entity_under_the_point(get_remote_client, get_examples):
    """Picking a shared actor selects the one entity the point falls on."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        assert len(batch.infos) > 1, "need a batch holding several entities"

        centers = batch.mesh.cell_centers().points
        for cell_id in (0, batch.mesh.n_cells // 2, batch.mesh.n_cells - 1):
            expected = int(batch.entity_ids[cell_id])
            display._picked_entities.clear()
            assert display._pick_entity(actor, centers[cell_id])
            assert [int(info.id) for info in display.selected_entity_infos] == [expected]

            # the picked entity is highlighted, and only it
            colors = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
            highlighted = np.unique(batch.entity_ids[colors[:, 0] == colors[cell_id][0]])
            assert set(highlighted.tolist()) == {expected}

            # picking it again clears the selection
            assert display._pick_entity(actor, centers[cell_id])
            assert display.selected_entity_infos == []
    finally:
        display.scene.close()


def test_hiding_an_entity_leaves_the_rest_drawn(get_remote_client, get_examples):
    """Hiding an entity drops its cells from what is drawn, and only its own.

    A cell of a shared mesh cannot be hidden by flagging it: the ghost array is
    honored when a surface is built from a data set, not by the mapper of a
    polygonal mesh, so the drawn geometry has to hold the visible cells only.
    """
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        entity_id = int(batch.entity_ids[0])
        hidden_cells = int(np.count_nonzero(batch.entity_ids == entity_id))
        assert 0 < hidden_cells < batch.mesh.n_cells
        # the first screenshot of a window only sets it up, so it can come back blank
        display.scene.screenshot()
        everything = _drawn_pixels(display)

        display.set_entities_visible([entity_id], False)
        drawn = display._drawn_geometry[actor]
        assert drawn.n_cells == batch.mesh.n_cells - hidden_cells
        assert entity_id not in set(drawn.cell_data[ENTITY_ID_ARRAY].tolist())
        # the entity is only masked from the scene, never lost
        assert batch.mesh.n_cells == drawn.n_cells + hidden_cells
        assert entity_id in batch.infos
        # the mapper keeps no reference of its own to what it draws, so the geometry
        # has to be checked on screen and not only in the state of the plotter
        assert 0 < _drawn_pixels(display) < everything

        display.set_entities_visible([entity_id], True)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells
        assert entity_id in set(display._drawn_geometry[actor].cell_data[ENTITY_ID_ARRAY].tolist())
        # showing the entity again has to bring every pixel of it back
        assert _drawn_pixels(display) == everything
    finally:
        display.scene.close()


def test_hidden_entities_stay_hidden_when_recolored(get_remote_client, get_examples):
    """Recoloring rebuilds the drawn geometry, which must stay free of hidden cells."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        entity_id = int(batch.entity_ids[0])
        display.set_entities_visible([entity_id], False)
        drawn_cells = display._drawn_geometry[actor].n_cells

        display.set_color_by_type(ColorByType.ZONELET)
        drawn = display._drawn_geometry[actor]
        assert drawn.n_cells == drawn_cells
        assert entity_id not in set(drawn.cell_data[ENTITY_ID_ARRAY].tolist())
        # the drawn copy carries the colors that were just computed
        assert ENTITY_COLOR_ARRAY in drawn.cell_data
    finally:
        display.scene.close()


def test_hidden_entities_cannot_be_picked(get_remote_client, get_examples):
    """A pick resolves against what is drawn, so hidden entities are not selectable."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        entity_id = int(batch.entity_ids[0])
        center = batch.mesh.cell_centers().points[0]

        display.set_entities_visible([entity_id], False)
        assert display._pick_entity(actor, center)
        assert entity_id not in {int(info.id) for info in display.selected_entity_infos}
    finally:
        display.scene.close()


def _pick_display_point(display, world_point):
    """Pick the scene where a world point is drawn, the way a click does."""
    scene = display.scene
    coordinate = pv._vtk.vtkCoordinate()
    coordinate.SetCoordinateSystemToWorld()
    coordinate.SetValue(*world_point)
    x, y = coordinate.GetComputedDisplayValue(scene.renderer)
    scene.iren.picker.Pick(x, y, 0, scene.renderer)


def test_clicking_a_shared_actor_selects_and_labels_an_entity(get_remote_client, get_examples):
    """A click travels from the backend picker to the entity under the cursor.

    The entities of a part share an actor, so the pick has to be resolved against
    the cell it landed on, and the picked entity has to be labeled here, since the
    generic backend can only label an object that owns an actor of its own.
    """
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        display._backend.enable_picking()
        display.scene.show(auto_close=False)
        display.scene.render()

        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        _pick_display_point(display, batch.mesh.cell_centers().points[0])
        picked_point = display.scene.picked_point
        assert picked_point is not None, "the click has to land on the model"

        drawn = display._drawn_geometry[display.scene.picked_actor]
        expected = int(
            drawn.cell_data[ENTITY_ID_ARRAY][drawn.find_closest_cell(list(picked_point))]
        )
        assert [int(info.id) for info in display.selected_entity_infos] == [expected]

        # the entity is named on screen, as an individually drawn object would be
        assert expected in display._entity_labels
        assert display._entity_labels[expected] in display.scene.actors.values()

        # clicking it again clears both the selection and its label
        _pick_display_point(display, batch.mesh.cell_centers().points[0])
        assert display.selected_entity_infos == []
        assert display._entity_labels == {}
    finally:
        display.scene.close()


def test_hiding_a_picked_entity_hides_its_label(get_remote_client, get_examples):
    """The label of an entity follows the entity in and out of the scene."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        entity_id = int(batch.entity_ids[0])
        display._pick_entity(actor, batch.mesh.cell_centers().points[0])
        assert entity_id in display._entity_labels

        display.set_entities_visible([entity_id], False)
        assert display._entity_labels == {}
        # the entity stays picked, so the widgets keep reporting it
        assert [int(info.id) for info in display.selected_entity_infos] == [entity_id]

        display.set_entities_visible([entity_id], True)
        assert entity_id in display._entity_labels
    finally:
        display.scene.close()


def test_hide_picked_widget_hides_and_restores_entities(get_remote_client, get_examples):
    """The hide widget takes the picked entities out of the scene and brings them back."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        actor, batch = max(display._batches.items(), key=lambda item: len(item[1].infos))
        entity_id = int(batch.entity_ids[0])
        hidden_cells = int(np.count_nonzero(batch.entity_ids == entity_id))
        display._pick_entity(actor, batch.mesh.cell_centers().points[0])

        widget = next(w for w in display._backend._widgets if isinstance(w, HidePicked))
        widget.callback(True)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells - hidden_cells

        widget.callback(False)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells
    finally:
        display.scene.close()


def test_color_by_type_recolors_shared_meshes(get_remote_client, get_examples):
    """Switching color mode recolors cells rather than actors."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        batch = max(display._batches.values(), key=lambda candidate: len(candidate.infos))

        display.set_color_by_type(ColorByType.PART)
        by_part = batch.mesh.cell_data[ENTITY_COLOR_ARRAY].copy()
        assert len(np.unique(by_part, axis=0)) == 1

        display.set_color_by_type(ColorByType.ZONELET)
        by_zonelet = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
        assert len(np.unique(by_zonelet, axis=0)) > 1
        # cells of one entity always share a color
        for entity_id in list(batch.infos)[:5]:
            cells = batch.entity_ids == entity_id
            assert len(np.unique(by_zonelet[cells], axis=0)) == 1
    finally:
        display.scene.close()


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
