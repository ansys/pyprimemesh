# Copyright 2025 ANSYS, Inc. Unauthorized use, distribution, or duplication is prohibited.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module for testing plotter related functions."""
from pathlib import Path

import pyvista as pv

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh import (
    compute_distance,
    compute_face_list_from_structured_nodes,
)
from ansys.meshing.prime.graphics import PrimePlotter

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

    display = PrimePlotter()
    display.plot(model)
    display.show()


def test_compute_distance():
    point1 = [1, 1, 3]
    point2 = [1, 1, 1]
    assert compute_distance(point1=point1, point2=point2) == 2.0


def test_compute_face_list():
    dim = []
    dim.append(2)
    dim.append(2)
    dim.append(2)
    flist = compute_face_list_from_structured_nodes(dim)
    assert len(flist) == 30
