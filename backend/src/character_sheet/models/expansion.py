from sqlmodel import Field

from src.core.models import BaseTableMixin


class Expansion(BaseTableMixin):
    __tablename__ = "expansion"

    name: str = Field()
