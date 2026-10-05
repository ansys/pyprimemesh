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
.. _ref_pipe_tee:

====================================================================
Mesh a pipe T-section for structural thermal and fluid flow analysis
====================================================================

**Summary**: This example demonstrates how to mesh a pipe T-section for both
structural thermal and fluid flow simulation.


Objective
~~~~~~~~~~

This example meshes the solids of a pipe T-section for a
structural thermal analysis using tetrahedral elements and uses the
wrapper to extract the fluid domain and mesh using polyhedral cells with
prismatic boundary layers.

.. figure:: ../../../images/pipe_tee.png
   :align: center
   :width: 800

   **Thermal structural and fluid flow meshes**

Procedure
~~~~~~~~~~

-   Launch an Ansys Prime Server instance and connect the PyPrimeMesh client.
-   Read the CAD geometry.
-   Mesh for the structural thermal analysis.
-   Write the mesh for the structural thermal analysis.
-   Extract the fluid by wrapping.
-   Mesh with polyhedral and prisms.
-   Write the mesh for the fluid simulation.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch the Ansys Prime Server instance and connect the client.
# Get the client model and instantiate meshing utilities from the ``lucid`` class.

import os
import tempfile

import ansys.meshing.prime.graphics as graphics
from ansys.meshing import prime
from ansys.meshing.prime import lucid

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = lucid.Mesh(model)

###############################################################################
# Read CAD geometry
# ~~~~~~~~~~~~~~~~~
# Download the example FMD geometry file.
# The FMD  file format is exported from SpaceClaim and is compatible with Linux.
# Read and display the geometry file.
# The file contains several unmeshed parts, which is what you would get after you
# import from a CAD file.
# For Windows OS users, the SCDOC format is also available:
# ``pipe_tee = prime.examples.download_pipe_tee_scdoc()``
pipe_tee = prime.examples.download_pipe_tee_fmd()
mesh_util.read(pipe_tee)

display = graphics.Graphics(model)
display()

print(model)

###############################################################################
# Mesh for structural
# ~~~~~~~~~~~~~~~~~~~
# Surface mesh using curvature sizing.
# Volume mesh with tetrahedral elements.
# Delete unwanted capping surface geometries by deleting
# parts that do not have any volume zones.
# Display structural thermal mesh ready for export.

mesh_util.surface_mesh(min_size=2.5, max_size=10)
mesh_util.volume_mesh()

toDelete = [part.id for part in model.parts if not part.get_volume_zones()]

if toDelete:
    model.delete_parts(toDelete)

display = graphics.Graphics(model)
display()

###############################################################################
# Write structural mesh
# ~~~~~~~~~~~~~~~~~~~~~
# Labels are exported to the CDB file as components for
# applying load boundary conditions in the solver.

with tempfile.TemporaryDirectory() as temp_folder:
    structural_mesh = os.path.join(temp_folder, "pipe_tee.cdb")
    mesh_util.write(structural_mesh)
    print("\nExported Structural Mesh: ", structural_mesh)

###############################################################################
# Extract fluid by wrapping
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# You can deal with the small internal diameter change between flanges in several ways:
#
# * Connect the geometry to extract a volume and refine the
#   mesh around this detail to capture.
# * Modify the geometry to remove the feature.
# * Wrap to extract the internal flow volume and walk over the feature.
#
# This example wraps and walks over these features.
#
# Read in the geometry again.
#
# Use a constant size wrap to walk over the diameter change
# feature and extract the largest internal volume as the fluid.
#
# By default, the wrap uses all parts as input and deletes the input
# geometry after wrapping unless ``keep_input`` is set as ``True``.

mesh_util.read(pipe_tee)

wrap = mesh_util.wrap(min_size=6, region_extract=prime.WrapRegion.LARGESTINTERNAL)

print(model)

display()

###############################################################################
# Volume mesh fluid
# ~~~~~~~~~~~~~~~~~
# Create zones for each label to use for boundary condition definitions.
# Volume mesh with prism polyhedral, not growing prisms from inlets and outlets.
# Visualize the generated volume mesh.
# When displaying, you can avoid displaying unnecessary edge zones.
# You can clearly see the prism layers that were specified by the Prism control.

# set global sizing
params = prime.GlobalSizingParams(model, min=6, max=50)
model.set_global_sizing_params(params)

mesh_util.create_zones_from_labels("outlet_main,in1_inlet,in2_inlet")

mesh_util.volume_mesh(
    prism_layers=5,
    prism_surface_expression="* !*inlet* !*outlet*",
    volume_fill_type=prime.VolumeFillType.POLY,
)

print(model)
display(update=True, scope=prime.ScopeDefinition(model=model, label_expression="* !*__*"))

###############################################################################
# Write fluid mesh
# ~~~~~~~~~~~~~~~~
# Write a MSH file for the Fluent solver.

with tempfile.TemporaryDirectory() as temp_folder:
    fluid_mesh = os.path.join(temp_folder, "pipe_tee.msh")
    mesh_util.write(fluid_mesh)
    assert os.path.exists(fluid_mesh)
    print("\nExported Fluid Mesh: ", fluid_mesh)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
