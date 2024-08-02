from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.connectutils import TolerantConnect

def tolerant_connect(model : prime.Model, tc_params : dict, cached_data: CachedData):
    tc = TolerantConnect(model)
    tc.fuse(
        connect_tolerance= tc_params["connect_tolerance"],
        side_tolerance= tc_params["side_tolerance"],
        connect_parts_with_diff_tol= tc_params["connect_parts_with_different_tolerance"],
        interfering_parts_exp= "",
        interfering_parts_priority= [],
        contact_parts_exp= "*",
        part_name= tc_params["part_name"],
        use_absolute_connect_tolerance= True,
        use_mesh_match= True,
        mesh_match_angle= 45,
        refine_at_contacts= tc_params["refine_at_contacts"],
        write_intermediate_files= False,
        delete_topology = tc_params["delete_topology"],
    )