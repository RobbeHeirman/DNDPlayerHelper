from pydantic.class_validators import Optional
from sqlmodel import Field

import src.character_sheet.models.expansion as expansion_models
import src.core.models as base_model


class Race(base_model.EntityTableMixin, Table=True):
    __tablename__ = "race"

    expansion: int = Field(foreign_key=expansion_models.Expansion.get_foreign_key_reference(), index=True)
    parent_race: Optional[int] = Field(foreign_key=expansion_models.Expansion.get_foreign_key_reference(), index=True)

    # Ability score increases:
    strength_modifier: int = Field(default=0)
    dexterity_modifier: int = Field(default=0)
    intellect_modifier: int = Field(default=0)
    wisdom_modifier: int = Field(default=0)
    charisma_modifier: int = Field(default=0)
