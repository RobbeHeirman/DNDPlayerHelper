from functools import reduce
from typing import Optional, TypeVar, Type

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, DeclarativeMeta, declared_attr, relationship


class Base(DeclarativeBase):
    pass


class BaseTableMixin(Base):
    """
    MixinClass to be used if one of our models is a table.
    Enforces all our tables will have on int PK and tablename to be set.
    Fill with util Methods.
    """
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        result = cls.__name__[0].lower()
        for letter in cls.__name__[1:]:
            if letter.isupper():
                result += "_"
            result += letter.lower()
        return result

    id: Mapped[int] = mapped_column(primary_key=True)

    @classmethod
    def get_foreign_key_reference(cls: Base):
        return f"{cls.__tablename__}.id"


class EntityTableMixin(BaseTableMixin):
    """
    Base model for all "static" entities withing DND.
    Those are informative tables that describe the game. And designed for mostly read operations.
    """
    __abstract__ = True

    name: Mapped[str] = mapped_column(unique=True, index=True)

def RelationField(cls: Type[BaseTableMixin], **kwargs):
    return mapped_column(ForeignKey(cls.get_foreign_key_reference(), **kwargs))


# def base_relation_table_factory(table1: Type[BaseTableMixin],
#                                 table2: Type[BaseTableMixin],
#                                 relation1_args: dict | None = None,
#                                 relation2_args: dict | None = None
#                                 ) -> DeclarativeMeta:
#     if relation1_args is None:
#         relation1_args = {}
#
#     if relation2_args is None:
#         relation2_args = {}
#
#     table1_name = table1.__name__
#     table2_name = table2.__name__
#     class_name = f"{table1_name}{table2_name}Base"
#     bases = (BaseTableMixin,)
#     attributes = {
#         f"{table1_name}_id": RelationField(table1, **relation1_args),
#         f"{table2_name}_id": RelationField(table2, **relation2_args),
#
#         '__annotations__': {
#             f"{table1_name}_id": int,
#             f"{table2_name}_id": int
#         }}
#     return DeclarativeMeta(class_name, bases, attributes, table=False)


T = TypeVar('T', bound=type)


def make_fields_optional(cls: T) -> T:
    """
    Decorator,
    replaces base class annotations with optional annotations.
    """
    if cls.__base__ is None:
        return cls

    for key, val in cls.__base__.__annotations__.items():
        if key not in cls.__annotations__:
            cls.__annotations__[key] = Optional[val]
    return cls


