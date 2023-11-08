from typing import TypeVar, Generic, Type

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import Session, SQLModel

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    _CONNECTION_PARAMS = {
        'url': "sqlite:///../dndplayerhelper.sqlite",
        'echo': True
    }

    __model__: Type[T] = SQLModel

    @staticmethod
    def get_session():
        return Session(create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True))

    @staticmethod
    def get_async_session():
        return Session(create_async_engine(**BaseRepository._CONNECTION_PARAMS))

    @classmethod
    def create(cls: Type[T], data: SQLModel) -> T:
        with cls.get_session() as session:
            db_sheet = cls.__model__.from_orm(data)
            session.add(db_sheet)
            session.commit()
            session.refresh(db_sheet)
            return db_sheet

    @classmethod
    def get(cls: Type[T], obj_id: int) -> T:
        with cls.get_session() as session:
            return session.get(cls.__model__, obj_id)

    @classmethod
    async def get_list(cls: T) -> [T]:
        with cls.get_session() as session:
            return session.query(cls.__model__).all()
