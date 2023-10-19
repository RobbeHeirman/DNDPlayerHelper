from sqlalchemy import create_engine, MetaData, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///../dndplayerhelper.sqlite", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata_obj = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata_obj)


def create_range_constraint(column_name: str, lower_bound: int, upper_bound: int) -> CheckConstraint:
    """
    Creates a CheckConstraint for given column name that numbers need to be between lower_bound and upper_bound
    :param column_name: a string column name.
    :param lower_bound: lower integer bound, lower bound of a range
    :param upper_bound: a upper bound of a range
    :return: representive check constraint
    """
    naming = f"{column_name}_[{lower_bound}, {upper_bound}]"
    return CheckConstraint(f"{column_name} BETWEEN {lower_bound} AND {upper_bound}", name=naming)
