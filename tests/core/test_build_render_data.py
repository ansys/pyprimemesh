# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT

"""Tests for the fast render-data build path."""

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    build_edge_render_batches,
    build_element_edge_batches,
    build_face_render_batches,
)


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
