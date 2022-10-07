.. _ref_index_contributing:

=============
Contributing
=============

Overall guidance on contributing to a PyAnsys library appears in the
`Contributing <https://dev.docs.pyansys.com/overview/contributing.html>`_ topic
in the *PyAnsys Developer's Guide*. Ensure that you are thoroughly familiar
with it and all `Guidelines and Best Practices
<https://dev.docs.pyansys.com/guidelines/index.html>`_ before attempting to
contribute to PyPrime.
 
The following contribution information is specific to PyPrime.

------------------------------
Cloning the Source Repository
------------------------------
You can clone the source repository from PyPrime GitHub and install the latest version in development mode by running:

>>> git clone https://github.com/pyansys/pyprime
>>> cd pyprime
>>> pip install -e .

---------------
Posting Issues
---------------
Use the `PyPrime Issues <https://github.com/pyansys/pyprime/issues>`_
page to submit questions, report bugs, and request new features.

To reach the project support team, email `pyansys.support@ansys.com <pyansys.support@ansys.com>`_.

------------------------------
Viewing PyPrime Documentation
------------------------------
Documentation for the latest stable release of PyPrime is hosted at
`PyPrime Documentation <https://prime.docs.pyansys.com>`_.

-----------------------------------------
Code Structure and Contributing New Code
-----------------------------------------
Much of the PyPrime code base is auto-generated based on the Prime server.  For the auto-generated 
code, contributions are therefore limited to raising issues and enhancement requests.  

You should not modify files marked as auto-generated.

Contributions from pull requests can be included elsewhere.  Specific areas that should be considered
for contributions are:

`PyPrime Examples <https://github.com/pyansys/pyprime/tree/main/examples>`_

`Graphics Functionality <https://github.com/pyansys/pyprime/tree/main/src/ansys/meshing/prime/graphics>`_

`High Level APIs <https://github.com/pyansys/pyprime/blob/main/src/ansys/meshing/prime/core/lucid.py>`_

If you have an idea on how to enhance PyPrime, consider first creating an issue as a feature request 
which we can use as a discussion thread to work on for implementing the contribution.

-----------
Code Style
-----------
PyPrime follows PEP8 standard as outlined in the `PyAnsys Development Guide
<https://dev.docs.pyansys.com>`_ and implements style checking using
`pre-commit <https://pre-commit.com/>`_.

To ensure your code meets minimum code styling standards, run::

  pip install pre-commit
  pre-commit run --all-files

You can also install this as a pre-commit hook by running::

  pre-commit install

This way, it's not possible for you to push code that fails the style checks. For example::

  $ pre-commit install
  $ git commit -am "added my cool feature"
  black....................................................................Passed
  flake8...................................................................Passed

----------
Licensing
----------
All contributed code will be licensed under The MIT License found in the repository.
If you did not write the code yourself, it is your responsibility to ensure that the existing license is compatible 
and included in the contributed files or you can obtain permission from the original author to relicense the code.

