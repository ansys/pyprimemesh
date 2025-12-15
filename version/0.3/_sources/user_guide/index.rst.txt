.. _ref_index_user_guide:

==========
User guide
==========
This section provides an overview of how you use PyPrimeMesh for mesh preparation.

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
The :func:`launch_prime() <ansys.meshing.prime.launch_prime>` method in PyPrimeMesh launches
the Ansys Prime server and returns an instance of the :class:`Client <ansys.meshing.prime.Client>`
class. You can then send gRPC commands to the Ansys Prime server and receive responses 
from it.

.. code:: python

    from ansys.meshing.prime import launch_prime

    prime_client = launch_prime()

