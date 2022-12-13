.. _ref_index_launching_pyprime:

**********************
Launching PyPrimeMesh
**********************

==============================================
Launching Server from within a Python Script
==============================================

Ansys Prime Server can be launched using the :func:`launch_prime() <ansys.meshing.prime.launch_prime>` function.  
The function returns an instance of the PyPrimeMesh :class:`Client <ansys.meshing.prime.Client>` that is connected to the launched server session.  

.. code:: python

    import ansys.meshing.prime as prime
    prime_client = prime.launch_prime()

This enables you to send commands to the Ansys Prime Server and receive responses from the server.

The :class:`Client <ansys.meshing.prime.Client>` can then be used to get the :attr:`model <ansys.meshing.prime.Client.model>` associated with the client instance.

.. code:: python
 
    model = prime_client.model

=======================================================================
Launching Server from a Windows/Linux console and Connecting the Client
=======================================================================

Ansys Prime Server can be launched from a Linux or Windows console and then connected to, as needed.  

A Windows example, starting the server in parallel mode on 4 nodes, and specifying the ip address and port,
is shown below, first launching a server from cmd line:

.. code:: shell-session

    "%AWP_ROOT231%\meshing\Prime\runPrime.bat" server -np 4 --ip 127.0.0.1 --port 50055

And then connecting to the server in python using a PyPrimeMesh :class:`Client <ansys.meshing.prime.Client>` as follows:

.. code:: python

    import ansys.meshing.prime as prime
    prime_client = prime.Client(ip="127.0.0.1", port=50055)
    model = prime_client.model

.. note::
    Only a single client session can be connected to an active Ansys Prime Server instance at any time.


=============================
Disconnecting from the Server
=============================

The :func:`Client.exit() <ansys.meshing.prime.Client.exit>` function closes the connection with the server.

If the :class:`Client <ansys.meshing.prime.Client>` launched the server, then this will also kill the server process.

==============================================
Running a python script in batch on the Server
==============================================

A python script can be ran directly on the server from a Linux or Windows console.

Here is an example on Windows for running a python script directly from the cmd line.

.. code:: shell-session

    "%AWP_ROOT231%\meshing\Prime\runPrime.bat" my_script.py

=========================================
Recommendations for Launching the Server
=========================================

While developing it can be convenient to use python context to launch the server so that if an exception occurs during runtime the server closes cleanly.  This prevents servers being spawned and left open blocking ports.  

An example of how context can be used to manage the server lifecycle to make developing easier, is shown below.

.. code:: python

    import ansys.meshing.prime as prime
    with prime.launch_prime() as prime_client:
       model = prime_client.model
       # Indented code to run...

It is not required to use the :func:`Client.exit() <ansys.meshing.prime.Client.exit()>` function to close the server in this instance.
