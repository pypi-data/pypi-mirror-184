import abc
from typing import Any, Iterable, List

from idp_authentication.users.domain.entities.user import User


class RepositoryPort(abc.ABC):
    @abc.abstractmethod
    def get_or_none(self, **kwargs) -> User:
        """Get a record by its attributes."""

    @abc.abstractmethod
    def get_first(self, **filters):
        """Get the first record, after applying filters"""

    @abc.abstractmethod
    def filter_by_identifier(
        self, identifier_attr: str, identifier_values: Iterable[Any]
    ):
        """Filter by identifier values"""

    @abc.abstractmethod
    def all(self):
        """Get all records"""

    @abc.abstractmethod
    def create(self, **kwargs):
        """Create a new record."""

    @abc.abstractmethod
    def update_record(self, record, **kwargs):
        """Update a record."""


class UserRepositoryPort(RepositoryPort, abc.ABC):
    """User repository port."""

    @abc.abstractmethod
    def get_users_with_access_to_records(self, *args, **kwargs) -> List[User]:
        """Get users with access to records."""

    @abc.abstractmethod
    def remove_user_role(self, user, role):
        """Remove user role."""


class UserRoleRepositoryPort(RepositoryPort, abc.ABC):
    """User role repository port."""

    @abc.abstractmethod
    def delete(self, record):
        """Delete a record."""


class AppEntityRepositoryPort(RepositoryPort, abc.ABC):
    """App entity repository port."""

    @classmethod
    @abc.abstractmethod
    def get_idp_identifier_attr(cls) -> str:
        """Get the identifier attribute for the app entity."""
