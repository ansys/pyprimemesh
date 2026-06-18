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
   solver_translation
   logging
   graphics
   surfer
   wrapper
   automesh
   iga
   multizone
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


Ansys developer ecosystem resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ansys has an extensive developer ecosystem where you can find assistance for a variety of issues.

- `Developer Portal <https://developer.ansys.com/>`_: Blog posts, documentation, and guide
- `Developer Forum <https://discuss.ansys.com/>`_: Scripting and usage support for PyAnsys and other Ansys developer tools
- `Ansys Innovation Space <https://innovationspace.ansys.com/>`_: Product support forum and training materials
- `GitHub <https://github.com/ansys/pymechanical>`_: Development support, bug reporting, feature requests, and more.
- `Ansys Learning Hub <https://learninghub.ansys.com/>`_: Training, courses and learning plans

