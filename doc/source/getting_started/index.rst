.. _ref_index_getting_started:

===============
Getting started
===============

PyPrimeMesh supports a Python client for the Ansys Prime server
that provides core Ansys meshing technology.

To use PyPrimeMesh, you must have a local installation of Ansys. The
version of Ansys that you have installed dictates the features available to you.

For more information on getting a licensed copy of Ansys, visit the `Ansys website <https://www.ansys.com/>`_.

.. note::
   The PyPrimeMesh client release has one-to-one compatibility with the Ansys Prime server release.
   That is, PyPrimeMesh client is only compatible with its corresponding Ansys Prime server.

This table provides compatiblity information:

===========================  ===========================
PyPrimeMesh client release   Ansys Prime server release
===========================  ===========================
0.2.0                        23.1.0 (2023 R1) 
0.3.0                        23.1.1 (2023 R1 SP1)  
0.4.0                        23.2.0 (2023 R2)
===========================  ===========================

Installation
------------

The ``ansys-meshing-prime`` package currently supports Python 3.7
to Python 3.11 on the Windows and Linux operating systems.

You can install PyPrimeMesh with all dependencies directly from PyPI with this command:

.. code-block::

   pip install ansys-meshing-prime[all]


Alternatively, you can clone this repository and install the client using these commands:

.. code-block::

   git clone https://github.com/pyansys/pyprimemesh
   cd pyprimemesh
   pip install -e .[all]


The preceding commands install all features that are important to development.
To install a basic version of the client, use this command instead:

.. code-block::

   pip install -e .


Dependencies
------------

You must have Ansys 2023 R1 or later installed for the Ansys Prime server.
(Optionally, CAD readers can be configured.) The Ansys Prime server requires
a Preppost or CFD Preppost license to run.

Launch PyPrimeMesh
------------------

To launch PyPrimeMesh, use this code:

.. code-block:: python

   import ansys.meshing.prime as prime

   with prime.launch_prime() as prime_client:
       model = prime_client.model

