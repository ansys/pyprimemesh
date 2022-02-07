PyPRIME
=======
--------------------------
Introduction and Purpose 
--------------------------

PyPrime is an integral part of PyAnsys effort to facilitate the use of Ansys technologies directly from Python. PyPrime consists of various python modules that help you to acquire geometry and generate surface and volume meshes for multiple solvers. PyPrime uses ansys.meshing.fm as primary module to acquire geometry data. For generating mesh, the primary module is ansys.meshing.prime. PyPrime enables you to: 

* Generate quad dominant and triangular surface meshes 

* Generate surface meshes with various sizing options like volumetric, constant, and so on 

* Generate volume meshes with linear and quadratic elements of various shapes like tetrahedra, hexahedra, pyramids, prisms 

* Generate volume meshes with single process or distributed process 

* Check mesh quality to provide the best solution for the problem and improve predictive capabilities 

* Perform mesh diagnostics for free, multi-connected edges, self-intersection and overlapping faces in the model 

* Modularize meshing algorithms, components, and services for easier reuse in other applications 

* Expose micro services and APIs for meshing operations to promote meshing workflow prototyping 

 
PyPrime integrates the meshing capabilities of the Ansys Prime directly into client applications. PyPrime package provides a Python-friendly interface to drive the software that manages the submission of low-level Prime commands, while exchanging data through high-performance gRPC interfaces. 

PyPrime  enables you to serve the meshing needs of the industry providing solutions to complex issues. PyPrime along with the general-purpose Python code effortlessly manages your meshing needs. PyPrime is now an open source. Enjoy it! Contributions are welcome. 

-----------
Background 
-----------

PyPrime is based on PRIME gRPC, which helps Prime to be a server and seamlessly connect with the client and respond to the queries. 

gRPC is a lightweight protocol from Google using universal RPC framework which helps it to run on any environment effortlessly. gRPC stands for grpc remote procedure call and is an open source. gRPC is built on universal RPC framework which is compatible with any environment and provides high performance. 

PyPrime uses Prime gRPC to establish connection with the client and helps to call the prime APIs on the remote Prime instance. Prime gRPC  converts python statements into Prime commands and is transferred to prime instance in the server and enables communication between the client and Prime server. 

---------------------
Features of PyPrime 
---------------------
PyPrime comprises of many robust APIs which do many jobs just on calling the API once and APIs that just do one job on calling them. These APIs also enable you to query the model and allow you to build complex models based on the underlying queries. PyPrime has some distinct features that make them unique. They are: 

* Easy to setup and execute 

* Support simple and complex models

* Supports CAD import 

* Exports meshes in solver format 

* Supports parallel processing like Distributed Parallel, Threaded Parallel, and multiple servers driven from python 

------------------
Quick Code
------------------
This section provides a brief idea on how PyPrime works: 

To launch PyPrime: 

>>> from ansys.meshing.prime import ( 
>>> launch_prime
>>> ) 
>>> with launch_prime(ip='127.0.0.1', port=50055) as prime: 
>>> model = prime.model 


To read a mesh file: 

>>> file_io = prime.FileIO(model)
>>> file_io.read_pmdat(r"E:\2box_inside_box.pmdat")
>>> print(model)


-----------------------------
Calling PyPrime Pythonically
-----------------------------
PyPrime APIs are called directly from Prime instance in a pythonic manner.  

(To be added by Sourabh)


