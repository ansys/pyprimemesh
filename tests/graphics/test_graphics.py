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

"""Tests for Prime plotting and actor-per-entity-type rendering."""

from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
import pyvista as pv
from ansys.tools.visualization_interface.backends.pyvista.widgets.mesh_slider import (
    MeshSliderWidget,
)
from ansys.tools.visualization_interface.utils.color import Color

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    EDGE_DISPLAY_MESH_TYPES,
    ENTITY_COLOR_ARRAY,
    ENTITY_ID_ARRAY,
    ENTITY_TYPE_ARRAY,
    FACE_CONNECTIVITY_COLORS,
    FACE_DISPLAY_MESH_TYPES,
    PART_ID_ARRAY,
    RENDER_ENTITY_ID_ARRAY,
    ZONE_ID_ARRAY,
    ColorByType,
    DisplayEntityKey,
    DisplayMeshInfo,
    DisplayMeshType,
    FaceConnectivity,
    SelectionTarget,
    compute_distance,
    compute_face_list_from_structured_nodes,
    connectivity_color,
)
from ansys.meshing.prime.graphics import PrimePlotter
from ansys.meshing.prime.graphics.widgets.clip_plane import ClipPlaneWidget
from ansys.meshing.prime.graphics.widgets.color_by_type import ColorByTypeWidget
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked
from ansys.meshing.prime.graphics.widgets.toggle_edges import ToggleEdges
from ansys.meshing.prime.graphics.widgets.toolbar import BUTTON_SIZE

pv.OFF_SCREEN = True
IMAGE_RESULTS_DIR = Path(Path(__file__).parent, "image_cache", "results")


def test_plotter(get_remote_client, get_examples, verify_image_cache):
    """Test basic plotter functionality."""
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
    """Validate explicit triangulations and outlines; return outlined entity keys."""
    outlined = set()
    for part_pd in model_pd.values():
        for mesh_object, info in part_pd["faces"]:
            higher_order = mesh_object.mesh.GetPolys().GetMaxCellSize() > 4
            expected = info.has_mesh and higher_order
            assert (info.element_edges is not None) == expected
            assert (info.render_mesh is not None) == expected
            if expected:
                assert info.element_edges.n_cells > 0
                assert info.render_mesh.GetPolys().GetMaxCellSize() == 3
                assert info.render_mesh.n_cells > mesh_object.mesh.n_cells
                outlined.add(info.key)
    return outlined


def _mesh_elbow(model, mixing_elbow, quadratic):
    """Volume mesh the elbow in an empty model and return its PolyData."""
    part_ids = [part.id for part in model.parts]
    if part_ids:
        model.delete_parts(part_ids)
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(mixing_elbow)
    mesh_util.surface_mesh(min_size=5, max_size=20)
    mesh_util.volume_mesh(quadratic=quadratic, volume_fill_type=prime.VolumeFillType.TET)
    return model.as_polydata(update=True)


def _entry_info(batch, cell_id=0):
    """Return render ID, metadata, and unique key for a batch cell."""
    render_id = int(batch.render_entity_ids[cell_id])
    info = batch.infos[render_id]
    return render_id, info, info.key


def _largest_pickable_batch(display):
    """Return the pickable face actor and batch with the most registered entities."""
    actor, batch = max(
        (
            (actor, batch)
            for actor, batch in display._batches.items()
            if batch.pickable and batch.display_mesh_type in FACE_DISPLAY_MESH_TYPES
        ),
        key=lambda item: len(item[1].infos),
    )
    return actor, batch


def _batches_of_types(display, display_mesh_types):
    """Return every registered actor and batch of the given display entity types."""
    return [
        (actor, batch)
        for actor, batch in display._batches.items()
        if batch.display_mesh_type in display_mesh_types
    ]


def _read_only(model, file_name):
    """Replace every part of a model with the contents of one file."""
    if model.parts:
        model.delete_parts([part.id for part in model.parts])
    prime.lucid.Mesh(model=model).read(file_name)


def _cells_for_key(batch, key):
    """Return a mask selecting one model-unique entity in a batch."""
    render_ids = {int(render_id) for render_id, info in batch.infos.items() if info.key == key}
    return np.isin(batch.render_entity_ids, tuple(render_ids))


def _keys_in_mesh(batch, mesh):
    """Return model-unique entity keys represented in a displayed mesh."""
    if mesh is None or mesh.n_cells == 0:
        return set()
    return {
        batch.infos[int(render_id)].key
        for render_id in np.unique(mesh.cell_data[RENDER_ENTITY_ID_ARRAY])
    }


