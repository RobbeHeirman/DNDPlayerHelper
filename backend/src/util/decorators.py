from typing import Optional, TypeVar

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


if __name__ == "__main__":
    class Base:
        field: int


    @make_fields_optional
    class Test(Base):
        field2: str


    print(Test.__annotations__)
