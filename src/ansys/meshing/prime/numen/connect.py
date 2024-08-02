# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

"""Module for connect."""
from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.connectutils import TolerantConnect


def tolerant_connect(model: prime.Model, tc_params: dict, cached_data: CachedData):
    """Tolernt connect."""
    tc = TolerantConnect(model)
    tc.fuse(
        connect_tolerance=tc_params["connect_tolerance"],
        side_tolerance=tc_params["side_tolerance"],
        connect_parts_with_diff_tol=tc_params["connect_parts_with_different_tolerance"],
        interfering_parts_exp="",
        interfering_parts_priority=[],
        contact_parts_exp="*",
        part_name=tc_params["part_name"],
        use_absolute_connect_tolerance=True,
        use_mesh_match=True,
        mesh_match_angle=45,
        refine_at_contacts=tc_params["refine_at_contacts"],
        write_intermediate_files=False,
        delete_topology=tc_params["delete_topology"],
    )
