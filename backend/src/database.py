from typing import TypeVar

from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel


def get_session():
    return Session(create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True))


class BaseRepository:
    __model__ = SQLModel
    T = TypeVar("T", bound=__model__)
    U = TypeVar("U", bound=__model__)

    @classmethod
    def create(cls, data: U) -> T:
        with get_session() as session:
            db_sheet = cls.__model__.from_orm(data)
            session.add(db_sheet)
            session.commit()
            session.refresh(db_sheet)
            return db_sheet

    @classmethod
    def get_list(cls) -> [T]:
        with get_session() as session:
            return session.query(cls.__model__).all()
