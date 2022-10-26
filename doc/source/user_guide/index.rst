.. _ref_index_user_guide:

==========
User Guide
==========
This guide provides a general overview of using the PyPrime library for
mesh preparation.

.. toctree::
   :maxdepth: 1
   :hidden:

   concepts
   launching_pyprime
   lucid
   fileio
   graphics
   surfer
   automesh
   size_field
   controls
   features
   expressions

Overview
========
The :func:`launch_prime() <ansys.meshing.prime.launch_prime>_` function
within the ``ansys-meshing-prime`` library launches the Prime server and
returns an instance of the :class:`Client <ansys.meshing.prime.Client>`. 
This enables the user to send gRPC commands to Prime and receive the response 
from the server.

.. code:: python

    from ansys.meshing.prime import launch_prime

    prime_client = launch_prime()

