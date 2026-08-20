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
"""Module for the Prime plotter."""

import warnings
from typing import Any, Dict, Iterable, List, Optional, Sequence

import numpy as np
import pyvista as pv
from ansys.tools.visualization_interface import Plotter
from ansys.tools.visualization_interface.backends.pyvista import PyVistaBackend
from ansys.tools.visualization_interface.utils.color import Color

import ansys.meshing.prime as prime

# Kept importable from here for callers that build their own coloring.
from ansys.meshing.prime.core.mesh import color_matrix  # noqa: F401
from ansys.meshing.prime.core.mesh import (
    ENTITY_COLOR_ARRAY,
    RENDER_ENTITY_ID_ARRAY,
    ColorByType,
    DisplayEntityKey,
    DisplayMeshInfo,
    DisplayMeshType,
    ModelRenderData,
    RenderBatch,
    build_edge_render_batches,
    build_element_edge_batches,
    build_face_render_batches,
    compute_entity_colors,
    entity_color,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.graphics.widgets.color_by_type import ColorByTypeWidget
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked
from ansys.meshing.prime.graphics.widgets.picked_info import PickedInfo
from ansys.meshing.prime.graphics.widgets.toggle_edges import ToggleEdges

# Depth-buffer offset applied to a face actor when element outlines are drawn as
# separate line geometry.
POLYGON_OFFSET_FACTOR = 1.0
POLYGON_OFFSET_UNITS = 1.0


class _EntityPickingBackend(PyVistaBackend):
    """Resolve a PyVista actor pick to the Prime entity under the cursor."""

    prime_plotter = None

    def picker_callback(self, actor: "pv.Actor") -> None:
        """Select the Prime display entity under the cursor."""
        plotter = self.prime_plotter
        picked_point = getattr(self._pl.scene, "picked_point", None)
        if plotter is not None and plotter._pick_entity(actor, picked_point):
            return
        super().picker_callback(actor)


class PrimePlotter(Plotter):
    """Create a plotter for PyPrimeMesh models.

    Geometry from every displayed part is merged by display entity type. The
    resulting actor count therefore depends on the populated rendering types,
    not on the number of parts or zonelets. Per-cell metadata retains part,
    entity, type, and zone identity for picking, coloring, and visibility.

    Parameters
    ----------
    use_trame : bool, optional
        Whether to use the Trame visualizer.
    allow_picking : bool, default: True
        Whether to allow picking.
    """

    def __init__(
        self,
        use_trame: Optional[bool] = None,
        allow_picking: Optional[bool] = True,
    ) -> None:
        """Initialize the plotter."""
        self._backend = _EntityPickingBackend(
            use_trame=use_trame,
            allow_picking=allow_picking,
        )
        self._backend.prime_plotter = self
        super().__init__(backend=self._backend)
        self._reset_prime_state()
        self._add_widgets()

    def _reset_prime_state(self) -> None:
        """Reset all Prime-specific rendering state."""
        self._info_actor_map: Dict[Any, DisplayMeshInfo] = {}
        self._batches: Dict[Any, RenderBatch] = {}
        self._element_edge_batches: Dict[Any, RenderBatch] = {}
        self._spline_actors: Dict[DisplayMeshType, Any] = {}
        self._entity_infos: Dict[DisplayEntityKey, DisplayMeshInfo] = {}
        self._picked_entities: Dict[DisplayEntityKey, DisplayMeshInfo] = {}
        self._picked_points: Dict[DisplayEntityKey, np.ndarray] = {}
        self._entity_labels: Dict[DisplayEntityKey, Any] = {}
        self._hidden_entities: set[DisplayEntityKey] = set()
        self._drawn_geometry: Dict[Any, pv.DataSet] = {}
        self._color_type: Optional[ColorByType] = None
        self._show_element_edges = True

    def _add_widgets(self) -> None:
        """Attach the PyPrimeMesh widgets to the backend."""
        self._backend.add_widget(ToggleEdges(self))
        self._backend.add_widget(ColorByTypeWidget(self))
        self._backend.add_widget(HidePicked(self))
        self._backend.add_widget(PickedInfo(self))

    @property
    def info_actor_map(self) -> Dict:
        """Return metadata for individually added actors."""
        return self._info_actor_map

    @info_actor_map.setter
    def info_actor_map(self, value: Dict) -> None:
        """Set metadata for individually added actors."""
        self._info_actor_map = value

    @property
    def element_edge_actors(self) -> Dict:
        """Return element-outline actors keyed by actor."""
        return self._element_edge_batches

    @property
    def scene(self):
        """Return the underlying PyVista scene."""
        return self._backend.pv_interface.scene

    @property
    def entity_infos(self) -> Dict[DisplayEntityKey, DisplayMeshInfo]:
        """Return all displayed entities keyed by model-unique entity key."""
        return self._entity_infos

    @property
    def picked_entities(self) -> Dict[DisplayEntityKey, DisplayMeshInfo]:
        """Return picked entities keyed by model-unique entity key."""
        return self._picked_entities

    def get_scalar_colors(self, mesh_info: DisplayMeshInfo) -> np.ndarray:
        """Return the default scalar color for a display entity."""
        return entity_color(mesh_info).tolist()

    def add_mesh(self, mesh, metadata=None, **pyvista_kwargs):
        """Add a raw mesh or ``MeshObjectPlot`` with optional metadata."""
        mesh = mesh.mesh if hasattr(mesh, "mesh") else mesh
        actor = self.scene.add_mesh(mesh, **pyvista_kwargs)
        if metadata is not None:
            self._info_actor_map[actor] = metadata
        return actor

    def add_point_labels(self, points, labels, **kwargs):
        """Add point labels to the scene."""
        return self.scene.add_point_labels(points, labels, **kwargs)

    def add_legend(self, entries, **kwargs):
        """Add a legend to the scene."""
        return self.scene.add_legend(entries, **kwargs)

    def add_text(self, text, **kwargs):
        """Add text annotation to the scene."""
        return self.scene.add_text(text, **kwargs)

    def add_model(
        self,
        model: Model,
        scope: prime.ScopeDefinition = None,
        update: bool = False,
    ) -> None:
        """Add a Prime model or a scoped subset to the plotter."""
        if scope is None:
            self.add_render_data(model.build_render_data(update=update))
        else:
            self.add_scope(model, scope, update=update)

    def add_render_data(self, render_data: ModelRenderData) -> None:
        """Add pre-built model-wide render batches to the plotter."""
        self._add_render_batches(render_data.batches)
        self._add_spline_batch(
            render_data.ctrlpts,
            DisplayMeshType.SPLINECONTROLPOINTS,
        )
        self._add_spline_batch(
            render_data.splines,
            DisplayMeshType.SPLINESURFACE,
        )

    @staticmethod
    def _entries(model_pd: Dict, key: str) -> List:
        """Collect one stored geometry category across all parts."""
        output = []
        for part_polydata in model_pd.values():
            output.extend(entry for entry in part_polydata.get(key, []) if entry is not None)
        return output

    def add_model_pd(self, model_pd: Dict) -> None:
        """Add part-organized PolyData using model-wide entity-type actors."""
        face_entries = self._entries(model_pd, "faces")
        edge_entries = self._entries(model_pd, "edges")
        control_point_entries = self._entries(model_pd, "ctrlpts")
        spline_surface_entries = self._entries(model_pd, "splinesurf")

        self._add_face_batches(face_entries)
        self._add_edge_batches(edge_entries)
        self._add_element_edge_batches(face_entries)
        self._add_spline_batch(
            control_point_entries,
            DisplayMeshType.SPLINECONTROLPOINTS,
        )
        self._add_spline_batch(
            spline_surface_entries,
            DisplayMeshType.SPLINESURFACE,
        )

    def _add_render_batches(
        self,
        batches: Dict[str, Dict[DisplayMeshType, RenderBatch]],
    ) -> None:
        """Add pre-built model-wide batches to the scene."""
        for batch in batches.get("faces", {}).values():
            actor = self.scene.add_mesh(
                batch.mesh,
                scalars=ENTITY_COLOR_ARRAY,
                rgb=True,
                show_edges=False,
                pickable=batch.pickable,
            )
            self._offset_polygons(actor)
            self._register_batch(actor, batch)

        for batch in batches.get("edges", {}).values():
            has_colors = ENTITY_COLOR_ARRAY in batch.mesh.cell_data
            actor = self.scene.add_mesh(
                batch.mesh,
                scalars=ENTITY_COLOR_ARRAY if has_colors else None,
                rgb=has_colors,
                pickable=batch.pickable,
                line_width=4,
            )
            self._register_batch(actor, batch)

        for batch in batches.get("element_edges", {}).values():
            actor = self.scene.add_mesh(
                batch.mesh,
                color=pv.global_theme.edge_color,
                line_width=1,
                pickable=False,
            )
            self._element_edge_batches[actor] = batch
            self._drawn_geometry[actor] = batch.mesh

    def _register_batch(self, actor, batch: RenderBatch) -> None:
        """Register a persistent actor and all entities in its batch."""
        self._batches[actor] = batch
        self._drawn_geometry[actor] = batch.mesh
        for info in batch.infos.values():
            self._entity_infos[info.key] = info

    def _add_face_batches(self, face_entries: Sequence) -> None:
        """Add at most one shaded actor for each face entity type."""
        for batch in build_face_render_batches(face_entries).values():
            actor = self.scene.add_mesh(
                batch.mesh,
                scalars=ENTITY_COLOR_ARRAY,
                rgb=True,
                show_edges=False,
                pickable=batch.pickable,
            )
            self._offset_polygons(actor)
            self._register_batch(actor, batch)

    def _add_edge_batches(self, edge_entries: Sequence) -> None:
        """Add at most one line actor for each edge entity type."""
        for batch in build_edge_render_batches(edge_entries).values():
            has_colors = ENTITY_COLOR_ARRAY in batch.mesh.cell_data
            actor = self.scene.add_mesh(
                batch.mesh,
                scalars=ENTITY_COLOR_ARRAY if has_colors else None,
                rgb=has_colors,
                pickable=batch.pickable,
                line_width=4,
            )
            self._register_batch(actor, batch)

    def _add_element_edge_batches(self, face_entries: Sequence) -> None:
        """Add at most one element-outline actor for each face entity type."""
        for batch in build_element_edge_batches(face_entries).values():
            actor = self.scene.add_mesh(
                batch.mesh,
                color=pv.global_theme.edge_color,
                line_width=1,
                pickable=False,
            )
            self._element_edge_batches[actor] = batch
            self._drawn_geometry[actor] = batch.mesh

    @staticmethod
    def _merge_mesh_objects(entries: Sequence) -> Optional[pv.PolyData]:
        """Merge ``MeshObjectPlot`` meshes without merging points."""
        meshes = [
            entry.mesh
            for entry in entries
            if entry is not None
            and getattr(entry, "mesh", None) is not None
            and entry.mesh.n_cells > 0
        ]
        if not meshes:
            return None
        if len(meshes) == 1:
            return meshes[0].copy(deep=False)
        return pv.merge(meshes, merge_points=False)

    def _add_spline_batch(
        self,
        entries: Sequence,
        display_mesh_type: DisplayMeshType,
    ) -> None:
        """Add one non-pickable actor for a spline rendering type."""
        merged = self._merge_mesh_objects(entries)
        if merged is None:
            return

        is_control_points = display_mesh_type == DisplayMeshType.SPLINECONTROLPOINTS
        has_colors = ENTITY_COLOR_ARRAY in merged.cell_data
        actor = self.scene.add_mesh(
            merged,
            scalars=ENTITY_COLOR_ARRAY if has_colors else None,
            rgb=has_colors,
            show_edges=False,
            pickable=False,
            style="wireframe" if is_control_points else "surface",
            edge_color=[0, 0, 255] if is_control_points else None,
        )
        self._spline_actors[display_mesh_type] = actor
        self._drawn_geometry[actor] = merged

    @staticmethod
    def _offset_polygons(actor) -> None:
        """Push shaded surfaces back so coincident line geometry stays visible."""
        mapper = actor.GetMapper()
        mapper.SetResolveCoincidentTopologyToPolygonOffset()
        mapper.SetRelativeCoincidentTopologyPolygonOffsetParameters(
            POLYGON_OFFSET_FACTOR,
            POLYGON_OFFSET_UNITS,
        )

    @staticmethod
    def _info_from_cell(batch: RenderBatch, mesh: pv.DataSet, cell_id: int):
        """Resolve a cell in a displayed dataset to its batch metadata."""
        if RENDER_ENTITY_ID_ARRAY not in mesh.cell_data:
            return None
        render_id = int(mesh.cell_data[RENDER_ENTITY_ID_ARRAY][cell_id])
        return batch.infos.get(render_id)

    def _pick_entity(self, actor, point) -> bool:
        """Toggle the model-unique entity under a picked point."""
        batch = self._batches.get(actor)
        if batch is None or not batch.pickable or point is None:
            return False

        mesh = self._drawn_geometry.get(actor)
        if mesh is None or mesh.n_cells == 0:
            return True

        cell_id = int(mesh.find_closest_cell(np.asarray(point, dtype=float)))
        if cell_id < 0:
            return True

        info = self._info_from_cell(batch, mesh, cell_id)
        if info is None:
            return True

        key = info.key
        if key in self._picked_entities:
            self._picked_entities.pop(key, None)
            self._picked_points.pop(key, None)
            self._remove_entity_label(key)
        else:
            self._picked_entities[key] = info
            self._picked_points[key] = np.asarray(point, dtype=float)
            self._add_entity_label(key)

        self.refresh_colors()
        return True

    @staticmethod
    def entity_label(info: DisplayMeshInfo) -> str:
        """Return the label text for a picked entity."""
        name = info.zone_name or info.part_name
        return f"{name} ({info.id})" if name else str(info.id)

    def _add_entity_label(self, key: DisplayEntityKey) -> None:
        """Label a visible picked entity at its picked point."""
        point = self._picked_points.get(key)
        info = self._entity_infos.get(key)
        if point is None or info is None or key in self._entity_labels:
            return
        if key in self._hidden_entities:
            return
        if not getattr(self._backend, "_plot_picked_names", True):
            return

        self._entity_labels[key] = self.scene.add_point_labels(
            [point],
            [self.entity_label(info)],
            always_visible=True,
            point_size=0,
            render_points_as_spheres=False,
            show_points=False,
        )

    def _remove_entity_label(self, key: DisplayEntityKey) -> None:
        """Remove an entity label if present."""
        label = self._entity_labels.pop(key, None)
        if label is not None:
            self.scene.remove_actor(label)

    def _update_entity_labels(self) -> None:
        """Synchronize labels with selection and visibility state."""
        for key in list(self._entity_labels):
            if key in self._hidden_entities or key not in self._picked_entities:
                self._remove_entity_label(key)
        for key in self._picked_entities:
            self._add_entity_label(key)

    @staticmethod
    def _render_ids_for_keys(batch: RenderBatch, keys: Iterable[DisplayEntityKey]) -> set[int]:
        """Return batch-local render IDs corresponding to model entity keys."""
        wanted = set(keys)
        return {int(render_id) for render_id, info in batch.infos.items() if info.key in wanted}

    def refresh_colors(self) -> None:
        """Recolor every shared actor from current mode and selection."""
        highlight = np.asarray(
            pv.Color(Color.PICKED.value).int_rgb,
            dtype=np.uint8,
        )

        for batch in self._batches.values():
            colors = compute_entity_colors(
                batch.infos,
                batch.render_entity_ids,
                self._color_type,
            )
            selected_render_ids = self._render_ids_for_keys(
                batch,
                self._picked_entities,
            )
            if selected_render_ids:
                selected = np.isin(
                    batch.render_entity_ids,
                    tuple(selected_render_ids),
                )
                colors[selected] = highlight
            batch.mesh.cell_data[ENTITY_COLOR_ARRAY] = colors
            batch.mesh.set_active_scalars(ENTITY_COLOR_ARRAY, preference="cell")

        self._apply_visibility()

    def set_color_by_type(self, color_type: "ColorByType") -> None:
        """Color displayed entities by zone, zonelet, or part."""
        self._color_type = ColorByType(color_type)
        for actor, info in self._info_actor_map.items():
            actor.prop.color = entity_color(info, self._color_type).tolist()
        self.refresh_colors()

    @property
    def selected_entity_infos(self) -> List[DisplayMeshInfo]:
        """Return metadata for all currently picked entities."""
        infos = list(self._picked_entities.values())

        custom_picker = getattr(self._backend, "_custom_picker", None)
        picked = getattr(custom_picker, "picked_dict", {})
        for mesh_object in picked.values():
            actor = getattr(mesh_object, "actor", None)
            info = self._info_actor_map.get(actor)
            if info is not None:
                infos.append(info)
        return infos

    def _normalise_entity_keys(self, entities: Iterable) -> set[DisplayEntityKey]:
        """Normalize entity keys while retaining limited ID compatibility."""
        keys: set[DisplayEntityKey] = set()
        integer_ids = set()
        for entity in entities:
            if isinstance(entity, DisplayEntityKey):
                keys.add(entity)
            elif isinstance(entity, DisplayMeshInfo):
                keys.add(entity.key)
            else:
                integer_ids.add(int(entity))

        if integer_ids:
            keys.update(key for key in self._entity_infos if key.entity_id in integer_ids)
        return keys

    def set_entities_visible(self, entities, visible: bool) -> None:
        """Show or hide display entities without changing actor count."""
        keys = self._normalise_entity_keys(entities)
        if visible:
            self._hidden_entities.difference_update(keys)
        else:
            self._hidden_entities.update(keys)

        for actor, info in self._info_actor_map.items():
            if info.key in keys:
                actor.visibility = visible
        self._apply_visibility()

    def _visible_geometry(self, batch: RenderBatch) -> pv.DataSet:
        """Return a batch dataset excluding hidden entities."""
        hidden_render_ids = self._render_ids_for_keys(
            batch,
            self._hidden_entities,
        )
        if not hidden_render_ids:
            return batch.mesh

        hidden = np.isin(
            batch.render_entity_ids,
            tuple(hidden_render_ids),
        )
        if not hidden.any():
            return batch.mesh
        return batch.mesh.remove_cells(np.flatnonzero(hidden), inplace=False)

    def _draw(self, actor, mesh: pv.DataSet) -> None:
        """Assign live geometry to an actor and keep a strong reference."""
        self._drawn_geometry[actor] = mesh
        if mesh.n_cells == 0:
            actor.visibility = False
            return
        actor.mapper.dataset = mesh
        actor.visibility = True

    def _apply_visibility(self) -> None:
        """Update mapper inputs for hidden Prime entities."""
        for actor, batch in self._batches.items():
            self._draw(actor, self._visible_geometry(batch))

        for actor, batch in self._element_edge_batches.items():
            visible = self._visible_geometry(batch)
            self._draw(actor, visible)
            actor.visibility = bool(self._show_element_edges and visible.n_cells > 0)

        self._update_entity_labels()
        self.render()

    def set_show_edges(self, show: bool) -> None:
        """Show or hide model-wide element-outline actors."""
        self._show_element_edges = bool(show)
        for actor in self._element_edge_batches:
            mesh = self._drawn_geometry.get(actor)
            actor.visibility = bool(show and mesh is not None and mesh.n_cells > 0)
        for actor, info in self._info_actor_map.items():
            if info.has_mesh:
                actor.prop.show_edges = bool(show)
        self.render()

    def render(self) -> None:
        """Redraw the scene if it is already on screen."""
        scene = self.scene
        if scene is not None and getattr(scene, "render_window", None) is not None:
            scene.render()

    def clear(self) -> None:
        """Remove scene contents and reset Prime-specific state."""
        super().clear()
        self._backend.prime_plotter = self
        self._reset_prime_state()
        self._add_widgets()

    def add_scope(
        self,
        model: Model,
        scope: prime.ScopeDefinition,
        update: bool = False,
    ) -> None:
        """Add a scoped subset of a model."""
        self.add_render_data(model.get_scoped_render_data(scope, update=update))

    def plot_iter(
        self,
        plotting_list: List[Any],
        name_filter: str = None,
        update: bool = False,
        **plotting_options,
    ) -> None:
        """Add a list of PyPrime models or PyVista objects to the scene."""
        for plottable_object in plotting_list:
            self.plot(
                plottable_object,
                name_filter=name_filter,
                update=update,
                **plotting_options,
            )

    def plot(
        self,
        plottable_object: Any,
        scope: prime.ScopeDefinition = None,
        name_filter: str = None,
        update: bool = False,
        **plotting_options,
    ):
        """Add a Prime model or PyVista plottable object."""
        if isinstance(plottable_object, Model):
            self.add_model(plottable_object, scope, update=update)
        elif isinstance(plottable_object, list):
            self.plot_iter(
                plottable_object,
                name_filter=name_filter,
                update=update,
                **plotting_options,
            )
        else:
            self._backend.pv_interface.plot(
                plottable_object,
                name_filter,
                **plotting_options,
            )

    def show(
        self,
        plottable_object: Any = None,
        screenshot: str = None,
        name_filter: str = None,
        scope: prime.ScopeDefinition = None,
        **plotting_options,
    ) -> None:
        """Show plotted content and optionally save a screenshot."""
        if plottable_object is not None:
            self.plot(
                plottable_object,
                name_filter=name_filter,
                scope=scope,
                **plotting_options,
            )
        self._backend.show(
            plottable_object=plottable_object,
            screenshot=screenshot,
            name_filter=name_filter,
            **plotting_options,
        )


class Graphics:
    """Manage legacy PyPrime graphics.

    .. deprecated:: 0.6.0
        Use :class:`PrimePlotter` instead.
    """

    def __init__(self, model: prime.Model, use_trame: bool = False) -> None:
        """Initialize legacy graphics."""
        self.model = model
        self.use_trame = use_trame
        warnings.warn(
            "The `Graphics` class is deprecated. Use `PrimePlotter` instead.",
            DeprecationWarning,
            stacklevel=2,
        )

    def __call__(
        self,
        parts: List = None,
        update: bool = True,
        spline: bool = False,
        scope: prime.ScopeDefinition = None,
    ) -> None:
        """Display the configured model."""
        plotter = PrimePlotter(use_trame=self.use_trame)
        plotter.add_model(self.model, scope=scope, update=update)
        plotter.show()
