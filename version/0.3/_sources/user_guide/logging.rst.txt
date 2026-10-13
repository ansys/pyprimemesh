.. _ref_index_logging:

*******
Logging
*******

A logger can be attached to a session to handle streamed output from PyPrimeMesh.  

This code attaches a logger and formats the output as needed:

.. code:: python

   import ansys.meshing.prime as prime
   import logging

   prime_client = prime.launch_prime()
   model = prime_client.model

   # Attach logger to PyPrimeMesh model and set logging level
   model.python_logger.setLevel(logging.DEBUG)
   ch = logging.StreamHandler()
   ch.setLevel(logging.DEBUG)

   # Create formatter for message output
   formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

   # Add formatter to ch stream handler
   ch.setFormatter(formatter)
   model.python_logger.addHandler(ch)
