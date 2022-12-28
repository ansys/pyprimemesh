import math

import ansys.meshing.prime as prime

def test_case_0(get_remote_client):
    # downloads pmdat file
    case_0 = prime.examples.download_file(
        "case-0.pmdat",
        "https://github.com/pyansys/example-data/tree/master/pyprimemesh/case_0"
        )
    # reads file
    model = get_remote_client.model
    fileIO = prime.FileIO(model=model)
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=case_0)
    #file_read_params = prime.FileReadParams(model=model)
    #res = fileIO.read_pmdat(file_name=case_0,file_read_params=file_read_params)
    model.set_global_sizing_params(params=prime.GlobalSizingParams(
        model = model,
        min = 0.2, max = 10.0, growth_rate = 1.2))

	#Surface mesh size controls

    softControl = model.control_data.create_size_control(prime.SizingType.SOFT)
    params = prime.SoftSizingParams(model=model, max=5.0, growth_rate=1.2)
    softControl.set_soft_sizing_params(params=params)
    scope = prime.ScopeDefinition(model=model)
    scope.entity_type = prime.ScopeEntity.FACEZONELETS
    scope.part_expression = "*" # check
    softControl.set_scope(scope)
    print(softControl)
    hardControl = model.control_data.create_size_control(prime.SizingType.HARD)
    params = prime.HardSizingParams(model=model, min=0.4,  growth_rate=1.2)
    hardControl.set_hard_sizing_params(params=params)
    scope = prime.ScopeDefinition(model=model)
    scope.entity_type = prime.ScopeEntity.FACEZONELETS
    scope.part_expression = "cyl"
    res = hardControl.set_scope(scope)
    size_control =  model.control_data.size_controls 
    print(size_control)
    ids = []
    for eachSizeControl in size_control:
        ids.append(eachSizeControl.id)
    size_field = prime.SizeField(model)
    res = size_field.compute_volumetric(
        ids,
        prime.VolumetricSizeFieldComputeParams(enable_multi_threading=False)
        )
    #Surface mesh
    surfer_params = prime.SurferParams(model = model)
    partIDs = []
    for part in model.parts:
        partIDs.append(part.id)
    print(partIDs) #inline
    for part in model.parts:
        surfer = prime.Surfer(model)
        params = prime.SurferParams(
            model = model, size_field_type= prime.SizeFieldType.VOLUMETRIC
            )
        result = surfer.mesh_topo_faces(
            part.id, topo_faces = part.get_topo_faces(),params = params
            )
    #Validate surface meshing operation
    assert result.error_code == prime.ErrorCode.NOERROR

	#delete topo entities
    upperpart = model.get_part_by_name("upper")
    middlepart = model.get_part_by_name("middle")
    lowerpart = model.get_part_by_name("lower")
    cylpart = model.get_part_by_name("cyl")
    res_geom_all = upperpart.delete_topo_entities(
        params = prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
        )
    res_geom_all = middlepart.delete_topo_entities(
        params = prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
        )
    res_geom_all = lowerpart.delete_topo_entities(
        params = prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
        )
    res_geom_all = cylpart.delete_topo_entities(
        params = prime.DeleteTopoEntitiesParams(model=model, delete_geom_zonelets=True, delete_mesh_zonelets=False)
        )
    upperpart.add_labels_on_zonelets(labels= ["upper"] , zonelets = upperpart.get_face_zonelets() )
    middlepart.add_labels_on_zonelets(labels= ["middle"], zonelets = middlepart.get_face_zonelets() )
    lowerpart.add_labels_on_zonelets(labels= ["lower"], zonelets = lowerpart.get_face_zonelets() )
    cylpart.add_labels_on_zonelets(labels= ["cyl"], zonelets = cylpart.get_face_zonelets() )
    #merge parts
    params =  prime.MergePartsParams(model = model)
    params.merged_part_suggested_name ="combined"
    model.merge_parts(partIDs, params = params)
    part = model.get_part_by_name("combined")
    # connect all boxes
    connector = prime.Connect(model)
    params = prime.JoinParams(model=model, tolerance=0.2)
    result = connector.join_face_zonelets(part.id, 
        part.get_face_zonelets_of_label_name_pattern("lower,middle,upper", prime.NamePatternParams(model)), 
        part.get_face_zonelets_of_label_name_pattern("lower,middle,upper", prime.NamePatternParams(model)), params)
    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model, print_id=False, print_mesh=True))
    print(part_summary_res)

	# subtract cylinder from the middle box and dlete the cylinder
    subtractor = prime.SurfaceUtilities(model)
    subParam = prime.SubtractZoneletsParams(
        model = model, retain_cutter = False, extract_edges = False, trace_edges = False)
    zonelets = part.get_face_zonelets_of_label_name_pattern(
        "middle", prime.NamePatternParams(model))
    print(zonelets)
    cutters = []
    cutters.append(prime.PartZonelets(model, part_id=part.id, 
        face_zonelets=part.get_face_zonelets_of_label_name_pattern("cyl", prime.NamePatternParams(model))))
    print(cutters)
    subtractor.subtract_zonelets(part.id, zonelets = zonelets, cutters= cutters, params = subParam)
    part_summary_res = part.get_summary(
        prime.PartSummaryParams(model=model, print_id=False, print_mesh=True))
    print(part_summary_res)

	#Volume mesh
    volres = part.compute_closed_volumes(prime.ComputeVolumesParams(model=model))
    print("Number of volumes computed : " + str(len(volres.volumes)))
    params = prime.ComputeVolumesParams(model=model)
    result = part.compute_closed_volumes(params=params)
    print(result)
    autoMesher = prime.AutoMesh(model=model)
    autoMesherParams = prime.AutoMeshParams(model=model)
    res = autoMesher.mesh(part.id, automesh_params=autoMesherParams)
    part_summary_res = part.get_summary(
        prime.PartSummaryParams(model=model, print_id=False, print_mesh=True))
    #Validate volume meshing operation and mesh statistics
    assert res.error_code == prime.ErrorCode.NOERROR
    assert math.isclose(5230, float(part_summary_res.n_tri_faces), rel_tol=0.05)
    assert math.isclose(31679, float(part_summary_res.n_tet_cells), rel_tol=0.03)
    assert math.isclose(0, float(part_summary_res.n_poly_cells), rel_tol=0.02)