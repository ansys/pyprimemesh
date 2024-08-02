from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData

def set_cwd(model: prime.Model, cwd_params: dict, cached_data: CachedData):
    path = cwd_params["path"]
    model.set_working_directory(path)
