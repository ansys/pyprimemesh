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
from ansys.tools.visualization_interface.backends.pyvista.widgets.mesh_slider import (
    MeshSliderWidget,
)
from ansys.tools.visualization_interface.utils.color import Color
from vtk import vtkPlane, vtkTextActor

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
    SelectionTarget,
    build_edge_render_batches,
    build_element_edge_batches,
    build_face_render_batches,
    classify_face_connectivity,
    entity_color,
    selectable_display_types,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.graphics.widgets.clip_plane import ClipPlaneWidget
from ansys.meshing.prime.graphics.widgets.color_by_type import ColorByTypeWidget
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked
from ansys.meshing.prime.graphics.widgets.picked_info import PickedInfo
from ansys.meshing.prime.graphics.widgets.reset_display import ResetDisplay
from ansys.meshing.prime.graphics.widgets.selection_target import SelectionTargetWidget
from ansys.meshing.prime.graphics.widgets.toggle_edges import ToggleEdges

# Depth-buffer offset applied to a face actor when element outlines are drawn as
# separate line geometry.
POLYGON_OFFSET_FACTOR = 1.0
POLYGON_OFFSET_UNITS = 1.0

# Facets approximating an unmeshed CAD surface are drawn faintly so that they read as
# tessellation rather than as a real mesh.
FACET_EDGE_COLOR = "#b4b4b4"
FACET_EDGE_OPACITY = 0.35

TOOLTIP_FONT_SIZE = 14
# Distance from the cursor to the hover text, so the text clears the button.
TOOLTIP_GAP = 24
TOOLTIP_TEXT_COLOR = (0.0, 0.0, 0.0)
TOOLTIP_BACKGROUND_COLOR = (1.0, 1.0, 0.88)
TOOLTIP_FRAME_COLOR = (0.25, 0.25, 0.25)