def test_quadratic_element_outlines(get_remote_client, get_examples):
    """Quadratic facets use model-wide explicit outline actors."""
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model

    linear_pd = _mesh_elbow(model, mixing_elbow, quadratic=False)
    assert _check_element_outlines(linear_pd) == set()
    linear_meshed_keys = {
        info.key for part_pd in linear_pd.values() for _, info in part_pd["faces"] if info.has_mesh
    }
    assert linear_meshed_keys
    linear_display = PrimePlotter()
    try:
        linear_display.add_model_pd(linear_pd)
        assert linear_display.element_edge_actors
        represented = set()
        for actor, batch in linear_display.element_edge_actors.items():
            represented.update(_keys_in_mesh(batch, linear_display._drawn_geometry[actor]))
        assert linear_meshed_keys <= represented
    finally:
        linear_display.scene.close()

    quadratic_pd = _mesh_elbow(model, mixing_elbow, quadratic=True)
    expected_keys = _check_element_outlines(quadratic_pd)
    assert expected_keys

    display = PrimePlotter()
    try:
        display.add_model_pd(quadratic_pd)
        outlines = display.element_edge_actors
        assert outlines
        assert all(actor.visibility for actor in outlines)
        assert len(outlines) <= 2  # TOPOFACE and FACEZONELET outline roles.

        represented = set()
        for actor, batch in outlines.items():
            represented.update(_keys_in_mesh(batch, display._drawn_geometry[actor]))
        assert represented == expected_keys

        hidden_key = next(iter(expected_keys))
        display.set_entities_visible([hidden_key], False)
        for actor, batch in outlines.items():
            assert hidden_key not in _keys_in_mesh(batch, display._drawn_geometry[actor])

        display.set_entities_visible([hidden_key], True)
        represented = set()
        for actor, batch in outlines.items():
            represented.update(_keys_in_mesh(batch, display._drawn_geometry[actor]))
        assert hidden_key in represented
    finally:
        display.scene.close()


def test_add_model_shows_linear_meshed_element_outlines(get_remote_client, get_examples):
    """Fast render path draws element outlines for linear meshed faces."""
    model = get_remote_client.model
    _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    meshed_keys = {
        info.key
        for part_pd in model.as_polydata(update=True).values()
        for _, info in part_pd["faces"]
        if info.has_mesh
    }
    assert meshed_keys

    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        assert display.element_edge_actors
        represented = set()
        for actor, batch in display.element_edge_actors.items():
            represented.update(_keys_in_mesh(batch, display._drawn_geometry[actor]))
        assert meshed_keys <= represented
    finally:
        display.scene.close()


def test_cad_without_mesh_is_outlined_by_its_facets(get_remote_client, get_examples):
    """Unmeshed CAD faces keep has_mesh=False but still show their facets."""
    model = get_remote_client.model
    _read_only(model, get_examples["elbow_lucid"])

    model_pd = model.as_polydata(update=True)
    assert all(not info.has_mesh for part_pd in model_pd.values() for _, info in part_pd["faces"])

    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        assert display.facet_edge_actors
        assert not display.element_edge_actors

        outlined = set()
        for actor, batch in display.facet_edge_actors.items():
            assert all(not info.has_mesh for info in batch.infos.values())
            outlined.update(_keys_in_mesh(batch, display._drawn_geometry[actor]))
        expected = {info.key for part_pd in model_pd.values() for _, info in part_pd["faces"]}
        assert expected <= outlined

        # Facets stand in for a mesh that is not there, so they start hidden and the
        # show-edges button reveals them.
        assert not any(actor.visibility for actor in display.facet_edge_actors)
        display.set_show_edges(False)
        assert all(actor.visibility for actor in display.facet_edge_actors)
        display.set_show_edges(True)
        assert not any(actor.visibility for actor in display.facet_edge_actors)
    finally:
        display.scene.close()


def test_picking_a_face_keeps_edges_colored_by_connectivity(get_remote_client, get_examples):
    """Selecting a face leaves edge connectivity colors untouched."""
    model = get_remote_client.model
    part_ids = [part.id for part in model.parts]
    if part_ids:
        model.delete_parts(part_ids)
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(get_examples["elbow_lucid"])

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model(model, update=True)
        edge_batches = [
            batch
            for batch in display._batches.values()
            if batch.display_mesh_type in (DisplayMeshType.TOPOEDGE, DisplayMeshType.EDGEZONELET)
        ]
        assert edge_batches
        assert all(batch.base_colors is not None for batch in edge_batches)
        before = [batch.mesh.cell_data[ENTITY_COLOR_ARRAY].copy() for batch in edge_batches]

        actor, batch = _largest_pickable_batch(display)
        assert display._pick_entity(actor, batch.mesh.cell_centers().points[0])
        assert display.selected_entity_infos

        for edge_batch, original in zip(edge_batches, before):
            assert np.array_equal(edge_batch.mesh.cell_data[ENTITY_COLOR_ARRAY], original)
    finally:
        display.scene.close()


@pytest.mark.parametrize(
    "example,expected",
    [
        ("bracket", FaceConnectivity.SURFACE),
        ("elbow_lucid", FaceConnectivity.BODY),
    ],
)
def test_connectivity_mode_colors_faces_by_volume_membership(
    get_remote_client, get_examples, example, expected
):
    """Sheet bodies and the skin of a solid take different connectivity colors."""
    model = get_remote_client.model
    _read_only(model, get_examples[example])

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model(model, update=True)
        faces = _batches_of_types(display, FACE_DISPLAY_MESH_TYPES)
        assert faces
        assert all(info.connectivity is None for _, batch in faces for info in batch.infos.values())

        display.set_color_by_type(ColorByType.CONNECTIVITY)

        wanted = np.asarray(FACE_CONNECTIVITY_COLORS[expected], dtype=np.uint8)
        for _, batch in faces:
            assert all(info.connectivity == int(expected) for info in batch.infos.values())
            assert np.all(batch.mesh.cell_data[ENTITY_COLOR_ARRAY] == wanted)
    finally:
        display.scene.close()


