import os
import platform
import tempfile

import pytest

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics


@pytest.mark.skipif(platform.system() != 'Windows', reason="Windows specific test.")
def test_elbow_lucid(get_remote_client, get_examples):
    """Tests an use case with the elbow example."""

    model = get_remote_client.model
    prime_client = prime.launch_prime()
    mesh_util = prime.lucid.Mesh(model=model)

    mixing_elbow = get_examples["elbow_lucid_scdoc"]
    mesh_util.read(file_name=mixing_elbow)
    mesh_util.create_zones_from_labels("inlet,outlet")

    mesh_util.surface_mesh(min_size=5, max_size=20)

    mesh_util.volume_mesh(
        volume_fill_type=prime.VolumeFillType.POLY,
        prism_surface_expression="* !inlet !outlet",
        prism_layers=3,
    )

    display = Graphics(model=model)
    display()

    part = model.get_part_by_name("flow_volume")

    part_summary_res = part.get_summary(prime.PartSummaryParams(model=model))

    search = prime.VolumeSearch(model=model)
    params = prime.VolumeQualitySummaryParams(
        model=model,
        scope=prime.ScopeDefinition(model=model, part_expression="*"),
        cell_quality_measures=[prime.CellQualityMeasure.SKEWNESS],
        quality_limit=[0.95],
    )
    results = search.get_volume_quality_summary(params=params)

    with tempfile.TemporaryDirectory() as temp_folder:
        mesh_file = os.path.join(temp_folder, "mixing_elbow.cas")
        mesh_util.write(mesh_file)
        assert os.path.exists(mesh_file)
    prime_client.exit()
