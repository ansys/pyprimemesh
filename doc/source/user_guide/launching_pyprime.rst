.. _ref_index_launching_pyprime:

**********************
Launching PyPrimeMesh
**********************

==============================================
Launching Server from within A Python Script
==============================================

The :func:`launch_prime() <ansys.meshing.prime.launch_prime>` function launches the Ansys Prime Server.  
The function returns an instance of the PyPrimeMesh :class:`Client <ansys.meshing.prime.Client>` connected to the launched server session.  

.. code:: python

    import ansys.meshing.prime as prime
    prime_client = prime.launch_prime()

You can send commands to the Ansys Prime Server and receive responses from the server.

The :class:`Client <ansys.meshing.prime.Client>` is used to get the :attr:`model <ansys.meshing.prime.Client.model>` associated with the client instance.

.. code:: python
 
    model = prime_client.model

===========================================================================
Launching Server from A Windows or Linux Console and Connecting The Client
===========================================================================

Ansys Prime Server can be launched from a Linux or Windows using command prompt and then connected to the Client as needed.  

A Window's example to start the server in parallel mode on 4 nodes, specifying the IP address and port,
is shown below:

#. Launch a server from command line:

    .. code:: shell-session

      "%AWP_ROOT231%\meshing\Prime\runPrime.bat" server -np 4 --ip 127.0.0.1 --port 50055

#. Connect to the server in python using a PyPrimeMesh :class:`Client <ansys.meshing.prime.Client>` as follows:

    .. code:: python

      import ansys.meshing.prime as prime
      prime_client = prime.Client(ip="127.0.0.1", port=50055)
      model = prime_client.model

.. note::
    Only a single client session can be connected to an active Ansys Prime Server instance at any time.


=============================
Disconnecting from The Server
=============================

The :func:`Client.exit() <ansys.meshing.prime.Client.exit>` function ends the connection with the server.

If the :class:`Client <ansys.meshing.prime.Client>` launched the server, then this terminates the server process.

==============================================
Running a Python Script in Batch on The Server
==============================================

A python script can be run directly on the server from a Linux or Windows console.

Here is an example on Windows for running a python script directly from the command line.

.. code:: shell-session

    "%AWP_ROOT231%\meshing\Prime\runPrime.bat" my_script.py

