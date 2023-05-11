"""
.. _ref_pcb:

=============================================
Meshing a PCB for structural thermal analysis
=============================================

**Summary**: This example demonstrates how to mesh a PCB (printed circuit
board) for structural thermal simulation using the stacker method.

Objective
~~~~~~~~~~
This example meshes the solids of a PCB using the stacker method for a
structural thermal analysis using predominantly hexahedral elements.

.. image:: ../../../images/pcb_stacker.png
   :align: center
   :width: 800
   :alt: Thermal structural mesh.

Procedure
~~~~~~~~~~
* Launch an Ansys Prime Server instance and connect the PyPrimeMesh client.
* Read the CAD geometry.
* Create a base face, projecting edge loops and imprinting to capture the geometry.
* Surface mesh the base face with quad elements.
* Stack the base face mesh through the volumes to create mainly hexahedral volume mesh.
* Write the mesh for the structural thermal analysis.
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
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the PCB's geometry (FMD) file exported by SpaceClaim.
# Import the geometry.
# Display the imported geometry.

pcb_geometry = prime.examples.download_pcb_pmdat()

mesh_util.read(file_name=pcb_geometry)

display = Graphics(model)
display()

###############################################################################
# Create base face
# ~~~~~~~~~~~~~~~~
# Define stacker parameters:
#
# - Set the direction vector for defining stacking.
# - Set the maximum offset size for mesh layers created by the stacker method.
# - Set the base faces to delete after stacking.
#
# Create the base face from the part and volumes.
# Define a label for the generated base faces and display.

part = model.parts[0]
sweeper = prime.VolumeSweeper(model)

stacker_params = prime.MeshStackerParams(
    model=model,
    direction=[0, 1, 0],
    max_offset_size=1.0,
    delete_base=True,
)

createbase_results = sweeper.create_base_face(
    part_id=part.id,
    topo_volume_ids=part.get_topo_volumes(),
    params=stacker_params,
)

base_faces = createbase_results.base_face_ids

part.add_labels_on_topo_entities(["base_faces"], base_faces)

scope = prime.ScopeDefinition(model=model, label_expression="base_faces")

display(scope=scope)

###############################################################################
# Surface mesh base face
# ~~~~~~~~~~~~~~~~~~~~~~
# Quad surface mesh the generated base faces for stacking.

base_scope = prime.lucid.SurfaceScope(
    entity_expression="base_faces",
    part_expression=part.name,
    scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
)

mesh_util.surface_mesh(min_size=0.5, scope=base_scope, generate_quads=True)

display(scope=scope)

###############################################################################
# Stack base face
# ~~~~~~~~~~~~~~~~~~~~~~
# Create mainly hexahedral volume mesh using the stacker method.
# Display the volume mesh.

stackbase_results = sweeper.stack_base_face(
    part_id=part.id,
    base_face_ids=base_faces,
    topo_volume_ids=part.get_topo_volumes(),
    params=stacker_params,
)

display()

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CDB file.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "pcb.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
