from abc import abstractmethod
from typing import Optional, TypeVar

from sqlmodel import SQLModel, Field


class _BaseTableMixinMeta(type(SQLModel)):
    def __new__(cls, *args, **kwargs):
        if args[0] != "BaseModel":
            kwargs['table'] = True
        return type(SQLModel).__new__(cls, *args, **kwargs)


class BaseTableMixin(SQLModel, metaclass=_BaseTableMixinMeta):
    id: int = Field(primary_key=True, default=None)

    @property
    @abstractmethod
    def __tablename__(self) -> str:
        ...

    @classmethod
    def get_foreign_key_reference(cls: SQLModel):
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
