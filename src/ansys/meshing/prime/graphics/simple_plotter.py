"""Simple plotter module."""
import os
import tempfile

import pyvista as pv

from ansys.meshing.prime.autogen.fileiostructs import ExportSTLParams
from ansys.meshing.prime.core.fileio import FileIO


class SimplePlotter:
    """Simple plotter that export the model as STL to show it.

    Exports the model as STL file and the loads this file with
    PyVista directly to be able to visualize large meshes.

    Parameters
    ----------
    model : prime.Model
        Model we want to plot.
    """

    def __init__(self, model: "prime.Model") -> None:
        """Initialize the plotter variables."""
        self._model = model
        self._fileio = FileIO(model)
        self._tempdir = tempfile.gettempdir()
        self._tmpfile = os.path.join(self._tempdir, "output.stl")
        self._export_stl()

    def _get_part_ids(self):
        """Return all the parts of a model."""
        return [part.id for part in self._model.parts]

    def _export_stl(self):
        """Export the model to STL format in tmp folder."""
        part_ids = self._get_part_ids()
        self._fileio.export_stl(
            self._tmpfile, params=ExportSTLParams(self._model, part_ids=part_ids)
        )

    def plot_stl(self):
        """Plot the stl file with PyVista."""
        mesh = pv.read(self._tmpfile)
        _ = mesh.plot(show_edges=True)


def plot(model: "prime.Model"):
    """Plot the given model in a simple PyVista plotter.

    Parameters
    ----------
    model : prime.Model
        The model you want to plot.
    """
    sp = SimplePlotter(model)
    sp.plot_stl()
