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
Export a toy car mesh as OpenUSD HTML
====================================================

**Summary**: This example imports the toy car mesh, and exports the resulting
surface mesh as a self-contained HTML viewer using OpenUSD.

Procedure
~~~~~~~~~~
#. Launch an Ansys Prime Server instance.
#. Import the toy car mesh.
#. Display the imported mesh.
#. Export the mesh as a USD file and a self-contained Three.js HTML viewer.
#. Exit the PyPrimeMesh session.
"""

# sphinx_gallery_tags = ["USD"]

###############################################################################
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
mesh_util = prime.lucid.Mesh(model=model)

###############################################################################
# Import geometry
# ~~~~~~~~~~~~~~~
# Download the toy car mesh file and import it into the model.

toy_car = prime.examples.download_toy_car_pmdat()
mesh_util.read(toy_car)

###############################################################################
# Display the mesh
# ~~~~~~~~~~~~~~~~
# Show the imported surface mesh.

display = PrimePlotter()
display.plot(model)
display.show()

###############################################################################
# Export to OpenUSD and HTML
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build the USD geometry representation from the surface mesh and export it
# as both a ``.usd`` file and a self-contained Three.js HTML viewer.

usd_geom = model.as_usd(update=True)

out_dir = Path.cwd() / "examples" / "gallery" / "_generated"
out_dir.mkdir(parents=True, exist_ok=True)

usd_path = out_dir / "toy_car_mesh.usd"
html_path = export_usd_viewer_html(usd_geom, usd_path, out_dir / "toy_car_mesh_viewer.html")

print(f"USD file: {usd_path}")
print(f"HTML viewer: {html_path}")
print("Controls: left-drag orbit, right-drag pan, scroll zoom.")

###############################################################################
# Exit
# ~~~~
# Exit the PyPrimeMesh session.

prime_client.exit()
