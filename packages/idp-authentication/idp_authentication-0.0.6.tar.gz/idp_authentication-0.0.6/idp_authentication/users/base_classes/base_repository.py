from typing import Any, ClassVar, Generic, Iterable, List, Optional

from idp_authentication.custom_types import T
from idp_authentication.users.domain.ports import RepositoryPort, SessionPort


class BaseRepository(Generic[T], RepositoryPort):
    entity: ClassVar[T]

    def __init__(self, session: SessionPort):
        self.session = session

    def get_or_none(self, **filters) -> Optional[T]:
        return self.session.query(self.entity).filter_by(**filters).one_or_none()

    def get_first(self, **filters) -> Optional[T]:
        return self.session.query(self.entity).filter_by(**filters).first()

    def filter_by_identifier(
        self, identifier_attr: str, identifier_values: Iterable[Any]
    ):
        entity_attr = getattr(self.entity, identifier_attr)
        return (
            self.session.query(self.entity)
            .filter(entity_attr.in_(identifier_values))
            .all()
        )

    def all(self) -> List[T]:
        return self.session.query(self.entity).all()

    def create(self, **attr) -> T:
        record = self.entity(**attr)
        self.session.add(record)
        self.session.commit()
        return record

    def update_record(self, record: T, **attr) -> T:
        for key, value in attr.items():
            setattr(record, key, value)
        self.session.commit()
        return record

    def delete(self, record: T) -> None:
        self.session.delete(record)
        self.session.commit()
