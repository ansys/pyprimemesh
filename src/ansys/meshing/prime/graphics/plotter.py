from ansys.visualizer import PlotterInterface
from beartype.typing import Any, Dict, List, Optional, Union

from ansys.meshing.prime.core.model import Model


class PrimePlotter(PlotterInterface):
    def __init__(
        self, use_trame: Optional[bool] = None, allow_picking: Optional[bool] = False
    ) -> None:
        super().init(use_trame, allow_picking)

    def add_model(self, model):
        # type: (Model) -> None
        """Add a model to the plotter.

        Parameters
        ----------
        model : Model
            Model to add to the plotter.
        """
        for part_polydata in model.as_polydata():
            for face_mesh in part_polydata["faces"]:
                actor = self.add_mesh(
                    face_mesh,
                    show_edges=True,
                    color="w",
                    opacity=0.5,
                    pickable=self.allow_picking,
                )
            for edge_mesh in part_polydata["edges"]:
                actor = self.add_mesh(
                    edge_mesh,
                    show_edges=True,
                    color="k",
                    opacity=1.0,
                    pickable=self.allow_picking,
                )
            for ctrlpoint_mesh in part_polydata["ctrlpoints"]:
                actor = self.add_mesh(
                    ctrlpoint_mesh,
                    show_edges=False,
                    color="r",
                    opacity=1.0,
                    pickable=self.allow_picking,
                )

            for spline_mesh in part_polydata["splines"]:
                actor = self.add_mesh(
                    spline_mesh,
                    show_edges=False,
                    color="r",
                    opacity=1.0,
                    pickable=self.allow_picking,
                )
