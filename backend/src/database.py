from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel


def get_session():
    return Session(create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True))


class BaseRepository:
    __model__ = SQLModel

    @classmethod
    def create(cls, data: SQLModel) -> __model__:
        with get_session() as session:
            db_sheet = cls.__model__.from_orm(data)
            session.add(db_sheet)
            session.commit()
            session.refresh(db_sheet)
            return db_sheet

    @classmethod
    def get_list(cls) -> [__model__]:
        with get_session() as session:
            return session.query(cls.__model__).all()
