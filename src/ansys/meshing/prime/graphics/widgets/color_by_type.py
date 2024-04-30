"""Module for ColorByTypeWidget."""
import enum
import os

import numpy as np
from ansys.visualizer import Plotter, PlotterWidget
from vtk import vtkButtonWidget, vtkPNGReader

from ansys.meshing.prime.core.mesh import DisplayMeshInfo

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


class ColorByTypeWidget(PlotterWidget):
    """Initialize the color by type button widget. This widget allows the user to
    change the color of the mesh based on the zone, zonelet or part.

    Parameters
    ----------
    plotter_helper : Plotter
        Plotter object to use.
    """

    def __init__(self, plotter_helper: "Plotter") -> None:
        """ColorByTypeWidget constructor."""
        super().__init__(plotter_helper._pl.scene)
        self.plotter_helper = plotter_helper
        self._object_actors_map = self.plotter_helper._object_to_actors_map
        self._info_actor_map = self.plotter_helper._info_actor_map
        self._button = self.plotter_helper._pl.scene.add_checkbox_button_widget(
            self.callback, position=(5, 630), size=30, border_size=3
        )
        self._button.GetRepresentation().SetNumberOfStates(3)
        self._color_type = ColorByType.ZONE

    def callback(self, state) -> None:
        """Callback function for the button widget."""
        color_type = ColorByType(self._button.GetRepresentation().GetState())
        for actor, object in self._object_actors_map.items():
            if actor in self.plotter_helper._info_actor_map:
                mesh_info = self.plotter_helper._info_actor_map[actor]
                actor.prop.color = self.set_color_by_type(color_type, mesh_info)
                self.update(color_type)

    def update(self, color_type=ColorByType.ZONE) -> None:
        """Define the configuration and representation of the button widget button.

        Parameters
        ----------
        color_type : ColorByType, optional
            Color type to use, by default ColorByType.ZONE.
        """
        vr = self._button.GetRepresentation()
        icon_file = os.path.join(os.path.dirname(__file__), "images", "bin.png")

        if color_type == ColorByType.ZONE:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "bin.png")
        elif color_type == ColorByType.ZONELET:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "surface_body.png")
        elif color_type == ColorByType.PART:
            icon_file = os.path.join(os.path.dirname(__file__), "images", "parts.png")
        reader = vtkPNGReader()
        reader.SetFileName(icon_file)
        reader.Update()
        image = reader.GetOutput()
        vr.SetButtonTexture(0, image)
        vr.SetButtonTexture(1, image)
        vr.SetButtonTexture(2, image)

    def set_color_by_type(self, color_type: ColorByType, mesh_info: DisplayMeshInfo):
        """Get the colors of faces.

        Parameters
        ----------
        color_type : ColorByType
            Color type to use.
        mesh_info : DisplayMeshInfo
            Mesh info that generates an appropiate color.

        Returns
        -------
        List
            List of colors for faces.
        """
        num_colors = int(color_matrix.size / 3)
        if color_type == ColorByType.ZONELET:
            return color_matrix[mesh_info.id % num_colors].tolist()
        elif color_type == ColorByType.PART:
            return color_matrix[mesh_info.part_id % num_colors].tolist()
        else:
            return color_matrix[mesh_info.zone_id % num_colors].tolist()
