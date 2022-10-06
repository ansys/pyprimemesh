"""
.. _ref_how_to_set_number_of_threads_for_parallel_processing:

===============================================
Setup threads for parallel processing
===============================================

**Summary**: This example illustrates how to set number of threads for parallel processing.

"""

###############################################################################
# Import all necessary modules and launch an instance of Prime.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import ansys.meshing.prime as prime

# start prime and get the model
model = prime.launch_prime().model


###############################################################################
# set number of threads for parallel processing
settings = {
    "number_of_threads" : 12
}

model.set_num_threads(settings["number_of_threads"])

###############################################################################
# set number of threads for parallel processing
print(model.get_num_threads())

###############################################################################

