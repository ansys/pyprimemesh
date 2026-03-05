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

"""
.. _ref_toy_car_wrap:

==================================
Wrap a toy car for a flow analysis
==================================

**Summary**: This example demonstrates how to wrap a toy car for a flow analysis.

Objective
~~~~~~~~~
This example wraps a toy car and volume meshes with a tetrahedral mesh with prisms.
It uses several meshing utilities available in the ``lucid`` class for convenience and ease.

.. image:: ../../../images/toy_car.png
   :align: center
   :width: 400
   :alt: Toy car wrap.

Procedure
~~~~~~~~~
#. Launch an Ansys Prime Server instance.
#. Instantiate the meshing utilities from the ``lucid`` class.
#. Import the geometry.
#. Coarse wrap parts with holes to clean up.
#. Extract the fluid region using a wrapper.
#. Check that the wrap surface is closed and that the quality is suitable.
#. Mesh only fluid with tetrahedral elements and boundary layer refinement.
#. Create face zones from labels imported from the geometry.
#. Print statistics on the generated mesh.
#. Improve the mesh quality.
#. Write a CAS file for use in the Fluent solver.
#. Exit the PyPrimeMesh session.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules and launch an instance of Ansys Prime Server.
# From the PyPrimeMesh client get the model.
# Instantiate meshing utilities from the ``lucid`` class.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

prime_client = prime.launch_prime()
model = prime_client.model

mesh_util = prime.lucid.Mesh(model)
###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the toy car geometry (FMD) file exported by SpaceClaim.
# Import the geometry and display everything except the tunnel.


# For Windows OS users, scdoc is also available:
# toy_car = prime.examples.download_toy_car_scdoc()

toy_car = prime.examples.download_toy_car_fmd()

mesh_util.read(file_name=toy_car)

scope = prime.ScopeDefinition(model, part_expression="* !*tunnel*")

pl = PrimePlotter()
pl.plot(model, scope)
pl.show()
###############################################################################
# Close holes
# ~~~~~~~~~~~
# Several parts are open surfaces (with holes).
# Coarse wrap to close the holes and delete the originals.
# You could use leakage detection to close these regions.
# This example uses a coarse wrap and disables feature edge refinement to walk over the holes.
# As this is not the final wrap, this example does not remesh after the wrap.
# Wrapping each object in turn avoids coarse wrap bridging across narrow gaps.

coarse_wrap = {"cabin": 1.5, "exhaust": 0.6, "engine": 1.5}

for part_name in coarse_wrap:
    # Each open part before wrap
    scope = prime.ScopeDefinition(model, part_expression=part_name)
    pl = PrimePlotter()
    pl.plot(model, scope)
    pl.show()
    closed_part = mesh_util.wrap(
        input_parts=part_name,
        max_size=coarse_wrap[part_name],
        remesh_postwrap=False,
        enable_feature_octree_refinement=False,
    )
    # Closed part with no hole
    scope = prime.ScopeDefinition(model, part_expression=closed_part.name)
    pl = PrimePlotter()
    pl.plot(model, scope)
    pl.show()


###############################################################################
# Extract fluid using a wrapper
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Wrap the full model and extract the largest internal region as the fluid.
# Create edges at intersecting regions to improve the quality.
# Refine mesh to avoid contact between different parts.
# The new wrap object replaces all original geometry unless ``keep_input``
# is set to ``True``.  Volumes are generated from the wrap for use later.

wrap_part = mesh_util.wrap(
    min_size=0.1,
    max_size=2.0,
    region_extract=prime.WrapRegion.LARGESTINTERNAL,
    create_intersection_loops=True,
    contact_prevention_size=0.1,
)

print(model)

###############################################################################
# Check wrap
# ~~~~~~~~~~
# Check that the wrap surface is closed and that the quality is suitable to use
# as surface mesh.

scope = prime.ScopeDefinition(model=model, part_expression=wrap_part.name)
diag = prime.SurfaceSearch(model)

diag_params = prime.SurfaceDiagnosticSummaryParams(
    model,
    scope=scope,
    compute_free_edges=True,
    compute_multi_edges=True,
    compute_self_intersections=True,
)

diag_res = diag.get_surface_diagnostic_summary(diag_params)

print('Number of free edges', diag_res.n_free_edges)
print('Number of multi edges', diag_res.n_multi_edges)
print('Number of self intersections', diag_res.n_self_intersections)

face_quality_measures = [prime.FaceQualityMeasure.SKEWNESS, prime.FaceQualityMeasure.ASPECTRATIO]
quality_params = prime.SurfaceQualitySummaryParams(
    model=model, scope=scope, face_quality_measures=face_quality_measures, quality_limit=[0.9, 20]
)

quality = prime.SurfaceSearch(model)
qual_summary_res = quality.get_surface_quality_summary(quality_params)

for summary_res in qual_summary_res.quality_results:
    print("\nMax value of ", summary_res.measure_name, ": ", summary_res.max_quality)
    print("Faces above limit: ", summary_res.n_found)

###############################################################################
# Create zones
# ~~~~~~~~~~~~
# Create face zones from labels imported from the geometry that can be used
# in the solver to define boundary conditions.
# If specifying individual labels to create zones, the order is important.
# The last label in the list wins.
# Providing no ``label_expression`` flattens all labels into zones.
# For example, if ``LabelA`` and ``LabelB`` are overlapping, three zones are
# created: ``LabelA``, ``LabelB``, and ``LabelA_LabelB``.

mesh_util.create_zones_from_labels()

print(model)

###############################################################################
# Volume mesh
# ~~~~~~~~~~~
# Mesh only fluid volume with tetrahedral elements and boundary layer refinement.
# This example does not mesh other volumetric regions.
# Volume zones exist already for volume meshing and passing to the solver.
# The largest face zonelet is used by default to define volume zone names at creation.
# After volume meshing, you can see that you have a cell zonelet in the part summary.

volume = prime.lucid.VolumeScope(
    part_expression=wrap_part.name,
    entity_expression="tunnel*",
    scope_evaluation_type=prime.ScopeEvaluationType.ZONES,
)

# Use expressions to define which surfaces to grow inflation layers from
mesh_util.volume_mesh(
    scope=volume,
    prism_layers=3,
    prism_surface_expression="*cabin*,*component*,*engine*,*exhaust*,*ground*,*outer*,*wheel*",
    prism_volume_expression="tunnel*",
)

scope = prime.ScopeDefinition(
    model,
    label_expression="*cabin*,*component*,*engine*,*exhaust*,*ground*,*outer*,*wheel*,*outlet*",
)

pl = PrimePlotter()
pl.plot(model, scope)
pl.show()
print(model)

###############################################################################
# Print mesh stats
# ~~~~~~~~~~~~~~~~
# Print statistics on the generated mesh.

vtool = prime.VolumeMeshTool(model=model)
result = vtool.check_mesh(part_id=wrap_part.id, params=prime.CheckMeshParams(model=model))

print("Non positive volumes:", result.has_non_positive_volumes)
print("Non positive areas:", result.has_non_positive_areas)
print("Invalid shape:", result.has_invalid_shape)
print("Left handed faces:", result.has_left_handed_faces)

quality = prime.VolumeSearch(model)
scope = prime.ScopeDefinition(model, part_expression=wrap_part.name)

part_summary_res = wrap_part.get_summary(
    prime.PartSummaryParams(model=model, print_id=False, print_mesh=True)
)

print("\nNo. of cells : ", part_summary_res.n_cells)

qual_summary_res = quality.get_volume_quality_summary(
    prime.VolumeQualitySummaryParams(
        model=model,
        scope=scope,
        cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
        quality_limit=[0.95],
    )
)

for summary_res in qual_summary_res.quality_results_part:
    print("\nMax value of ", summary_res.measure_name, ": ", summary_res.max_quality)
    print("Cells above limit: ", summary_res.n_found)

###############################################################################
# Improve quality
# ~~~~~~~~~~~~~~~
# Because the mesh quality is poor, use the ``improve_by_auto_node_move`` method
# to improve the mesh.

improve = prime.VolumeMeshTool(model=model)
params = prime.AutoNodeMoveParams(
    model=model,
    quality_measure=prime.CellQualityMeasure.SKEWNESS,
    target_quality=0.95,
    dihedral_angle=90,
    n_iterations_per_node=50,
    restrict_boundary_nodes_along_surface=True,
    n_attempts=10,
)

improve.improve_by_auto_node_move(
    part_id=wrap_part.id,
    cell_zonelets=wrap_part.get_cell_zonelets(),
    boundary_zonelets=wrap_part.get_face_zonelets(),
    params=params,
)

result = vtool.check_mesh(part_id=wrap_part.id, params=prime.CheckMeshParams(model=model))

print("Non positive volumes:", result.has_non_positive_volumes)
print("Non positive areas:", result.has_non_positive_areas)
print("Invalid shape:", result.has_invalid_shape)
print("Left handed faces:", result.has_left_handed_faces)

qual_summary_res = quality.get_volume_quality_summary(
    prime.VolumeQualitySummaryParams(
        model=model,
        scope=scope,
        cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
        quality_limit=[0.95],
    )
)

for summary_res in qual_summary_res.quality_results_part:
    print("\nMax value of ", summary_res.measure_name, ": ", summary_res.max_quality)
    print("Cells above limit: ", summary_res.n_found)

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CAS file for use in the Fluent solver.
with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "toy_car_lucid.cas")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
