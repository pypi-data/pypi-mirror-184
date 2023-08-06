from typing import Any, List

from idp_authentication.users.base_classes.base_use_case import BaseUseCase


class GetUsersWithAccessToAppEntityRecordUseCase(BaseUseCase):
    def execute(self, app_entity_type: str, record_identifier: Any, roles: List[str]):
        self._get_app_entity_repository(app_entity_type)
        return self.users_unit_of_work.user_repository.get_users_with_access_to_records(
            app_entity_type=app_entity_type,
            record_identifier=record_identifier,
            roles=roles,
        )
