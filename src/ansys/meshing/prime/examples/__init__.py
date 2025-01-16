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

from .download_utilities import DownloadManager
from .examples import (
    download_block_model_fmd,
    download_block_model_pmdat,
    download_block_model_scdoc,
    download_bracket_dsco,
    download_bracket_fmd,
    download_bracket_scdoc,
    download_deformed_blade_dsco,
    download_deformed_blade_fmd,
    download_deformed_blade_scdoc,
    download_elbow_dsco,
    download_elbow_fmd,
    download_elbow_pmdat,
    download_elbow_scdoc,
    download_f1_rw_drs_stl,
    download_f1_rw_enclosure_stl,
    download_f1_rw_end_plates_stl,
    download_f1_rw_main_plane_stl,
    download_multi_layer_quad_mesh_pcb_dsco,
    download_multi_layer_quad_mesh_pcb_fmd,
    download_multi_layer_quad_mesh_pcb_pmdat,
    download_multi_layer_quad_mesh_pcb_pmdb,
    download_multi_layer_quad_mesh_pcb_scdoc,
    download_pcb_pmdat,
    download_pcb_scdoc,
    download_pipe_tee_dsco,
    download_pipe_tee_fmd,
    download_pipe_tee_pmdat,
    download_pipe_tee_scdoc,
    download_saddle_bracket_dsco,
    download_saddle_bracket_fmd,
    download_saddle_bracket_scdoc,
    download_solder_ball_fmd,
    download_solder_ball_target_fmd,
    download_toy_car_dsco,
    download_toy_car_fmd,
    download_toy_car_pmdat,
    download_toy_car_scdoc,
    download_turbine_blade_cdb,
    download_wheel_ground_dsco,
    download_wheel_ground_fmd,
    download_wheel_ground_scdoc,
)
from .unit_test_examples import download_test_examples
