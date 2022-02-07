.. _ref_index_getting_started:

===============
Getting Started
===============

Overview
--------
The PyPRIME project supports Pythonic access to Ansys' PRIME Meshing Engine.


Installation
------------
The ``ansys-meshing-prime`` package currently supports Python 3.6 through
Python 3.9 on Windows, MacOS and Linux.

Install PyPrime with:

.. code::

   pip install ansys-meshing-prime

Alternatively, clone and install in development mode with:

.. code::

   git clone https://github.com/pyansys/pyprime
   cd pyprime
   pip install -e .


Documentation
-------------
Include a link to the full sphinx documentation.  For example `PyAnsys <https://docs.pyansys.com/>`_


Usage
-----
It's best to provide a sample code or even a figure demonstrating the usage of your library.  For example:

.. code:: python

   >>> from ansys.meshing.prime import launch_prime
   >>> with launch_prime() as prime:
   >>>     model = client.model
   

Testing
-------
You can feel free to include this at the README level or in CONTRIBUTING.md


License
-------
``PyPRIME`` is licensed under the MIT license.

This module, ``ansys-meshing-prime`` makes no commercial claim over Ansys
whatsoever.  This tool extends the functionality of ``PRIME`` by
adding a Python interface to the PRIME service without changing the
core behavior or license of the original software.  The use of ``PyPRIME`` requires a legally licensed
local copy of Ansys.

To get a copy of Ansys, please visit `Ansys <https://www.ansys.com/>`_.