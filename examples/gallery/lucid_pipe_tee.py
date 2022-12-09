"""
.. _ref_pipe_tee:

===============================================================
Meshing a Pipe T-Section for Structural Thermal and Fluid Flow
===============================================================

**Summary**: This example demonstrates how to mesh a pipe T-section for both fluid
and structural thermal simulation.


Objective
~~~~~~~~~~

In this example we will mesh the solids of a pipe T-section for a
structural thermal analysis using tetrahedral elements and use the
wrapper to extract the fluid domain and mesh using polyhedral cells with
prismatic boundary layers.

.. figure:: ../../../images/pipe_tee.png
   :align: center
   :width: 800

   **Thermal structural and fluid flow meshes**

Procedure
~~~~~~~~~~

-   Launch Ansys Prime Server instance and connect PyPrimeMesh client.
-   Read CAD geometry.
-   Mesh for structural thermal analysis.
-   Write mesh for structural thermal analysis.
-   Extract fluid by wrapping.
-   Mesh with polyhedral and prisms.
-   Write mesh for fluid simulation.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch Ansys Prime Server instance and connect client.
# Get the client model and instantiate meshing utilities from lucid class.

from ansys.meshing import prime
import ansys.meshing.prime.graphics as graphics
from ansys.meshing.prime import lucid

import os

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = lucid.Mesh(model)

###############################################################################
# Read CAD Geometry
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Download example FMD geometry file.
# FMD format is exported from SpaceClaim and is compatible with Linux.
# Read and display the geometry file.
# The file contains several unmeshed parts as you would get after you imported from CAD.

file_name = prime.examples.download_pipe_tee_fmd()
mesh_util.read(file_name)

display = graphics.Graphics(model)
display()

print(model)

###############################################################################
# Mesh for Structural
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Write Structural Mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Labels will be exported to CDB as collections for use in
# applying load boundary conditions in the solver.

struc_mesh = os.path.join(os.getcwd(), "pipe_tee.cdb")
mesh_util.write(struc_mesh)

print("\nExported Structural Mesh: ", struc_mesh)

###############################################################################
# Extract Fluid by Wrapping
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# There is a small internal diameter change between flanges that
# can be dealt with in several ways:
#
#  * Connect the geometry to extract a volume and refine the
#    mesh around this detail to capture.
#  * Modify the geometry to remove the feature.
#  * Wrap to extract the internal flow volume and walk over the feature.
#
# Here we will choose to wrap and walk over these features.
#
# We will start by reading in the geometry again.
# Next we will use a constant size wrap to walk over the diameter change
# feature and extract the largest internal volume as the fluid.
# By default the wrap will use all parts as input and delete the input
# geometry after wrapping unless keep_input is set as True.
# When displaying we can avoid displaying unnecessary edge zones.

mesh_util.read(file_name)

wrap = mesh_util.wrap(min_size=6, region_extract=prime.WrapRegion.LARGESTINTERNAL)

print(model)

display()

###############################################################################
# Volume Mesh Fluid
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create zones for each label to be used for boundary conditions definitions.
# Volume mesh with prism polyhedral not growing prisms from inlets and outlets.
# Let us visualize the generated volume mesh.
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
# Write Fluid Mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a MSH file for the Fluent solver.

fluid_mesh = os.path.join(os.getcwd(), "pipe_tee.msh")

mesh_util.write(fluid_mesh)

print("\nExported Fluid Mesh: ", fluid_mesh)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
