from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.communicator import call_method

def _get_part_ids(model: prime.Model, part_scope):
    args = {"part_name_pattern": part_scope, "name_pattern_params": {}}
    command_name = "PrimeMesh::Model/GetPartIdsOfNamePattern"
    part_ids = call_method(model, command_name, model._object_id, args=args)
    return part_ids

def _get_topo_faces(model: prime.Model):
    topo_data = model.topo_data
    return call_method(model, "PrimeMesh::TopoData/GetTopoFaces",
                                 topo_data._object_id, {})

def _get_topo_nodes(model: prime.Model):
    topo_data = model.topo_data
    return call_method(model, "PrimeMesh::TopoData/GetTopoNodes",
                                 topo_data._object_id, {})

def _get_interior_topoedges_of_topoface(model: prime.Model, topo_face: int):
    topo_data = model.topo_data
    args = {"topo_face": topo_face}
    command_name = "PrimeMesh::TopoData/GetInteriorTopoEdgesOfTopoFace"
    return call_method(model, command_name, topo_data._object_id, args)

def _check_size_control_scope(model: prime.Model, part_id: int, entity_type: str,
                              entity_scope: str, scope_evaluation_type: str):
    if(entity_scope == "*"):
        return True
    part = model.get_part(part_id)
    name_pattern_params = prime.NamePatternParams(model)
    face_zonelets = []
    edge_zonelets = []
    if entity_type == "face" or entity_type == "face_and_edge":
        if scope_evaluation_type == "labels":
            face_zonelets = part.get_face_zonelets_of_label_name_pattern(entity_scope,
                                                                            name_pattern_params)
        elif scope_evaluation_type == "zones":
            face_zonelets = part.get_face_zonelets_of_zone_name_pattern(entity_scope,
                                                                        name_pattern_params)
    if entity_type == "edge" or entity_type == "face_and_edge":
        if scope_evaluation_type == "labels":
            edge_zonelets = part.get_edge_zonelets_of_label_name_pattern(entity_scope,
                                                                             name_pattern_params)
    if len(face_zonelets) > 0 or len(edge_zonelets) > 0:
        return True

    return False
