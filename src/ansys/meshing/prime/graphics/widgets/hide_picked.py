import os

from ansys.visualizer import Plotter
from ansys.visualizer.widgets import PlotterWidget
from vtk import vtkButtonWidget, vtkPNGReader


class HidePicked(PlotterWidget):
    def __init__(self, plotter_helper: "Plotter") -> None:
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
        if state:
            for meshobject in self._picked_list:
                self.plotter_helper._pl.scene.remove_actor(meshobject.actor)
                self._removed_actors.append(meshobject.actor)
        else:
            for actor in self._removed_actors:
                self.plotter_helper._pl.scene.add_actor(actor)

    def update(self) -> None:
        """Define the configuration and representation of the button widget button."""
        show_point_vr = self._button.GetRepresentation()
        show_point_icon_file = os.path.join(
            os.path.dirname(__file__), "images", "invert_visibility.png"
        )
        show_point_r = vtkPNGReader()
        show_point_r.SetFileName(show_point_icon_file)
        show_point_r.Update()
        image = show_point_r.GetOutput()
        show_point_vr.SetButtonTexture(0, image)
        show_point_vr.SetButtonTexture(1, image)
