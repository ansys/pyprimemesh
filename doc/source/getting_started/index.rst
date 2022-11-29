.. _ref_index_getting_started:

===============
Getting Started
===============

The PyPrimeMesh project supports a python client for Ansys Prime Server
that provides core Ansys meshing technology.

To use PyPrimeMesh, you must have a local installation of Ansys. The
version of Ansys installed dictates the features available to you.

For more information on getting a licensed copy of Ansys, visit
`Ansys <ansys>`.

Installation
------------

The ``ansys-meshing-prime`` package currently supports Python 3.7
to Python 3.9 on Windows and Linux operating systems.

PyPrimeMesh can be installed directly from PyPi as follows:

.. code::

   pip install ansys-meshing-prime

.. note::
   PyPrimeMesh is not available on PyPi at present.

Alternatively, clone and install in development mode with:

.. code::

   git clone https://github.com/pyansys/pyprime
   cd pyprime
   pip install -e .[graphics] --find-links deps

Dependencies
------------
You must have a licensed copy of the latest version of Ansys 2023 R1 locally.

Launching PyPrimeMesh
-----------------

To launch PyPrimeMesh:

.. code::

   import ansys.meshing.prime as prime
   with prime.launch_prime() as prime_client:
   	model = prime_client.model
