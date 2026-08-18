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
"""Module for the plotter."""

import warnings
from typing import Any, Dict, List, Optional

import numpy as np
import pyvista as pv
from ansys.tools.visualization_interface import Plotter
from ansys.tools.visualization_interface.backends.pyvista import PyVistaBackend
from ansys.tools.visualization_interface.utils.color import Color

import ansys.meshing.prime as prime

# kept importable from here for callers that build their own coloring
from ansys.meshing.prime.core.mesh import color_matrix  # noqa: F401
from ansys.meshing.prime.core.mesh import (
    ENTITY_COLOR_ARRAY,
    ENTITY_ID_ARRAY,
    ColorByType,
    DisplayMeshInfo,
    build_edge_render_mesh,
    build_element_edge_mesh,
    build_face_render_batches,
    compute_entity_colors,
    entity_color,
)
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.graphics.widgets.color_by_type import ColorByTypeWidget
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked
from ansys.meshing.prime.graphics.widgets.picked_info import PickedInfo
from ansys.meshing.prime.graphics.widgets.toggle_edges import ToggleEdges

# Depth-buffer offset applied to a face actor whose element outlines are drawn as a
# separate line actor, so that the shaded surface cannot z-fight with those lines.
# The first value scales with the depth slope of the polygon, the second is constant.
POLYGON_OFFSET_FACTOR = 1.0
POLYGON_OFFSET_UNITS = 1.0


class _EntityPickingBackend(PyVistaBackend):
    """PyVista backend that resolves a pick to the display entity under the cursor.

    Display entities of a part share an actor, so the actor alone no longer
    identifies what was picked. Picks that land on a shared actor are resolved
    against the cell the pick point falls on, and anything else is left to the
    generic backend.
    """

    prime_plotter = None

    def picker_callback(self, actor: "pv.Actor") -> None:
        """Select the display entity under the cursor.

        Parameters
        ----------
        actor : pv.Actor
            Actor the pick landed on.
        """
        plotter = self.prime_plotter
        if plotter is not None and plotter._pick_entity(actor, self._pl.scene.picked_point):
            return
        super().picker_callback(actor)


