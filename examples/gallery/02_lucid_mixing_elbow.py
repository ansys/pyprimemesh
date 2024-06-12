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
.. _ref_mixing_elbow_mesh:

=======================================
Mesh a mixing elbow for a flow analysis
=======================================

**Summary**: This example demonstrates how to mesh a mixing elbow for a flow analysis.

Objective
~~~~~~~~~

This example meshes a mixing elbow with polyhedral elements and wall boundary
layer refinement. It uses several meshing utilities available in the ``lucid`` class for
convenience and ease.

.. image:: ../../../images/elbow.png
   :align: center
   :width: 400
   :alt: Mixing elbow mesh.

Procedure
~~~~~~~~~
* Launch Ansys Prime Server and instantiate meshing utilities from the ``lucid`` class.
* Import the geometry and create face zones from labels imported from the geometry.
* Surface mesh geometry with curvature sizing.
* Volume mesh with polyhedral elements and boundary layer refinement.
* Print statistics on the generated mesh.
* Write a CAS file for use in the Fluent solver.
* Exit the PyPrimeMesh session.
"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.
# Instantiate meshing utilities from the ``lucid`` class.

import os
import tempfile

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the elbow geometry (FMD) file exported by SpaceClaim.
# Import the geometry.
# Create face zones from labels imported from the geometry for use in Fluent solver.


# For Windows OS users, scdoc is also available:
# mixing_elbow = prime.examples.download_elbow_scdoc()

mixing_elbow = prime.examples.download_elbow_fmd()

mesh_util.read(file_name=mixing_elbow)
mesh_util.create_zones_from_labels("inlet,outlet")

###############################################################################
# Surface mesh
# ~~~~~~~~~~~~
# Surface mesh the geometry setting minimum and maximum sizing
# to use for curvature refinement.

mesh_util.surface_mesh(min_size=5, max_size=20)

###############################################################################
# Volume mesh
# ~~~~~~~~~~~
# Volume mesh with polyhedral elements and boundary layer refinement.
# Fill the volume with polyhedral and prism mesh
# specifying the location and number of layers for prisms.
# Use expressions to define the surfaces to have prisms grown
# where ``* !inlet !outlet`` states ``all not inlet or outlet``.

mesh_util.volume_mesh(
    volume_fill_type=prime.VolumeFillType.POLY,
    prism_surface_expression="* !inlet !outlet",
    prism_layers=3,
)

# Display the mesh
display = Graphics(model=model)
display()

###############################################################################
# Print mesh statistics
# ~~~~~~~~~~~~~~~~~~~~~

# Get meshed part
part = model.get_part_by_name("flow_volume")

# Get statistics on the mesh
part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))

# Get element quality on all parts in the model
search = prime.VolumeSearch(model=model)
params = prime.VolumeQualitySummaryParams(
    model=model,
    scope=prime.ScopeDefinition(model=model, part_expression="*"),
    cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
    quality_limit=[0.95],
)
results = search.get_volume_quality_summary(params=params)

# Print statistics on meshed part
print(part_summary_res)
print("\nMaximum skewness: ", results.quality_results_part[0].max_quality)

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CAS file for use in the Fluent solver.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "mixing_elbow.cas")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
