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

"""Integration test for the bracket scaffold example."""
import math

import ansys.meshing.prime as prime


def test_bracket_scaffold(get_remote_client, get_examples):
    """Tests an use case with the bracket scaffold example."""
    # downloads  file
    bracket_file = get_examples["bracket"]
    model = get_remote_client.model
    # import cad model
    file_io = prime.FileIO(model)
    file_io.import_cad(
        file_name=bracket_file,
        params=prime.ImportCadParams(
            model=model,
            length_unit=prime.LengthUnit.MM,
            part_creation_type=prime.PartCreationType.MODEL,
        ),
    )
    part = model.get_part_by_name('bracket_mid_surface-3')
    part_summary_res = part.get_summary(prime.PartSummaryParams(model, print_mesh=False))
    # Validate topo faces and edges
    assert math.isclose(67, float(part_summary_res.n_topo_edges), rel_tol=0.05)
    assert math.isclose(9, float(part_summary_res.n_topo_faces), rel_tol=0.02)
    # target element size
    element_size = 0.5

    params = prime.ScaffolderParams(
        model,
        absolute_dist_tol=0.1 * element_size,
        intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
        constant_mesh_size=element_size,
    )
    # Get existing topoface/topoedge ids
    faces = part.get_topo_faces()
    beams = []

    scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
        topo_faces=faces, topo_beams=beams, params=params
    )
    # Validate scaffold Operation
    assert scaffold_res.error_code == prime.ErrorCode.NOERROR
    # Mesh topofaces with constant size and generate quad elements.
    surfer_params = prime.SurferParams(
        model=model,
        size_field_type=prime.SizeFieldType.CONSTANT,
        constant_size=element_size,
        generate_quads=True,
    )
    surfer_result = prime.Surfer(model).mesh_topo_faces(
        part.id, topo_faces=faces, params=surfer_params
    )
    # Validate scaffold Operation
    assert surfer_result.error_code == prime.ErrorCode.NOERROR