def test_connectivity_mode_keeps_edge_connectivity_colors(get_remote_client, get_examples):
    """Edges already carry connectivity colors, so the mode leaves them alone."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model(model, update=True)
        edges = _batches_of_types(display, EDGE_DISPLAY_MESH_TYPES)
        assert edges
        assert all(batch.base_colors is not None for _, batch in edges)

        for color_type in (ColorByType.PART, ColorByType.CONNECTIVITY):
            display.set_color_by_type(color_type)
            for _, batch in edges:
                applied = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
                assert np.array_equal(applied, batch.base_colors) == (
                    color_type == ColorByType.CONNECTIVITY
                )
    finally:
        display.scene.close()


def test_edges_can_be_picked(get_remote_client, get_examples):
    """An edge batch resolves a pick to its own entity."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model(model, update=True)
        edges = _batches_of_types(display, EDGE_DISPLAY_MESH_TYPES)
        assert edges
        actor, batch = edges[0]
        assert batch.pickable

        _, _, key = _entry_info(batch)
        assert display._pick_entity(actor, batch.mesh.cell_centers().points[0])
        assert [info.key for info in display.selected_entity_infos] == [key]

        highlight = np.asarray(pv.Color(Color.PICKED.value).int_rgb, dtype=np.uint8)
        selected = _cells_for_key(batch, key)
        applied = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
        assert np.all(applied[selected] == highlight)
        assert np.array_equal(applied[~selected], batch.base_colors[~selected])
    finally:
        display.scene.close()


def _spaced_copies(model, file_name, copies, spacing):
    """Replace the model with several copies of one CAD file, spaced along X."""
    if model.parts:
        model.delete_parts([part.id for part in model.parts])
    for index in range(copies):
        prime.FileIO(model).import_cad(
            file_name,
            params=prime.ImportCadParams(model=model, append=index > 0),
        )
    for index, part in enumerate(model.parts):
        if not index:
            continue
        params = prime.TransformParams(model)
        # fmt: off
        params.transformation_matrix = [
            1.0, 0.0, 0.0, index * spacing,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0,
        ]
        # fmt: on
        prime.Transform(model).transform_zonelets(
            part.id,
            list(part.get_topo_faces()) + list(part.get_topo_edges()),
            params,
        )


def test_multiple_parts_keep_edge_colors_and_pick_correctly(get_remote_client, get_examples):
    """Edge connectivity colors and picking hold up once a model has many parts."""
    model = get_remote_client.model
    _spaced_copies(model, get_examples["bracket"], copies=3, spacing=250.0)
    assert len(model.parts) > 2

    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model(model, update=True)

        edge_parts = set()
        for _, batch in _batches_of_types(display, EDGE_DISPLAY_MESH_TYPES):
            colors = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
            for render_id, info in batch.infos.items():
                edge_parts.add(info.part_id)
                cells = batch.render_entity_ids == render_id
                expected = np.asarray(connectivity_color(info), dtype=np.uint8)
                assert np.all(colors[cells] == expected)
        assert edge_parts == {part.id for part in model.parts}

        picked_parts = set()
        for actor, batch in _batches_of_types(display, FACE_DISPLAY_MESH_TYPES):
            if not batch.pickable:
                continue
            centers = batch.mesh.cell_centers().points
            for render_id, info in batch.infos.items():
                cell = int(np.flatnonzero(batch.render_entity_ids == render_id)[0])
                display._picked_entities.clear()
                assert display._pick_entity(actor, centers[cell])
                assert [picked.key for picked in display.selected_entity_infos] == [info.key]
                picked_parts.add(info.part_id)
        assert picked_parts == {part.id for part in model.parts}
    finally:
        display.scene.close()


def _face_scope(model, label_expression):
    """Return a face-zonelet scope selecting one label."""
    return prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.FACEZONELETS,
        evaluation_type=prime.ScopeEvaluationType.LABELS,
        label_expression=label_expression,
    )


def _face_keys(render_data):
    """Return the face entity keys present in render data."""
    return {
        info.key
        for batch in render_data.batches.get("faces", {}).values()
        for info in batch.infos.values()
    }


def test_scoped_render_data_returns_only_the_scoped_faces(get_remote_client, get_examples):
    """A face scope delivers the scoped faces and no other entity."""
    model = get_remote_client.model
    _read_only(model, get_examples["elbow_fmd"])
    prime.lucid.Mesh(model=model).surface_mesh(min_size=5, max_size=20)

    labels = model.parts[0].get_labels()
    assert labels

    everything = _face_keys(model.build_render_data(update=True))
    scoped_data = model.get_scoped_render_data(_face_scope(model, labels[0]), update=True)
    scoped = _face_keys(scoped_data)

    assert scoped
    assert scoped < everything
    # The scope selects faces, so the rest of the part's edges are not its entities.
    assert not scoped_data.batches.get("edges")
    outlined = {
        info.key
        for batch in scoped_data.batches.get("element_edges", {}).values()
        for info in batch.infos.values()
    }
    assert outlined <= scoped


def test_scope_matching_nothing_returns_empty_render_data(get_remote_client, get_examples):
    """A scope that matches nothing terminates rather than recursing forever."""
    model = get_remote_client.model
    _read_only(model, get_examples["elbow_fmd"])

    data = model.get_scoped_render_data(_face_scope(model, "no_such_label"), update=True)
    assert data.batches == {}


