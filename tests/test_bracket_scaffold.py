import math

import ansys.meshing.prime as prime


def test_bracket_scaffold(get_remote_client):
    # downloads  file
    bracket_file = prime.examples.download_bracket_fmd()
    model = get_remote_client.model
    # import cad model
    file_io = prime.FileIO(model)
    file_io.import_cad(
        file_name=bracket_file,
        params=prime.ImportCadParams(
            model=model,
            length_unit=prime.LengthUnit.MM,
            part_creation_type=prime.PartCreationType.MODEL,
        ),
    )
    part = model.get_part_by_name('bracket_mid_surface-3')
    part_summary_res = part.get_summary(prime.PartSummaryParams(model, print_mesh=False))
    print(part_summary_res)
    # Validate topo faces and edges
    assert math.isclose(67, float(part_summary_res.n_topo_edges), rel_tol=0.05)
    assert math.isclose(9, float(part_summary_res.n_topo_faces), rel_tol=0.02)
    # target element size
    element_size = 0.5

    params = prime.ScaffolderParams(
        model,
        absolute_dist_tol=0.1 * element_size,
        intersection_control_mask=prime.IntersectionMask.FACEFACEANDEDGEEDGE,
        constant_mesh_size=element_size,
    )
    # Get existing topoface/topoedge ids
    faces = part.get_topo_faces()
    beams = []

    scaffold_res = prime.Scaffolder(model, part.id).scaffold_topo_faces_and_beams(
        topo_faces=faces, topo_beams=beams, params=params
    )
    print(scaffold_res)
    # Validate scaffold Operation
    assert scaffold_res.error_code == prime.ErrorCode.NOERROR
    # Mesh topofaces with constant size and generate quad elements.
    surfer_params = prime.SurferParams(
        model=model,
        size_field_type=prime.SizeFieldType.CONSTANT,
        constant_size=element_size,
        generate_quads=True,
    )
    surfer_result = prime.Surfer(model).mesh_topo_faces(
        part.id, topo_faces=faces, params=surfer_params
    )
    # Validate scaffold Operation
    assert surfer_result.error_code == prime.ErrorCode.NOERROR
