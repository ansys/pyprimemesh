PyPrime Documentation |version| BETA
====================================

.. toctree::
   :hidden:
   :maxdepth: 3

   getting_started/index
   user_guide/index
   examples/index
   api/index
   contributing/index

Introduction and Purpose
------------------------

PyPrime is part of the `PyAnsys <pyansys>`_ effort to facilitate the use of Ansys technologies directly
from Python. PyPrime consists of various python modules that help you to acquire geometry and
prepare surface and volume meshes for multiple solvers. Its primary package is ``ansys-meshing-prime``.

PyPrime enables you to: 

* Generate quad dominant and triangular surface meshes
* Generate surface meshes with various sizing options like volumetric, constant, and so on 
* Generate volume meshes with linear and quadratic elements of various shapes like tetrahedra,
  hexahedra, pyramids, prisms
* Generate volume meshes with single process or distributed process 
* Check mesh quality to provide the best solution for the problem and improve predictive
  capabilities
* Perform mesh diagnostics for free, multi-connected edges, self-intersection and overlapping faces
  in the model
* Modularize meshing algorithms, components, and services for easier reuse in other applications
* Expose micro services and APIs for meshing operations to promote meshing workflow prototyping
 
PyPrime integrates the meshing capabilities of the Ansys Prime Server directly into client applications.
PyPrime package provides a Python-friendly interface to drive the software that manages the
submission of low-level Prime commands, while exchanging data through high-performance gRPC
interfaces.

PyPrime  enables you to serve the meshing needs of the industry providing solutions to complex
issues. PyPrime along with the general-purpose Python code effortlessly manages your meshing needs.
PyPrime is now an open source. Enjoy it! Contributions are welcome.

Background
----------

PyPrime is based on Prime gRPC, which helps Prime to be a server and seamlessly connect with the
client and respond to the queries. ``gRPC`` is a lightweight protocol from Google using universal
RPC framework which helps it to run on any environment effortlessly. gRPC stands for grpc remote
procedure call and is an open source. gRPC is built on universal RPC framework which is compatible
with any environment and provides high performance.

PyPrime uses Prime gRPC to establish connection with the client and helps to call the prime APIs
on the remote Prime instance. Prime gRPC  converts python statements into Prime commands and is
transferred to prime instance in the server and enables communication between the client and Prime
server.

Features of PyPrime
-------------------
PyPrime comprises of many robust APIs which do many jobs just on calling the API once and APIs that
just do one job on calling them. These APIs also enable you to query the model and allow you to
build complex models based on the underlying queries. PyPrime has some distinct features that make
them unique. They are: 

* Easy to setup and execute
* Support simple and complex models
* Supports CAD import
* Exports meshes in solver format
* Supports parallel processing like Distributed Parallel, Threaded Parallel, and multiple servers
  driven from python

Quick Code
----------
This section provides a brief idea on how PyPrime works:

To launch PyPrime:

.. code:: python

   import ansys.meshing.prime as prime
   with prime.launch_prime() as prime_client:
       model = prime_client.model


To read a mesh file:

.. code:: python

   import ansys.meshing.prime as prime
   with prime.launch_prime() as prime_client:
       model = prime_client.model

       io = prime.FileIO(model)
       _ = io.read_pmdat(r'E:\Temp\box.pmdat', pyprime.FileReadParams(model=model))
