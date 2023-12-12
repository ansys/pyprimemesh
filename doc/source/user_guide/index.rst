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
   wrapper
   automesh
   iga
   stacker
   matchmorph
   sizing
   connections
   mesh_diagnostics
   expressions

Overview
========
The :func:`launch_prime() <ansys.meshing.prime.launch_prime>` method in PyPrimeMesh launches
Ansys Prime Server and returns an instance of the :class:`Client <ansys.meshing.prime.Client>`
class. You can then send gRPC commands to Ansys Prime Server and receive responses 
from it.

.. code-block:: python

    from ansys.meshing.prime import launch_prime

    prime_client = launch_prime()