def test_connectivity_classifies_mesh_parts_without_topology(get_remote_client, get_examples):
    """Face zonelets classify from mesh volumes once topology is deleted."""
    model = get_remote_client.model
    _read_only(model, get_examples["elbow_fmd"])
    prime.lucid.Mesh(model=model).surface_mesh(min_size=5, max_size=20)
    prime.lucid.Mesh(model=model).volume_mesh(volume_fill_type=prime.VolumeFillType.TET)
    for part in model.parts:
        part.delete_topo_entities(
            prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True)
        )

    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        faces = _batches_of_types(display, FACE_DISPLAY_MESH_TYPES)
        assert faces
        assert all(batch.display_mesh_type == DisplayMeshType.FACEZONELET for _, batch in faces)

        display.set_color_by_type(ColorByType.CONNECTIVITY)
        assert all(
            info.connectivity == int(FaceConnectivity.BODY)
            for _, batch in faces
            for info in batch.infos.values()
        )
    finally:
        display.scene.close()


def _curved_quadratic_elbow(model, elbow_fmd):
    """Create a coarse quadratic tet mesh whose mid-side nodes follow CAD."""
    if model.parts:
        model.delete_parts([part.id for part in model.parts])
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(file_name=elbow_fmd)
    mesh_util.surface_mesh(min_size=25, max_size=60)
    mesh_util.volume_mesh(quadratic=True, volume_fill_type=prime.VolumeFillType.TET)
    part = model.parts[0]
    prime.SurfaceUtilities(model).project_topo_faces_on_geometry(
        part.get_topo_faces(),
        prime.ProjectOnGeometryParams(
            model,
            project_on_facets_if_cadnot_found=True,
            project_only_mid_nodes=False,
        ),
    )


def test_quadratic_edge_zonelets_follow_mid_nodes(get_remote_client, get_examples):
    """Quadratic edge zonelets are drawn through their mid-side nodes."""
    model = get_remote_client.model
    _curved_quadratic_elbow(model, get_examples["elbow_lucid"])
    model_pd = model.as_polydata(update=True)

    checked = 0
    for part_pd in model_pd.values():
        for edge_entry in part_pd["edges"]:
            edge_mesh_part = edge_entry
            assert not isinstance(edge_entry, tuple)
            edge = edge_mesh_part.mesh
            assert PART_ID_ARRAY in edge.cell_data
            assert ENTITY_ID_ARRAY in edge.cell_data
            assert ENTITY_TYPE_ARRAY in edge.cell_data
            assert ZONE_ID_ARRAY in edge.cell_data
            if edge.n_cells == 0:
                continue
            lines = edge.lines.reshape(-1, 3)
            assert (lines[:, 0] == 2).all()
            referenced = set(lines[:, 1]) | set(lines[:, 2])
            assert len(referenced) == edge.n_points
            checked += 1
    assert checked > 0


def test_edge_polydata_preserves_public_entry_type(
    get_remote_client,
    get_examples,
):
    """Edge PolyData entries remain MeshObjectPlot objects."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(
        model,
        get_examples["elbow_lucid"],
        quadratic=False,
    )

    checked = 0

    for part_data in model_pd.values():
        for edge_entry in part_data["edges"]:
            if edge_entry is None:
                continue

            assert not isinstance(edge_entry, tuple)
            assert hasattr(edge_entry, "mesh")

            edge = edge_entry.mesh
            assert PART_ID_ARRAY in edge.cell_data
            assert ENTITY_ID_ARRAY in edge.cell_data
            assert ENTITY_TYPE_ARRAY in edge.cell_data
            assert ZONE_ID_ARRAY in edge.cell_data

            checked += 1

    assert checked > 0


def test_quadratic_tet_plotter(get_remote_client, get_examples, verify_image_cache):
    """Visual regression for quadratic tet outlines on a curved model."""
    model = get_remote_client.model
    _curved_quadratic_elbow(model, get_examples["elbow_lucid"])
    display = PrimePlotter()
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
    scene.camera_position = [
        tuple(target + direction * span * 1.6),
        tuple(target),
        (0, 0, 1),
    ]
    scene.camera.zoom(2.4)
    display.show()


def _plot_model(model_pd):
    """Plot PolyData and return the plotter."""
    display = PrimePlotter(allow_picking=False)
    display.add_model_pd(model_pd)
    return display


def _drawn_pixels(display):
    """Count non-background pixels without moving the camera."""
    image = np.asarray(display.scene.screenshot())
    return int(np.count_nonzero((image != 255).any(axis=2)))


def test_model_uses_actor_per_entity_type(get_remote_client, get_examples):
    """Actor count depends on rendering types, not entity or part count."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    empty = PrimePlotter(allow_picking=False)
    baseline = len(empty.scene.actors)
    empty.scene.close()

    display = _plot_model(model_pd)
    try:
        face_entities = sum(len(part_pd["faces"]) for part_pd in model_pd.values())
        face_types = {DisplayMeshType.TOPOFACE, DisplayMeshType.FACEZONELET}
        registered_faces = sum(
            1 for info in display.entity_infos.values() if info.display_mesh_type in face_types
        )
        model_actors = len(display.scene.actors) - baseline
        # Four geometry types, two outline roles, and two spline roles at most.
        assert model_actors <= 8
        assert model_actors < face_entities
        assert registered_faces == face_entities
        assert len(display._batches) <= 4
        assert len(display.element_edge_actors) <= 2
    finally:
        display.scene.close()


