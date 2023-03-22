"""
.. _ref_pcb:
=====================================
Meshing a PCB for Structural Thermal
=====================================
**Summary**: This example demonstrates how to mesh a printed circuit board
for structural thermal simulation using the stacker method.
Objective
~~~~~~~~~~
In this example, you can mesh the solids of a printed circuit board,
using the stacker method, for a structural thermal analysis
using predominantly hexahedral elements.
.. figure:: ../../../images/pcb.png
   :align: center
   :width: 800
   **Thermal structural mesh**
Procedure
~~~~~~~~~~
-   Launch Ansys Prime Server instance and connect PyPrimeMesh client.
-   Read CAD geometry.
-   Create a base face, projecting edge loops and imprinting to capture geometry.
-   Surface mesh the base face with quad elements.
-   Stack the base face mesh through the volumes to create mainly hexahedral volume mesh.
-   Write mesh for structural thermal analysis.
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
# Import Geometry
# ~~~~~~~~~~~~~~~
# Download the pcb geometry file (.fmd file exported by SpaceClaim).
# Import geometry.
# Display imported geometry.

# For Windows OS users scdoc is also available:
# pcb_geometry = prime.examples.download_pcb_scdoc()

pcb_geometry = prime.examples.download_pcb_pmdat()

mesh_util.read(file_name=pcb_geometry)

display = Graphics(model)
display()

###############################################################################
# Create Base Face
# ~~~~~~~~~~~~~~~~
# Define stacker parameters:
# -   Set direction vector used to define stacking.
# -   Set max offset size for mesh layers created by stacker.
# -   Set the base faces to be deleted after stacking.
# Create base face from part and volumes.
# Define a label for the generated base faces and display.

part = model.parts[0]
sweeper = prime.VolumeSweeper(model)

stacker_params = prime.MeshStackerParams(
    model=model,
    direction=[0,1,0],
    max_offset_size=1.0,
    delete_base=True,
)

createbase_results = sweeper.create_base_face(
    part_id=part.id,
    topo_volume_ids=part.get_topo_volumes(),
    params=stacker_params,
)

base_faces = createbase_results.base_face_ids

part.add_labels_on_topo_entities(["base_faces"],base_faces)

scope = prime.ScopeDefinition(model=model,label_expression="base_faces")

display(scope=scope)

###############################################################################
# Surface Mesh Base Face
# ~~~~~~~~~~~~~~~~~~~~~~
# Quad surface mesh the generated base faces for stacking.

base_scope = prime.lucid.SurfaceScope(
    entity_expression="base_faces",
    part_expression=part.name,
    scope_evaluation_type=prime.ScopeEvaluationType.LABELS,
)

mesh_util.surface_mesh(min_size=0.5,scope=base_scope,generate_quads=True)

display(scope=scope)

###############################################################################
# Stack Base Face
# ~~~~~~~~~~~~~~~~~~~~~~
# Create mainly hexahedral volume mesh using stacker.
# Display volume mesh.

stackbase_results = sweeper.stack_base_face(
    part_id=part.id,
    base_face_ids=base_faces,
    topo_volume_ids=part.get_topo_volumes(),
    params=stacker_params,
)

display()

###############################################################################
# Write Mesh
# ~~~~~~~~~~
# Write a cdb file.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "pcb.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()