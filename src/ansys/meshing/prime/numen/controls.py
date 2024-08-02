from ansys.meshing import prime
from ansys.meshing.prime.numen.utils.cached_data import CachedData

def _get_size_control_type(control_params):
    sizing_type_mapping = {
        "boi": prime.SizingType.BOI,
        "curvature": prime.SizingType.CURVATURE,
        "hard": prime.SizingType.HARD,
        "soft": prime.SizingType.SOFT,
        "proximity": prime.SizingType.PROXIMITY
    }
    control_type = control_params["control_type"]
    sizing_type = sizing_type_mapping[control_type]
    return sizing_type

def _get_size_control_params(model: prime.Model, control_params: dict):
    sizing_type = _get_size_control_type(control_params)
    max_size = control_params.get("max_size")
    min_size = control_params.get("min_size")
    growth_rate = control_params.get("growth_rate")
    normal_angle = control_params.get("normal_angle")
    params = {}
    if sizing_type == prime.SizingType.CURVATURE:
        params = prime.CurvatureSizingParams(model)
        params.max = max_size
        params.min = min_size
        params.growth_rate = growth_rate
        params.normal_angle = normal_angle
        params.use_cad_curvature = True

    elif sizing_type == prime.SizingType.HARD:
        params = prime.HardSizingParams(model)
        params.min = min_size
        params.growth_rate = growth_rate

    elif sizing_type == prime.SizingType.SOFT:
        params = prime.SoftSizingParams(model)
        params.max = max_size
        params.growth_rate = growth_rate

    elif sizing_type == prime.SizingType.BOI:
        params = prime.BoiSizingParams(model)
        params.max = max_size
        params.growth_rate = growth_rate

    elif sizing_type == prime.SizingType.PROXIMITY:
        params = prime.ProximitySizingParams(model)
        params.min = min_size
        params.max = max_size
        params.growth_rate = growth_rate
        params.elements_per_gap = control_params["elements_per_gap"]

    return params

def _get_scope(model: prime.Model, control_params: dict):
    scope = prime.ScopeDefinition(model)
    scope.entity_type = prime.ScopeEntity.FACEZONELETS
    if control_params["scope_evaluation_type"] == "labels":
        scope.evaluation_type = prime.ScopeEvaluationType.LABELS
    elif control_params["scope_evaluation_type"] == "zones":
        scope.evaluation_type = prime.ScopeEvaluationType.ZONES
    entity_type = control_params["entity_type"]
    if entity_type == "edge":
        scope.entity_type = prime.ScopeEntity.EDGEZONELETS
    elif entity_type == "face":
        scope.entity_type = prime.ScopeEntity.FACEZONELETS
    elif entity_type == "face_and_edge":
        scope.entity_type = prime.ScopeEntity.FACEANDEDGEZONELETS
    if scope.evaluation_type == prime.ScopeEvaluationType.LABELS:
        scope.label_expression = control_params.get("entity_scope")
    else:
        scope.zone_expression = control_params.get("entity_scope")
    scope.part_expression = control_params.get("part_scope")
    return scope

def create_size_control(model: prime.Model, size_control_params: dict, cached_data: CachedData):
    parameters = {
        "sizing_type": _get_size_control_type(size_control_params),
        "sizing_params": _get_size_control_params(model, size_control_params),
        "scope": _get_scope(model, size_control_params)
    }
    cached_data.push_cached_object(size_control_params["control_name"],
                                   "numen.controls.create_size_control",
                                   parameters)

def create_size_field(model: prime.Model, size_field_params: dict, cached_data: CachedData):
    size_control_names = size_field_params["size_control_names"]
    parameters = {
        "size_controls": size_control_names
    }
    cached_data.push_cached_object(size_field_params["size_field_name"],
                                   "numen.controls.create_size_field",
                                   parameters)

def delete_control(model: prime.Model, read_params: dict, cached_data: CachedData):
    control = model.control_data.get_size_control_by_name(read_params["name"])
    model.control_data.delete_controls([control.id])
