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
from ansys.meshing.prime.graphics import Graphics

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
# `use_trame` flag to True. When `display()` function executes, it will
# pop a browser window with the visualizer open.

display = Graphics(model, use_trame=True)
display()


###############################################################################
# Stopping Ansys Prime Server
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
prime_client.exit()
