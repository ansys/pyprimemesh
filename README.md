# PyPrimeMesh

[![pyansys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![GH-CI](https://github.com/pyansys/pyprimemesh/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/pyansys/pyprimemesh/actions/workflows/ci_cd.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)

## Overview

PyPrimeMesh provides a Python client to the Ansys Prime server. The Ansys Prime server
delivers core Ansys meshing technology.

## Documentation and Issues

For information on PyPrimeMesh, refer to the latest [documentation](
https://prime.docs.pyansys.com).

For queries related to PyPrimeMesh, post on the [PyPrimeMesh Discussions](
https://github.com/pyansys/pyprimemesh/discussions) page. 

For bugs or enhancement requests, file an issue on the [PyPrimeMesh Issues](
https://github.com/pyansys/pyprimemesh/issues) page. 

For assistance, reach out to the support team at
[pyansys.core@ansys.com](mailto:pyansys.core@ansys.com).

## Installation

The ``ansys-meshing-prime`` package supports Python 3.7 to Python 3.11 on
the Windows and Linux operating systems.

PyPrimeMesh can be installed with all dependencies directly from PyPi by running
this command:

```bash
pip install ansys-meshing-prime[all]
```

Alternatively, you can clone this repository and install the client using
these commands:

```bash
git clone https://github.com/pyansys/pyprimemesh
cd pyprimemesh
pip install -e .[all]
```

The preceding commands install all functionality that is important to development.
To install a basic version of the client, use this command instead:

```bash
pip install -e .
```

## Dependencies

You must have Ansys 2023 R1 or later installed for the Ansys Prime server.
(Optionally, CAD readers can be configured.) The Ansys Prime server requires
a PrepPost or a Mechanical or Fluids PrepPost (CFD) license to run.

## Get Started

### Launching PyPrimeMesh

To launch PyPrimeMesh, use this code:

```python
import ansys.meshing.prime as prime

with prime.launch_prime() as prime_client:
    model = prime_client.model
```

## License and Acknowledgments

PyPrimeMesh is licensed under the MIT license.

PyPrimeMesh makes no commercial claim over Ansys whatsoever. This library extends the functionality of
the Ansys Prime server by adding a Python interface without changing the core behavior or license
of the original software. The use of the Ansys Prime server requires a legally licensed copy of Ansys
Workbench.
