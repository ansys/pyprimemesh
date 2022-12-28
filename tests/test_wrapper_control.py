import ansys.meshing.prime as prime


def test_wrapper_control(get_remote_client):

    model = get_remote_client.model
    model.set_global_sizing_params(
        prime.GlobalSizingParams(model=model, min=2.0, max=20, growth_rate=1.2)
    )
    # Test contanct preventation
    params = prime.ContactPreventionParams(model=model)
    glob_sf_params = model.get_global_sizing_params()
    # Validate size for contact prevention params
    assert glob_sf_params.min >= params.size

    # Test leak prevention
    params = prime.LeakPreventionParams(model=model)
    glob_sf_params = model.get_global_sizing_params()
    # Validate size for leak prevention params
    assert glob_sf_params.min >= params.max_hole_size

    # Test default feature recovery
    params = prime.FeatureRecoveryParams(model=model)
    glob_sf_params = model.get_global_sizing_params()
    # Validate size at features
    assert glob_sf_params.min >= params.size_at_features

    # Test set contact preventions

    wrapper_control = model.control_data.create_wrapper_control()
    sscope = prime.ScopeDefinition(model=model, part_expression="frame1")
    tscope = prime.ScopeDefinition(model=model, part_expression="breaks1*, *tyres1*")
    con_prev_params1 = prime.ContactPreventionParams(
        model=model, source_scope=sscope, target_scope=tscope, size=0.2
    )
    sscope2 = prime.ScopeDefinition(model=model, part_expression="frame2")
    tscope2 = prime.ScopeDefinition(model=model, part_expression="breaks2*, *tyres2*")
    con_prev_params2 = prime.ContactPreventionParams(
        model=model, source_scope=sscope2, target_scope=tscope2, size=0.1
    )
    res_con_prev = wrapper_control.set_contact_preventions([con_prev_params1, con_prev_params2])
    # Validate number of controls set
    assert len(res_con_prev.ids) == 2

    # Test set leak preventions
    wrapper_control = model.control_data.create_wrapper_control()
    scope1 = prime.ScopeDefinition(model=model, part_expression="frame1")
    leak_prev_params1 = prime.LeakPreventionParams(
        model=model, scope=scope1, max_hole_size=0.2, material_points=["cabin"]
    )
    scope2 = prime.ScopeDefinition(model=model, part_expression="breaks2*, *tyres2*")
    leak_prev_params2 = prime.LeakPreventionParams(
        model=model, scope=scope2, max_hole_size=0.1, material_points=["cargo"]
    )
    res_leak_prev = wrapper_control.set_leak_preventions([leak_prev_params1, leak_prev_params2])
    # Validate number of controls set
    assert len(res_leak_prev.ids) == 2

    # Test set feature recoveries
    wrapper_control = model.control_data.create_wrapper_control()
    scope = prime.ScopeDefinition(model=model, part_expression="*!tunnel")
    feat_params1 = prime.FeatureRecoveryParams(
        model=model, scope=scope, enable_feature_octree_refinement=True, size_at_features=0.3
    )
    scope2 = prime.ScopeDefinition(model=model, part_expression="tunnel")
    feat_params2 = prime.FeatureRecoveryParams(model=model, scope=scope2)
    res_feat_rec = wrapper_control.set_feature_recoveries([feat_params1, feat_params2])
    # Validate number of controls set
    assert len(res_feat_rec.ids) == 2

    # Test set geometry scope

    wrapper_control = model.control_data.create_wrapper_control()
    wrapper_control.set_geometry_scope(
        prime.ScopeDefinition(model=model, entity_type=prime.ScopeEntity.FACEANDEDGEZONELETS)
    )
    scope = wrapper_control.get_geometry_scope()
    # Validate entity type for default scope
    assert scope.entity_type == prime.ScopeEntity.FACEANDEDGEZONELETS
    # Validate evaluation type for default scope.
    assert scope.evaluation_type == prime.ScopeEvaluationType.LABELS
    # Validate part expression for default scope.
    assert scope.part_expression == "*"
    # Validate label expression for default scope.
    assert scope.label_expression == "*"
    # Validate zone expression for default scope.
    assert scope.zone_expression == "*"
