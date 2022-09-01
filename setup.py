"""Template setup file."""
import codecs
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


# Get the long description from the README file
# This is needed for the description on PyPI
def read(rel_path):
    with codecs.open(os.path.join(HERE, rel_path), 'r') as fp:
        return fp.read()


with open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


packages = []
for package in find_namespace_packages('src', include="ansys*"):
    if package.startswith("ansys.meshing.prime"):
        packages.append(package)


setup(
    name='ansys-meshing-prime',
    packages=packages,
    package_dir={'': 'src'},
    version=__version__,
    description='Prime Meshing Library',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/pyansys/pyprime/',
    license='MIT',
    author='ANSYS, Inc.',  # this is required
    maintainer='PyAnsys developers',  # you can change this
    maintainer_email='pyansys.support@ansys.com',
    install_requires=[
        'ansys-api-meshing-prime==0.1.1',
        'numpy>=1.14.0',
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