class PrimePlotter(Plotter):
    """Create a plotter for PyPrimeMesh models.

    This plotter is a wrapper around the PyAnsys generic plotter
    with additional functionality for PyPrimeMesh.

    Display entities of a part are merged into a small number of actors that are
    drawn together, rather than one actor per entity. The entity each cell belongs
    to is kept on the mesh, so picking, coloring, and visibility remain per entity
    while the scene stays cheap to render and to export.

    Parameters
    ----------
    use_trame : Optional[bool], default: None
        Whether to use the Trame visualizer.
    allow_picking : Optional[bool], default: True.
        Whether to allow picking.
    """

    def __init__(
        self,
        use_trame: Optional[bool] = None,
        allow_picking: Optional[bool] = True,
    ) -> None:
        """Initialize the widget."""
        self._backend = _EntityPickingBackend(use_trame=use_trame, allow_picking=allow_picking)
        self._backend.prime_plotter = self
        super().__init__(backend=self._backend)

        # actors added through add_mesh(..., metadata=...), keyed for the widgets
        self._info_actor_map = {}
        # element outlines drawn separately, keyed by the ID of the part they belong to
        self._element_edge_actors = {}
        # merged rendering state, keyed by the actor that draws each batch
        self._batches = {}
        self._entity_infos = {}
        self._picked_entities = {}
        # point each entity was picked at, so its label can be restored
        self._picked_points = {}
        # label actor shown for each picked entity, keyed by entity ID
        self._entity_labels = {}
        self._hidden_entities = set()
        # merged element outlines of each part, keyed by part ID
        self._element_edge_meshes = {}
        # geometry handed to each actor, keyed by actor; the mapper does not own it
        self._drawn_geometry = {}
        # no color mode is chosen until a caller or the widget picks one
        self._color_type = None
        self._add_widgets()

    def _add_widgets(self) -> None:
        """Attach the PyPrimeMesh widgets to the backend."""
        self._backend.add_widget(ToggleEdges(self))
        self._backend.add_widget(ColorByTypeWidget(self))
        self._backend.add_widget(HidePicked(self))
        self._backend.add_widget(PickedInfo(self))

    @property
    def info_actor_map(self) -> Dict:
        """Get the information actor map for meshes added with metadata.

        Returns
        -------
        Dict
            Information actor map.
        """
        return self._info_actor_map

    @info_actor_map.setter
    def info_actor_map(self, value: Dict) -> None:
        """Set the information actor map for meshes added with metadata.

        Parameters
        ----------
        value : Dict
            Information actor map.
        """
        self._info_actor_map = value

    @property
    def element_edge_actors(self) -> Dict:
        """Get the element outlines that are drawn as separate line geometry.

        Returns
        -------
        Dict
            Actor holding the outlines of each part that has them.
        """
        return self._element_edge_actors

    @property
    def scene(self):
        """Get the underlying PyVista plotter scene for direct rendering control."""
        return self._backend.pv_interface.scene

    @property
    def entity_infos(self) -> Dict[int, DisplayMeshInfo]:
        """Get the display information of every entity in the scene, keyed by entity ID.

        Returns
        -------
        Dict[int, DisplayMeshInfo]
            Display information of every entity in the scene.
        """
        return self._entity_infos

    @property
    def picked_entities(self) -> Dict[int, DisplayMeshInfo]:
        """Get the display information of the picked entities, keyed by entity ID.

        Returns
        -------
        Dict[int, DisplayMeshInfo]
            Display information of the picked entities.
        """
        return self._picked_entities

    def get_scalar_colors(self, mesh_info: DisplayMeshInfo) -> np.ndarray:
        """Get the scalar colors for the mesh.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Mesh information that generates an appropriate color.

        Returns
        -------
        np.ndarray
            Scalar colors for the mesh.
        """
        return entity_color(mesh_info).tolist()

    def add_mesh(self, mesh, metadata=None, **pyvista_kwargs):
        """Add a mesh or MeshObjectPlot to the scene with optional metadata tracking.

        Parameters
        ----------
        mesh: pyvista.DataSet or MeshObjectPlot
            A raw PyVista mesh or a MeshObjectPlot (which has a ``.mesh`` attribute).
        metadata : DisplayMeshInfo, optional
            If provided, registers the actor in ``info_actor_map`` so the built-in
            widgets can color, hide, and report it.
        **pyvista_kwargs
            Additional keyword arguments passed to ``scene.add_mesh()``.

        Returns
        -------
        actor
            The PyVista actor added to the scene.
        """
        mesh = mesh.mesh if hasattr(mesh, 'mesh') else mesh
        actor = self.scene.add_mesh(mesh, **pyvista_kwargs)
        if metadata is not None:
            self._info_actor_map[actor] = metadata
        return actor

    def add_point_labels(self, points, labels, **kwargs):
        """Add point labels to the scene.

        Parameters
        ----------
        points : array_like
            Points where labels are placed.
        labels : list of str
            Label text for each point.
        **kwargs
            Additional keyword arguments passed to ``scene.add_point_labels()``.
        """
        return self.scene.add_point_labels(points, labels, **kwargs)

    def add_legend(self, entries, **kwargs):
        """Add a legend to the scene.

        Parameters
        ----------
        entries : list
            Legend entries (each a [name, color] pair).
        **kwargs
            Additional keyword arguments passed to ``scene.add_legend()``.
        """
        return self.scene.add_legend(entries, **kwargs)

    def add_text(self, text, **kwargs):
        """Add text annotation to the scene.

        Parameters
        ----------
        text : str
            Text to display.
        **kwargs
            Additional keyword arguments passed to ``scene.add_text()``.
        """
        return self.scene.add_text(text, **kwargs)

    def add_model(
        self, model: Model, scope: prime.ScopeDefinition = None, update: bool = False
    ) -> None:
        """Add a Prime model to the plotter.

        Parameters
        ----------
        model : Model
            Prime model to add.
        scope : prime.ScopeDefinition, default: None
            Scope to show, if any.
        update : bool, default: False
            Whether to update the display.
        """
        if scope is None:
            model_pd = model.as_polydata(update=update)
            self.add_model_pd(model_pd)
        else:
            self.add_scope(model, scope, update=update)

    def add_model_pd(self, model_pd: Dict) -> None:
        """Add a model to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        """
        for part_id, part_polydata in model_pd.items():
            # proceed if scope won't be used or if the part is in the scope
            if "faces" in part_polydata.keys():
                self._add_merged_faces(part_id, part_polydata["faces"])

            if "edges" in part_polydata.keys():
                self._add_edges(part_polydata["edges"])

            if "ctrlpoints" in part_polydata.keys():
                for ctrlpoint_mesh_part in part_polydata["ctrlpoints"]:
                    actor = self._backend.pv_interface.scene.add_mesh(
                        ctrlpoint_mesh_part.mesh,
                        show_edges=False,
                        # scalars="colors",
                        rgb=True,
                        pickable=False,
                        style='wireframe',
                        edge_color=[0, 0, 255],
                    )
                    ctrlpoint_mesh_part.actor = actor
                    self._backend._object_to_actors_map[actor] = ctrlpoint_mesh_part

            if "splines" in part_polydata.keys():
                for spline_mesh_part in part_polydata["splines"]:
                    actor = self._backend._pl.scene.add_mesh(
                        spline_mesh_part.mesh,
                        show_edges=False,
                        # scalars="colors",
                        rgb=True,
                        pickable=False,
                    )
                    spline_mesh_part.actor = actor
                    self._backend._object_to_actors_map[actor] = spline_mesh_part

    def _add_merged_faces(self, part_id: int, face_entries: List) -> None:
        """Draw the faces of a part as a small number of shared actors.

        Parameters
        ----------
        part_id : int
            ID of the part the faces belong to.
        face_entries : List
            ``(MeshObjectPlot, DisplayMeshInfo)`` pairs of the faces of the part.
        """
        outlines = build_element_edge_mesh(face_entries)
        for batch in build_face_render_batches(face_entries, part_id):
            # the actor draws a copy: the batch stays the whole geometry so that
            # hidden cells can be taken away from it and put back
            drawn = batch.mesh.copy()
            actor = self.scene.add_mesh(
                drawn,
                scalars=ENTITY_COLOR_ARRAY,
                rgb=True,
                show_edges=batch.show_edges,
                pickable=True,
            )
            if outlines is not None and not batch.show_edges:
                # the outlines of these entities are drawn as separate line geometry,
                # so the shaded surface is pushed back to stop it z-fighting the lines
                self._offset_polygons(actor)
            self._batches[actor] = batch
            self._drawn_geometry[actor] = drawn
            self._entity_infos.update(batch.infos)

        if outlines is not None:
            self._element_edge_meshes[part_id] = outlines
            drawn_outlines = outlines.copy()
            outline_actor = self.scene.add_mesh(
                drawn_outlines,
                color=pv.global_theme.edge_color,
                line_width=1,
                pickable=False,
            )
            self._element_edge_actors[part_id] = outline_actor
            self._drawn_geometry[outline_actor] = drawn_outlines

    def _add_edges(self, edge_entries: List) -> None:
        """Draw the edges of a part.

        Parameters
        ----------
        edge_entries : List
            ``MeshObjectPlot`` objects of the edges of the part.
        """
        merged = build_edge_render_mesh(edge_entries)
        if merged is None:
            return
        # merging does not carry over which array is active, so the colors
        # the edges were built with have to be named explicitly
        has_colors = ENTITY_COLOR_ARRAY in merged.cell_data
        self.scene.add_mesh(
            merged,
            scalars=ENTITY_COLOR_ARRAY if has_colors else None,
            rgb=has_colors,
            pickable=False,
            line_width=4,
        )

    @staticmethod
    def _offset_polygons(actor) -> None:
        """Push a shaded surface back so coincident line geometry stays visible.

        Parameters
        ----------
        actor : pyvista.Actor
            Actor of the shaded faces to push back.
        """
        mapper = actor.GetMapper()
        mapper.SetResolveCoincidentTopologyToPolygonOffset()
        mapper.SetRelativeCoincidentTopologyPolygonOffsetParameters(
            POLYGON_OFFSET_FACTOR, POLYGON_OFFSET_UNITS
        )

    def _pick_entity(self, actor, point) -> bool:
        """Toggle the selection of the entity the pick landed on.

        Parameters
        ----------
        actor : pyvista.Actor
            Actor the pick landed on.
        point : Sequence[float]
            Point the pick landed on.

        Returns
        -------
        bool
            Whether the pick landed on a shared actor and was handled here.
        """
        batch = self._batches.get(actor)
        if batch is None or point is None:
            return False

        # resolve against what is drawn rather than the full batch, so that hidden
        # entities cannot be picked through the entities that are still shown
        mesh = self._drawn_geometry.get(actor)
        if mesh is None or mesh.n_cells == 0:
            return True

        cell_id = mesh.find_closest_cell(list(point))
        if cell_id < 0:
            return True

        entity_id = int(mesh.cell_data[ENTITY_ID_ARRAY][cell_id])
        if entity_id in self._picked_entities:
            self._picked_entities.pop(entity_id)
            self._picked_points.pop(entity_id, None)
            self._remove_entity_label(entity_id)
        else:
            self._picked_entities[entity_id] = batch.infos[entity_id]
            self._picked_points[entity_id] = np.asarray(point, dtype=float)
            self._add_entity_label(entity_id)
        self.refresh_colors()
        return True

    @staticmethod
    def entity_label(info: DisplayMeshInfo) -> str:
        """Get the text shown next to a picked entity.

        Parameters
        ----------
        info : DisplayMeshInfo
            Display information of the entity.

        Returns
        -------
        str
            Text shown next to the entity.
        """
        name = info.zone_name or info.part_name
        return f"{name} ({info.id})" if name else str(info.id)

    def _add_entity_label(self, entity_id: int) -> None:
        """Label a picked entity at the point it was picked at.

        Parameters
        ----------
        entity_id : int
            ID of the entity to label.
        """
        point = self._picked_points.get(entity_id)
        info = self._entity_infos.get(entity_id)
        if point is None or info is None or entity_id in self._entity_labels:
            return
        if not getattr(self._backend, "_plot_picked_names", True):
            return
        self._entity_labels[entity_id] = self.scene.add_point_labels(
            [point],
            [self.entity_label(info)],
            always_visible=True,
            point_size=0,
            render_points_as_spheres=False,
            show_points=False,
        )

    def _remove_entity_label(self, entity_id: int) -> None:
        """Remove the label of an entity, if it has one.

        Parameters
        ----------
        entity_id : int
            ID of the entity to remove the label of.
        """
        label = self._entity_labels.pop(entity_id, None)
        if label is not None:
            self.scene.remove_actor(label)

    def _update_entity_labels(self) -> None:
        """Show the label of every picked entity that is visible, and only those."""
        for entity_id in list(self._entity_labels):
            if entity_id in self._hidden_entities or entity_id not in self._picked_entities:
                self._remove_entity_label(entity_id)
        for entity_id in self._picked_entities:
            if entity_id not in self._hidden_entities:
                self._add_entity_label(entity_id)

    def refresh_colors(self) -> None:
        """Recolor every shared actor from the current color mode and selection."""
        picked = Color.PICKED.value
        highlight = np.array(pv.Color(picked).int_rgb, dtype=np.uint8)
        for batch in self._batches.values():
            colors = compute_entity_colors(batch.infos, batch.entity_ids, self._color_type)
            if self._picked_entities:
                selected = np.isin(batch.entity_ids, list(self._picked_entities))
                colors[selected] = highlight
            batch.mesh.cell_data[ENTITY_COLOR_ARRAY] = colors
        # the drawn geometry is a copy of the batch whenever something is hidden,
        # so it has to be rebuilt from the colors that were just written
        self._apply_visibility()

    def set_color_by_type(self, color_type: "ColorByType") -> None:
        """Color the entities in the scene by the given entity property.

        Parameters
        ----------
        color_type : ColorByType
            Entity property to take the color from.
        """
        self._color_type = color_type
        for actor, info in self._info_actor_map.items():
            actor.prop.color = entity_color(info, color_type).tolist()
        self.refresh_colors()

    @property
    def selected_entity_infos(self) -> List[DisplayMeshInfo]:
        """Get the display information of the entities that are currently picked.

        Returns
        -------
        List[DisplayMeshInfo]
            Display information of the entities that are currently picked.
        """
        infos = list(self._picked_entities.values())
        # meshes added through add_mesh(..., metadata=...) are picked by the backend
        picked = getattr(self._backend._custom_picker, "picked_dict", {})
        infos.extend(
            self._info_actor_map[mesh_object.actor]
            for mesh_object in picked.values()
            if getattr(mesh_object, "actor", None) in self._info_actor_map
        )
        return infos

    def set_entities_visible(self, entity_ids, visible: bool) -> None:
        """Show or hide display entities without rebuilding the meshes they share.

        Parameters
        ----------
        entity_ids : Iterable[int]
            IDs of the entities to show or hide.
        visible : bool
            Whether to show the entities.
        """
        entity_ids = set(int(entity_id) for entity_id in entity_ids)
        if visible:
            self._hidden_entities -= entity_ids
        else:
            self._hidden_entities |= entity_ids

        for actor, info in self._info_actor_map.items():
            if info.id in entity_ids:
                actor.visibility = visible
        self._apply_visibility()

    def _visible_geometry(self, mesh, entity_ids):
        """Get the geometry of a merged mesh without the cells of hidden entities.

        Parameters
        ----------
        mesh : pyvista.DataSet
            Merged mesh to take the visible cells of.
        entity_ids : np.ndarray
            Entity ID of every cell of the merged mesh.

        Returns
        -------
        pyvista.DataSet
            The mesh itself when nothing it holds is hidden, and a copy holding only
            the visible cells otherwise. The type of the mesh is kept, so that the
            geometry can be copied straight over what is drawn.
        """
        if not self._hidden_entities:
            return mesh
        hidden = np.isin(entity_ids, list(self._hidden_entities))
        if not hidden.any():
            return mesh
        return mesh.remove_cells(np.flatnonzero(hidden), inplace=False)

    def _draw(self, actor, mesh) -> None:
        """Update the geometry an actor draws.

        The geometry is copied over the mesh the actor was built from instead of
        being handed to the mapper as a new data set: a mapper keeps no reference of
        its own to what it is given, and replacing its input leaves the actor blank.

        Parameters
        ----------
        actor : pyvista.Actor
            Actor to draw the geometry with.
        mesh : pyvista.DataSet
            Geometry to draw.
        """
        drawn = self._drawn_geometry.get(actor)
        if drawn is None or drawn is mesh:
            return
        drawn.copy_from(mesh)

    def _apply_visibility(self) -> None:
        """Draw only the cells of the entities that are visible.

        Cells cannot be masked in place: a ghost array is honored by the filters that
        build a surface from a data set, not by the mapper of a polygonal mesh, so the
        drawn geometry has to hold the visible cells and nothing else.
        """
        for actor, batch in self._batches.items():
            self._draw(actor, self._visible_geometry(batch.mesh, batch.entity_ids))

        for part_id, outlines in self._element_edge_actors.items():
            mesh = self._element_edge_meshes.get(part_id)
            if mesh is None or ENTITY_ID_ARRAY not in mesh.cell_data:
                continue
            self._draw(outlines, self._visible_geometry(mesh, mesh.cell_data[ENTITY_ID_ARRAY]))
        self._update_entity_labels()
        self.render()

    def set_show_edges(self, show: bool) -> None:
        """Show or hide the element edges of every entity that has a mesh.

        Parameters
        ----------
        show : bool
            Whether to show the element edges.
        """
        for actor, batch in self._batches.items():
            if batch.show_edges:
                actor.prop.show_edges = show
        for actor, info in self._info_actor_map.items():
            if info.has_mesh:
                actor.prop.show_edges = show
        # element outlines drawn as separate line geometry are hidden as a whole,
        # since they are lines rather than the edges of a shaded actor
        for outlines in self._element_edge_actors.values():
            outlines.visibility = show
        self.render()

    def render(self) -> None:
        """Redraw the scene if it is already on screen."""
        scene = self.scene
        if scene is not None and getattr(scene, "render_window", None) is not None:
            scene.render()

    def clear(self) -> None:
        """Remove everything from the scene and reset the plotter."""
        super().clear()
        self._backend.prime_plotter = self
        self._info_actor_map = {}
        self._element_edge_actors = {}
        self._batches = {}
        self._entity_infos = {}
        self._picked_entities = {}
        self._picked_points = {}
        self._entity_labels = {}
        self._hidden_entities = set()
        self._element_edge_meshes = {}
        self._drawn_geometry = {}
        self._add_widgets()

    def add_scope(self, model: Model, scope: prime.ScopeDefinition, update: bool = False) -> None:
        """Add a scope to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        scope : prime.ScopeDefinition
            Scope to add to the plotter.
        update : bool, default: False
            Whether to update the display.
        """
        model_pd = model.get_scoped_polydata(scope, update=update)
        self.add_model_pd(model_pd)

    def plot_iter(
        self,
        plotting_list: List[Any],
        name_filter: str = None,
        update: bool = False,
        **plotting_options,
    ) -> None:
        """
        Add a list of any type of object to the scene.

        Allowed types are PyPrime models or any PyVista plottable object.

        Parameters
        ----------
        plotting_list : List[Any]
            List of objects to plot.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the plotter.
        update: bool, default: False
            Whether to update the display.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
            Options only applied to PyVista plottable objects.
        """
        for plottable_object in plotting_list:
            _ = self.plot(plottable_object, name_filter, **plotting_options)

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
            Scope to plot.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the plotter.
        update: bool, default: False
            Whether to update the display. Required when any mesh is updated.
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
        elif isinstance(plottable_object, List):
            self.plot_iter(plottable_object, name_filter, update=update, **plotting_options)
        else:
            self._backend.pv_interface.plot(plottable_object, name_filter, **plotting_options)

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
            Object to show.
        screenshot : str, default: None
            Path to save a screenshot to.
        name_filter : str, default: None
            Regular expression with the desired name or names to include in the plotter.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
            Options only applied to PyVista plottable objects.
        """
        if plottable_object is not None:
            self.plot(plottable_object, name_filter=name_filter, scope=scope, **plotting_options)
        self._backend.show(
            plottable_object=plottable_object,
            screenshot=screenshot,
            name_filter=name_filter,
            **plotting_options,
        )


class Graphics:
    """Manages graphics in PyPrime.

    .. deprecated:: 0.6.0
        Use :class:`PrimePlotter` instead.

    Parameters
    ----------
    model : prime.Model
        Model to show.
    use_trame : bool, default: False
        Whether to use the Trame visualizer.
    """

    def __init__(self, model: prime.Model, use_trame: bool = False) -> None:
        """Initialize graphics."""
        self.model = model
        self.use_trame = use_trame
        warnings.warn(
            "DeprecationWarning: The `Graphics` class is deprecated. "
            + "Use the `PrimePlotter` class instead."
        )

    def __call__(
        self,
        parts: List = None,
        update: bool = True,
        spline: bool = False,
        scope: prime.ScopeDefinition = None,
    ) -> None:
        """Show the appropriate display based on parameters.

        Parameters
        ----------
        parts : Any, default: None
            Parts to show.
        update : bool, default: True
            Whether to update the display.
        spline : bool, default: False
            Whether to use splines.
        scope : prime.ScopeDefinition, default: None
            Scope of the parts.
        """
        plotter = PrimePlotter(use_trame=self.use_trame)
        plotter.add_model(self.model, scope=scope)
        plotter.show()
