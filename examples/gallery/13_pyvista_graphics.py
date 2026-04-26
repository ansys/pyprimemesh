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

"""
.. _ref_pyvista_graphics:

=========================================
Using PyVista for Graphics in PyPrimeMesh
=========================================

**Summary**: This example demonstrates how to visualize all aspects of the
PyPrimeMesh data model with fine-grained control using PyVista, through the
``PrimePlotter`` API and direct scene access.

The pipe tee junction model is used to show six visualization stages:

1. **High-level plotting** — ``plotter.show(model)`` for quick visualization
2. **Zone name visualization** — face and volume zones colored distinctly with
   bounding boxes, names, and a legend
3. **Label visualization** — CAD labels mapped to TopoFace IDs with bounding
   boxes, labels, and a legend
4. **Scope-based plotting** — ``ScopeDefinition`` to selectively display only
   labeled inlet/outlet faces
5. **Face zonelet visualization** — post-meshing face zonelets with distinct
   colors and ID annotations
6. **Per-element face coloring** — individual mesh face cells colored uniquely
   via ``cell_data`` scalars

Key data model concepts demonstrated:

- **DisplayMeshType** filtering (``TOPOFACE``, ``TOPOEDGE``, ``FACEZONELET``,
  ``EDGEZONELET``) to distinguish entity types
- **DisplayMeshInfo** metadata (``id``, ``zone_name``, ``has_mesh``,
  ``display_mesh_type``) preserved through ``info_actor_map``
- **Labels vs Zones**: labels are overlapping CAD metadata queried via
  ``Part.get_labels()``; zones are non-overlapping mesh groupings from
  ``Part.get_face_zones()`` / ``Part.get_volume_zones()``
- **Polydata access**: ``model.as_polydata()`` returns a dict keyed by part ID
  with ``"faces"`` (tuples of ``MeshObjectPlot, DisplayMeshInfo``),
  ``"edges"`` (``MeshObjectPlot``), ``"ctrlpts"``, and ``"splinesurf"`` lists
- **Scene-level control**: direct ``scene.add_mesh()`` / ``add_point_labels()``
  for full PyVista parameter access
"""
import colorsys

import ansys.meshing.prime as prime
import numpy as np
import pyvista as pv
from ansys.meshing.prime.core.mesh import DisplayMeshType
from ansys.meshing.prime.graphics import PrimePlotter


def make_distinct_colors(n):
    """Generate n maximally distinct colors using HSV spacing."""
    colors = {}
    for i in range(n):
        hue = i / max(n, 1)
        rgb = colorsys.hsv_to_rgb(hue, 0.85, 0.95)
        colors[i] = list(rgb)
    return colors


# Launch Prime server and initialize model
prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model)

# Load pipe tee CAD geometry
pipe_tee = prime.examples.download_pipe_tee_fmd()
mesh_util.read(file_name=pipe_tee)

# ============================================================================
# PLOT 1: HIGH-LEVEL — plotter.show(model)
# ============================================================================
# The simplest way to visualize a model: one line of code.
# PrimePlotter.show() accepts a Model directly and plots all entities
# using the default color scheme (zone-based coloring with edge visibility
# determined by has_mesh).

