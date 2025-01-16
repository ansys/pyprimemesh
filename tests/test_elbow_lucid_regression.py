# Copyright (C) 2024 - 2025 ANSYS, Inc. and/or its affiliates.
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

"""Integration test for the elbow example."""
import math

import ansys.meshing.prime as prime


def test_elbow_lucid(get_remote_client, get_examples):
    """Tests an use case with the elbow example."""
    # downloads pmdat file
    elbow_lucid = get_examples["elbow_lucid"]
    # reads file
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)
    mesher.create_zones_from_labels("inlet,outlet")
    mesher.surface_mesh(min_size=5, max_size=20)
    result = mesher.volume_mesh(
        prism_layers=3,
        prism_surface_expression="* !inlet !outlet",
        volume_fill_type=prime.VolumeFillType.POLY,
    )
    part = model.get_part_by_name("flow_volume")
    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))
    # validate number of face zones
    assert part_summary_res.n_face_zones == 2

    # validate number of tri faces
    assert part_summary_res.n_tri_faces == 0

    # validate number of poly faces
    assert math.isclose(1964.0, float(part_summary_res.n_poly_faces), rel_tol=0.02)

    # validate number of poly cells
    assert math.isclose(7613.0, float(part_summary_res.n_poly_cells), rel_tol=0.02)
