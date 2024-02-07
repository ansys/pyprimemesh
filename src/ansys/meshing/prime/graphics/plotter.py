import enum

import numpy as np
from ansys.visualizer import MeshObjectPlot, PlotterInterface
from beartype.typing import Any, Dict, List, Optional, Union

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import DisplayMeshInfo
from ansys.meshing.prime.core.model import Model
from ansys.meshing.prime.graphics.widgets.color_by_type import \
    ColorByTypeWidget
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
    """Create a plotter for PyPrimeMesh models. This plotter is a wrapper around the
    PyAnsys generic plotter with additional functionality for PyPrimeMesh.

    Parameters
    ----------
    use_trame : Optional[bool], optional.
        Whether to use trame or not, by default None.
    allow_picking : Optional[bool], optional.
        Whether to allow picking ot not, by default True.
    """
    def __init__(
        self, use_trame: Optional[bool] = None, allow_picking: Optional[bool] = True
    ) -> None:
        """PrimePlotter constructor."""
        super().__init__(use_trame, allow_picking)

        # info of the actor to pass to picked info widget
        self._info_actor_map = {}
        self.add_widget(ToogleEdges(self))
        self.add_widget(ColorByTypeWidget(self))
        self.add_widget(HidePicked(self))
        self.add_widget(PickedInfo(self))

    @property
    def info_actor_map(self) -> Dict:
        """Get the info actor map for picked info widget.

        Returns
        -------
        Dict
            Info actor map.
        """
        return self._info_actor_map

    @info_actor_map.setter
    def info_actor_map(self, value: Dict) -> None:
        """Set the info actor map for picked info widget.

        Parameters
        ----------
        value : Dict
            Info actor map.
        """
        self._info_actor_map = value

    def get_scalar_colors(self, mesh_info: DisplayMeshInfo) -> np.ndarray:
        """Get the scalar colors for the mesh.

        Parameters
        ----------
        mesh_info : DisplayMeshInfo
            Mesh info that generates an appropiate color.

        Returns
        -------
        np.ndarray
            Scalar colors for the mesh.
        """
        mesh_type = mesh_info.display_mesh_type
        num_colors = int(color_matrix.size / 3)
        if mesh_type == ColorByType.ZONELET:
            return color_matrix[mesh_info.id % num_colors].tolist()
        elif mesh_type == ColorByType.PART:
            return color_matrix[mesh_info.part_id % num_colors].tolist()
        else:
            return color_matrix[mesh_info.zone_id % num_colors].tolist()

    def add_model(self, model: Model, scope: prime.ScopeDefinition = None) -> None:
        """Add a Prime model to the plotter.

        Parameters
        ----------
        model : _type_
            _description_
        scope : _type_, optional
            _description_, by default None
        """
        model_pd = model.as_polydata()
        if scope is None:
            self.add_model_pd(model_pd)
        else:
            self.add_scope(model, scope)

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

    def add_scope(self, model: Model, scope: prime.ScopeDefinition) -> None:
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
        filter : str, default: None
            Regular expression with the desired name or names you want to include in the plotter.
        **plotting_options : dict, default: None
            Keyword arguments. For allowable keyword arguments, see the
            :meth:`Plotter.add_mesh <pyvista.Plotter.add_mesh>` method.
        """
        for object in plotting_list:
            _ = self.add(object, filter, **plotting_options)

    def add(self, object: Any, scope: prime.ScopeDefinition = None, filter: str = None, **plotting_options):
        """Add an object to the plotter.

        Parameters
        ----------
        object : Any
            Object to add to the plotter.
        scope : prime.ScopeDefinition, optional
            Scope you want to plot, by default None.
        filter : str, optional
            Regular expression with the desired name or names you want to include in the plotter, by default None.
        """
        if isinstance(object, Model):
            self.add_model(object, scope)
        elif isinstance(object, List):
            self.add_list(object, filter, **plotting_options)
        else:
            self.pv_interface.add(object, filter, **plotting_options)
