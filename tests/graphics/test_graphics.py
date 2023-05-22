"""Module for testing plotter related functions."""
from pathlib import Path

import pyvista as pv

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics
from ansys.meshing.prime.graphics.graphics import Picker, compute_distance

pv.OFF_SCREEN = True
IMAGE_RESULTS_DIR = Path(Path(__file__).parent, "image_cache", "results")


def test_plotter(get_remote_client, get_examples, verify_image_cache):
    """Test the basic functionality of the plotter."""
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(mixing_elbow)

    mesh_util.surface_mesh(min_size=5, max_size=20)
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    display = Graphics(model)

    mesh_data = display.get_face_mesh_data()
    assert mesh_data != None

    plotter = pv.Plotter()

    # test picker
    picker = Picker(plotter, display)
    selections = picker.selections
    picker.clear_selection()
    assert len(selections) == 0
    picker.ignore(ignore_pick=True)
    assert picker._ignore == True

    # Can't run picker calls, but ideally we should test it
    # picker()

    # test graphics class
    # can't test most callback functions automatically
    display()


def test_compute_distance():
    point1 = [1, 1, 3]
    point2 = [1, 1, 1]
    assert compute_distance(point1=point1, point2=point2) == 2.0
