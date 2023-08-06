from idp_authentication.conftest import TEST_ROLE_1, VEHICLE_APP_ENTITY_IDENTIFIER


def test_user_with_access_to_app_entity_record(container, vehicle, user):
    user_with_access_to_app = (
        container.users_module()
        .use_cases()
        .get_users_with_access_to_app_entity_record_use_case()
    )
    user_with_access_to_app.execute(
        app_entity_type=VEHICLE_APP_ENTITY_IDENTIFIER,
        record_identifier=[2],
        roles=[TEST_ROLE_1],
    )
