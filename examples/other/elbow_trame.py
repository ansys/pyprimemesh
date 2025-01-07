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
.. _ref_mixing_elbow_mesh_trame:

===========================================
Meshing a Mixing Elbow for showcasing Trame
===========================================

**Summary**: This example demonstrates how to use the Trame visualizer in PyPrime.

Objective
~~~~~~~~~

In this example, you can see how to use the Trame visualizer using the mixing elbow
as an example.

"""

###############################################################################
# Launch Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Import all necessary modules.
# Launch an instance of Ansys Prime Server.
# Connect PyPrimeMesh client and get the model.
# Instantiate meshing utilities from Lucid class.

import ansys.meshing.prime as prime
from ansys.meshing.prime.graphics import PrimePlotter

# start Ansys Prime Server and get client model
prime_client = prime.launch_prime()
model = prime_client.model

###############################################################################
# Import Geometry
# ~~~~~~~~~~~~~~~
# Download the elbow geometry file (.fmd file exported by SpaceClaim).
# Import geometry.

mesh_util = prime.lucid.Mesh(model=model)
mixing_elbow = prime.examples.download_elbow_fmd()
mesh_util.read(mixing_elbow)
print(model)


mesh_util.surface_mesh(min_size=5, max_size=20)
mesh_util.volume_mesh(
    volume_fill_type=prime.VolumeFillType.POLY,
    prism_surface_expression="* !inlet !outlet",
    prism_layers=3,
)

###############################################################################
# Rendering graphics in Trame
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# When you want to display graphics using Trame, you just need to set the
# ``use_trame`=True``. When the ``display()`` function executes, it
# opens the visualizer in a browser window.

display = PrimePlotter(use_trame=True)
display.plot(model)
display.show()


###############################################################################
# Stopping Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
prime_client.exit()