plotter = PrimePlotter()
plotter._backend.pv_interface.scene.add_text(
    "Plot 1 \u2014 High-Level: plotter.show(model)",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(model, title="Plot 1 — High-Level: plotter.show(model)")

# ============================================================================
# PLOT 2: ZONE NAME VISUALIZATION (face zones + volume zones)
# ============================================================================
# Demonstrates:
#   - Querying face and volume zones via Part.get_face_zones() / get_volume_zones()
#   - Mapping zone IDs to names via model.get_zone_name()
#   - Custom coloring per zone with bounding boxes and point labels
#   - Legend showing all zone names (volume zones annotated)

plotter = PrimePlotter()
graphics_data = model.as_polydata()

# Collect all zone names from parts, and build zone_id -> zone_name map
all_zone_names = set()
volume_zone_info = {}
zone_id_to_name = {}
for part in model.parts:
    for fz_id in part.get_face_zones():
        name = model.get_zone_name(fz_id)
        if name:
            all_zone_names.add(name)
            zone_id_to_name[fz_id] = name
    for vz_id in part.get_volume_zones():
        name = model.get_zone_name(vz_id)
        if name:
            all_zone_names.add(name)
            volume_zone_info[name] = vz_id
            zone_id_to_name[vz_id] = name

# For faces without a zone name, generate an auto-name from zone_id or part
auto_zone_counter = 0

# Assign distinct colors
zone_list = sorted(all_zone_names)
zone_color_map = make_distinct_colors(max(len(zone_list), 1))
zone_colors = {name: zone_color_map[i] for i, name in enumerate(zone_list)}

# Add faces colored by zone; collect meshes for bounding boxes
zone_face_meshes = {}
for part_id, part_data in graphics_data.items():
    for entity_type, entity_list in part_data.items():
        if entity_type == "faces":
            for item in entity_list:
                if item is None:
                    continue
                polydata, metadata = item
                # Resolve zone name: prefer metadata.zone_name, then zone_id lookup
                zname = metadata.zone_name
                if not zname and metadata.zone_id:
                    zname = zone_id_to_name.get(metadata.zone_id)
                if not zname:
                    # Auto-name for faces with no zone assignment
                    zname = f"zone_{metadata.zone_id}" if metadata.zone_id else metadata.part_name
                    if zname not in zone_colors:
                        hue = (len(zone_colors) * 0.618) % 1.0  # golden ratio spacing
                        rgb = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
                        zone_colors[zname] = list(rgb)
                        zone_list.append(zname)
                color = zone_colors.get(zname, [0.5, 0.5, 0.5])
                zone_face_meshes.setdefault(zname, []).append(polydata.mesh)
                plotter.add_entity_with_attributes(
                    polydata, metadata, color=color, opacity=1.0, show_edges=False
                )
        elif entity_type == "edges":
            for edge_obj in entity_list:
                if edge_obj is None:
                    continue
                scene = plotter._backend.pv_interface.scene
                scene.add_mesh(edge_obj.mesh, color=[0.3, 0.3, 0.3], line_width=2, pickable=False)

# Add bounding boxes and labels for zones that have face geometry
scene = plotter._backend.pv_interface.scene
for zname, meshes in zone_face_meshes.items():
    combined = meshes[0] if len(meshes) == 1 else meshes[0].merge(meshes[1:])
    bounds = combined.bounds
    bbox = pv.Box(bounds)
    color = zone_colors[zname]
    scene.add_mesh(bbox, color=color, style="wireframe", line_width=2, pickable=False)
    center = [
        (bounds[0] + bounds[1]) / 2,
        (bounds[2] + bounds[3]) / 2,
        bounds[5],
    ]
    scene.add_point_labels(
        np.array([center]),
        [zname],
        font_size=16,
        text_color=color,
        bold=True,
        shape=None,
        render_points_as_spheres=False,
        point_size=0,
    )

# Legend with face and volume zones distinguished
legend_entries = []
for zname in zone_list:
    suffix = " (volume)" if zname in volume_zone_info else ""
    legend_entries.append([zname + suffix, zone_colors[zname]])
scene.add_legend(legend_entries, bcolor="white", border=True, size=(0.2, 0.35))
scene.add_text(
    "Plot 2 \u2014 Zone Names (Face & Volume)",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(title="Plot 2 — Zone Names (Face & Volume)")

# ============================================================================
# PLOT 3: LABEL VISUALIZATION (CAD labels → TopoFace IDs)
# ============================================================================
# Demonstrates:
#   - Querying labels via Part.get_labels()
#   - Resolving label → TopoFace IDs via get_topo_faces_of_label_name_pattern()
#   - Matching metadata.id to TopoFace IDs for coloring
#   - Filtering by DisplayMeshType.TOPOFACE and TOPOEDGE

plotter = PrimePlotter()
graphics_data = model.as_polydata()

# Build label → TopoFace ID mapping
label_topoface_map = {}
for part in model.parts:
    for label in part.get_labels():
        topo_face_ids = part.get_topo_faces_of_label_name_pattern(
            label, prime.NamePatternParams(model)
        )
        if topo_face_ids:
            label_topoface_map.setdefault(label, set()).update(topo_face_ids)

# Reverse map: TopoFace ID → label
topoface_label_map = {}
for label, topo_ids in label_topoface_map.items():
    for tid in topo_ids:
        topoface_label_map.setdefault(tid, label)

# Assign distinct colors
label_list = sorted(label_topoface_map.keys())
label_color_map = make_distinct_colors(len(label_list))
label_colors = {name: label_color_map[i] for i, name in enumerate(label_list)}

# Add faces and edges, filtering by DisplayMeshType
label_face_meshes = {}
for part_id, part_data in graphics_data.items():
    for entity_type, entity_list in part_data.items():
        if entity_type == "faces":
            for item in entity_list:
                if item is None:
                    continue
                polydata, metadata = item
                # Use DisplayMeshType to confirm this is a topology face
                if metadata.display_mesh_type == DisplayMeshType.TOPOFACE:
                    face_label = topoface_label_map.get(metadata.id)
                    if face_label and face_label in label_colors:
                        color = label_colors[face_label]
                        opacity = 1.0
                        label_face_meshes.setdefault(face_label, []).append(polydata.mesh)
                    else:
                        color = [0.5, 0.5, 0.5]
                        opacity = 0.3
                    plotter.add_entity_with_attributes(
                        polydata, metadata, color=color, opacity=opacity, show_edges=False
                    )
        elif entity_type == "edges":
            for edge_obj in entity_list:
                if edge_obj is None:
                    continue
                scene = plotter._backend.pv_interface.scene
                scene.add_mesh(edge_obj.mesh, color=[0.2, 0.2, 0.2], line_width=2, pickable=False)

# Bounding boxes and labels
scene = plotter._backend.pv_interface.scene
for label_name, meshes in label_face_meshes.items():
    combined = meshes[0] if len(meshes) == 1 else meshes[0].merge(meshes[1:])
    bounds = combined.bounds
    bbox = pv.Box(bounds)
    color = label_colors[label_name]
    scene.add_mesh(bbox, color=color, style="wireframe", line_width=2, pickable=False)
    center = [
        (bounds[0] + bounds[1]) / 2,
        (bounds[2] + bounds[3]) / 2,
        bounds[5],
    ]
    scene.add_point_labels(
        np.array([center]),
        [label_name],
        font_size=16,
        text_color=color,
        bold=True,
        shape=None,
        render_points_as_spheres=False,
        point_size=0,
    )

# Legend
legend_entries = [[name, label_colors[name]] for name in label_list]
legend_entries.append(["unlabeled", [0.5, 0.5, 0.5]])
scene.add_legend(legend_entries, bcolor="white", border=True, size=(0.2, 0.3))
scene.add_text(
    "Plot 3 \u2014 CAD Labels on TopoFaces",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(title="Plot 3 — CAD Labels on TopoFaces")

# ============================================================================
# PLOT 4: SCOPE-BASED PLOTTING
# ============================================================================
# Demonstrates:
#   - ScopeDefinition with label_expression to select specific entities
#   - plotter.plot(model, scope=scope) for selective display
#   - Combining scoped plots with different visual styles

plotter = PrimePlotter()

# Show only inlet and outlet faces using label-based scoping
scope_inlets = prime.ScopeDefinition(model, label_expression="in1_inlet,in2_inlet,outlet_main")
plotter.plot(model, scope=scope_inlets)
plotter._backend.pv_interface.scene.add_text(
    "Plot 4 \u2014 Scope-Based: Inlet & Outlet Faces Only",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(title="Plot 4 — Scope-Based: Inlet & Outlet Faces Only")

# ============================================================================
# MESHING — wrap, surface mesh, volume mesh
# ============================================================================

mesh_util.wrap(min_size=6, region_extract=prime.WrapRegion.LARGESTINTERNAL)
model.set_global_sizing_params(prime.GlobalSizingParams(model, min=6, max=50))
mesh_util.create_zones_from_labels("outlet_main,in1_inlet,in2_inlet")
mesh_util.surface_mesh(min_size=5, max_size=20)
mesh_util.volume_mesh(
    prism_layers=5,
    prism_surface_expression="* !*inlet* !*outlet*",
    volume_fill_type=prime.VolumeFillType.POLY,
)

# ============================================================================
# PLOT 5: FACE ZONELET VISUALIZATION (post-meshing)
# ============================================================================
# Demonstrates:
#   - update=True on as_polydata() to refresh after meshing
#   - Filtering by DisplayMeshType.FACEZONELET and has_mesh=True
#   - Distinct color per face zonelet with ID annotations
#   - Direct scene.add_point_labels() for face zonelet IDs

plotter = PrimePlotter()
volume_graphics_data = model.as_polydata(update=True)

# Collect meshed face zonelets
zonelet_items = []
for part_id, part_data in volume_graphics_data.items():
    for entity_type, entity_list in part_data.items():
        if entity_type == "faces":
            for item in entity_list:
                if item is None:
                    continue
                polydata, metadata = item
                if metadata.has_mesh and metadata.display_mesh_type == DisplayMeshType.FACEZONELET:
                    zonelet_items.append((polydata, metadata))

# Assign distinct colors and add ID labels
zonelet_color_map = make_distinct_colors(len(zonelet_items))
scene = plotter._backend.pv_interface.scene
for i, (polydata, metadata) in enumerate(zonelet_items):
    color = zonelet_color_map[i]
    plotter.add_entity_with_attributes(
        polydata,
        metadata,
        color=color,
        opacity=1.0,
        show_edges=True,
        line_width=0.5,
    )
    # Annotate each face zonelet with its ID at the mesh center
    center = np.array(polydata.mesh.center)
    scene.add_point_labels(
        np.array([center]),
        [str(metadata.id)],
        font_size=12,
        text_color="black",
        bold=True,
        shape=None,
        render_points_as_spheres=False,
        point_size=0,
    )
scene.add_text(
    "Plot 5 \u2014 Face Zonelets with IDs",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(title="Plot 5 — Face Zonelets with IDs")

# ============================================================================
# PLOT 6: PER-ELEMENT FACE COLORING
# ============================================================================
# Demonstrates:
#   - Assigning per-cell RGB scalars via cell_data on a copy of the mesh
#   - Direct scene.add_mesh() with scalars='RGB' and rgb=True
#   - Preserving metadata linkage via info_actor_map

plotter = PrimePlotter()
scene = plotter._backend.pv_interface.scene

for part_id, part_data in volume_graphics_data.items():
    for entity_type, entity_list in part_data.items():
        if entity_type == "faces":
            for item in entity_list:
                if item is None:
                    continue
                polydata, metadata = item
                if metadata.has_mesh:
                    # Copy to avoid mutating cached polydata
                    mesh_copy = polydata.mesh.copy()
                    n_cells = mesh_copy.n_cells
                    if n_cells > 0:
                        cell_colors = np.random.randint(0, 256, size=(n_cells, 3), dtype=np.uint8)
                        mesh_copy.cell_data["RGB"] = cell_colors
                        actor = scene.add_mesh(
                            mesh_copy,
                            scalars="RGB",
                            rgb=True,
                            show_edges=True,
                            line_width=0.5,
                            pickable=True,
                        )
                        plotter._info_actor_map[actor] = metadata
scene.add_text(
    "Plot 6 \u2014 Per-Element Face Colors",
    position="upper_left",
    font_size=10,
    color="black",
)
plotter.show(title="Plot 6 — Per-Element Face Colors")

# ============================================================================
# MESH STATISTICS
# ============================================================================

part = model.get_part_by_name("__wrap__")
part_summary = part.get_summary(prime.PartSummaryParams(model=model))
print("Volume Mesh Statistics:")
print(f"  Poly faces: {part_summary.n_poly_faces}")
print(f"  Poly cells: {part_summary.n_poly_cells}")

prime_client.exit()
