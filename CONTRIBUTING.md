# Contributing

Repositories should have a contributing section, but we don't need to have all the contributing information here.  You should reference the [Contributing](https://dev.docs.pyansys.com/how-to/contributing.html) topic in the *PyAnsys developer's guide*.

We welcome any code contributions and hope that this
guide facilitates an understanding of the PyPrimeMesh code. It is important to
note that while the PyPrimeMesh package is maintained by Ansys and submissions are reviewed
thoroughly before merging, we still seek to foster a community that can
support user questions and develop new features to make this software
a useful tool for all users.  As such, we welcome and encourage any
questions or submissions to this repository.

Please reference the [PyAnsys Developer's
Guide](https://dev.docs.pyansys.com/) for the full documentation
regarding contributing to the PyPrimeMesh project.

## Run tests locally

To run tests locally, run the following command:

```bash
    pytest
```

Note that you must have access to PyPrimeMesh to run the tests.
Some of the graphical-related tests must have a previously generated image cache, so
you might get errors due to this.

## Build documentation

To build PyPrimeMesh documentation, run this command.

In Windows:
```bash
    ./doc/make.bat html
    ./doc/make.bat pdf
```

In Linux:
```bash
    make html
    make pdf
```