class _EntityPickingBackend(PyVistaBackend):
    """Resolve a PyVista actor pick to the Prime entity under the cursor."""

    prime_plotter = None

    def enable_widgets(self, dark_mode: bool = False) -> None:
        """Add the backend widgets, minus the clip slider.

        That slider clips by rebuilding the scene from combined geometry and
        identifying actors by dataset address, neither of which holds once entities
        are merged into render batches and hidden by filtering cells. PyPrimeMesh
        supplies its own clip button instead.

        Parameters
        ----------
        dark_mode : bool, default: False
            Whether to use dark mode for the widgets.
        """
        super().enable_widgets(dark_mode)

        kept = []
        for widget in getattr(self, "_widgets", []):
            if isinstance(widget, MeshSliderWidget):
                widget._button.Off()
                widget._button.GetRepresentation().SetVisibility(0)
                continue
            kept.append(widget)
        self._widgets = kept

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
        self._facet_edge_batches: Dict[Any, RenderBatch] = {}
        self._spline_actors: Dict[DisplayMeshType, Any] = {}
        self._entity_infos: Dict[DisplayEntityKey, DisplayMeshInfo] = {}
        self._picked_entities: Dict[DisplayEntityKey, DisplayMeshInfo] = {}
        self._picked_points: Dict[DisplayEntityKey, np.ndarray] = {}
        self._entity_labels: Dict[DisplayEntityKey, Any] = {}
        self._hidden_entities: set[DisplayEntityKey] = set()
        self._drawn_geometry: Dict[Any, pv.DataSet] = {}
        self._color_type: Optional[ColorByType] = None
        self._show_element_edges = True
        self._selection_target = SelectionTarget.BOTH
        self._initial_camera = None
        self._camera_observer = None
        self._tooltip_actor = None
        self._tooltip_text = None
        self._hover_position = None
        self._hover_observer = None
        self._clip_plane = None
        self._prime_widget_list: List = []
        self._model: Optional[Model] = None

    def _add_widgets(self) -> None:
        """Attach the PyPrimeMesh widgets to the backend.

        The backend rebuilds its own widget list when the scene is shown, dropping
        the widgets added here, so they are also kept locally. The buttons themselves
        stay live because they are registered with the scene.
        """
        self._prime_widget_list = [
            ToggleEdges(self),
            ColorByTypeWidget(self),
            HidePicked(self),
            PickedInfo(self),
            SelectionTargetWidget(self),
            ClipPlaneWidget(self),
            ResetDisplay(self),
        ]
        for widget in self._prime_widget_list:
            self._backend.add_widget(widget)

    @property
    def info_actor_map(self) -> Dict:
        """Return metadata for individually added actors.

        Returns
        -------
        Dict
            Display information of each actor added with :meth:`add_mesh`.
        """
        return self._info_actor_map

    @info_actor_map.setter
    def info_actor_map(self, value: Dict) -> None:
        """Set metadata for individually added actors.

        Parameters
        ----------
        value : Dict
            Display information of each actor added with :meth:`add_mesh`.
        """
        self._info_actor_map = value

    @property
    def element_edge_actors(self) -> Dict:
        """Return element-outline actors of meshed faces.

        Returns
        -------
        Dict
            Render batch of each element-outline actor, keyed by actor.
        """
        return self._element_edge_batches

    @property
    def facet_edge_actors(self) -> Dict:
        """Return facet-outline actors of unmeshed faces.

        Returns
        -------
        Dict
            Render batch of each facet-outline actor, keyed by actor.
        """
        return self._facet_edge_batches

    @property
    def has_faceting(self) -> bool:
        """Whether anything on display has CAD faceting to show in place of a mesh.

        Only an unmeshed face has faceting to fall back on, so this is ``False``
        once everything shown is meshed, whether it is topology or mesh.

        Returns
        -------
        bool
            ``True`` when faceting can be drawn instead of mesh edges.
        """
        if any(batch.mesh.n_cells > 0 for batch in self._facet_edge_batches.values()):
            return True
        return any(not info.has_mesh for info in self._info_actor_map.values())

    def _outline_groups(self):
        """Pair each outline group with whether the show-edges state draws it.

        A meshed face shows its element edges by default and an unmeshed face hides
        its facets, so the two groups follow opposite sides of the same state.
        """
        return (
            (self._element_edge_batches, self._show_element_edges),
            (self._facet_edge_batches, not self._show_element_edges),
        )

    @property
    def scene(self):
        """Return the underlying PyVista scene.

        Returns
        -------
        pyvista.Plotter
            Scene used for direct rendering control.
        """
        return self._backend.pv_interface.scene

    @property
    def entity_infos(self) -> Dict[DisplayEntityKey, DisplayMeshInfo]:
        """Return all displayed entities.

        Returns
        -------
        Dict[DisplayEntityKey, DisplayMeshInfo]
            Display information of every entity, keyed by model-unique entity key.
        """
        return self._entity_infos

    @property
    def picked_entities(self) -> Dict[DisplayEntityKey, DisplayMeshInfo]:
        """Return the entities currently picked.

        Returns
        -------
        Dict[DisplayEntityKey, DisplayMeshInfo]
            Display information of each picked entity, keyed by model-unique
            entity key.
        """
        return self._picked_entities

    def get_scalar_colors(self, mesh_info: DisplayMeshInfo) -> np.ndarray:
        """Get the default scalar color of a display entity.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Display information that the color is generated from.

        Returns
        -------
        np.ndarray
            RGB color of the entity.
        """
        return entity_color(mesh_info).tolist()

    def add_mesh(self, mesh, metadata=None, **pyvista_kwargs):
        """Add a mesh or ``MeshObjectPlot`` to the scene, optionally tracking metadata.

        Parameters
        ----------
        mesh : pyvista.DataSet or MeshObjectPlot
            Raw PyVista mesh, or a ``MeshObjectPlot`` holding one as ``.mesh``.
        metadata : DisplayMeshInfo, default: None
            Display information of the mesh. When given, the actor is registered in
            :attr:`info_actor_map` so that the widgets can act on it.
        **pyvista_kwargs : dict, default: None
            Keyword arguments passed to ``scene.add_mesh()``.

        Returns
        -------
        pyvista.Actor
            Actor added to the scene.
        """
        mesh = mesh.mesh if hasattr(mesh, "mesh") else mesh
        actor = self.scene.add_mesh(mesh, **pyvista_kwargs)
        if metadata is not None:
            self._info_actor_map[actor] = metadata
        return actor

    def add_point_labels(self, points, labels, **kwargs):
        """Add point labels to the scene.

        Parameters
        ----------
        points : array_like
            Points where the labels are placed.
        labels : list of str
            Label text of each point.
        **kwargs : dict, default: None
            Keyword arguments passed to ``scene.add_point_labels()``.

        Returns
        -------
        pyvista.Actor
            Actor holding the labels.
        """
        return self.scene.add_point_labels(points, labels, **kwargs)

    def add_legend(self, entries, **kwargs):
        """Add a legend to the scene.

        Parameters
        ----------
        entries : list
            Legend entries, each a ``[name, color]`` pair.
        **kwargs : dict, default: None
            Keyword arguments passed to ``scene.add_legend()``.

        Returns
        -------
        pyvista.Actor
            Actor holding the legend.
        """
        return self.scene.add_legend(entries, **kwargs)

    def add_text(self, text, **kwargs):
        """Add a text annotation to the scene.

        Parameters
        ----------
        text : str
            Text to display.
        **kwargs : dict, default: None
            Keyword arguments passed to ``scene.add_text()``.

        Returns
        -------
        pyvista.Actor
            Actor holding the text.
        """
        return self.scene.add_text(text, **kwargs)

    def add_model(
        self,
        model: Model,
        scope: prime.ScopeDefinition = None,
        update: bool = False,
    ) -> None:
        """Add a Prime model, or a scoped subset of one, to the plotter.

        Parameters
        ----------
        model : Model
            Prime model to add.
        scope : prime.ScopeDefinition, default: None
            Scope to show. When this is ``None``, the whole model is shown.
        update : bool, default: False
            Whether to rebuild the display geometry rather than reuse what is cached.
        """
        self._model = model
        if scope is None:
            self.add_render_data(model.build_render_data(update=update))
        else:
            self.add_scope(model, scope, update=update)

    def add_render_data(self, render_data: ModelRenderData) -> None:
        """Add render geometry that has already been built.

        Parameters
        ----------
        render_data : ModelRenderData
            Model-wide render batches, as returned by
            :func:`Model.build_render_data`.
        """
        self._add_render_batches(render_data.batches)
        self._add_spline_batch(
            render_data.ctrlpts,
            DisplayMeshType.SPLINECONTROLPOINTS,
        )
        self._add_spline_batch(
            render_data.splines,
            DisplayMeshType.SPLINESURFACE,
        )
        # Geometry added while clipping is on has to be clipped as well.
        self._apply_clip_plane()

    @staticmethod
    def _entries(model_pd: Dict, key: str) -> List:
        """Collect one stored geometry category across all parts."""
        output = []
        for part_polydata in model_pd.values():
            output.extend(entry for entry in part_polydata.get(key, []) if entry is not None)
        return output

    def add_model_pd(self, model_pd: Dict) -> None:
        """Add part-organized PolyData using model-wide entity-type actors.

        Parameters
        ----------
        model_pd : Dict
            PolyData of each part keyed by part ID, as returned by
            :func:`Model.as_polydata`.
        """
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
        self._apply_clip_plane()

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

        for batch in batches.get("facet_edges", {}).values():
            actor = self.scene.add_mesh(
                batch.mesh,
                color=FACET_EDGE_COLOR,
                opacity=FACET_EDGE_OPACITY,
                line_width=1,
                pickable=False,
            )
            actor.visibility = not self._show_element_edges
            self._facet_edge_batches[actor] = batch
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
        """Add at most one outline actor for each face entity type.

        Meshed faces contribute element edges, and unmeshed faces contribute the
        facets approximating their CAD surface, drawn faintly to keep the two apart.
        """
        groups = (
            (True, self._element_edge_batches, {"color": pv.global_theme.edge_color}),
            (
                False,
                self._facet_edge_batches,
                {"color": FACET_EDGE_COLOR, "opacity": FACET_EDGE_OPACITY},
            ),
        )
        for meshed, group, style in groups:
            for batch in build_element_edge_batches(face_entries, meshed=meshed).values():
                actor = self.scene.add_mesh(
                    batch.mesh,
                    line_width=1,
                    pickable=False,
                    **style,
                )
                actor.visibility = meshed == self._show_element_edges
                group[actor] = batch
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

        if batch.display_mesh_type not in selectable_display_types(self._selection_target):
            return True

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
        self.refresh_tooltips()
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
            if not batch.cell_colored:
                continue
            colors = batch.colors_for(self._color_type)
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

    def _ensure_face_connectivity(self) -> None:
        """Classify face connectivity on first use of the connectivity color mode.

        Faces carry no connectivity in the render data, so it is queried here rather
        than during every build. Already classified entities are skipped, so the cost
        is paid once per model.
        """
        if self._model is None:
            return
        infos = list(self._entity_infos.values())
        infos.extend(self._info_actor_map.values())
        classify_face_connectivity(self._model, infos)

    def set_color_by_type(self, color_type: "ColorByType") -> None:
        """Color displayed entities by zone, zonelet, part, or connectivity.

        Parameters
        ----------
        color_type : ColorByType
            Entity property to take the color from. Selecting
            ``ColorByType.CONNECTIVITY`` classifies face connectivity on first use.
        """
        self._color_type = ColorByType(color_type)
        if self._color_type == ColorByType.CONNECTIVITY:
            self._ensure_face_connectivity()
        for actor, info in self._info_actor_map.items():
            actor.prop.color = entity_color(info, self._color_type).tolist()
        self.refresh_colors()

    @property
    def selected_entity_infos(self) -> List[DisplayMeshInfo]:
        """Return metadata for all currently picked entities.

        Returns
        -------
        List[DisplayMeshInfo]
            Display information of each picked entity, including anything picked
            through an actor added with :meth:`add_mesh`.
        """
        infos = list(self._picked_entities.values())

        custom_picker = getattr(self._backend, "_custom_picker", None)
        picked = getattr(custom_picker, "picked_dict", {})
        for mesh_object in picked.values():
            actor = getattr(mesh_object, "actor", None)
            info = self._info_actor_map.get(actor)
            if info is not None:
                infos.append(info)
        return infos

    @property
    def selection_target(self) -> SelectionTarget:
        """Return the kinds of entity that respond to picking.

        Returns
        -------
        SelectionTarget
            Active selection target.
        """
        return self._selection_target

    def set_selection_target(self, target: SelectionTarget) -> None:
        """Choose whether picking selects faces, edges, or both.

        Entities already selected stay selected, so narrowing the target is a way
        to add edges to a face selection without losing it.

        Parameters
        ----------
        target : SelectionTarget
            Kinds of entity that respond to picking.
        """
        self._selection_target = SelectionTarget(target)
        selectable = selectable_display_types(self._selection_target)
        for actor, batch in self._batches.items():
            # Dropping pickability keeps VTK from returning a face actor that sits
            # in front of the edge the user is aiming at.
            actor.SetPickable(bool(batch.pickable and batch.display_mesh_type in selectable))
        self.render()

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
        """Show or hide display entities without changing the actor count.

        Parameters
        ----------
        entities : Iterable
            Entities to update, given as ``DisplayEntityKey``, ``DisplayMeshInfo``,
            or entity ID.
        visible : bool
            Whether to show the entities.
        """
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

        for group, shown in self._outline_groups():
            for actor, batch in group.items():
                visible = self._visible_geometry(batch)
                self._draw(actor, visible)
                actor.visibility = bool(shown and visible.n_cells > 0)

        self._update_entity_labels()
        self.render()

    def set_show_edges(self, show: bool) -> None:
        """Show the element edges of meshed faces or the facets of unmeshed ones.

        Parameters
        ----------
        show : bool
            Whether to draw element edges. Facets follow the opposite state, so an
            unmeshed CAD surface starts clean and reveals its tessellation when
            element edges are turned off.
        """
        self._show_element_edges = bool(show)
        for group, shown in self._outline_groups():
            for actor in group:
                mesh = self._drawn_geometry.get(actor)
                actor.visibility = bool(shown and mesh is not None and mesh.n_cells > 0)
        for actor, info in self._info_actor_map.items():
            actor.prop.show_edges = bool(show) if info.has_mesh else not show
            if not info.has_mesh:
                actor.prop.edge_color = FACET_EDGE_COLOR
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

    def _reset_widget_buttons(self) -> None:
        """Return every Prime toggle button to its unpressed state."""
        for widget in self._prime_widgets():
            reset = getattr(widget, "reset", None)
            if callable(reset):
                reset()

    def _prime_actors(self) -> List:
        """Return every actor this plotter owns."""
        actors = list(self._batches)
        actors.extend(self._element_edge_batches)
        actors.extend(self._facet_edge_batches)
        actors.extend(self._info_actor_map)
        return actors

    def _remove_clipping(self) -> None:
        """Undo clipping applied by the backend slider widget.

        That widget clips by replacing the model with a combined copy and taking the
        original actors out of the renderer, so dropping the plane alone would leave
        nothing on screen. The originals are put back and the widget is emptied of the
        actors it captured, which would otherwise be restored again later.
        """
        scene = self.scene
        if scene is None:
            return

        self._disable_clipping()

        for widget in getattr(self._backend, "_widgets", []):
            clipped = getattr(widget, "_widget_actor", None)
            if clipped is None:
                continue
            scene.remove_actor(clipped)
            widget._widget_actor = None
            widget._mesh_actor_list = []
            button = getattr(widget, "_button", None)
            if button is not None:
                button.GetRepresentation().SetState(0)

        clear_planes = getattr(scene, "clear_plane_widgets", None)
        if callable(clear_planes):
            clear_planes()

        renderer = scene.renderer
        for actor in self._prime_actors():
            if not renderer.HasViewProp(actor):
                renderer.AddActor(actor)

    def reset_display(self) -> None:
        """Restore the display to how the model was first drawn.

        Selections, hidden entities, coloring, edge visibility, the selection
        target, and any clip plane are all cleared, and the camera returns to its
        opening view. Unlike :meth:`clear`, the model geometry is kept, so the
        model does not need to be added again.
        """
        for key in list(self._entity_labels):
            self._remove_entity_label(key)
        self._picked_entities.clear()
        self._picked_points.clear()

        self._hidden_entities.clear()
        for actor in self._info_actor_map:
            actor.visibility = True

        self._color_type = None
        self._show_element_edges = True
        self._selection_target = SelectionTarget.BOTH
        for actor, batch in self._batches.items():
            actor.SetPickable(bool(batch.pickable))

        self._remove_clipping()
        self._reset_widget_buttons()

        # Recoloring rebuilds the mapper inputs, which is what brings back the cells
        # the hide widget filtered out.
        self.refresh_colors()
        self.set_show_edges(True)
        self._reset_camera()
        self.refresh_tooltips()
        self.render()

    def _reset_camera(self) -> None:
        """Return the camera to the view the model opened with."""
        scene = self.scene
        if scene is None:
            return
        if self._initial_camera is not None:
            scene.camera_position = self._initial_camera
        else:
            scene.reset_camera()

    def _store_initial_camera(self) -> None:
        """Arrange for the opening view to be remembered.

        The camera only frames the model once the window is shown, so the view is
        taken from the first completed render rather than read here, where it would
        still be the default camera.
        """
        scene = self.scene
        if scene is None or self._initial_camera is not None:
            return
        if self._camera_observer is not None:
            return

        renderer = scene.renderer

        def capture(caller, event) -> None:
            if self._initial_camera is None:
                self._initial_camera = scene.camera_position
            self._release_camera_observer()

        self._camera_observer = renderer.AddObserver("EndEvent", capture)

    def _prime_widgets(self) -> List:
        """Return the widgets this plotter created."""
        return list(self._prime_widget_list)

    @property
    def clipping(self) -> bool:
        """Whether a clip plane is currently applied.

        Returns
        -------
        bool
            ``True`` while the model is clipped.
        """
        return self._clip_plane is not None

    def set_clipping(self, enabled: bool) -> None:
        """Clip the model with an interactive plane, or stop clipping.

        The plane is applied to the mappers rather than to the geometry, so the
        entities, their colors, and what is selectable are all unaffected: only
        which part of them is drawn changes.

        Parameters
        ----------
        enabled : bool
            Whether to clip the model.
        """
        if bool(enabled) == self.clipping:
            return
        if enabled:
            self._enable_clipping()
        else:
            self._disable_clipping()

    def _enable_clipping(self) -> None:
        """Add the clip plane and its widget."""
        scene = self.scene
        if scene is None:
            return

        bounds = scene.bounds
        center = (
            (bounds[0] + bounds[1]) / 2.0,
            (bounds[2] + bounds[3]) / 2.0,
            (bounds[4] + bounds[5]) / 2.0,
        )

        plane = vtkPlane()
        plane.SetOrigin(center)
        plane.SetNormal(1.0, 0.0, 0.0)
        self._clip_plane = plane
        self._apply_clip_plane()

        scene.add_plane_widget(
            self._move_clip_plane,
            normal="x",
            origin=center,
            outline_translation=False,
            normal_rotation=True,
        )
        self.render()

    def _move_clip_plane(self, normal, origin) -> None:
        """Follow the plane widget.

        Parameters
        ----------
        normal : Sequence[float]
            Plane normal given by the widget.
        origin : Sequence[float]
            Point on the plane given by the widget.
        """
        if self._clip_plane is None:
            return
        # The mapper keeps what the normal points away from, so the visible half is
        # the one behind the widget arrow.
        self._clip_plane.SetNormal(-normal[0], -normal[1], -normal[2])
        self._clip_plane.SetOrigin(origin)
        self.render()

    def _disable_clipping(self) -> None:
        """Remove the clip plane and its widget."""
        self._clip_plane = None
        self._apply_clip_plane()

        scene = self.scene
        if scene is not None:
            clear_planes = getattr(scene, "clear_plane_widgets", None)
            if callable(clear_planes):
                clear_planes()
        self.render()

    def _apply_clip_plane(self) -> None:
        """Put the current clip plane, if any, on every Prime mapper."""
        for actor in self._prime_actors():
            mapper = actor.GetMapper()
            if mapper is None:
                continue
            mapper.RemoveAllClippingPlanes()
            if self._clip_plane is not None:
                mapper.AddClippingPlane(self._clip_plane)

    def _enable_tooltips(self) -> None:
        """Give the Prime buttons hover text describing what they do.

        VTK's balloon widget is not used because it finds what the cursor is over by
        picking, which reports only 3D props and so never matches a button. Its pick
        also runs a selection render on every hover, which is costly on a large
        model. The buttons are asked directly instead.
        """
        scene = self.scene
        if scene is None or self._tooltip_actor is not None:
            return
        interactor = getattr(scene, "iren", None)
        if interactor is None:
            return

        tooltip = vtkTextActor()
        tooltip.SetInput(" ")
        tooltip.SetVisibility(False)
        text = tooltip.GetTextProperty()
        text.SetFontSize(TOOLTIP_FONT_SIZE)
        text.SetColor(*TOOLTIP_TEXT_COLOR)
        text.SetBackgroundColor(*TOOLTIP_BACKGROUND_COLOR)
        text.SetBackgroundOpacity(1.0)
        text.SetFrame(True)
        text.SetFrameColor(*TOOLTIP_FRAME_COLOR)

        scene.add_actor(tooltip, render=False)
        self._tooltip_actor = tooltip
        self._hover_observer = interactor.interactor.AddObserver(
            "MouseMoveEvent",
            self._hover,
        )

    def _hover(self, caller, event) -> None:
        """Follow the cursor.

        Parameters
        ----------
        caller : vtkRenderWindowInteractor
            Interactor reporting the movement.
        event : str
            Name of the VTK event. Unused.
        """
        del event

        self._update_tooltip(*caller.GetEventPosition())

    def _update_tooltip(self, x: int, y: int) -> None:
        """Show the hover text of the button at a display position, if any.

        Parameters
        ----------
        x : int
            Horizontal display coordinate.
        y : int
            Vertical display coordinate.
        """
        tooltip = self._tooltip_actor
        if tooltip is None:
            return

        self._hover_position = (x, y)
        hovered = next(
            (widget for widget in self._prime_widgets() if widget.contains(x, y)),
            None,
        )
        text = hovered.tooltip() if hovered is not None else ""
        if text == self._tooltip_text:
            return

        self._tooltip_text = text
        tooltip.SetInput(text or " ")
        tooltip.SetDisplayPosition(x + TOOLTIP_GAP, y)
        tooltip.SetVisibility(bool(text))
        self.render()

    def refresh_tooltips(self) -> None:
        """Update the hover text of every Prime button to match its current state."""
        if self._tooltip_actor is None or self._hover_position is None:
            return
        # The state that the text describes has just changed, so it has to be rebuilt
        # even though the cursor has not moved.
        self._tooltip_text = None
        self._update_tooltip(*self._hover_position)

    def _release_camera_observer(self) -> None:
        """Stop watching for the first render."""
        scene = self.scene
        if self._camera_observer is None or scene is None:
            return
        scene.renderer.RemoveObserver(self._camera_observer)
        self._camera_observer = None

    def add_scope(
        self,
        model: Model,
        scope: prime.ScopeDefinition,
        update: bool = False,
    ) -> None:
        """Add a scoped subset of a model.

        Parameters
        ----------
        model : Model
            Prime model the scope is evaluated against.
        scope : prime.ScopeDefinition
            Scope selecting the entities to show.
        update : bool, default: False
            Whether to rebuild the display geometry rather than reuse what is cached.
        """
        self._model = model
        self.add_render_data(model.get_scoped_render_data(scope, update=update))

    def plot_iter(
        self,
        plotting_list: List[Any],
        name_filter: str = None,
        update: bool = False,
        **plotting_options,
    ) -> None:
        """Add a list of objects to the scene.

        Allowed types are PyPrime models or any PyVista plottable object.

        Parameters
        ----------
        plotting_list : List[Any]
            Objects to plot.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the
            plotter.
        update : bool, default: False
            Whether to rebuild the display geometry rather than reuse what is cached.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
            Options only applied to PyVista plottable objects.
        """
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
        """Add an object to the plotter.

        Allowed types are PyPrime models or any PyVista plottable object.

        Parameters
        ----------
        plottable_object : Any
            Object to add to the plotter.
        scope : prime.ScopeDefinition, default: None
            Scope to plot. Only applied to Prime models.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the
            plotter.
        update : bool, default: False
            Whether to rebuild the display geometry rather than reuse what is cached.
            Required when any mesh has been updated.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
            Options only applied to PyVista plottable objects.

        Examples
        --------
        >>> import pyvista as pv
        >>> from ansys.meshing.prime.graphics import PrimePlotter
        >>> import ansys.meshing.prime as prime
        >>> model = prime.launch_prime().model
        >>> prime.lucid.Mesh(model).read(prime.examples.download_block_model_fmd())
        >>> scope = prime.ScopeDefinition(model, label_expression="my_group")
        >>> plotter = PrimePlotter()
        >>> # pyvista sphere with plotting options added for opacity and color
        >>> plotter.plot(plottable_object=pv.Sphere(radius=2.0), opacity=0.5, color="red")
        >>> plotter.plot(plottable_object=model, scope=scope)
        >>> plotter.show()
        """
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
        """Show the plotted objects.

        Parameters
        ----------
        plottable_object : Any, default: None
            Object to show. When this is ``None``, only what is already plotted
            is shown.
        screenshot : str, default: None
            Path to save a screenshot to.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the
            plotter.
        scope : prime.ScopeDefinition, default: None
            Scope to plot. Only applied to Prime models.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
            Options only applied to PyVista plottable objects.
        """
        if plottable_object is not None:
            self.plot(
                plottable_object,
                name_filter=name_filter,
                scope=scope,
                **plotting_options,
            )
        self._store_initial_camera()
        self._enable_tooltips()
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

    Parameters
    ----------
    model : prime.Model
        Prime model to display.
    use_trame : bool, default: False
        Whether to render through Trame rather than a native window.
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
        """Display the configured model.

        Parameters
        ----------
        parts : List, default: None
            Unused, kept for backward compatibility.
        update : bool, default: True
            Whether to rebuild the display geometry rather than reuse what is cached.
        spline : bool, default: False
            Unused, kept for backward compatibility.
        scope : prime.ScopeDefinition, default: None
            Scope to show. When this is ``None``, the whole model is shown.
        """
        plotter = PrimePlotter(use_trame=self.use_trame)
        plotter.add_model(self.model, scope=scope, update=update)
        plotter.show()
