from typing import Union

from idp_authentication.custom_types import UserTenantData
from idp_authentication.users.base_classes.base_use_case import UseCasePort
from idp_authentication.users.domain.entities.user import User
from idp_authentication.users.domain.ports.unit_of_work import UsersUnitOfWorkPort

user_data_keys = [
    "username",
    "email",
    "first_name",
    "last_name",
    "is_active",
    "is_staff",
    "is_superuser",
    "date_joined",
]


class CreateOrUpdateUserUseCase(UseCasePort):
    def __init__(self, users_unit_of_work: UsersUnitOfWorkPort):
        self.user_tenant_data = None
        self.users_unit_of_work = users_unit_of_work

    def keep_keys(self, keys: list) -> UserTenantData:
        return {k: v for k, v in self.user_tenant_data.items() if k in keys}

    def check_if_user_exists(self) -> Union[User, bool]:
        user = self.users_unit_of_work.user_repository.get_or_none(
            username=self.user_tenant_data.get("username")
        )
        return user or False

    def execute(self, data: UserTenantData) -> User:
        self.user_tenant_data = data
        user_data = self.keep_keys(user_data_keys)
        user = self.check_if_user_exists()
        return (
            self.users_unit_of_work.user_repository.update_record(user, **user_data)
            if user
            else self.users_unit_of_work.user_repository.create(**user_data)
        )