def test_pick_resolves_to_model_unique_entity(get_remote_client, get_examples):
    """Picking a shared actor resolves the exact entity beneath the point."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)

    display = _plot_model(model_pd)
    try:
        actor, batch = _largest_pickable_batch(display)
        assert len(batch.infos) > 1

        centers = batch.mesh.cell_centers().points
        for cell_id in (0, batch.mesh.n_cells // 2, batch.mesh.n_cells - 1):
            _, expected_info, expected_key = _entry_info(batch, cell_id)
            display._picked_entities.clear()
            assert display._pick_entity(actor, centers[cell_id])
            assert [info.key for info in display.selected_entity_infos] == [expected_key]

            highlight = np.asarray(pv.Color(Color.PICKED.value).int_rgb, dtype=np.uint8)
            highlighted = np.all(
                batch.mesh.cell_data[ENTITY_COLOR_ARRAY] == highlight,
                axis=1,
            )
            selected_render_id = int(batch.render_entity_ids[cell_id])
            assert highlighted[batch.render_entity_ids == selected_render_id].all()
            assert not highlighted[batch.render_entity_ids != selected_render_id].any()

            assert display._pick_entity(actor, centers[cell_id])
            assert display.selected_entity_infos == []
            assert expected_info.key not in display._picked_entities
    finally:
        display.scene.close()


def test_hiding_an_entity_leaves_the_rest_drawn(get_remote_client, get_examples):
    """Hiding one entity filters only its cells from the shared actor."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = _plot_model(model_pd)
    try:
        actor, batch = _largest_pickable_batch(display)
        _, _, key = _entry_info(batch)
        mask = _cells_for_key(batch, key)
        hidden_cells = int(np.count_nonzero(mask))
        assert 0 < hidden_cells < batch.mesh.n_cells
        display.scene.screenshot()
        everything = _drawn_pixels(display)

        display.set_entities_visible([key], False)
        drawn = display._drawn_geometry[actor]
        assert drawn.n_cells == batch.mesh.n_cells - hidden_cells
        assert key not in _keys_in_mesh(batch, drawn)
        assert key in display.entity_infos

        display.set_entities_visible([key], True)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells
        assert key in _keys_in_mesh(batch, display._drawn_geometry[actor])
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells
    finally:
        display.scene.close()


def test_hidden_entities_stay_hidden_when_recolored(get_remote_client, get_examples):
    """Recoloring preserves entity visibility filtering."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = _plot_model(model_pd)
    try:
        actor, batch = _largest_pickable_batch(display)
        _, _, key = _entry_info(batch)
        display.set_entities_visible([key], False)
        drawn_cells = display._drawn_geometry[actor].n_cells

        display.set_color_by_type(ColorByType.ZONELET)
        drawn = display._drawn_geometry[actor]
        assert drawn.n_cells == drawn_cells
        assert key not in _keys_in_mesh(batch, drawn)
        assert ENTITY_COLOR_ARRAY in drawn.cell_data
    finally:
        display.scene.close()


def test_hidden_entities_cannot_be_picked(get_remote_client, get_examples):
    """A pick resolves against displayed geometry, never hidden cells."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = _plot_model(model_pd)
    try:
        actor, batch = _largest_pickable_batch(display)
        _, _, hidden_key = _entry_info(batch)
        visible_render_id = next(
            render_id for render_id, info in batch.infos.items() if info.key != hidden_key
        )

        cell_id = np.flatnonzero(batch.render_entity_ids == visible_render_id)[0]

        center = batch.mesh.cell_centers().points[cell_id]

        display.set_entities_visible([hidden_key], False)
        assert display._pick_entity(actor, center)
        assert hidden_key not in {info.key for info in display.selected_entity_infos}
    finally:
        display.scene.close()


def _pick_display_point(display, world_point):
    """Pick the scene at the display coordinate of a world point."""
    scene = display.scene
    coordinate = pv._vtk.vtkCoordinate()
    coordinate.SetCoordinateSystemToWorld()
    coordinate.SetValue(*world_point)
    x, y = coordinate.GetComputedDisplayValue(scene.renderer)
    scene.iren.picker.Pick(x, y, 0, scene.renderer)


def test_clicking_shared_actor_selects_and_labels_entity(get_remote_client, get_examples):
    """A backend click selects and labels one model-unique entity."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        display._backend.enable_picking()
        display.scene.show(auto_close=False)
        display.scene.render()

        actor, batch = _largest_pickable_batch(display)
        _pick_display_point(display, batch.mesh.cell_centers().points[0])
        picked_point = display.scene.picked_point
        assert picked_point is not None

        picked_actor = display.scene.picked_actor
        drawn = display._drawn_geometry[picked_actor]
        cell_id = drawn.find_closest_cell(list(picked_point))
        render_id = int(drawn.cell_data[RENDER_ENTITY_ID_ARRAY][cell_id])
        expected_key = display._batches[picked_actor].infos[render_id].key
        assert [info.key for info in display.selected_entity_infos] == [expected_key]
        assert expected_key in display._entity_labels
        assert display._entity_labels[expected_key] in display.scene.actors.values()

        _pick_display_point(display, batch.mesh.cell_centers().points[0])
        assert display.selected_entity_infos == []
        assert display._entity_labels == {}
    finally:
        display.scene.close()


def test_hiding_picked_entity_hides_its_label(get_remote_client, get_examples):
    """A picked entity label follows visibility while selection persists."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        actor, batch = _largest_pickable_batch(display)
        _, _, key = _entry_info(batch)
        display._pick_entity(actor, batch.mesh.cell_centers().points[0])
        assert key in display._entity_labels

        display.set_entities_visible([key], False)
        assert display._entity_labels == {}
        assert [info.key for info in display.selected_entity_infos] == [key]

        display.set_entities_visible([key], True)
        assert key in display._entity_labels
    finally:
        display.scene.close()


