# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Mixing elbow example."""
import os
import tempfile

import ansys.meshing.prime as prime
import ansys.meshing.prime.graphics as pyprime_graphics

with prime.launch_prime() as session:
    print('Connected to server!')
    model = session.model

    mixing_elbow = prime.examples.download_elbow_pmdat()

    print(f'Reading file {mixing_elbow}...')
    with prime.FileIO(model) as io:
        _ = io.read_pmdat(mixing_elbow, prime.FileReadParams(model=model))

    display = pyprime_graphics.Graphics(model)
    display()

    part = model.get_part_by_name('flow_volume')

    inlet_zone = model.create_zone('inlet', prime.ZoneType.FACE).zone_id
    inlet_faces = part.get_topo_faces_of_label_name_pattern(
        'inlet', prime.NamePatternParams(model=model)
    )
    _ = part.add_topo_entities_to_zone(inlet_zone, inlet_faces)

    outlet_zone = model.create_zone('outlet', prime.ZoneType.FACE).zone_id
    outlet_faces = part.get_topo_faces_of_label_name_pattern(
        'outlet', prime.NamePatternParams(model=model)
    )
    _ = part.add_topo_entities_to_zone(outlet_zone, outlet_faces)

    model.set_global_sizing_params(
        prime.GlobalSizingParams(model=model, min=5, max=20, growth_rate=1.2)
    )

    control = model.control_data.create_size_control(prime.SizingType.CURVATURE)
    _ = control.set_scope(prime.ScopeDefinition(model=model))

    field = prime.SizeField(model)
    _ = field.compute_volumetric(
        [control.id], prime.VolumetricSizeFieldComputeParams(enable_multi_threading=False)
    )

    with prime.Surfer(model) as surfacemesher:
        _ = surfacemesher.mesh_topo_faces(
            part.id,
            part.get_topo_faces(),
            prime.SurferParams(model=model, size_field_type=prime.SizeFieldType.VOLUMETRIC),
        )

    display(update=True)

    prism_control = model.control_data.create_prism_control()
    face_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.FACEZONELETS,
        evaluation_type=prime.ScopeEvaluationType.ZONES,
        zone_expression='* !inlet !outlet',
    )
    volume_scope = prime.ScopeDefinition(
        model=model,
        entity_type=prime.ScopeEntity.VOLUME,
        evaluation_type=prime.ScopeEvaluationType.ZONES,
        zone_expression="*",
    )
    prism_control.set_surface_scope(face_scope)
    prism_control.set_volume_scope(volume_scope)
    prism_control.set_growth_params(
        prime.PrismControlGrowthParams(
            model=model,
            offset_type=prime.PrismControlOffsetType.ASPECTRATIO,
            first_aspect_ratio=10.0,
            min_aspect_ratio=1.0,
            n_layers=3,
            growth_rate=1.2,
        )
    )

    with prime.AutoMesh(model) as volumemesher:
        _ = volumemesher.mesh(
            part.id,
            prime.AutoMeshParams(
                model,
                volume_fill_type=prime.VolumeFillType.TET,
                prism_control_ids=[prism_control.id],
            ),
        )

    display(update=True)

    with tempfile.TemporaryDirectory() as temp_folder:
        fluent_case = os.path.join(temp_folder, 'mixing_elbow.cas')
        with prime.FileIO(model) as io:
            _ = io.export_fluent_case(fluent_case, prime.ExportFluentCaseParams(model=model))

        assert os.path.exists(fluent_case)
        print(f'Fluent case exported at {fluent_case}')
