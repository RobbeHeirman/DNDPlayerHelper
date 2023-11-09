from pydantic.class_validators import Optional
from sqlmodel import Field

from src.character_sheet.models.expansion import Expansion
from src.core.models import BaseTableMixin


class Race(BaseTableMixin, Table=True):
    __tablename__ = "race"

    name: str = Field()

    expansion: int = Field(foreign_key=Expansion.get_foreign_key_reference())
    parent_race: Optional[int] = Field(foreign_key=Expansion.get_foreign_key_reference())

