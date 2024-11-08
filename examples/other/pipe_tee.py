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

"""
.. _ref_pipe_tee_mesh:

================================================================
Meshing a pipe tee for both flow and thermal structural analysis
================================================================

**Summary**: This example demonstrates how to mesh a pipe T-section for both fluid
and structural thermal simulation.

Objective
~~~~~~~~~

In this example we will mesh the solids of a pipe T-section for a
structural thermal analysis using tetrahedral elements and use the
wrapper to extract the fluid domain and mesh using polyhedral cells with
prismatic boundary layers.

To achieve these tasks we will use the high level API packaged with PyPrimeMesh called Lucid.

.. image:: ../images/pipe_tee.png
   :align: center
   :height: 400
   :alt: Pipe tee mesh.

Procedure
~~~~~~~~~
* Launch Prime instance and instantiate meshing utilities from lucid class.
* Import CAD geometry.
* Mesh for structural.
* Write mesh for structural thermal analysis.
* Extract fluid by wrapping.
* Mesh with polyhedral and prisms.
* Write a cas file for use in the Fluent solver.
* Exit the Prime session.
"""

###############################################################################
# Import all necessary modules and launch an instance of Prime
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

# Start prime and get the model.
prime_client = prime.launch_prime()
model = prime_client.model

# Instantiate meshing utilities from lucid class.
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Import CAD geometry
# ~~~~~~~~~~~~~~~~~~~

# Download the pipe tee geometry file (.fmd file exported by SpaceClaim).
cad_file = prime.examples.download_pipe_tee_fmd()

# Import geometry.
mesh_util.read(cad_file)

# Read from the file, which is an unmeshed part
# like you would get after you imported from a CAD file.
display = PrimePlotter()
display.plot(model)
display.show()

###############################################################################
# Mesh for structural
# ~~~~~~~~~~~~~~~~~~~

# Surface and volume mesh structural parts
# specifying only min/max size performs a tri surface mesh with curvature refinement.
mesh_util.surface_mesh(min_size=2.5, max_size=10)

# Providing no inputs creates a tetrahedral volume mesh for all closed regions in the model.
mesh_util.volume_mesh()

# Delete unwanted capping surfaces.
toDelete = [part.id for part in model.parts if not part.get_volume_zones()]

if toDelete:
    model.delete_parts(toDelete)

# Display structural mesh.
display = PrimePlotter()
display.plot(model)
display.show()

###############################################################################
# Write mesh for structural thermal analysis.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Writing a file with extension cdb exports the mesh in cdb format.
mesh_util.write(os.path.join(os.getcwd(), r"t-junction-solids.cdb"))

###############################################################################
# Extract fluid by wrapping
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# Reread cad.
mesh_util.read(cad_file)

# Wrap internal region to extract CFD model with a constant size.
wrap = mesh_util.wrap(min_size=6, region_extract=prime.WrapRegion.LARGESTINTERNAL)

# View only the wrap.
display = PrimePlotter()
display.plot(model, scope=prime.ScopeDefinition(model=model, part_expression=wrap.name))
display.show()


# Delete unwanted parts to leave only wrap.
toDelete = [part.id for part in model.parts if part.name != wrap.name]

if toDelete:
    model.delete_parts(toDelete)

###############################################################################
# Mesh with polyhedral and prisms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Compute volume zones and create zones from labels for use in the Fluent solver.
mesh_util.compute_volumes()
mesh_util.create_zones_from_labels("in1_inlet,in2_inlet,outlet_main")

print(model)

# Set global sizing to be used by the volume mesh.
params = prime.GlobalSizingParams(model, min=6, max=50)
model.set_global_sizing_params(params)

# Volume mesh wrap with prisms.
mesh_util.volume_mesh(
    prism_layers=5,
    prism_surface_expression="* !*inlet !outlet*",
    scope=prime.lucid.VolumeScope(),
    volume_fill_type=prime.VolumeFillType.POLY,
)

# Display mesh without unwanted edge zonelets. You can clearly see the
# prism layers that were specified by the ``Prism`` control.
display = PrimePlotter()
display.plot(model, scope=prime.ScopeDefinition(model=model, label_expression="* !*__*"))
display.show()

###############################################################################
# Write a CAS file for use in the Fluent solver
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Write CFD model.
mesh_util.write(os.path.join(os.getcwd(), r"t-junction-fluid.cas"))

###############################################################################
# Exit the Prime session
# ~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
