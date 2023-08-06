from dataclasses import asdict

import pytest

from idp_authentication import UserRole
from idp_authentication.conftest import TEST_PERMISSION, TEST_ROLE_1, TEST_ROLE_2


@pytest.mark.parametrize(
    "user,user_role,expected_role",
    [
        ("user", "test_role_3", "test_role_3"),
        ("user_2", "test_role_4", "test_role_4"),
    ],
    indirect=["user"],
)
def test_user_role_create(container, user, user_role, expected_role):
    process_user, user_as_dict = process_user_use_case(container, user, user_role)
    new_role = UserRole(role=user_role, app_entities_restrictions={}, user_id=user.id)
    user_as_dict["user_roles"] = new_role
    process_user.execute(user_as_dict)
    assert user.user_roles[0].role == expected_role


@pytest.mark.parametrize(
    "user,user_role,expected_role",
    [
        ("user", TEST_ROLE_1, TEST_ROLE_1),
        ("user_2", TEST_ROLE_2, TEST_ROLE_2),
    ],
    indirect=["user"],
)
def test_user_role_update(container, user, user_role, expected_role):
    process_user, user_as_dict = process_user_use_case(container, user, user_role)
    process_user.execute(user_as_dict)
    assert user.user_roles[0].role == expected_role


def process_user_use_case(container, user, user_role):
    process_user = container.users_module().use_cases().process_user_message_use_case()
    user_as_dict = asdict(user)
    user_as_dict["app_specific_configs"] = {
        "test": {
            "default": {
                user_role: {
                    "app_entities_restrictions": {
                        "vehicle": [3],
                    },
                    "permission_restrictions": {TEST_PERMISSION: {"vehicle": [1, 2]}},
                }
            }
        }
    }
    return process_user, user_as_dict
