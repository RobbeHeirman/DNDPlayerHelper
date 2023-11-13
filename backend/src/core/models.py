from abc import abstractmethod
from typing import Optional, TypeVar, Type

import sqlmodel
from sqlmodel import Field


class _BaseTableMixinMeta(type(sqlmodel.SQLModel)):
    """
    Metaclass for our mixin. Makes sure to set table attribute to true.
    Needed for SQLModel.
    """

    def __new__(cls, *args, **kwargs):
        if "table" not in kwargs:
            kwargs['table'] = True
        return super().__new__(cls, *args, **kwargs)


class BaseTableMixin(sqlmodel.SQLModel, metaclass=_BaseTableMixinMeta, table=False):
    """
    MixinClass to be used if one of our models is a table.
    Enforces all our tables will have on int PK and tablename to be set.
    Fill with util Methods.
    """
    id: Optional[int] = sqlmodel.Field(primary_key=True, default=None)

    @property
    @abstractmethod
    def __tablename__(self) -> str:
        ...

    @classmethod
    def get_foreign_key_reference(cls: sqlmodel.SQLModel):
        return f"{cls.__tablename__}.id"


class EntityTableMixin(BaseTableMixin, table=False):
    """
    Base model for all "static" entities withing DND.
    Those are informative tables that describe the game. And designed for mostly read operations.
    """

    @property
    @abstractmethod
    def __tablename__(self) -> str:
        ...

    name: str = sqlmodel.Field(unique=True, index=True)


def RelationField(cls: Type[BaseTableMixin], **kwargs):
    return Field(foreign_key=cls.get_foreign_key_reference(), **kwargs)


def base_relation_table_factory(table1: Type[BaseTableMixin],
                                table2: Type[BaseTableMixin],
                                relation1_args: dict | None = None,
                                relation2_args: dict | None = None
                                ) -> _BaseTableMixinMeta:
    if relation1_args is None:
        relation1_args = {}

    if relation2_args is None:
        relation2_args = {}

    table1_name = table1.__name__
    table2_name = table2.__name__
    class_name = f"{table1_name}{table2_name}Base"
    bases = (BaseTableMixin,)
    attributes = {
        f"{table1_name}_id": RelationField(table1, **relation1_args),
        f"{table2_name}_id": RelationField(table2, **relation2_args),

        '__annotations__': {
            f"{table1_name}_id": int,
            f"{table2_name}_id": int
        }}
    return _BaseTableMixinMeta(class_name, bases, attributes, table=False)


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
