from idp_authentication.users.adapters.repositories.user_repository import (
    UserRepository,
)
from idp_authentication.users.adapters.repositories.user_role_repository import (
    UserRoleRepository,
)
from idp_authentication.users.domain.ports.session import SessionPort
from idp_authentication.users.domain.ports.unit_of_work import (
    AuthUnitOfWorkPort,
    UsersUnitOfWorkPort,
)


class UsersUnitOfWork(UsersUnitOfWorkPort):
    def __init__(self, session: SessionPort):

        self.session = session
        self.user_repository = UserRepository(session)
        self.user_role_repository = UserRoleRepository(session)


class AuthUnitOfWork(AuthUnitOfWorkPort):
    def __init__(self, session: SessionPort):
        self.session = session
        self.user = UserRepository(session)
