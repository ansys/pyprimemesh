# PyPrimeMesh

[![pyansys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![GH-CI](https://github.com/pyansys/pyprime/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/pyansys/pyprime/actions/workflows/ci_cd.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)

## Overview

PyPrime provides a python client to Ansys Prime Server. Ansys Prime Server delivers core Ansys meshing technology.

## Documentation and Issues

For information on PyPrime see the latest [documentation](
https://dev.prime.docs.pyansys.com)

If you have questions about PyPrime please post them to the [Discussion](
https://github.com/pyansys/pyprime/discussions) page. If you have problems using PyPrime or want to
request new features, please file an issue on our [Issues](
https://github.com/pyansys/pyprime/issues) page. For assistance, reach out to the PyAnsys
Support team at [pyansys.support@ansys.com](mailto:pyansys.support@ansys.com).

## Installation

The `ansys-meshing-prime` package supports Python 3.7 to Python 3.9 on Windows and Linux
operating system.

PyPrime can be installed directly from PyPi as follows:

```bash
pip install ansys-meshing-prime
```

> **NOTE:** PyPrime is not available on PyPi at present.

Alternatively, clone and install in development mode with:

```bash
git clone https://github.com/pyansys/pyprime
cd pyprime
pip install -e .[graphics] --find-links deps
```

## Dependencies

You must have a licensed copy of the latest version of Ansys 2023 R1 locally.

## Get Started

### Launching PyPrime

To launch PyPrime:

```python
import ansys.meshing.prime as prime
with prime.launch_prime() as prime_client:
   model = prime_client.model
```

## License and Acknowledgments

PyPrime is licensed under the MIT license.

PyPrime makes no commercial claim over Ansys whatsoever. This library extends the functionality of
Ansys Prime Server by adding a Python interface without changing the core behavior or license
of the original software. The use of Ansys Prime Server requires a legally licensed copy of Ansys
Workbench.
