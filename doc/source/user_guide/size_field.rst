.. _ref_index_size_field:

***********
Size Fields
***********

Size field type helps you to fetch the element size at a given location. The size field types available in PyPrime are: 

- Geometric-Computes sizes based on the existing boundary sizes. Sizes can gradually increase from minimum size to maximum size based on the growth rate. 

- Volumetric- Computes the volumetric size field based on the size controls specified. 

- Geodesic- Computes geodesic sizes on face nodes based on the size controls specified. Defines the sizes along a surface rather than the volume. Geodesic sizing enables you to confine sizes to surfaces and avoid problems like dead space refinement. 

- Constant- Computes constant sizes based on the size controls specified. 

- Meshedgeodesic- Computes size fields using average mesh edge lengths and are diffused geodesical. 
