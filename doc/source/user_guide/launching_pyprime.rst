.. _ref_index_launching_pyprime:

Launching PyPrime
-----------------
PyPrime uses ``launch_prime`` to launch the Prime server from ansys.meshing.prime that returns an instance of the ``ansys.meshing.prime.Client``.
 This enables you to send commands to prime and receive the response from the server. ``prime_client.exit()`` disconnects the PyPrime client from the server. 