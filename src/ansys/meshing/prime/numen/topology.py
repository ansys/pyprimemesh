from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils import volume_utils
import ansys.meshing.prime.numen.utils.communicator as Comm
import ansys.meshing.prime.numen.utils.macros as macros

def topology_cleanup(model: prime.Model, topology_cleanup_params: dict, cached_data: CachedData):
    part_scope = topology_cleanup_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)

    for part_id in part_ids:
        vt_composer = Comm.PrimeObj(model, "VTComposer", part_id)
        topo_faces = macros._get_topo_faces(model)
        topo_edges = []

        for topo_face in topo_faces:
            topo_edge = macros._get_interior_topoedges_of_topoface(model, topo_face)
            topo_edges.extend(topo_edge)

        part = model.get_part(part_id)
        part_name = str(part.get_name())
        vt_params = Comm.vt_composer_params.copy()
        if "boi" not in part_name.lower():
            vt_params["deleteMeshAfterMerge"] = False
            suppress_edge_args = {"topo_edge_ids": topo_edges, "params": vt_params}
            try:
                vt_composer.call_method("SuppressTopoEdges", suppress_edge_args)
            except Exception as e:
                pass

        topo_nodes = macros._get_topo_nodes(model)
        vt_params["mergeFaceNormalsAngleDeg"] = 180.0
        vt_params["mergeEdgeAllowSelfClose"] = True
        suppress_node_args = {
            "topo_node_ids": topo_nodes,
            "params": vt_params
        }
        try:
            vt_composer.call_method("SuppressTopoNodes", suppress_node_args)
        except Exception as e:
            pass

        scaffolder = Comm.PrimeObj(model, "Scaffolder", part_id)
        if "boi" not in part_name.lower():
            scafolding_params = {}
            faces = macros._get_topo_faces(model)
            scafolding_params["constantMeshSize"] = 0.02
            scafolding_params['absoluteDistTol'] = 0.02
            repair_edge_args = {
                "topo_faces": faces,
                "params": scafolding_params
            }
            scaffold_result = scaffolder.call_method("RepairTopoEdgesOfTopoFaces", repair_edge_args)
        scaffolder.destruct()

def suppress_interior_topoedges(model: prime.Model, suppress_topoedges_params: dict,
                       cached_data: CachedData):
    part_scope = suppress_topoedges_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        vt_composer = Comm.PrimeObj(model, "VTComposer", part_id)
        topo_faces = macros._get_topo_faces(model)
        topo_edges = []
        for topo_face in topo_faces:
            topo_edge = macros._get_interior_topoedges_of_topoface(model, topo_face)
            topo_edges.extend(topo_edge)

        vt_params = Comm.vt_composer_params.copy()
        vt_params["deleteMeshAfterMerge"] = False
        suppress_edge_args = {"topo_edge_ids": topo_edges, "params": vt_params}
        try:
            vt_composer.call_method("SuppressTopoEdges", suppress_edge_args)
        except Exception as e:
            pass
        vt_composer.destruct()


def suppress_toponodes(model: prime.Model, suppress_toponodes_params: dict,
                       cached_data: CachedData):
    part_scope = suppress_toponodes_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        vt_composer = Comm.PrimeObj(model, "VTComposer", part_id)
        topo_nodes = macros._get_topo_nodes(model)
        vt_params = Comm.vt_composer_params.copy()
        vt_params["mergeFaceNormalsAngleDeg"] = 180.0
        vt_params["mergeEdgeAllowSelfClose"] = True
        suppress_node_args = {
            "topo_node_ids": topo_nodes,
            "params": vt_params
        }
        try:
            vt_composer.call_method("SuppressTopoNodes", suppress_node_args)
        except Exception as e:
            pass
        vt_composer.destruct()

def repair_topoedges_of_topofaces(model: prime.Model, repair_topoedges_params: dict,
                                  cached_data: CachedData):
    part_scope = repair_topoedges_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        scaffolder = Comm.PrimeObj(model, "Scaffolder", part_id)
        scafolding_params = {}
        faces = macros._get_topo_faces(model)
        scafolding_params["constantMeshSize"] = 0.05
        scafolding_params['absoluteDistTol'] = 0.05
        repair_edge_args = {
            "topo_faces": faces,
            "params": scafolding_params
        }
        try:
            scaffolder.call_method("RepairTopoEdgesOfTopoFaces", repair_edge_args)
        except Exception as e:
            pass
        scaffolder.destruct()

def delete_topology(model: prime.Model, delete_topology_params: dict, cached_data: CachedData):
    merge_zonelets_by_label = delete_topology_params["merge_zonelets_by_label"]
    merge_zonelets_by_zone = delete_topology_params["merge_zonelets_by_zone"]
    if merge_zonelets_by_label and merge_zonelets_by_zone:
        er = "Both \"merge_zonelets_by_label\" and \"merge_zonelets_by_zone\" cannot be True."
        raise RuntimeError(er)

    part_scope = delete_topology_params["part_scope"]
    delete_edges = delete_topology_params["delete_edges"]
    delete_parts_without_topology = delete_topology_params["delete_parts_without_topology"]

    merge_params = prime.MergeZoneletsParams(model, False, 5)
    name_pattern_params = prime.NamePatternParams(model)
    params = prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True,
                                            delete_mesh_zonelets=False)

    part_ids = macros._get_part_ids(model, part_scope)
    part_ids_to_delete = []
    for part_id in part_ids:
        part = model.get_part(part_id)
        if len(part.get_topo_faces()):
            part.delete_topo_entities(params)
            if delete_edges:
                part.delete_zonelets(part.get_edge_zonelets())
            if merge_zonelets_by_label:
                labels = part.get_labels()
                for label in labels:
                    label_face_zonelets = part.get_face_zonelets_of_label_name_pattern(label,
                                                                         name_pattern_params)
                    if len(label_face_zonelets) > 1:
                        part.merge_zonelets(label_face_zonelets, merge_params)
            elif merge_zonelets_by_zone:
                zones = part.get_face_zones()
                for zone in zones:
                    zone_face_zonelets = part.get_face_zonelets_of_zone_name_pattern(zone,
                                                                      name_pattern_params)
                    if len(zone_face_zonelets) > 1:
                        part.merge_zonelets(zone_face_zonelets, merge_params)
        elif delete_parts_without_topology:
            part_ids_to_delete.append(part.id)
    if len(part_ids_to_delete) > 0:
        model.delete_parts(part_ids_to_delete)

def detect_thin_volumes(model: prime.Model, thin_volume_params: dict, cached_data: CachedData):
    part_scope = thin_volume_params["part_scope"]
    thickness = thin_volume_params["thickness"]
    volume_scope = thin_volume_params["volume_scope"]
    source_label = thin_volume_params["source_face_label"]
    target_label = thin_volume_params["target_face_label"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        part = model.get_part(part_id)
        volume_utils.detect_thin_volumes(model, part, thickness, volume_scope,
                                         source_label, target_label)
