from typing import TypeVar, Generic, Type

from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel


def get_session():
    return Session(create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True))


T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    __model__: Type[T] = SQLModel

    @classmethod
    async def create(cls: Type[T], data: SQLModel) -> T:
        with get_session() as session:
            db_sheet = cls.__model__.from_orm(data)
            session.add(db_sheet)
            session.commit()
            session.refresh(db_sheet)
            return db_sheet

    @classmethod
    async def get(cls: Type[T], obj_id: int) -> T:
        with get_session() as session:
            return session.query(cls).get(obj_id)

    @classmethod
    async def get_list(cls: T) -> [T]:
        with get_session() as session:
            return session.query(cls.__model__).all()
