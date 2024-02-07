"""This module contains the HidePicked class."""
import os

from ansys.visualizer import Plotter
from ansys.visualizer.widgets import PlotterWidget
from vtk import vtkButtonWidget, vtkPNGReader


class HidePicked(PlotterWidget):
    """Initialize the hide picked button widget. This widget allows the user to hide
    the picked mesh objects.

    Parameters
    ----------
    plotter_helper : Plotter
        Plotter where to apply this widget.
    """
    def __init__(self, plotter_helper: "Plotter") -> None:
        """HidePicked constructor."""
        super().__init__(plotter_helper._pl.scene)
        self.plotter_helper = plotter_helper
        self._picked_list = self.plotter_helper._picked_list
        self._object_actors_map = self.plotter_helper._object_to_actors_map
        self._button = self.plotter_helper._pl.scene.add_checkbox_button_widget(
            self.callback,
            position=(5, 660),
            size=30,
            border_size=3,
            color_off="white",
            color_on="white",
        )
        self._removed_actors = []

    def callback(self, state: bool) -> None:
        """Callback function for the button widget."""
        if state:
            for meshobject in self._picked_list:
                self.plotter_helper.pv_interface.scene.remove_actor(meshobject.actor)
                self._removed_actors.append(meshobject.actor)
        else:
            for actor in self._removed_actors:
                self.plotter_helper._pl.scene.add_actor(actor)

    def update(self) -> None:
        """Define the configuration and representation of the button widget button."""
        vr = self._button.GetRepresentation()
        icon_file = os.path.join(
            os.path.dirname(__file__), "images", "invert_visibility.png"
        )
        r = vtkPNGReader()
        r.SetFileName(icon_file)
        r.Update()
        image = r.GetOutput()
        vr.SetButtonTexture(0, image)
        vr.SetButtonTexture(1, image)
