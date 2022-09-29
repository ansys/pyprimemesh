"""
.. _mixing_elbow_mesh:

===============================================
Meshing a mixing elbow for a flow analysis
===============================================

**Summary**: This example illustrates how to mesh a mixing elbow for a flow analysis.

Objective
~~~~~~~~~

In this example, we will mesh a mixing elbow with polyhedral elements and wall boundary layer refinement.
We will use several meshing utilities available in the lucid class for convenience and ease.

.. image:: ../../../images/elbow.gif
   :align: center
   :width: 400
   :alt: Mixing elbow mesh.

Procedure
~~~~~~~~~
* Launch Prime instance and instantiate meshing utilities from lucid class
* Import geometry and create face zones from labels imported from geometry.
* Surface mesh geometry with curvature sizing.
* Volume mesh with polyhedral elements and boundary layer refinement.
* Print statistics on generated mesh.
* Write a cas file for use in the Fluent solver.
* Exit the Prime session.

"""

###############################################################################
# Import all necessary modules and launch an instance of Prime.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics
import os

# start prime and get the model
prime_client = prime.launch_prime()
model = prime_client.model

# instantiate meshing utilities from lucid class
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Import geometry and create face zones from labels imported from geometry.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Download the elbow geometry file (.fmd file exported by SpaceClaim)
mixing_elbow = prime.examples.download_elbow_fmd()

# Import geometry
mesh_util.read(file_name=mixing_elbow)

# Create face zones from imported labels on geometry for use in Fluent solver
mesh_util.create_zones_from_labels(["inlet", "outlet"])

###############################################################################
# Surface mesh geometry with curvature sizing.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Surface mesh the geometry setting min and max sizing that will be used for curvature refinement
mesh_util.surface_mesh(min_size=5, max_size=20)

###############################################################################
# Volume mesh with polyhedral elements and boundary layer refinement.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Fill the volume with polyhedral and prism mesh specifying location and number of layers for prisms 
# Expressions are used to define the surfaces to have prisms grown where "* !inlet !outlet" states "all not inlet or outlet".
mesh_util.volume_mesh(volume_fill_type=prime.VolumeFillType.POLY,
    prism_surface_expression="* !inlet !outlet",
    prism_layers=3
    )

###############################################################################
# Print statistics on generated mesh.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Display the mesh
display=Graphics(model=model)
display()

# Get meshed part
part = model.get_part_by_name("flow_volume")

# Get statistics on the mesh 
part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))

# Get element quality on all parts in the model
search = prime.VolumeSearch(model=model)
params = prime.VolumeQualitySummaryParams(model=model)
results = search.get_volume_quality_summary(
    prime.VolumeQualitySummaryParams(model=model, scope=prime.ScopeDefinition(model=model, part_expression="*"), 
    cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],quality_limit=[0.95]))

# Print statistics on meshed part
print(part_summary_res)
print(results.quality_results_part[0].max_quality,results.quality_results_part[0].min_quality)

###############################################################################
# Write a cas file for use in the Fluent solver.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mesh_util.write(os.path.join(os.getcwd(), "mixing_elbow.cas"))
print(os.getcwd())

###############################################################################
# Exit the Prime session.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
