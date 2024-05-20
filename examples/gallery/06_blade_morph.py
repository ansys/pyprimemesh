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

"""
.. _ref_turbine_blade:

=========================================================
Morph a hexahedral mesh of a turbine blade to a new shape
=========================================================

**Summary**: This example demonstrates how to morph a structural
hexahedral mesh of a turbine blade to a new deformed shape
defined by a target geometry file.

Objective
~~~~~~~~~~

This example appends a CDB mesh with a CAD geometry
and match morphs the mesh to the geometry.

.. image:: ../../../images/turbine_blade.png
   :align: center
   :width: 800
   :alt: Turbine blade hexahedral mesh.

Procedure
~~~~~~~~~~
* Launch an Ansys Prime Server instance and connect the PyPrimeMesh client.
* Read the mesh and append the new CAD geometry shape.
* Define the mesh source faces and the target geometry faces to match morph.
* Match morph the turbine blade mesh to the new CAD geometry shape.
* Write the mesh for structural analysis.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch the Ansys Prime Server instance and connect the client.
# Get the client model and instantiate meshing utilities from the ``lucid`` class.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Read files
# ~~~~~~~~~~
# Download the turbine blade mesh file and CAD geometry.
# Read the mesh and append the geometry.
# Display the source and the target.

# For Windows OS users, scdoc is also available for geometry:
# target_geometry = prime.examples.download_turbine_blade_target_scdoc()

source_mesh = prime.examples.download_turbine_blade_cdb()
target_geometry = prime.examples.download_deformed_blade_fmd()
mesh_util.read(file_name=source_mesh)
mesh_util.read(file_name=target_geometry, append=True)


display = Graphics(model)
display()
print(model)

###############################################################################
# Define source and target faces
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

source_part = model.get_part(2)
target_part = model.get_part(3)
source = source_part.get_face_zonelets()
target = target_part.get_topo_faces()

###############################################################################
# Match morph mesh
# ~~~~~~~~~~~~~~~~
# Set the target type to be for topoface because the target is geometry.
# Morph the source face zonelets of ``source_part`` to the
# target topofaces of the geometry.

morpher = prime.Morpher(model)
match_pair = prime.MatchPair(
    model=model,
    source_surfaces=source,
    target_surfaces=target,
    target_type=prime.MatchPairTargetType.TOPOFACE,
)

params = prime.MatchMorphParams(model)
bc_params = prime.MorphBCParams(model)
solver_params = prime.MorphSolveParams(model)

morpher.match_morph(
    part_id=source_part.id,
    match_pairs=[match_pair],
    match_morph_params=params,
    bc_params=bc_params,
    solve_params=solver_params,
)

# Display the morphed mesh
display()

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write the morphed CDB file. The geometry is ignored when exporting to a CDB
# file.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "morphed_turbine_blade.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
