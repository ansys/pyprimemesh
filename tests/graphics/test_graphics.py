import pyvista as pv

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

pv.OFF_SCREEN = True
IMAGE_RESULTS_DIR = "../../image_cache_dir/results/"


def test_plotter(get_remote_client, get_examples, verify_image_cache):
    mixing_elbow = get_examples["elbow_lucid"]
    model = get_remote_client.model
    # Your code goes here...
    mesh_util = prime.lucid.Mesh(model=model)
    mesh_util.read(mixing_elbow)

    mesh_util.surface_mesh(min_size=5, max_size=20)
    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    display = Graphics(model)
    display()
