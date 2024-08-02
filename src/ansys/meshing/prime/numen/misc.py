# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Numen miscellaneous module."""
import os

import ansys.meshing.prime.numen.utils.macros as macros
from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData
from ansys.meshing.prime.numen.utils.communicator import call_method


def read(model: prime.Model, read_params: dict, cached_data: CachedData):
    """Read a file depending on extension."""
    length_unit_mapping = {
        "m": prime.LengthUnit.M,
        "cm": prime.LengthUnit.CM,
        "mm": prime.LengthUnit.MM,
        "um": prime.LengthUnit.UM,
        "nm": prime.LengthUnit.NM,
        "in": prime.LengthUnit.IN,
        "ft": prime.LengthUnit.FT,
    }
    cad_reader_route_mapping = {
        "program_controlled": prime.CadReaderRoute.PROGRAMCONTROLLED,
        "native": prime.CadReaderRoute.NATIVE,
        "workbench": prime.CadReaderRoute.WORKBENCH,
        "spaceclaim": prime.CadReaderRoute.SPACECLAIM,
        "discovery": prime.CadReaderRoute.DISCOVERY,
    }
    part_creation_type_mapping = {
        "model": prime.PartCreationType.MODEL,
        "assembly": prime.PartCreationType.ASSEMBLY,
        "part": prime.PartCreationType.PART,
        "body": prime.PartCreationType.BODY,
    }
    supported_cad_formats = []
    if os.name == "nt":
        supported_cad_formats = [
            ".scdoc",
            ".fmd",
            ".agdb",
            ".pmdb",
            ".meshdat",
            ".mechdat",
            ".dsdb",
            ".cmdb",
            ".sat",
            ".sab",
            ".dwg",
            ".dxf",
            ".model",
            ".exp",
            ".CATPart",
            ".CATProduct",
            ".cgr",
            ".3dxml",
            ".iges",
            ".igs",
            ".ipt",
            ".iam",
            ".jt",
            ".prt",
            ".x_t",
            ".x_b",
            ".par",
            ".psm",
            ".asm",
            ".sldprt",
            ".sldasm",
            ".step",
            ".stp",
            ".stl",
            ".plmxml",
            ".tgf",
            ".dsco",
            ".scdocx",
        ]
    else:
        supported_cad_formats = [
            ".fmd",
            ".agdb",
            ".pmdb",
            ".meshdat",
            ".mechdat",
            ".dsdb",
            ".cmdb",
            ".sat",
            ".sab",
            ".CATPart",
            ".CATProduct",
            ".iges",
            ".igs",
            ".jt",
            ".x_t",
            ".x_b",
            ".step",
            ".stp",
            ".stl",
            ".plmxml",
            ".tgf",
            ".dsco",
        ]
    file_name = read_params["file_name"]
    file_ext = os.path.splitext(file_name)[1]
    if file_ext == ".msh" or file_name[-7:] == ".msh.gz":
        prime.FileIO(model).import_fluent_meshing_meshes(
            [file_name], prime.ImportFluentMeshingMeshParams(model, append=read_params["append"])
        )
    elif file_ext == ".cas" or file_name[-7:] == ".cas.gz" or file_name[-7:] == ".cas.h5":
        prime.FileIO(model).import_fluent_case(
            file_name, prime.ImportFluentCaseParams(model, append=read_params["append"])
        )
    elif file_ext == ".cdb":
        prime.FileIO(model).import_mapdl_cdb(
            file_name, prime.ImportMapdlCdbParams(model, append=read_params["append"])
        )
    elif file_ext == ".pmdat" or file_name[-9:] == ".pmdat.gz":
        prime.FileIO(model).read_pmdat(
            file_name, prime.FileReadParams(model, append=read_params["append"])
        )
        call_method(model, "PrimeMesh::Model/EnableLocalGSProjectionMethod", model._object_id, {})
    elif file_ext == ".psf" or file_name[-7:] == ".psf.gz":
        prime.FileIO(model).read_size_field(file_name, prime.ReadSizeFieldParams(model))
    elif file_ext in supported_cad_formats:
        params = prime.ImportCadParams(
            model=model,
            length_unit=length_unit_mapping[read_params["length_unit"]],
            cad_reader_route=cad_reader_route_mapping[read_params["cad_reader_route"]],
            part_creation_type=part_creation_type_mapping[read_params["part_creation_type"]],
            geometry_transfer=True,
            append=read_params["append"],
        )
        fileio = prime.FileIO(model)
        fileio.import_cad(file_name=file_name, params=params)
    model._comm.serve(
        model, "PrimeMesh::Model/EnableLocalGSProjectionMethod", model._object_id, args={}
    )


