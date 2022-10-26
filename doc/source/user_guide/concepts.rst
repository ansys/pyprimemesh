.. _ref_index_concepts:

*****************************
Concepts and Model Structure
*****************************

------
Model 
------

The :class:`Model <ansys.meshing.prime.Model>` class is the top-level container for PyPrime. It contains all information about the PyPrime session.  

.. figure:: ../images/model_structure.png
    :width: 200pt
    :align: center

    **Model structure**
    
The :class:`Model <ansys.meshing.prime.Model>` is accessed from the :class:`Client <ansys.meshing.prime.Client>` class as follows:
  
.. code:: python

    >>> import ansys.meshing.prime as prime
    >>> prime_client = prime.launch_prime()
    >>> model = prime_client.model

:class:`Model <ansys.meshing.prime.Model>` can be printed to give a summary of the current session.
  
.. code:: python

    >>> print(model)

------
Parts 
------

Geometry topology and mesh data in the :class:`Model <ansys.meshing.prime.Model>` is stored within any number of :attr:`parts <ansys.meshing.prime.Model.parts>`.

.. code:: python

    >>> model.parts

Each :class:`Part <ansys.meshing.prime.Part>` can contain either TopoEntities (TopoPart created from CAD geometry import) 
or Zonelets (MeshPart created from faceted geometry and mesh import).

.. figure:: ../images/part_type.png
    :width: 400pt
    :align: center

    **Part types**
  
TopoEntities and Zonelets are characterized by dimension of entities.
  
TopoEntities
------------

TopoEntities are created from importing CAD and represent connectivity information.  TopoEntities have geometric representation 
which may be defined by splines or facets.  The mesh generated on TopoEntities will be projected on geometry representation.  

There are four types of TopoEntities:
  
    * TopoNode: TopoEntity representing points.
    * TopoEdge: TopoEntity representing curves.
    * TopoFace: TopoEntity representing surfaces.
    * TopoVolume: TopoEntity representing volumes.

.. figure:: ../images/topo.png
    :width: 400pt
    :align: center

    **TopoEntities schematic**
  
Zonelets
--------

Zonelets are created from importing mesh files and are groups of interconnected elements in a mesh. 

There are three types of Zonelets:

    * FaceZonelet: A group of interconnected face elements.
    * EdgeZonelet: A group of interconnected edge elements.
    * CellZonelet: A group of interconnected cell elements.
  
A set of FaceZonelets that define a closed volume without containing any cell elements is defined as a Volume.

.. figure:: ../images/zonelets.png
    :width: 400pt
    :align: center

    **Zonelets schematic**

-----
Zones
-----

Zonelets or TopoEntities can be further grouped into zones.  A Zonelet or TopoEntity can only be present in a single zone.  

In order to export a mesh to the Fluent solver (.msh, .cas) zones are required to define boundary conditions.  

When importing a Fluent solver model each zone will be defined as a single zonelet.

------
Labels
------

Labels allow overlapping groups of Zonelets or TopoEntities.  

When importing CAD files each group or named selection will generate a label.  

When exporting to a mechanical solver file (.cdb) each label is exported as a collection.
