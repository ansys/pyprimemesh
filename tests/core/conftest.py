import pytest

import ansys.meshing.prime as prime


@pytest.fixture(scope="module")
def initialized_model_elbow(get_remote_client, get_examples):
    # load example from fixture
    elbow_lucid = get_examples["elbow_lucid"]

    # initialize model from fixture
    model = get_remote_client.model
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=elbow_lucid)
    return model, mesher


@pytest.fixture(scope="module")
def initialized_model_toycar(get_remote_client, get_examples):
    # load example from fixture
    toy_car = get_examples["toy_car"]

    # initialize model from fixture
    model = get_remote_client.model
    mesher = prime.lucid.Mesh(model)
    mesher.read(file_name=toy_car)
    return model, mesher