def read_size_field(model: prime.Model, size_field_read_params: dict, cached_data: CachedData):
    """Read size field."""
    file_name = size_field_read_params["file_name"]
    fileio = prime.FileIO(model)
    fileio.read_size_field(file_name, prime.ReadSizeFieldParams(model))


def write(model: prime.Model, write_params: dict, cached_data: CachedData):
    """Write or export a file depending on extension."""
    file_name = write_params["file_name"]
    file_ext = os.path.splitext(file_name)[1]
    fileio = prime.FileIO(model)
    if file_ext == ".pmdat" or file_name[-9:] == ".pmdat.gz":
        fileio.write_pmdat(write_params["file_name"], prime.FileWriteParams(model))
    elif file_ext == ".msh" or file_name[-7:] == ".msh.gz":
        fileio.write_pmdat(write_params["file_name"], prime.FileWriteParams(model))
    elif file_ext == ".psf" or file_name[-7:] == ".psf.gz":
        fileio.write_size_field(file_name, prime.WriteSizeFieldParams(model))


def set_global_sizing(model: prime.Model, global_params: dict, cached_data: CachedData):
    """Set global sizing."""
    model.set_global_sizing_params(
        prime.GlobalSizingParams(
            model,
            global_params["min_size"],
            global_params["max_size"],
            global_params["growth_rate"],
        )
    )


def create_labels_per_part_entities(
    model: prime.Model, create_labels_params: dict, cached_data: CachedData
):
    """Create labels per zonelets or topo entities."""
    part_scope = create_labels_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        part = model.get_part(part_id)
        topo_faces = part.get_topo_faces()
        if len(topo_faces) > 0:
            if create_labels_params["entity_type"] == "face":
                part.add_labels_on_topo_entities([part.name], part.get_topo_faces())
            if create_labels_params["entity_type"] == "edge":
                part.add_labels_on_topo_entities([part.name], part.get_topo_edges())
        else:
            if create_labels_params["entity_type"] == "face":
                part.add_labels_on_zonelets([part.name], part.get_face_zonelets())
            if create_labels_params["entity_type"] == "edge":
                part.add_labels_on_topo_entities([part.name], part.get_edge_zonelets())


def merge_zonelets(model: prime.Model, merge_params: dict, cached_data: CachedData):
    """Merge zonelets with the given merge parameters."""
    part_scope = merge_params["part_scope"]
    scope_evaluation_type = merge_params["scope_evaluation_type"]
    entity_type = merge_params["entity_type"]
    entity_scope = merge_params["entity_scope"]
    add_to_zone = merge_params["add_to_zone"]
    add_label = merge_params["add_label"]
    merge_params = prime.MergeZoneletsParams(
        model=model,
        merge_small_zonelets_with_neighbors=False,
        element_count_limit=5,
    )
    name_pattern_params = prime.NamePatternParams(model)
    part_ids = macros._get_part_ids(model, part_scope)
    for part_id in part_ids:
        part = model.get_part(part_id)
        if entity_type == "face":
            face_zonelets = []
            if scope_evaluation_type == "labels":
                face_zonelets = part.get_face_zonelets_of_label_name_pattern(
                    entity_scope, name_pattern_params
                )
            elif scope_evaluation_type == "zones":
                face_zonelets = part.get_face_zonelets_of_zone_name_pattern(
                    entity_scope, name_pattern_params
                )
            merge_results = part.merge_zonelets(face_zonelets, merge_params)
            if add_to_zone != "":
                zone_id = model.get_zone_by_name(add_to_zone)
                if zone_id < 1:
                    zone_results = model.create_zone(add_to_zone, prime.ZoneType.FACE)
                    zone_id = zone_results.zone_id
                part.add_zonelets_to_zone(zone_id, merge_results.merged_zonelets)
            if add_label != "":
                part.add_labels_on_zonelets([add_label], merge_results.merged_zonelets)
        elif entity_type == "edge":
            edge_zonelets = []
            if scope_evaluation_type == "labels":
                edge_zonelets = part.get_edge_zonelets_of_label_name_pattern(
                    entity_scope, name_pattern_params
                )
                merge_results = part.merge_zonelets(edge_zonelets, merge_params)
                if add_to_zone != "":
                    zone_id = model.get_zone_by_name(add_to_zone)
                    if zone_id < 1:
                        zone_results = model.create_zone(add_to_zone, prime.ZoneType.EDGE)
                        zone_id = zone_results.zone_id
                    part.add_zonelets_to_zone(zone_id, merge_results.merged_zonelets)
                if add_label != "":
                    part.add_labels_on_zonelets([add_label], merge_results.merged_zonelets)


def delete_parts(model: prime.Model, delete_params: dict, cached_data: CachedData):
    """Delete parts specified by parameters."""
    part_scope = delete_params["part_scope"]
    part_ids = macros._get_part_ids(model, part_scope)
    if len(part_ids) > 0:
        model.delete_parts(part_ids)
