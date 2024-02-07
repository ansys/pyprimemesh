import enum

import numpy as np
from ansys.visualizer import MeshObjectPlot, PlotterInterface
from beartype.typing import Any, Dict, List, Optional, Union

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import DisplayMeshInfo
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.graphics.widgets.color_by_type import ColorByTypeWidget
from ansys.meshing.prime.graphics.widgets.hide_picked import HidePicked
from ansys.meshing.prime.graphics.widgets.picked_info import PickedInfo
from ansys.meshing.prime.graphics.widgets.toogle_edges import ToogleEdges

color_matrix = np.array(
    [
        [155, 186, 126],
        [242, 236, 175],
        [255, 187, 131],
        [194, 187, 97],
        [159, 131, 169],
        [157, 190, 139],
        [233, 218, 158],
        [254, 252, 196],
        [246, 210, 148],
        [215, 208, 198],
        [196, 235, 145],
    ]
)


class ColorByType(enum.IntEnum):
    """Contains the zone types to display."""

    ZONE = 0
    ZONELET = 1
    PART = 2


class PrimePlotter(PlotterInterface):
    def __init__(
        self, use_trame: Optional[bool] = None, allow_picking: Optional[bool] = True
    ) -> None:
        super().__init__(use_trame, allow_picking)

        # info of the actor to pass to picked info widget
        self._info_actor_map = {}
        self.add_widget(ToogleEdges(self))
        self.add_widget(ColorByTypeWidget(self))
        self.add_widget(HidePicked(self))
        self.add_widget(PickedInfo(self))

    @property
    def info_actor_map(self) -> Dict:
        return self._info_actor_map

    @info_actor_map.setter
    def info_actor_map(self, value: Dict) -> None:
        self._info_actor_map = value

    def widget_color_mock(self, type: str) -> ColorByType:
        if type == "zone":
            return ColorByType.ZONE
        elif type == "zonelet":
            return ColorByType.ZONELET
        elif type == "part":
            return ColorByType.PART

    def get_scalar_colors(self, mesh_info: DisplayMeshInfo) -> np.ndarray:
        type = mesh_info.display_mesh_type
        num_colors = int(color_matrix.size / 3)
        if type == ColorByType.ZONELET:
            return color_matrix[mesh_info.id % num_colors].tolist()
        elif type == ColorByType.PART:
            return color_matrix[mesh_info.part_id % num_colors].tolist()
        else:
            return color_matrix[mesh_info.zone_id % num_colors].tolist()

    def add_model(self, model, scope=None):
        model_pd = model.as_polydata()
        if scope is None:
            self.add_model_pd(model_pd)
        else:
            self.add_scope(model, scope)

    def add_model_pd(self, model_pd):
        """Add a model to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        """
        for part_id, part_polydata in model_pd.items():
            # proceed if scope won't be used or if the part is in the scope
            if "faces" in part_polydata.keys():
                for face_mesh_part, face_mesh_info in part_polydata["faces"]:

                    # These operations could be done downstream, but we need the actor for the picked info widget
                    colors = self.get_scalar_colors(face_mesh_info)
                    actor = self.pv_interface.scene.add_mesh(
                        face_mesh_part.mesh, show_edges=True, color=colors, pickable=True
                    )
                    face_mesh_part.actor = actor
                    self._object_to_actors_map[actor] = face_mesh_part
                    self._info_actor_map[actor] = face_mesh_info

            if "edges" in part_polydata.keys():
                for edge_mesh_part in part_polydata["edges"]:
                    plotting_options = {
                        "show_edges": True,
                        "rgb": True,
                        "pickable": False,
                    }
                    self.add(edge_mesh_part, **plotting_options)

            if "ctrlpoints" in part_polydata.keys():
                for ctrlpoint_mesh_part in part_polydata["ctrlpoints"]:
                    plotting_options = {
                        "show_edges": True,
                        "rgb": True,
                        "pickable": False,
                        "style": 'wireframe',
                        "edge_color": [0, 0, 255],
                    }
                    self.add(ctrlpoint_mesh_part, **plotting_options)

            if "splines" in part_polydata.keys():
                for spline_mesh_part in part_polydata["splines"]:
                    plottin_options = {
                        "show_edges": False,
                        "rgb": True,
                        "pickable": False,
                    }
                    self.add(spline_mesh_part, **plottin_options)

    def add_scope(self, model, scope):
        """Add a scope to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        scope : str
            Scope to add to the plotter.
        """
        model_pd = model.get_scoped_polydata(scope)
        self.add_model_pd(model_pd)

    def add_list(
        self,
        plotting_list: List[Any],
        filter: str = None,
        **plotting_options,
    ) -> None:
        """
        Add a list of any type of object to the scene.

        These types of objects are supported: ``Body``, ``Component``, ``List[pv.PolyData]``,
        ``pv.MultiBlock``, and ``Sketch``.

        Parameters
        ----------
        plotting_list : List[Any]
            List of objects you want to plot.
        merge_component : bool, default: False
            Whether to merge the component into a single dataset. When
            ``True``, all the individual bodies are effectively combined
            into a single dataset without any hierarchy.
        merge_bodies : bool, default: False
            Whether to merge each body into a single dataset. When ``True``,
            all the faces of each individual body are effectively combined
            into a single dataset without separating faces.
        filter : str, default: None
            Regular expression with the desired name or names you want to include in the plotter.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
        """
        for object in plotting_list:
            _ = self.add(object, filter, **plotting_options)

    def add(self, object, scope=None, filter=None, **plotting_options):
        if isinstance(object, Model):
            self.add_model(object, scope)
        elif isinstance(object, List):
            self.add_list(object, filter, **plotting_options)
        else:
            self.pv_interface.add(object, filter, **plotting_options)
