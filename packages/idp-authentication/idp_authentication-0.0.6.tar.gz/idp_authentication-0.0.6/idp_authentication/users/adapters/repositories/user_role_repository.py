from idp_authentication.users.base_classes.base_repository import BaseRepository
from idp_authentication.users.domain.entities import UserRole
from idp_authentication.users.domain.ports.repository import UserRoleRepositoryPort


class UserRoleRepository(UserRoleRepositoryPort, BaseRepository):
    entity = UserRole

    def delete(self, record: UserRole) -> None:
        self.session.delete(record)
        self.session.commit()
