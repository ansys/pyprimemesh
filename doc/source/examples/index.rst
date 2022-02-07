.. _ref_index_examples:

========
Examples
========

Pyprime provides some examples to guide with your mesh requirements using ansys-meshing-prime. 

Reading a Mesh File
--------------------

The following example helps you to read a mesh file:


>>> from ansys.meshing.prime import (launch_prime)
>>> with launch_prime(ip='127.0.0.1', port=50055) as prime:
>>> model = prime.model
>>> file_io = prime.FileIO(model)
>>> file_io.read_pmdat(r"E:\2box_inside_box.pmdat")
>>> print(model)

