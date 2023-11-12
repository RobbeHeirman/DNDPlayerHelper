from abc import abstractmethod
from typing import Optional, TypeVar

import sqlmodel


class _BaseTableMixinMeta(type(sqlmodel.SQLModel)):
    """
    Metaclass for our mixin. Makes sure to set table attribute to true.
    Needed for SQLModel.
    """
    def __new__(cls, *args, **kwargs):
        if not args[1][0] == sqlmodel.SQLModel:
            kwargs['table'] = True
        return type(sqlmodel.SQLModel).__new__(cls, *args, **kwargs)


class BaseTableMixin(sqlmodel.SQLModel, metaclass=_BaseTableMixinMeta):
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
