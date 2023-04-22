"""
.. _ref_turbine_blade:

============================================================
Morphing A Hexahedral Mesh Of A Turbine Blade To A New Shape
============================================================

**Summary**: This example demonstrates how to morph a structural
hexahedral mesh of a turbine blade to a new deformed shape
defined by a target geometry file.

Objective
~~~~~~~~~~

In this example, you can append a CDB mesh with a CAD geometry
and match morph the mesh to the geometry.
.. figure:: ../../../images/turbine_blade.png
   :align: center
   :width: 800
   **Turbine blade hexahedral mesh**

Procedure
~~~~~~~~~~
* Launch Ansys Prime Server instance and connect PyPrimeMesh client.
* Read mesh and append new CAD geometry shape.
* Define the mesh source faces and the target geometry faces to match morph.
* Match morph the turbine blade mesh to the new CAD geometry shape.
* Write mesh for structural analysis.
"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch Ansys Prime Server instance and connect client.
# Get the client model and instantiate meshing utilities from Lucid class.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Read Files
# ~~~~~~~~~~
# Download the turbine blade mesh file and CAD geometry.
# Read mesh and append geometry.
# Display source and target.

# For Windows OS users scdoc is also available for geometry:
# target_geometry = prime.examples.download_turbine_blade_target_scdoc()

source_mesh = prime.examples.download_turbine_blade_cdb()
target_geometry = prime.examples.download_deformed_blade_fmd()
mesh_util.read(file_name=target_geometry)
mesh_util.read(file_name=source_mesh, append=True)

display = Graphics(model)
display()
print(model)

###############################################################################
# Define Source and Target Faces
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

source_part = model.get_part_by_name("blade")
target_part = model.get_part_by_name("blade_deformed")
source = source_part.get_face_zonelets()
target = target_part.get_topo_faces()

###############################################################################
# Match Morph Mesh
# ~~~~~~~~~~~~~~~~

morpher = prime.Morpher(model)
match_pair = prime.MatchPair(
    model=model,
    source_surfaces=source,
    target_surfaces=target,
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

# display the morphed mesh
display()

# delete geometry as no longer needed ready for export
model.delete_parts([target_part.id])

###############################################################################
# Write Mesh
# ~~~~~~~~~~
# Write morphed cdb file.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "morphed_turbine_blade.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
