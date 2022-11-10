"""Version of ansys-meshing-prime library.

On the ``main`` branch, use 'dev0' to denote a development version.
For example:

version_info = 0, 1, 0, 'dev0'

Examples
--------
Print the version

>>> from ansys.meshing import prime
>>> print(prime.__version__)
0.2.0.dev17

"""

# major, minor, patch
version_info = 0, 2, 0, 'dev17'

# Nice string for the version
__version__ = '.'.join(map(str, version_info))
