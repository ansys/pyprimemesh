# Contribute

Overall guidance on contributing to a PyAnsys library appears in the
[Contributing] topic in the *PyAnsys developer's guide*. Ensure that you
are thoroughly familiar with this guide before attempting to contribute to
PyPrimeMesh.

The following contribution information is specific to PyPrimeMesh.

[Contributing]: https://dev.docs.pyansys.com/how-to/contributing.html

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