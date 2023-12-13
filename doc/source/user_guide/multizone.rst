.. _ref_index_multizone:

**********
MultiZone 
**********

MultiZone Method provides automatic decomposition of geometry into mapped (sweepable) regions and free regions. 
Mapped (sweepable) regions are filled with hexahedral elements and free regions are filled with non-hexahedral elements.
When you perform MultiZone Method meshing, all regions are meshed with a pure hexahedral mesh if possible.  

AutoMesh class enables you to automatically create the hex mesh on the scoped bodies using multizone meshing algorithms. 
AutoMesh.mesh() method allows you to perform MultiZone meshing with given MultiZone control. 

The below example shows how MultiZone Method can be applied on a body: 

1. Read the model.

.. code-block:: python

   file_io=prime.FileIO(model)
   res=file_io.read_pmdat(r"E:\Test\2Boxes_2Holes.pmdat",prime.FileReadParams(model=model))
   print(model)

2. Initialize the MultiZone control. MultiZone control sets the parameters and controls used for MultiZone meshing.  

.. code-block:: python

   multizone_control = model.control_data.create_multi_zone_control() 
