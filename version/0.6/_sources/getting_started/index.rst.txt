.. _ref_index_getting_started:

===============
Getting started
===============

PyPrimeMesh is a Python client for Ansys Prime Server,
which provides core Ansys meshing technology.

To use PyPrimeMesh, you must have a local installation of Ansys 2023 R1 or later.
The Ansys version that you have installed dictates the features available to you.

For more information on getting a licensed copy of Ansys, visit the `Ansys website <https://www.ansys.com/>`_.

.. note::
   The PyPrimeMesh client release has one-to-one compatibility with the Ansys Prime Server release.
   That is, the PyPrimeMesh client is only compatible with its corresponding Ansys Prime Server.

This table provides compatibility information:

===========================  ===========================
PyPrimeMesh client release   Ansys Prime Server release
===========================  ===========================
0.2.x                        23.1.0 (2023 R1) 
0.3.x                        23.1.1 (2023 R1 SP1)  
0.4.x                        23.2.0 (2023 R2)
0.5.x                        24.1.0 (2024 R1)
0.6.x                        24.2.0 (2024 R2)
===========================  ===========================

Installation
------------

The ``ansys-meshing-prime`` package currently supports Python 3.8
to Python 3.11 on the Windows and Linux operating systems.

You can install PyPrimeMesh with all dependencies directly from `PyPI <https://pypi.org/>`_  with this command:

.. code-block::

   pip install ansys-meshing-prime[all]


Alternatively, you can clone this repository and install the client using these commands:

.. code-block::

   git clone https://github.com/ansys/pyprimemesh
   cd pyprimemesh
   pip install -e .[all]


The preceding commands install all features that are important to development.
To install a basic version of the client, use this command instead:

.. code-block::

   pip install -e .


Dependencies
------------

You must have Ansys 2023 R1 or later installed to have access to Ansys Prime
Server. Optionally, CAD readers can be configured. 

Ansys Prime Server requires one of the following licenses to run. The system
checks out the first available license from the list in the following order:

1.  CFD PrepPost
2.  CFD PrepPost Pro
3.  Mechanical Enterprise PrepPost
4.  Mechanical Enterprise
5.  Mechanical Pro
6.  Mechanical Premium
7.  Ansys LS-DYNA

Launch PyPrimeMesh
------------------

To launch PyPrimeMesh, use this code:

.. code-block:: python

   import ansys.meshing.prime as prime

   with prime.launch_prime() as prime_client:
       model = prime_client.model

