"""PyPrimeMesh provides pythonic access to Prime server present in the Ansys Workbench install.

PyPrimeMesh is an integral part of PyAnsys effort to facilitate the use of Ansys technologies directly
from Python. PyPrimeMesh consists of various python modules that help you to acquire geometry and
generate surface and volume meshes for multiple solvers. PyPrimeMesh uses ansys.meshing.fm as primary
module to acquire geometry data. For generating mesh, the primary module is ansys.meshing.prime.

PyPrimeMesh enables you to:

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
"""

DOCLINES = (__doc__ or '').split("\n")

import os
from io import open as io_open

from setuptools import setup, find_namespace_packages

# Use single source package versioning.  Follows:
# https://packaging.python.org/guides/single-sourcing-package-version/
#
# With this approach, we can include the version within the setup file
# while at the same time allowing the user to print the version from
# the module
HERE = os.path.abspath(os.path.dirname(__file__))
__version__ = None
version_file = os.path.join(HERE, 'src', 'ansys', 'meshing', 'prime', '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())


packages = []
for package in find_namespace_packages('src', include="ansys*"):
    if package.startswith("ansys.meshing.prime"):
        packages.append(package)


setup(
    name='ansys-meshing-prime',
    packages=packages,
    package_dir={'': 'src'},
    version=__version__,
    description=DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    long_description_content_type='text/x-rst',
    url='https://github.com/pyansys/pyprime/',
    license='MIT',
    author='ANSYS, Inc.',  # this is required
    maintainer='PyAnsys developers',  # you can change this
    maintainer_email='pyansys.support@ansys.com',
    install_requires=[
        'ansys-api-meshing-prime==0.1.1',
        'numpy>=1.14.0',
        "appdirs>=1.4.0",
    ],
    extras_require={'graphics': ['pyvista>=0.32.0']},
    # Plan on supporting only the currently supported versions of Python
    python_requires='>=3.7, <3.10',
    # Less than critical but helpful
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
