import enum

import numpy as np
from ansys.visualizer import MeshObjectPlot, PlotterInterface
from beartype.typing import Any, Dict, List, Optional, Union

from ansys.meshing.prime.core.mesh import DisplayMeshInfo
from ansys.meshing.prime.core.model import Model

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
        self, use_trame: Optional[bool] = None, allow_picking: Optional[bool] = False
    ) -> None:
        super().__init__(use_trame, allow_picking)

    def get_zone_colors(self) -> np.ndarray:
        pass

    def get_zonelet_colors(self) -> np.ndarray:
        pass

    def get_part_colors(self) -> np.ndarray:
        pass

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

    def add_model(self, model):
        # type: (Model) -> None
        """Add a model to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        """
        for part_id, part_polydata in model.as_polydata().items():
            if "faces" in part_polydata.keys():
                for face_mesh_part, face_mesh_info in part_polydata["faces"]:
                    colors = self.get_scalar_colors(face_mesh_info)
                    actor = self._pl.scene.add_mesh(
                        face_mesh_part.mesh, show_edges=True, color=colors, pickable=True
                    )
                    face_mesh_part.actor = actor
            if "edges" in part_polydata.keys():
                for edge_mesh_part in part_polydata["edges"]:
                    actor = self._pl.scene.add_mesh(
                        edge_mesh_part.mesh,
                        # scalars="colors",
                        rgb=True,
                        line_width=4,
                    )
                    edge_mesh_part.actor = actor
            if "ctrlpoints" in part_polydata.keys():
                for ctrlpoint_mesh_part in part_polydata["ctrlpoints"]:
                    actor = self._pl.scene.add_mesh(
                        ctrlpoint_mesh_part.mesh,
                        show_edges=True,
                        # scalars="colors",
                        rgb=True,
                        pickable=False,
                        style='wireframe',
                        edge_color=[0, 0, 255],
                    )
                    ctrlpoint_mesh_part.actor = actor
            if "splines" in part_polydata.keys():
                for spline_mesh_part in part_polydata["splines"]:
                    actor = self._pl.scene.add_mesh(
                        spline_mesh_part.mesh,
                        show_edges=False,
                        # scalars="colors",
                        rgb=True,
                        pickable=False,
                    )
                    spline_mesh_part.actor = actor

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

    def add(self, object, filter=None, **plotting_options):
        if isinstance(object, Model):
            self.add_model(object)
        elif isinstance(object, List):
            self.add_list(object, filter, **plotting_options)
        else:
            self._pl.add(object, filter, **plotting_options)
