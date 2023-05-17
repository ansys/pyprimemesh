"""PyPrimeMesh provides a python client to Ansys Prime Server. Ansys Prime Server delivers core
Ansys meshing technology.
"""

DOCLINES = (__doc__ or '').split("\n")

import os
from io import open as io_open

from setuptools import find_namespace_packages, setup

# Use single source package versioning.  Follows:
# https://packaging.python.org/guides/single-sourcing-package-version/
#
# With this approach, we can include the version within the setup file
# while at the same time allowing the user to print the version from
# the module
HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md')) as f:
    long_description = f.read()

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
    version=__version__,
    description=DOCLINES[0],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ansys/pyprimemesh/',
    license='MIT',
    author='ANSYS, Inc.',  # this is required
    author_email="pyansys.support@ansys.com",
    maintainer='PyAnsys developers',  # you can change this
    maintainer_email='pyansys.maintainers@ansys.com',
    # Plan on supporting only the currently supported versions of Python
    python_requires='>=3.7, <4',
    install_requires=[
        'ansys-api-meshing-prime==0.1.1',
        'numpy>=1.14.0',
        "appdirs>=1.4.0",
    ],
    extras_require={'graphics': ['pyvista>=0.32.0'], 'all': ['pyvista>=0.32.0']},
    package_dir={'': 'src'},
    package_data={'': ['graphics/images/*.png']},
    # Less than critical but helpful
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
