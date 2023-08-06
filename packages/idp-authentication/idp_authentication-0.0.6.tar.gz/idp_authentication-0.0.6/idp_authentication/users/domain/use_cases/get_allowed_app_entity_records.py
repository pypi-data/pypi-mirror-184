from idp_authentication.enums import ChoiceEnum
from idp_authentication.users.base_classes.base_use_case import BaseUseCase


class GetAllowedAppEntityRecordsUseCase(BaseUseCase):
    """Get allowed app entity records use case."""

    def execute(self, user, role: ChoiceEnum, app_entity_type: str, permission: str):
        """Execute the use case."""
        allowed_app_entity_records_identifiers = (
            self._get_allowed_app_entity_records_identifiers(
                user=user,
                role=role,
                app_entity_type=app_entity_type,
                permission=permission,
            )
        )
        return self._get_records(
            app_entity_type=app_entity_type,
            records_identifiers=allowed_app_entity_records_identifiers,
        )
