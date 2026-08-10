# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
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
.. _ref_openusd_export:

====================================================
Export a bracket scaffold mesh as OpenUSD HTML
====================================================

**Summary**: This example imports the bracket scaffold geometry, scaffolds
and surface meshes it, and exports the resulting mesh as a self-contained
HTML viewer using OpenUSD.

Procedure
~~~~~~~~~~
#. Launch an Ansys Prime Server instance.
#. Import the bracket scaffold geometry.
#. Scaffold the topofaces and surface mesh them with quad elements.
#. Display the resulting mesh.
#. Export the mesh as a USD file and a self-contained Three.js HTML viewer.
#. Exit the PyPrimeMesh session.
"""

# sphinx_gallery_tags = ["USD"]

###########################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules, launch an instance of Ansys Prime Server,
# and connect the PyPrimeMesh client.

from pathlib import Path

import ansys.meshing.prime as prime
from ansys.meshing.prime.core.mesh_usd_io import export_usd_viewer_html
from ansys.meshing.prime.graphics import PrimePlotter

prime_client = prime.launch_prime()
model = prime_client.model

#################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the bracket scaffold geometry (FMD) file and import it into the
# model, creating a part per the CAD model for the topology-based connection.

bracket_file = prime.examples.download_bracket_fmd(force_download=True)

file_io = prime.FileIO(model)
file_io.import_cad(
    file_name=bracket_file,
    params=prime.ImportCadParams(
        model=model,
        length_unit=prime.LengthUnit.MM,
        part_creation_type=prime.PartCreationType.MODEL,
    ),
)

part = model.get_part_by_name('bracket_mid_surface-3')

###########################
# Scaffold and surface mesh
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Scaffold the topofaces to connect all the surface bodies, then surface
# mesh the topofaces with a constant size to generate quad elements.

element_size = 0.5

scaffolder_params = prime.ScaffolderParams(
    model,
    absolute_dist_tol=0.1 * element_size,
    intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
    constant_mesh_size=element_size,
)

faces = part.get_topo_faces()

scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
    topo_faces=faces, topo_beams=[], params=scaffolder_params
)
print(scaffold_res)

surfer_params = prime.SurferParams(
    model=model,
    size_field_type=prime.SizeFieldType.CONSTANT,
    constant_size=element_size,
    generate_quads=True,
)

surfer_result = prime.Surfer(model).mesh_topo_faces(part.id, topo_faces=faces, params=surfer_params)

##################
# Display the mesh
# ~~~~~~~~~~~~~~~~
# Show the resulting surface mesh.

display = PrimePlotter()
display.plot(model, update=True)
display.show()

############################
# Export to OpenUSD and HTML
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build the USD geometry representation from the surface mesh and export it
# as both a ``.usd`` file and a self-contained Three.js HTML viewer.

usd_geom = model.as_usd(update=True)

out_dir = Path.cwd() / "examples" / "gallery" / "_generated"
out_dir.mkdir(parents=True, exist_ok=True)

usd_path = out_dir / "bracket_scaffold_mesh.usd"
html_path = export_usd_viewer_html(
    usd_geom, usd_path, out_dir / "bracket_scaffold_mesh_viewer.html"
)

print(f"USD file: {usd_path}")
print(f"HTML viewer: {html_path}")
print("Controls: left-drag orbit, right-drag pan, scroll zoom.")

######
# Exit
# ~~~~
# Exit the PyPrimeMesh session.

prime_client.exit()
