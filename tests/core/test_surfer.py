# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""This module tests the different methods in Surfer class."""
import ansys.meshing.prime as prime


def test_mesh_topo_faces(initialized_model_elbow):
    """Test the meshing for topo faces."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    topo_faces = model.parts[0].get_topo_faces()

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    results = surfer.mesh_topo_faces(2, topo_faces, surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_remesh_face_zonelets_locally(initialized_model_elbow):
    """Test the remeshing of face zonelets locally."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    local_surfer_params = prime.LocalSurferParams(model)

    part = model.parts[0]
    part.delete_topo_entities(
        prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=False, delete_mesh_zonelets=True)
    )
    face_zonelets = part.get_face_zonelets()
    results = surfer.remesh_face_zonelets_locally(part.id, face_zonelets, 1, local_surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_remesh_face_zonelets(initialized_model_elbow):
    """Test the remeshing of face zonelets."""
    # load example from fixture
    model: prime.Model
    mesher: prime.lucid.Mesh
    model, mesher = initialized_model_elbow
    mesher.surface_mesh(min_size=1, max_size=200)

    surfer = prime.Surfer(model)
    surfer_params = prime.SurferParams(model)
    part = model.parts[0]
    part.delete_topo_entities(
        prime.DeleteTopoEntitiesParams(model, delete_geom_zonelets=False, delete_mesh_zonelets=True)
    )
    face_zonelets = part.get_face_zonelets()
    edge_zonelets = part.get_edge_zonelets()

    results = surfer.remesh_face_zonelets(part.id, face_zonelets, edge_zonelets, surfer_params)
    assert results.error_code is prime.ErrorCode.NOERROR


def test_initialize_surfer_params_for_wrapper(initialized_model_elbow):
    """Test the initialization of surfer parameters."""
    model: prime.Model
    model, _ = initialized_model_elbow
    surfer = prime.Surfer(model)
    surfer_params = surfer.initialize_surfer_params_for_wrapper()
    assert surfer_params != None
