"""
.. _ref_toy_car_wrap:

===============================================
Wrapping a toy car for a flow analysis
===============================================

**Summary**: This example illustrates how to wrap a toy car for a flow analysis.

Objective
~~~~~~~~~
In this example, we will wrap a toy car and volume mesh with a tetrahedral mesh with prisms.
We will use several meshing utilities available in the lucid class for convenience and ease.

.. image:: ../images/toy_car.png
   :align: center
   :width: 400
   :alt: Toy car wrap.

Procedure
~~~~~~~~~
* Launch Prime instance and instantiate meshing utilities from lucid class.
* Import geometry.
* Coarse wrap parts with holes to cleanup.
* Extract fluid region using wrapper.
* Check wrap surface is closed and suitable quality.
* Delete all unneeded parts.
* Compute volumes and mesh only fluid with tetrahedral elements and boundary layer refinement.
* Create face zones from labels imported from geometry.
* Print statistics on generated mesh.
* Write a cas file for use in the Fluent solver.
* Exit the Prime session.
"""

###############################################################################
# Import all necessary modules and launch an instance of Prime.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics
import os

# start prime and get the model
prime_client = prime.launch_prime()
model = prime_client.model
display = Graphics(model)

# instantiate meshing utilities from lucid class
mesh_util = prime.lucid.Mesh(model)

###############################################################################
# Import geometry.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Download the toy car geometry file (.fmd file exported by SpaceClaim)
toy_car = prime.examples.download_toy_car_fmd()

# Import geometry
mesh_util.read(file_name=toy_car)

###############################################################################
# Coarse wrap parts with holes to cleanup.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# several objects are open surfaces (with holes)
# coarse wrap to close holes and delete originals
display(scope=prime.ScopeDefinition(model, part_expression="cabin,exhaust,engine"))

# we could use leakage detection to close these regions
# here we use a coarse wrap and disable feature edge refinement to walk over the holes
# as this is not the final wrap we do not need to remesh after the wrap
# wrapping each object in turn we avoid the coarse wrap bridging across narrow gaps
coarse_wrap = {"cabin": 1.5, "exhaust": 0.6, "engine": 1.5}
for part_name in coarse_wrap:
    mesh_util.wrap(
        input_parts=part_name,
        max_size=coarse_wrap[part_name],
        remesh_postwrap=False,
        enable_feature_octree_refinement=False)
    model.delete_parts([model.get_part_by_name(part_name).id])

###############################################################################
# Extract fluid region using wrapper.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# wrap full model and extract largest internal region as the fluid
# creating edges at intersecting regions to improve quality
# refining mesh to avoid contact between different parts
wrap_part = mesh_util.wrap(
    min_size=0.1,
    max_size=2.0,
    region_extract=prime.WrapRegion.LARGESTINTERNAL,
    create_intersection_loops=True,
    contact_prevention_size=0.1)

# notice that no volume zones exist as yet for the wrap
# volume zones must be computed to define regions to volume mesh
# the model contains many geometry entities that are no longer needed
print(model)

###############################################################################
# Check wrap surface is closed and suitable quality.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# check wrap surface has valid connectivity and quality to use as surface mesh
scope = prime.ScopeDefinition(model=model, part_expression=wrap_part.name)
diag = prime.SurfaceSearch(model)
diag_params = prime.SurfaceDiagnosticSummaryParams(model, scope=scope,
    compute_free_edges= True, compute_multi_edges= True, compute_self_intersections=True)
diag_res = diag.get_surface_diagnostic_summary(diag_params)
print('Number of free edges', diag_res.n_free_edges)
print('Number of multi edges', diag_res.n_multi_edges)
print('Number of self intersections', diag_res.n_self_intersections)

face_quality_measures = [prime.FaceQualityMeasure.SKEWNESS, prime.FaceQualityMeasure.ASPECTRATIO]
quality_params = prime.SurfaceQualitySummaryParams(model = model, scope = scope,
    face_quality_measures = face_quality_measures, quality_limit=[0.9, 20])
quality = prime.SurfaceSearch(model)
qual_summary_res = quality.get_surface_quality_summary(quality_params)

for summary_res in qual_summary_res.quality_results:
    print("\nMax value of ", summary_res.measure_name, ": ", summary_res.max_quality)
    print("Faces above limit: ", summary_res.n_found)

###############################################################################
# Delete all unneeded parts.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# keep only the wrap surface
toDelete = [part.id for part in model.parts if part.name != wrap_part.name]
model.delete_parts(toDelete)

###############################################################################
# Compute volumes and mesh only fluid with tetrahedral elements and boundary layer refinement.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mesh_util.compute_volumes(part_expression=wrap_part.name)

# only the wrap part is now present
# volume zones exist ready for volume meshing and passing to the solver
print(model)

# the largest face zonelet
volume = prime.lucid.VolumeScope(part_expression=wrap_part.name,
    entity_expression="tunnel*",
    scope_evaluation_type=prime.ScopeEvaluationType.ZONES)

# using expressions to define which surfaces to grow inflation layers from
mesh_util.volume_mesh(scope=volume,
    prism_layers=3,
    prism_surface_expression="cabin*,component*,engine*,exhaust*,ground*,outer*,wheel*",
    prism_volume_expression="tunnel*")

display(update=True)

###############################################################################
# Create face zones from labels imported from geometry.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# last label will win so order can be important
label_list = wrap_part.get_labels()
all_labels = ",".join(label_list)
mesh_util.create_zones_from_labels(all_labels)

###############################################################################
# Print statistics on generated mesh.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## mesh checks
vtool = prime.VolumeMeshTool(model=model)
result = vtool.check_mesh(part_id=wrap_part.id, params = prime.CheckMeshParams(model=model))

print("Non positive volumes:", result.has_non_positive_volumes)
print("Non positive areas:", result.has_non_positive_areas)
print("Invalid shape:", result.has_invalid_shape)
print("Left handed faces:", result.has_left_handed_faces)

quality = prime.VolumeSearch(model)
qual_summary_res = quality.get_volume_quality_summary(
    prime.VolumeQualitySummaryParams(model = model, scope=scope,
    cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS], quality_limit=[0.95]))

part_summary_res = wrap_part.get_summary(
    prime.PartSummaryParams(model = model, print_id = False, print_mesh = True))

print("\nNo. of faces : ", part_summary_res.n_faces)

###############################################################################
# Write a cas file for use in the Fluent solver.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mesh_util.write(os.path.join(os.getcwd(), "toy_car_lucid.cas"))
print("\nCurrent working directory for exported files: ", os.getcwd())

###############################################################################
# Exit the Prime session.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
