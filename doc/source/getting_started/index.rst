.. _ref_index_getting_started:

===============
Getting started
===============

PyPrimeMesh supports a Python client for Ansys Prime server
that provides core Ansys meshing technology.

To use PyPrimeMesh, you must have a local installation of Ansys. The
version of Ansys installed dictates the features available to you.

For more information on getting a licensed copy of Ansys, visit
`Ansys <ansys>`.

Installation
------------

The ``ansys-meshing-prime`` package currently supports Python 3.7
to Python 3.11 on Windows and Linux operating systems.

You can install PyPrimeMesh with all dependencies directly from PyPI with this code:

.. code::

   pip install ansys-meshing-prime[all]


Alternatively, you can clone this repository and install the client using this code:

.. code::

   git clone https://github.com/pyansys/pyprimemesh
   cd pyprimemesh
   pip install -e .[all]


The preceding code installs all features that are important to development.
To install a basic version of the client, use this command instead:

.. code::

    pip install -e .


Dependencies
------------

You must have a licensed copy of the latest version of Ansys 2023 R1 locally.

Launch PyPrimeMesh
------------------

To launch PyPrimeMesh, use this code:

.. code::

   import ansys.meshing.prime as prime
   with prime.launch_prime() as prime_client:
   	model = prime_client.model

