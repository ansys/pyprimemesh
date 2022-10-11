.. _ref_index_user_guide:

==========
User Guide
==========

.. toctree::
   :maxdepth: 1
   :hidden:

   launching_pyprime
   reading_writing
   meshing
   size_field
   controls
   features


-------------
Introduction
-------------

About this Guide
-----------------
The PyPrime user guide provides information on PyPrime APIs and its usability in various industries. It helps you to build your meshing requirements using PyPrime API.
 
 
Purpose
--------
PyPrime user guide provides guidance to the developers who use PyPrime APIs to build their meshing needs.


---------------------
PyPrime Classes
---------------------

PyPrime has APIs which display efficient meshing capabilities. The PyPrime APIs are classified according to their capabilities to several classes. Some of the available classes and their capabilities are as follows:

Model
------

Model is the nucleus of PyPrime. Model forms the base and contains all information about PyPrime. You can access any information in PyPrime only through Model. Model is comprised of Parts, Size fields, Size controls, Prism control, checkpoints and other functions. You can perform different actions like get, check, activate, update, create, delete, deactivate on the mesh entities through Model to get the respective output. For example, you can create a Part through model using the function Create Part. 

Part
-----

Part contains zonelets and topoentities.

Topoentities and zonelets are characterized by dimension of entities.
Zonelets are a group of interconnected elements in a mesh. There are three types of zonelets. They are:

    * FaceZonelet: A group of interconnected face elements.
    * EdgeZonelet: A group of interconnected edge elements.
    * CellZonelet: A group of interconnected cell elements.

Topoentities represent connectivity information.
Topoentities can be queried from higher order to lower order topoentities and vice versa.
Topoentities have geometric representation which may be defined by splines or facets.
The mesh generated on topoentities will be projected on geometry representation.

    * TopoFace: Topoentity representing surfaces.
    * TopoEdge: Topoentity representing curves.
    * TopoVolume: Topoentity representing volumes.
	
Note: Each Part is assigned with an id. Each Part id is unique. The value cannot be zero or negative.

Surfer 
------
Surfer helps to generate surface mesh on the topofaces or face zonelets. 
Surfer performs surface meshing based on the various meshing algorithms. For example, constant size or volumetric size surface meshing.