def test_hide_picked_widget_hides_and_restores_entities(get_remote_client, get_examples):
    """The hide widget filters and restores exactly the picked entity."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        actor, batch = _largest_pickable_batch(display)
        _, _, key = _entry_info(batch)
        hidden_cells = int(np.count_nonzero(_cells_for_key(batch, key)))
        display._pick_entity(actor, batch.mesh.cell_centers().points[0])

        widget = next(
            widget for widget in display._backend._widgets if isinstance(widget, HidePicked)
        )
        widget.callback(True)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells - hidden_cells
        assert widget._hidden_entities == [key]

        widget.callback(False)
        assert display._drawn_geometry[actor].n_cells == batch.mesh.n_cells
        assert widget._hidden_entities == []
    finally:
        display.scene.close()


def _first_pickable_batch(display, display_mesh_types):
    """Return the first pickable actor and batch of the given display types."""
    return next(
        (actor, batch)
        for actor, batch in display._batches.items()
        if batch.pickable and batch.display_mesh_type in display_mesh_types
    )


def _pick_first_cell(display, actor, batch):
    """Pick the center of the first cell of a batch."""
    return display._pick_entity(actor, batch.mesh.cell_centers().points[0])


@pytest.mark.parametrize(
    "target,face_selects,edge_selects",
    [
        (SelectionTarget.BOTH, True, True),
        (SelectionTarget.FACES, True, False),
        (SelectionTarget.EDGES, False, True),
    ],
)
def test_selection_target_restricts_what_a_pick_selects(
    get_remote_client, get_examples, target, face_selects, edge_selects
):
    """Only the targeted kind of entity answers a pick."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        face_actor, face_batch = _first_pickable_batch(display, FACE_DISPLAY_MESH_TYPES)
        edge_actor, edge_batch = _first_pickable_batch(display, EDGE_DISPLAY_MESH_TYPES)

        display.set_selection_target(target)
        assert display.selection_target == target

        _pick_first_cell(display, face_actor, face_batch)
        assert bool(display.selected_entity_infos) == face_selects

        display._picked_entities.clear()
        _pick_first_cell(display, edge_actor, edge_batch)
        assert bool(display.selected_entity_infos) == edge_selects
    finally:
        display.scene.close()


def test_selection_target_leaves_only_target_actors_pickable(get_remote_client, get_examples):
    """Untargeted actors drop out of hit testing so they cannot shadow a pick."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)

        display.set_selection_target(SelectionTarget.EDGES)
        for actor, batch in display._batches.items():
            expected = batch.pickable and batch.display_mesh_type in EDGE_DISPLAY_MESH_TYPES
            assert bool(actor.GetPickable()) == expected

        display.set_selection_target(SelectionTarget.BOTH)
        for actor, batch in display._batches.items():
            assert bool(actor.GetPickable()) == batch.pickable
    finally:
        display.scene.close()


def test_selection_target_keeps_entities_already_selected(get_remote_client, get_examples):
    """Switching target collects faces and edges together rather than replacing."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        face_actor, face_batch = _first_pickable_batch(display, FACE_DISPLAY_MESH_TYPES)
        edge_actor, edge_batch = _first_pickable_batch(display, EDGE_DISPLAY_MESH_TYPES)

        display.set_selection_target(SelectionTarget.FACES)
        _pick_first_cell(display, face_actor, face_batch)
        display.set_selection_target(SelectionTarget.EDGES)
        _pick_first_cell(display, edge_actor, edge_batch)

        selected = {info.display_mesh_type for info in display.selected_entity_infos}
        assert selected & set(FACE_DISPLAY_MESH_TYPES)
        assert selected & set(EDGE_DISPLAY_MESH_TYPES)
    finally:
        display.scene.close()


