from sqlmodel import Field

import src.core.models as base_model


class Ability(base_model.EntityTableMixin):
    __tablename__ = "ability"
    ability_type = Field()  # Breath Weapon, Spells ??
