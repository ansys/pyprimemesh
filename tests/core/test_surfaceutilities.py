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

"""Tests for surfaceutilities module."""

import ansys.meshing.prime as prime


def test_surface_utilities(initialized_model_elbow):
    """Tests the SurfaceUtilities class initialization and methods."""
    model: prime.Model
    model, _ = initialized_model_elbow
    surf_utils = prime.SurfaceUtilities(model)

    # get the zonelets from one of the parts
    face_zonelets = model.parts[0].get_face_zonelets()

    # add some thickness to the selected face zonelets
    surf_utils_params = prime.AddThicknessParams(model, 0.3, False)

    result = surf_utils.add_thickness(face_zonelets, surf_utils_params)
    assert result.error_code is prime.ErrorCode.NOERROR
