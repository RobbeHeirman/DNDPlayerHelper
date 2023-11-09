import abc
from typing import TypeVar, Generic, Type

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

T = TypeVar("T", bound=SQLModel)

_CONNECTION_PARAMS = {
    'url': "sqlite+aiosqlite:///../dndplayerhelper.sqlite",
    'echo': True
}


class BaseRepository(Generic[T]):
    """
    Base class to interact with the database.
    __model__ prop should be set. This is the model the Child Repository will interact on.

    """
    get_session = sessionmaker(create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True))
    get_async_session = sessionmaker(
        create_async_engine("sqlite+aiosqlite:///../dndplayerhelper.sqlite", echo=True),
        class_=AsyncSession
    )

    @property
    @abc.abstractmethod
    def __model__(self) -> Type[T]:
        ...

    @classmethod
    def create(cls: Type[T], data: SQLModel) -> T:
        with cls.get_session() as session:
            db_sheet = cls.__model__.from_orm(data)
            session.add(db_sheet)
            session.commit()
            session.refresh(db_sheet)
            return db_sheet

    @classmethod
    async def create_aync(cls: Type[T], data: SQLModel):
        async with cls.get_async_session() as conn:
            db_sheet = cls.__model__.from_orm(data)
            conn.add(db_sheet)
            await conn.commit()
            await conn.refresh(db_sheet)
            return db_sheet

    @classmethod
    def get(cls: Type[T], obj_id: int) -> T:
        with cls.get_session() as session:
            return session.get(cls.__model__, obj_id)

    @classmethod
    async def get_list(cls: T) -> [T]:
        with cls.get_session() as session:
            return session.query(cls.__model__).all()