def test_reset_display_restores_the_opening_state(get_remote_client, get_examples):
    """A reset undoes selection, hiding, coloring, edges, and the selection target."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = PrimePlotter(allow_picking=True)
    try:
        display.add_model_pd(model_pd)
        # Showing rebuilds the backend widget list, so a reset has to survive that.
        display.show(auto_close=False)
        actor, batch = _largest_pickable_batch(display)
        cell_counts = {
            batch_actor: display._drawn_geometry[batch_actor].n_cells
            for batch_actor in display._batches
        }

        _pick_first_cell(display, actor, batch)
        assert display.selected_entity_infos
        hide_widget = next(
            widget for widget in display._prime_widgets() if isinstance(widget, HidePicked)
        )
        hide_widget.callback(True)
        display.set_color_by_type(ColorByType.PART)
        display.set_show_edges(False)
        display.set_selection_target(SelectionTarget.EDGES)

        display.reset_display()

        assert display.selected_entity_infos == []
        assert display._entity_labels == {}
        assert display._hidden_entities == set()
        assert hide_widget._hidden_entities == []
        assert display._color_type is None
        assert display._show_element_edges
        assert display.selection_target == SelectionTarget.BOTH
        assert all(
            widget._button.GetRepresentation().GetState() == 0
            for widget in display._prime_widgets()
        )
        assert all(actor.visibility for actor in display._info_actor_map)
        for batch_actor, n_cells in cell_counts.items():
            assert display._drawn_geometry[batch_actor].n_cells == n_cells
    finally:
        display.scene.close()


def _partly_meshed_model_pd():
    """Build a model where one face is meshed and another is not."""
    meshed = _synthetic_face_entry(part_id=1, entity_id=1, x_offset=-2.0, has_mesh=True)
    unmeshed = _synthetic_face_entry(part_id=2, entity_id=2, x_offset=2.0, has_mesh=False)
    return {
        1: {"faces": [meshed], "edges": [], "ctrlpts": [], "splinesurf": []},
        2: {"faces": [unmeshed], "edges": [], "ctrlpts": [], "splinesurf": []},
    }


def _button_center(widget):
    """Return the display position at the middle of a toolbar button."""
    left, bottom = widget._button_position
    return left + BUTTON_SIZE // 2, bottom + BUTTON_SIZE // 2


def test_button_tooltips_report_state_and_next_click(get_remote_client, get_examples):
    """Every Prime button carries hover text naming its state and the next click."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)

        tooltip = display._tooltip_actor
        assert tooltip is not None
        assert not tooltip.GetVisibility()

        widgets = display._prime_widgets()
        assert widgets
        for widget in widgets:
            display._update_tooltip(*_button_center(widget))
            assert tooltip.GetVisibility()
            assert tooltip.GetInput() == widget.tooltip()

        color = next(w for w in widgets if isinstance(w, ColorByTypeWidget))
        representation = color._button.GetRepresentation()
        display._update_tooltip(*_button_center(color))
        assert "Colouring by zone" in tooltip.GetInput()

        representation.SetState((representation.GetState() + 1) % len(ColorByType))
        color.callback(True)

        # The text follows the state even though the cursor has not moved.
        assert "Colouring by zonelet" in tooltip.GetInput()

        display._update_tooltip(600, 400)
        assert not tooltip.GetVisibility()
    finally:
        display.scene.close()


def test_show_edges_tooltip_names_what_is_actually_on_display(get_remote_client, get_examples):
    """The wording follows whether anything shown is meshed, unmeshed, or both."""
    model = get_remote_client.model
    _read_only(model, get_examples["elbow_lucid"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)
        assert display.has_faceting
        assert not display.has_mesh_edges
        edges = next(w for w in display._prime_widgets() if isinstance(w, ToggleEdges))

        # Nothing is meshed, so there are no mesh edges to claim to be showing.
        assert edges.tooltip() == "Showing topology.\nClick to show the CAD faceting."
        display.set_show_edges(False)
        assert edges.tooltip() == "Showing the CAD faceting.\nClick to show topology."
    finally:
        display.scene.close()

    _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)
        assert not display.has_faceting
        assert display.has_mesh_edges
        edges = next(w for w in display._prime_widgets() if isinstance(w, ToggleEdges))

        # Everything is meshed, so there is no faceting to offer.
        assert edges.tooltip() == "Showing mesh edges.\nClick to hide mesh edges."
        display.set_show_edges(False)
        assert edges.tooltip() == "Mesh edges hidden.\nClick to show mesh edges."
    finally:
        display.scene.close()

    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model_pd(_partly_meshed_model_pd())
        assert display.has_faceting
        assert display.has_mesh_edges
        edges = next(w for w in display._prime_widgets() if isinstance(w, ToggleEdges))

        # Both are present, so the button swaps one for the other.
        assert edges.tooltip() == (
            "Showing mesh edges.\nClick to show the CAD faceting of unmeshed faces."
        )
        display.set_show_edges(False)
        assert edges.tooltip() == (
            "Showing the CAD faceting of unmeshed faces.\nClick to show mesh edges."
        )
    finally:
        display.scene.close()


def test_clipping_cuts_the_view_without_altering_entities(get_remote_client, get_examples):
    """Clipping happens in the mappers, so the model itself is untouched."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)
        assert not display.clipping
        whole = _drawn_pixels(display)
        cells = {actor: batch.mesh.n_cells for actor, batch in display._batches.items()}

        display.set_clipping(True)

        assert display.clipping
        assert all(actor.GetMapper().GetNumberOfClippingPlanes() == 1 for actor in display._batches)
        # The geometry is intact; only what the mapper draws has changed.
        assert {actor: batch.mesh.n_cells for actor, batch in display._batches.items()} == cells
        assert _drawn_pixels(display) < whole

        actor, batch = _largest_pickable_batch(display)
        assert display._pick_entity(actor, batch.mesh.cell_centers().points[0])
        assert display.selected_entity_infos

        display.set_clipping(False)

        assert not display.clipping
        assert all(actor.GetMapper().GetNumberOfClippingPlanes() == 0 for actor in display._batches)
    finally:
        display.scene.close()


def test_backend_clip_slider_is_replaced(get_remote_client, get_examples):
    """The backend slider is removed, so only the Prime clip button is offered."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)

        assert not any(isinstance(widget, MeshSliderWidget) for widget in display._backend._widgets)
        assert any(isinstance(widget, ClipPlaneWidget) for widget in display._prime_widgets())
    finally:
        display.scene.close()


