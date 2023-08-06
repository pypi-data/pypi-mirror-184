from sqlalchemy import or_

from idp_authentication.users.base_classes.base_repository import BaseRepository
from idp_authentication.users.domain.entities.user import User
from idp_authentication.users.domain.entities.user_role import UserRole
from idp_authentication.users.domain.ports.repository import UserRepositoryPort


class UserRepository(UserRepositoryPort, BaseRepository):
    entity = User

    def get_users_with_access_to_records(self, *args, **kwargs):
        # Todo: Implement this method
        """Get users with access to records."""
        user_roles = kwargs.get("roles")
        # app_entity_type = kwargs.get("app_entity_type")
        # record_identifier = kwargs.get("record_identifier")
        roles = (
            self.session.query(UserRole)
            .join(User)
            .filter(
                UserRole.role.in_(user_roles),
                or_(
                    UserRole.app_entities_restrictions is not None,  # noqa: E711
                ),
            )
            .all()
        )
        role_ids = [role.id for role in roles]
        return (
            self.session.query(self.entity)
            .join(UserRole)
            .filter(
                self.entity.is_active.is_(True),
                User.user_roles.any(UserRole.id.in_(role_ids)),
            )
            .all()
        )

    def remove_user_role(self, user: User, role: UserRole):
        """Remove user role."""
        user.user_roles.remove(role)
        self.session.commit()
