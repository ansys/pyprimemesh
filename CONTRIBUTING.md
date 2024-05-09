# Contributing

Repositories should have a contributing section, but we don't need to have all the contributing information here.  Have them reference the developer guide.

We absolutely welcome any code contributions and we hope that this
guide will facilitate an understanding of the PyPrimeMesh code
repository. It is important to note that while the PyPrimeMesh software
package is maintained by ANSYS and any submissions will be reviewed
thoroughly before merging, we still seek to foster a community that can
support user questions and develop new features to make this software
a useful tool for all users.  As such, we welcome and encourage any
questions or submissions to this repository.

Please reference the [PyAnsys Developer's
Guide](https://dev.docs.pyansys.com/) for the full documentation
regarding contributing to the PyPrimeMesh project.

## Running the tests locally

To run the tests, you can simply run the following command in your local:

```bash
    pytest
```

Note that you need to have access to PyPrimeMesh product to run the tests.
Some of the graphical related tests need a previously generated image cache, so
you might get errors due to this.

## Building the documentation

To build the documentation of the project, you must run the following command.

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