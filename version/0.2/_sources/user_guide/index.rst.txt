.. _ref_index_user_guide:

==========
User Guide
==========
This guide provides a general overview of using the PyPrimeMesh library for
mesh preparation.

.. toctree::
   :maxdepth: 1
   :hidden:

   concepts
   launch_prime
   lucid
   fileio
   logging
   graphics
   surfer
   automesh
   sizing
   connections
   mesh_diagnostics
   expressions

Overview
========
The :func:`launch_prime() <ansys.meshing.prime.launch_prime>` function
within the ``ansys-meshing-prime`` library launches the Ansys Prime server and
returns an instance of the :class:`Client <ansys.meshing.prime.Client>`. 
This enables the user to send gRPC commands to Ansys Prime Server and receive the response 
from the server.

.. code:: python

    from ansys.meshing.prime import launch_prime

    prime_client = launch_prime()

