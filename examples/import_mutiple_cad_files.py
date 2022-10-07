"""
.. _ref_how_to_read_multiple_cad_files_in_pyprime:

===============================================
Reading multiple cad files in prime
===============================================

**Summary**: This example illustrates how to read multiple cad files in prime.


Objective
~~~~~~~~~
In this example, we will try reading multiple cad file with specific exensions into prime.

"""

###############################################################################
# Import all necessary modules and launch an instance of Prime.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import ansys.meshing.prime as prime
import ansys.meshing.prime.graphics as pyprime_graphics
import os

# start prime and get the model
prime_client = prime.launch_prime()
model = prime_client.model


###############################################################################
# Provide file extension and file directory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

input_settings = {'extension': '.stl', 'file_path': r"D:\2022\py-prime_test_cases\demo\multi_files"}

###############################################################################
# Define function for file preparations
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def prep_list(directory, files):
    f_list = []
    for file in files:
        file_name = os.path.join(directory, file)
        if file.endswith(input_settings["extension"]):
            f_list.append(file_name)
    return f_list


settings = {
    "input_directory": input_settings["file_path"],
    "files": os.listdir(input_settings["file_path"]),
}


#######################################################################################
# Create list of files that user planning to import and loop it through import function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file_list = prep_list(settings["input_directory"], settings["files"])

for file in file_list:
    file_io = prime.FileIO(model)
    params = prime.ImportCadParams(model=model)
    params.append = True
    params.part_creation_type = prime.PartCreationType.PART
    result = prime.FileIO(model=model).import_cad(file_name=file, params=params)

#######################################################################################
# Display cad using pyvista
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

d_cad = pyprime_graphics.Graphics(model=model)
d_cad()


###############################################################################
# Exit the Prime session.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

prime_client.exit()
