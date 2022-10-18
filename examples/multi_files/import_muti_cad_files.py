import ansys.meshing.prime as prime
import ansys.meshing.prime.graphics as pyprime_graphics
import os

model = prime.launch_prime().model


def prep_list(directory, files):
    f_list = []
    for file in files:
        file_name = os.path.join(directory, file)
        if file.endswith('.stl'):
            f_list.append(file_name)
    return f_list


# with prime.launch_prime() as pm:
# model = pm.model


global_settings = {
    "input_directory": r"D:\2022\py-prime_test_cases\demo\multi_files",
    "files": os.listdir(r"D:\2022\py-prime_test_cases\demo\multi_files"),
}

file_list = prep_list(global_settings["input_directory"], global_settings["files"])
print(file_list)

for file in file_list:
    file_io = prime.FileIO(model)
    params = prime.ImportCadParams(model=model)
    params.append = True
    params.part_creation_type = prime.PartCreationType.PART
    result = prime.FileIO(model=model).import_cad(file_name=file, params=params)


d_cad = pyprime_graphics.Graphics(model=model)
d_cad()
