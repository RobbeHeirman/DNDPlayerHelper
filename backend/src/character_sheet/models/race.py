from pydantic.class_validators import Optional
from sqlmodel import Field

import src.character_sheet.models.expansion as expansion_models
import src.core.models as base_model


class Race(base_model.BaseTableMixin, Table=True):
    __tablename__ = "race"

    name: str = Field()

    expansion: int = Field(foreign_key=expansion_models.Expansion.get_foreign_key_reference())
    parent_race: Optional[int] = Field(foreign_key=expansion_models.Expansion.get_foreign_key_reference())

