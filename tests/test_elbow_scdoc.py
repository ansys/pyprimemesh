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

import os
import platform
import tempfile

import pytest

from ansys.meshing import prime
from ansys.meshing.prime.graphics import PrimePlotter


@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows specific test.")
def test_elbow_lucid(get_remote_client, get_examples):
    """Tests an use case with the elbow example."""

    model = get_remote_client.model
    prime_client = prime.launch_prime()
    mesh_util = prime.lucid.Mesh(model=model)

    mixing_elbow = get_examples["elbow_lucid_scdoc"]
    mesh_util.read(file_name=mixing_elbow)
    mesh_util.create_zones_from_labels("inlet,outlet")

    mesh_util.surface_mesh(min_size=5, max_size=20)

    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    display = PrimePlotter()
    display.plot(model=model)
    display.show()

    part = model.get_part_by_name("flow_volume")

    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))

    search = prime.VolumeSearch(model=model)
    params = prime.VolumeQualitySummaryParams(
        model=model,
        scope=prime.ScopeDefinition(model=model, part_expression="*"),
        cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
        quality_limit=[0.95],
    )
    results = search.get_volume_quality_summary(params=params)

    with tempfile.TemporaryDirectory() as temp_folder:
        mesh_file = os.path.join(temp_folder, "mixing_elbow.cas")
        mesh_util.write(mesh_file)
        assert os.path.exists(mesh_file)
    prime_client.exit()
