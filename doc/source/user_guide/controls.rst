.. _ref_index_controls:

********************
Controls in PyPrime
********************

PyPrime provides various controls to help you refine your mesh to obtain the desired accuracy while meshing.

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


----------------
Wrapper Control
----------------

PyPrime provides :class:`WrapperControl <ansys.meshing.prime.WrapperControl>` class to extract a closed watertight surface used to create a volume mesh from geometry where the inputs:

* are not connected with overlaps

* have holes, leaks or gaps

* have small features that need to be ignored or stepped over

:class:`Wrapper <ansys.meshing.prime.Wrapper>` class is used for extracting flow regions from large assemblies, forming closed clean volumes from medical imaging and many more.


-------------
Prism Control
-------------

:class:`PrismControl <ansys.meshing.prime.PrismControl>` class helps you to control the prism mesh generation based on the face scope, volume scope and growth rate.
Prism cells creates either quadrilateral or triangular boundary faces, or both. They can resolve a boundary layer region of a tetrahedral mesh.


-----------------
Volume Control
-----------------

:class:`VolumeControl <ansys.meshing.prime.VolumeControl>` class helps you to control volume mesh zonelet (fluids, solid, dead) and elements (tetrahedrons, polyhedrons and so on).
It allows you to define the scope and generate the various types of volume mesh.

