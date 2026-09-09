"""
.. _ref_turbine_blade:

============================================================
Morphing a hexahedral mesh of a turbine blade to a new shape
============================================================

**Summary**: This example demonstrates how to morph a structural
hexahedral mesh of a turbine blade to a new deformed shape
defined by a target geometry file.

Objective
~~~~~~~~~~

This example appends a CDB mesh with a CAD geometry
and match morphes the mesh to the geometry.

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
mesh_util.read(file_name=target_geometry)
mesh_util.read(file_name=source_mesh, append=True)

display = Graphics(model)
display()
print(model)

###############################################################################
# Define source and target faces
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

source_part = model.get_part_by_name("blade")
target_part = model.get_part_by_name("blade_deformed")
source = source_part.get_face_zonelets()
target = target_part.get_topo_faces()

###############################################################################
# Match morph mesh
# ~~~~~~~~~~~~~~~~
# Set the target type to be for topoface because the target is geometry.
# Morph the source face zonelets of ``source_part`` to the
# target topo faces of the geometry.

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
