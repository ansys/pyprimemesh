"""
.. _ref_bracket_mid_surface_mesh:

========================================================
Meshing a mid-surfaced bracket for a structural analysis
========================================================

**Summary**: This example demonstrates how to use topology-based connection
to generate conformal surface mesh.

Objective
~~~~~~~~~

To create conformal surface mesh, you can scaffold topofaces, topoedges, or both to
connect all the surface bodies and mesh the bracket with quad elements.

.. image:: ../../../images/bracket_mid_surface_scaffold_w.png
   :align: center
   :width: 400
   :alt: Scaffolding result in a wireframe representation.

Procedure
~~~~~~~~~
* Launch Ansys Prime Server.
* Import the CAD geometry and create the part per the CAD model.
* Scaffold topofaces and topoedges with a tolerance parameter.
* Surface mesh topofaces with a constant size and generate quad elements.
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

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics

prime_client = prime.launch_prime()
model = prime_client.model

###############################################################################
# Import CAD geometry
# ~~~~~~~~~~~~~~~~~~~
# Download the bracket geometry (FMD) file exported by SpaceClaim.
# Import the CAD geometry.
# Create the part per the CAD model for the topology-based connection.

# For Windows OS users, scdoc is also available:
# bracket_file = prime.examples.download_bracket_scdoc()

bracket_file = prime.examples.download_bracket_fmd()

file_io = prime.FileIO(model)
file_io.import_cad(
    file_name=bracket_file,
    params=prime.ImportCadParams(
        model=model,
        length_unit=prime.LengthUnit.MM,
        part_creation_type=prime.PartCreationType.MODEL,
    ),
)

###############################################################################
# Review the part
# ~~~~~~~~~~~~~~~
# Get the part summary.
# Display the model to show edges by connection.
# Use keyboard shortcuts to switch between
# the surface (``s``) and wireframe (``w``) representations.
# Color code for edge connectivity:
#
# - Red: free
# - Black: double
# - Purple: triple

part = model.get_part_by_name('bracket_mid_surface-3')
part_summary_res = part.get_summary(prime.PartSummaryParams(model, print_mesh=False))
print(part_summary_res)

display = Graphics(model=model)
display()

###############################################################################
# Connection
# ~~~~~~~~~~
# Initialize the connection tolerance and other parameters. (The connection
# tolerance is smaller than the target element size.)
# Scaffold the topofaces, topoedges, or both with connection parameters.

# Target element size
element_size = 0.5

params = prime.ScaffolderParams(
    model,
    absolute_dist_tol=0.1 * element_size,
    intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
    constant_mesh_size=element_size,
)

# Get existing topoface or topoedge IDs
faces = part.get_topo_faces()
beams = []

scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
    topo_faces=faces, topo_beams=beams, params=params
)
print(scaffold_res)

###############################################################################
# Surface mesh
# ~~~~~~~~~~~~
# Initialize surface meshing parameters.
# Mesh topofaces with the constant size and generate quad elements.

surfer_params = prime.SurferParams(
    model=model,
    size_field_type=prime.SizeFieldType.CONSTANT,
    constant_size=element_size,
    generate_quads=True,
)

surfer_result = prime.Surfer(model).mesh_topo_faces(part.id, topo_faces=faces, params=surfer_params)

# Display the mesh
display = Graphics(model=model)
display()

###############################################################################
# Write mesh
# ~~~~~~~~~~
# Write a CDB file for use in the APDL solver.

with tempfile.TemporaryDirectory() as temp_folder:
    mapdl_cdb = os.path.join(temp_folder, 'bracket_scaffold.cdb')
    file_io.export_mapdl_cdb(mapdl_cdb, params=prime.ExportMapdlCdbParams(model))
    assert os.path.exists(mapdl_cdb)
    print(f'MAPDL case exported at {mapdl_cdb}')

###############################################################################
# Exit the PyPrimeMesh session
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
