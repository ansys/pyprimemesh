"""
.. _ref_saddle_thin_hex:

========================================================
Meshing a saddle bracket for a structural analysis
========================================================

**Summary**: This example demonstrates how to mesh a thin
solid with hexahedral elements.

Objective
~~~~~~~~~

To create a mainly hexahedral mesh on a thin solid volume.

.. image:: ../../../images/saddle_bracket.png
   :align: center
   :width: 400
   :alt: Thin volume hexahedral mesh.

Procedure
~~~~~~~~~
* Launch Ansys Prime Server.
* Import the CAD geometry.
* Quad surface mesh the source faces.
* Delete the topology.
* Define volume meshing controls to use thin volume meshing.
* Volume mesh with hexahedral cells.
* Write a CDB file for use in the APDL solver.
* Exit the PyPrimeMesh session.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch an instance of Ansys Prime Server.
# Connect the PyPrimeMesh client and get the model.

import os
import tempfile

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model
display = Graphics(model=model)

mesh_util = prime.lucid.Mesh(model)

###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the saddle bracket geometry (FMD) file exported by SpaceClaim.
# Import the geometry and display all.

# For Windows OS users, scdoc is also available:
# saddle_bracket = prime.examples.download_saddle_bracket_scdoc()

saddle_bracket = prime.examples.download_saddle_bracket_fmd()

mesh_util.read(file_name=saddle_bracket)

print(model)

display = Graphics(model)
display()

###############################################################################
# Quad mesh faces
# ~~~~~~~~~~~~~~~~~~~~~~
# Mesh the source faces for the thin volume control with quads.

mesh_util.surface_mesh(
    min_size=2.0,
    generate_quads=True,
)

display()

###############################################################################
# Delete topology
# ~~~~~~~~~~~~~~~
# Delete topology to leave only the surface mesh.

part.delete_topo_entities(
    prime.DeleteTopoEntitiesParams(
        model=model,
        delete_geom_zonelets=True,
        delete_mesh_zonelets=False,
    )
)

###############################################################################
# Define volume meshing controls
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define volume meshing controls to use thin volume meshing.
# Specify source and target faces for the thin volume using imported labels.
# Set the number of layers of cells through the thickness of the thin solid to be 4.
# To request a fully hexahedral mesh the side faces must be imprinted.

auto_mesh_params = prime.AutoMeshParams(model=model)
thin_vol_ctrls_ids = []
thin_vol_ctrl = model.control_data.create_thin_volume_control()

thin_vol_ctrl.set_source_scope(
    prime.ScopeDefinition(
        model=model,
        label_expression="source_thin",
    )
)

thin_vol_ctrl.set_target_scope(
    prime.ScopeDefinition(
        model=model,
        label_expression="target_thin",
    )
)

thin_params = prime.ThinVolumeMeshParams(
    model=model,
    n_layers=4,
    no_side_imprint=False,
)

thin_vol_ctrl.set_thin_volume_mesh_params(thin_volume_mesh_params=thin_params)
thin_vol_ctrls_ids.append(thin_vol_ctrl.id)
auto_mesh_params.thin_volume_control_ids = thin_vol_ctrls_ids
auto_mesh_params.volume_fill_type = prime.VolumeFillType.TET

###############################################################################
# Generate volume mesh
# ~~~~~~~~~~~~~~~~~~~~
# Volume mesh to obtain hexahedral cells.
# Print mesh summary.
# Display volume mesh.

volume_mesh = prime.AutoMesh(model=model)
result_vol = volume_mesh.mesh(part_id=part.id, automesh_params=auto_mesh_params)
print(part.get_summary(prime.PartSummaryParams(model)))

display()

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CDB file for use in the MAPDL solver.

with tempfile.TemporaryDirectory() as temp_folder:
    mesh_file = os.path.join(temp_folder, "saddle_bracket.cdb")
    mesh_util.write(mesh_file)
    assert os.path.exists(mesh_file)
    print("\nExported file:\n", mesh_file)

###############################################################################
# Exit PyPrimeMesh
# ~~~~~~~~~~~~~~~~

prime_client.exit()
