.. _ref_index_logging:

*******
Logging
*******

A logger can be attached to a session in order to handle streamed output from PyPrimeMesh.  

An example is shown below where the output is formatted as needed:

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
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

   # Add formatter to ch stream handler
   ch.setFormatter(formatter)
   model.python_logger.addHandler(ch)
