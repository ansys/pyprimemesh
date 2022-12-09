.. _ref_index_launching_pyprime:

**********************
Launching PyPrimeMesh
**********************

==============================================
Launching Server from a Python Script
==============================================

The :func:`launch_prime() <ansys.meshing.prime.launch_prime>` function launches the Ansys Prime Server.  
The function returns an instance of the PyPrimeMesh :class:`Client <ansys.meshing.prime.Client>` that is connected to the launched server session.  

.. code:: python

    import ansys.meshing.prime as prime
    prime_client = prime.launch_prime()

This enables you to send commands to the Ansys Prime Server and receive responses from the server.

The :class:`Client <ansys.meshing.prime.Client>` gets the :attr:`model <ansys.meshing.prime.Client.model>` associated with the client instance.

.. code:: python
 
    model = prime_client.model

===========================================================================
Launching Server from a Windows or Linux Console and Connecting the Client
===========================================================================

Ansys Prime Server can be launched from a Linux or Windows console and then connected to the client, as needed.  

A Windows example for starting the server in parallel mode on four nodes, and specifying the IP address and port,
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
Disconnecting from the Server
=============================

The :func:`Client.exit() <ansys.meshing.prime.Client.exit>` function ends the connection with the server.

If the :class:`Client <ansys.meshing.prime.Client>` launched the server, then this also terminates the server process.

==============================================
Running a Python Script in Batch on the Server
==============================================

Python script can be run directly on the server from a Linux or Windows console.

Below example shows how to run a python script directly from the command line on Windows:

.. code:: shell-session

    "%AWP_ROOT231%\meshing\Prime\runPrime.bat" my_script.py

