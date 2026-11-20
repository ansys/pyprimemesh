"""
.. _ref_mixing_elbow_mesh:

==========================================
Meshing a Mixing Elbow for a Flow Analysis
==========================================

**Summary**: This example illustrates how to mesh a mixing elbow for a flow analysis.

Objective
~~~~~~~~~

In this example, you can mesh a mixing elbow with polyhedral elements and wall boundary
layer refinement. you use several meshing utilities available in the lucid class for
convenience and ease.

.. image:: ../../../images/elbow.png
   :align: center
   :width: 400
   :alt: Mixing elbow mesh.

Procedure
~~~~~~~~~
* Launch Ansys Prime Server and instantiate meshing utilities from lucid class
* Import geometry and create face zones from labels imported from geometry.
* Surface mesh geometry with curvature sizing.
* Volume mesh with polyhedral elements and boundary layer refinement.
* Print statistics on generated mesh.
* Write a cas file for use in the Fluent solver.
* Exit the PyPrimeMesh session.
"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# . Import all necessary modules.

# . Launch an instance of Ansys Prime Server.

# . Connect PyPrimeMesh client and get the model.

# . Instantiate meshing utilities from Lucid class.

import os
import tempfile

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Import Geometry
# ~~~~~~~~~~~~~~~
# . Download the elbow geometry file (.fmd file exported by SpaceClaim).

# . Import geometry.

# . Create face zones from labels imported from geometry for use in Fluent solver.

mixing_elbow = prime.examples.download_elbow_fmd()
mesh_util.read(file_name=mixing_elbow)
mesh_util.create_zones_from_labels("inlet,outlet")

###############################################################################
# Surface Mesh
# ~~~~~~~~~~~~
# . Surface mesh the geometry setting min and max sizing
# that will be used for curvature refinement.

mesh_util.surface_mesh(min_size=5, max_size=20)

###############################################################################
# Volume Mesh
# ~~~~~~~~~~~
# . Volume mesh with polyhedral elements and boundary layer refinement.

# . Fill the volume with polyhedral and prism mesh
# specifying location and number of layers for prisms.

# Expressions are used to define the surfaces to have prisms grown
# where "* !inlet !outlet" states "all not inlet or outlet".

mesh_util.volume_mesh(
    volume_fill_type=prime.VolumeFillType.POLY,
    prism_surface_expression="* !inlet !outlet",
    prism_layers=3,
)

# Display the mesh
display = Graphics(model=model)
display()

###############################################################################
# Print Mesh Statistics
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
# Write Mesh
# ~~~~~~~~~~
# Write a cas file for use in the Fluent solver.
with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "mixing_elbow.cas")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
