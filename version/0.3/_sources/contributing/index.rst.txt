.. _ref_index_contributing:

============
Contributing
============

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/version/0.3/how-to/contributing.html>`_ topic
in the *PyAnsys Developer's Guide*.
 
The following contribution information is specific to PyPrimeMesh.

--------------------
Clone the repository
--------------------
You can clone the PyPrimeMesh repository from GitHub and install the latest version in
development mode with this code:

>>> git clone https://github.com/ansys/pyprimemesh
>>> cd pyprimemesh
>>> pip install -e .[graphics]

-----------
Post issues
-----------
Use the `PyPrimeMesh Issues <https://github.com/ansys/pyprimemesh/issues>`_
page to submit questions, report bugs, and request new features.

To reach the support team, email `pyansys.support@ansys.com <pyansys.support@ansys.com>`_.

------------------------------
View PyPrimeMesh documentation
------------------------------
Documentation for the latest stable release of PyPrimeMesh is hosted at
`PyPrimeMesh Documentation <https://prime.docs.pyansys.com>`_.

--------------------------------
Code structure and contributions
--------------------------------
The PyPrimeMesh code base is primarily auto-generated based on the Ansys Prime server. For the auto-generated 
code, contributions are limited to raising issues and enhancement requests.  

You should not modify files marked as auto-generated.

Contributions from pull requests can be included elsewhere. Specific areas that should be considered
for contributions are:

- `PyPrimeMesh examples <https://github.com/ansys/pyprimemesh/tree/release/0.3/examples>`_

- `Graphics Functionality <https://github.com/ansys/pyprimemesh/tree/release/0.3/src/ansys/meshing/prime/graphics>`_

- `High-level APIs <https://github.com/ansys/pyprimemesh/blob/release/0.3/src/ansys/meshing/prime/lucid>`_


If you have an idea on how to enhance PyPrimeMesh, consider first creating an issue as a feature request 
The PyPrimeMesh team can then use the request as a discussion thread to work on implementing the contribution.

----------
Code style
----------
PyPrimeMesh follows PEP8 standard as outlined in the `PyAnsys Development Guide
<https://dev.docs.pyansys.com>`_ and implements style checking using
`pre-commit <https://pre-commit.com/>`_.

To ensure your code meets minimum code styling standards, run this code::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a pre-commit hook by running this code::

  pre-commit install

This way, it's not possible for you to push code that fails the style checks. For example::

  $ pre-commit install
  $ git commit -am "added my cool feature"
  black....................................................................Passed
  flake8...................................................................Passed

---------
Licensing
---------
All contributed code is licensed under the MIT License found in the repository.
If you did not write the code yourself, it is your responsibility to ensure that the existing license is compatible 
and included in the contributed files or you obtain permission from the original author to relicense the code.

