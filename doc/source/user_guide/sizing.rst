.. _ref_index_sizing:

******
Sizing
******

PyPrime provides various sizing controls to help you refine your mesh to obtain the desired accuracy while meshing.


---------------
Sizing Control
---------------

When you mesh a model, you expect the mesh size to satisfy specific requirements at various locations in the mesh to provide accurate results.
You must use optimal sizes while meshing to achieve maximum simulation accuracy at minimum computational cost.
PyPrime specifies the sizing requirements using sizing controls. The sizing controls in PyPrime have the following:

* Scope

* Maximum rate of change of size

* Range within which the sizes should be, on or within the scope


The :class:`SizingType <ansys.meshing.prime.SizingType>` class offers various sizing control types to define sizing requirements:

 * Curvature

 * Proximity

 * Hard

 * Soft

 * Meshed

 * Body of Influence


Curvature Sizing
^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`CURVATURE <ansys.meshing.prime.SizingType.CURVATURE>`, sizes on the scope are based on the local curvature, with the size being small when the local curvature is large and vice versa. The :class:`CurvatureSizingParams <ansys.meshing.prime.CurvatureSizingParams>` is used to specify following parameters: min/max size, growth rate and normal angle.

Proximity Sizing
^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`PROXIMITY <ansys.meshing.prime.SizingType.PROXIMITY>`, sizes are based on the closeness of surfaces or edges specified in the scope. The :class:`ProximitySizingParams <ansys.meshing.prime.ProximitySizingParams>` is used to specify following parameters: min/max size, growth rate and the number of element per gap.

Hard Sizing
^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`HARD <ansys.meshing.prime.SizingType.HARD>`, sizes on the scope are based on a uniform value while meshing. The :class:`HardSizingParams <ansys.meshing.prime.HardSizingParams>` is used to specify following parameters: minimum size and growth rate.

Soft Sizing
^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`SOFT <ansys.meshing.prime.SizingType.SOFT>`, sizes on the scope are based on a certain maximum value which should not exceed while meshing. The :class:`SoftSizingParams <ansys.meshing.prime.SoftSizingParams>` is used to specify following parameters: maximum size and growth rate.

Meshed Sizing
^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`MESHED <ansys.meshing.prime.SizingType.MESHED>`, sizes are based on existing local sizes. The :class:`MeshedSizingParams <ansys.meshing.prime.MeshedSizingParams>` class is used to specify growth rate.

Body of Influence Sizing
^^^^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizingType <ansys.meshing.prime.SizingType>` attribute as :attr:`BOI <ansys.meshing.prime.SizingType.BOI>`, sizes inside a closed volume scope should not cross a certain maximum value. The :class:`BoiSizingParams <ansys.meshing.prime.BoiSizingParams>` is used to specify following parameters: maximum size and growth rate.


-----------
Size Fields
-----------

The :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` class helps you to fetch the element size at a given location. The size field types available in PyPrime are: 

- Geometric-Computes sizes based on the existing boundary sizes. Sizes can gradually increase from minimum size to maximum size based on the growth rate. 

- Volumetric- Computes the volumetric size field based on the size controls specified. 

- Geodesic- Computes geodesic sizes on face nodes based on the size controls specified. Defines the sizes along a surface rather than the volume. Geodesic sizing enables you to confine sizes to surfaces and avoid problems like dead space refinement. 

- Constant- Computes constant sizes based on the size controls specified. 

- Meshedgeodesic- Computes size fields using average mesh edge lengths and are diffused geodesical. 


Geometric size field
^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`GEOMETRIC <ansys.meshing.prime.SizeFieldType.GEOMETRIC>`, size field is computed based on the existing boundary sizes. Sizes can gradually increase from minimum size to maximum size based on the growth rate.

Volumetric size field
^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`VOLUMETRIC <ansys.meshing.prime.SizeFieldType.VOLUMETRIC>`, size field is computed based on the size controls specified.

Geodesic size field
^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`GEODESIC <ansys.meshing.prime.SizeFieldType.GEODESIC>`, size field is computed on face nodes based on the size controls specified. Sizes are defined along a surface rather than the volume. Geodesic sizing enables you to confine sizes to surfaces and avoid problems like dead space refinement.

Constant size field
^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`CONSTANT <ansys.meshing.prime.SizeFieldType.CONSTANT>`, size field is computed based on the size controls specified.

Meshedgeodesic size field
^^^^^^^^^^^^^^^^^^^^^^^^^

When you select the :class:`SizeFieldType <ansys.meshing.prime.SizeFieldType>` attribute as :attr:`MESHEDGEODESIC <ansys.meshing.prime.SizeFieldType.MESHEDGEODESIC>`, size field is computed using average mesh edge lengths and is diffused geodesical.