def test_reset_display_recovers_from_clipping(get_remote_client, get_examples):
    """Reset drops the clip plane, its widget, and the button that switched it on."""
    model = get_remote_client.model
    _read_only(model, get_examples["bracket"])
    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model(model, update=True)
        display.show(auto_close=False)
        clip = next(
            widget for widget in display._prime_widgets() if isinstance(widget, ClipPlaneWidget)
        )
        before = _drawn_pixels(display)

        clip.callback(True)
        assert display.clipping
        assert _drawn_pixels(display) < before

        display.reset_display()

        assert not display.clipping
        assert clip._button.GetRepresentation().GetState() == 0
        assert _drawn_pixels(display) == before
    finally:
        display.scene.close()


def test_reset_display_returns_the_camera_to_the_opening_view(get_remote_client, get_examples):
    """The camera goes back to the view captured when the model was first shown."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = _plot_model(model_pd)
    try:
        display.show(auto_close=False)

        # The view is only framed while showing, so the opening camera has to be
        # taken from the first render rather than read before it.
        opening = tuple(display.scene.camera_position)
        assert display._initial_camera is not None
        assert tuple(display._initial_camera) == opening

        display.scene.camera_position = "xy"
        display.scene.camera.zoom(2.5)
        assert tuple(display.scene.camera_position) != opening

        display.reset_display()
        assert tuple(display.scene.camera_position) == opening
    finally:
        display.scene.close()


def test_color_by_type_recolors_shared_meshes(get_remote_client, get_examples):
    """Changing color mode recolors cells rather than creating actors."""
    model = get_remote_client.model
    model_pd = _mesh_elbow(model, get_examples["elbow_lucid"], quadratic=False)
    display = _plot_model(model_pd)
    try:
        batch = max(display._batches.values(), key=lambda candidate: len(candidate.infos))
        actor_count = len(display.scene.actors)

        display.set_color_by_type(ColorByType.PART)
        by_part = batch.mesh.cell_data[ENTITY_COLOR_ARRAY].copy()
        part_count = len(np.unique(batch.mesh.cell_data[PART_ID_ARRAY]))
        assert len(np.unique(by_part, axis=0)) <= part_count

        display.set_color_by_type(ColorByType.ZONELET)
        by_zonelet = batch.mesh.cell_data[ENTITY_COLOR_ARRAY]
        assert len(np.unique(by_zonelet, axis=0)) > 1
        for render_id in list(batch.infos)[:5]:
            cells = batch.render_entity_ids == render_id
            assert len(np.unique(by_zonelet[cells], axis=0)) == 1

        assert len(display.scene.actors) == actor_count
    finally:
        display.scene.close()


def _synthetic_face_entry(part_id, entity_id, x_offset, has_mesh=False):
    """Create one synthetic face entry for duplicate-ID isolation tests."""
    mesh = pv.Plane(center=(x_offset, 0.0, 0.0), i_resolution=1, j_resolution=1)
    part = SimpleNamespace(id=part_id, name=f"part-{part_id}")
    mesh_object = SimpleNamespace(mesh=mesh, custom_object=part)
    info = DisplayMeshInfo(
        id=entity_id,
        part_id=part_id,
        part_name=part.name,
        zone_id=1,
        zone_name="zone",
        display_mesh_type=DisplayMeshType.FACEZONELET,
        has_mesh=has_mesh,
    )
    return mesh_object, info


def test_duplicate_entity_ids_in_different_parts_are_independent():
    """Equal entity IDs in different parts remain independently selectable and hideable."""
    first = _synthetic_face_entry(part_id=10, entity_id=7, x_offset=-2.0)
    second = _synthetic_face_entry(part_id=20, entity_id=7, x_offset=2.0)
    model_pd = {
        10: {"faces": [first], "edges": [], "ctrlpts": [], "splinesurf": []},
        20: {"faces": [second], "edges": [], "ctrlpts": [], "splinesurf": []},
    }

    display = PrimePlotter(allow_picking=False)
    try:
        display.add_model_pd(model_pd)
        assert len(display._batches) == 1
        actor, batch = next(iter(display._batches.items()))
        assert len(batch.infos) == 2

        first_key = DisplayEntityKey(10, DisplayMeshType.FACEZONELET, 7)
        second_key = DisplayEntityKey(20, DisplayMeshType.FACEZONELET, 7)
        assert set(display.entity_infos) == {first_key, second_key}

        cell_by_key = {
            info.key: int(np.flatnonzero(batch.render_entity_ids == render_id)[0])
            for render_id, info in batch.infos.items()
        }
        centers = batch.mesh.cell_centers().points
        assert display._pick_entity(actor, centers[cell_by_key[first_key]])
        assert set(display.picked_entities) == {first_key}

        display.set_entities_visible([first_key], False)
        drawn_keys = _keys_in_mesh(batch, display._drawn_geometry[actor])
        assert first_key not in drawn_keys
        assert second_key in drawn_keys

        display.set_entities_visible([first_key], True)
        assert _keys_in_mesh(batch, display._drawn_geometry[actor]) == {
            first_key,
            second_key,
        }
    finally:
        display.scene.close()


def test_compute_distance():
    """Test Euclidean distance."""
    assert compute_distance(point1=[1, 1, 3], point2=[1, 1, 1]) == 2.0


def test_compute_face_list():
    """Test structured-node face-list generation."""
    assert len(compute_face_list_from_structured_nodes([2, 2, 2])) == 30
