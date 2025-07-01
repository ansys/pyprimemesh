# PyPrimeMesh

[![pyansys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![PyPI - Version](https://img.shields.io/pypi/v/ansys-meshing-prime)](https://pypi.org/project/ansys-meshing-prime/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ansys-meshing-prime)](https://pypi.org/project/ansys-meshing-prime/)
[![GH-CI](https://github.com/ansys/pyprimemesh/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/ansys/pyprimemesh/actions/workflows/ci_cd.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ansys-meshing-prime)](https://pypi.org/project/ansys-meshing-prime/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ansys/pyprimemesh)

## Overview

PyPrimeMesh is a Python client to Ansys Prime Server, which
delivers core Ansys meshing technology.

## Documentation and issues

Documentation for the latest stable release of PyPrimeMesh is hosted at
[PyPrimeMesh documentation](https://prime.docs.pyansys.com/version/stable/).

In the upper right corner of the documentation's title bar, there is an option
for switching from viewing the documentation for the latest stable release
to viewing the documentation for the development version or previously
released versions.

You can also [view](https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.png) or
[download](https://cheatsheets.docs.pyansys.com/pyprimemesh_cheat_sheet.pdf) the
PyPrimeMesh cheat sheet. This one-page reference provides syntax rules and commands
for using PyPrimeMesh.

On the [PyPrimeMesh Issues](https://github.com/ansys/pyprimemesh/issues) page,
you can create issues to report bugs and request new features. On the
[PyPrimeMesh Discussions](https://github.com/ansys/pyprimemesh/discussions) page or the
[Discussions](https://discuss.ansys.com/) page on the Ansys Developer portal,
you can post questions, share ideas, and get community feedback. 

To reach the project support team, email [pyansys.core@ansys.com](mailtto:pyansys.core@ansys.com).

## Installation

The `ansys-meshing-prime` package supports Python 3.10 to Python 3.13 on the Windows and Linux
operating systems.


PyPrimeMesh can be installed with all dependencies directly from PyPi by running
this command:

```bash
pip install ansys-meshing-prime[all]
```

Alternatively, you can clone this repository and install the client using
these commands:

```bash
git clone https://github.com/ansys/pyprimemesh
cd pyprimemesh
pip install -e .[all]
```

The preceding commands install all functionality that is important to development.
To install a basic version of the client, use this command instead:

```bash
pip install -e .
```

## Dependencies

You must have Ansys 2023 R1 or later installed to have access to Ansys Prime Server. 
Optionally, CAD readers can be configured.

Ansys Prime Server requires one of the following licenses to run. 
The system checks out the first available license from the list in the following order:

1. CFD PrepPost

2. CFD PrepPost Pro

3. Mechanical Enterprise PrepPost

4. Mechanical Enterprise

5. Mechanical Pro

6. Mechanical Premium

7. Ansys LS-DYNA

## Get started

### Launch PyPrimeMesh

To launch PyPrimeMesh, use this code:

```python
import ansys.meshing.prime as prime

with prime.launch_prime() as prime_client:
    model = prime_client.model
```

## Run tests

Run tests locally with this command:
```bash
    pytest
```

## License and aknowledgments

PyPrimeMesh is licensed under the MIT license.

PyPrimeMesh makes no commercial claim over Ansys whatsoever. This library extends the functionality of
Ansys Prime Server by adding a Python interface without changing the core behavior or license
of the original software. The use of Ansys Prime Server requires a legally licensed copy of Ansys
2023 R1 or later.
