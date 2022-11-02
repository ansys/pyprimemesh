"""
.. _ref_bracket_mid_surface_mesh:
=========================================================
Meshing a mid-surfaced bracket for a structural analysis
=========================================================
**Summary**: This example illustrates how to mesh a mid-surfaced bracket.
Objective
~~~~~~~~~
To create conformal surface mesh, we will scaffold topofaces/topoedges to
connect all the surface bodies and mesh the bracket with quad elements.
Procedure
~~~~~~~~~
* Launch Ansys Prime Server
* Import CAD geometry and create part per CAD model
* Scaffold topofaces and topoedges with tolerance parameter
* Surface mesh topofaces with constant size and generate quad elements
* Write a cdb file for use in the APDL solver
* Exit the PyPrime session
"""

###############################################################################
# Import all necessary modules and launch an instance of Ansys Prime Server.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from ansys.meshing import prime
import os, tempfile
from ansys.meshing.prime.graphics import Graphics

# Start Ansys Prime Server, connect PyPrime client and get the model
prime_client = prime.launch_prime()
model = prime_client.model

###############################################################################
# Import geometry and review the part summary
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Download the geometry file (.fmd file exported by SpaceClaim)
bracket_file = prime.examples.download_bracket_fmd()

# Import geometry
# Create part per CAD model for topology based connection
file_io = prime.FileIO(model)
file_io.import_cad(
    file_name=bracket_file,
    params=prime.ImportCadParams(
        model=model,
        length_unit=prime.LengthUnit.MM,
        part_creation_type=prime.PartCreationType.MODEL,
    ),
)

# Display the model to show edges by connection
# Red: free; Black: double; Purple: triple
display = Graphics(model=model)
display()

# Get part summary
part = model.get_part_by_name('bracket_mid_surface-3')
part_summary_res = part.get_summary(prime.PartSummaryParams(model, print_mesh=False))
print(part_summary_res)

###############################################################################
# Scaffold topofaces and topoedges with tolerance parameter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Specify target element size
element_size = 0.5

# Initialize connection tolerance and other parameters
params = prime.ScaffolderParams(
    model,
    absolute_dist_tol=0.1 * element_size,
    intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
    constant_mesh_size=element_size,
)

# Get existing topoface/topoedge ids
faces = part.get_topo_faces()
beams = []

# Scaffold topofaces and/or topoedges with connection parameters
scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
    topo_faces=faces, topo_beams=beams, params=params
)
print(scaffold_res)

###############################################################################
# Surface mesh topofaces with constant size and generate quad elements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Initialize surface meshing parameters
surfer_params = prime.SurferParams(
    model=model,
    size_field_type=prime.SizeFieldType.CONSTANT,
    constant_size=element_size,
    generate_quads=True,
)

# Surface mesh the part with given surface meshing parameters
surfer_result = prime.Surfer(model).mesh_topo_faces(part.id, topo_faces=faces, params=surfer_params)

# Display the mesh
display = Graphics(model=model)
display()

###############################################################################
# Write a cdb file for use in the APDL solver
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with tempfile.TemporaryDirectory() as temp_folder:
    mapdl_cdb = os.path.join(temp_folder, 'bracket_scaffold.cdb')
    file_io.export_mapdl_cdb(mapdl_cdb, params=prime.ExportMapdlCdbParams(model))

    assert os.path.exists(mapdl_cdb)
    print(f'MAPDL case exported at {mapdl_cdb}')

###############################################################################
# Exit the PyPrime session
# ~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()