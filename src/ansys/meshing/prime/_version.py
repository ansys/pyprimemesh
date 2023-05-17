"""Version of ansys-meshing-prime library.

On the ``main`` branch, use 'devN' to denote a development version.
For example:

version_info = 0, 3, 0, 'dev0'

Examples
--------
Print the version

>>> from ansys.meshing import prime
>>> print(prime.__version__)
0.2.1

"""

# major, minor, patch
version_info = 0, 2, 1

# Nice string for the version
__version__ = '.'.join(map(str, version_info))
