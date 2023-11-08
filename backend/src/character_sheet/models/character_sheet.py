from typing import Optional

from sqlmodel import Field, SQLModel

import src.core.database as database
from src.core.models import BaseTableMixin, make_fields_optional


class CharacterSheetBase(SQLModel):
    # Core info
    character_name: str = Field(default="")

    lvl: int = Field(default=1, ge=1, le=20)
    experience: int = Field(default=0, ge=0)

    # Abilities
    strength: int = Field(default=10, ge=0)
    dexterity: int = Field(default=10, ge=0)
    intelligence: int = Field(default=10, ge=0)
    wisdom: int = Field(default=10, ge=0)
    charisma: int = Field(default=10, ge=0)


@make_fields_optional
class CharacterSheetPostSchema(CharacterSheetBase):
    pass


class CharacterSheet(CharacterSheetBase, BaseTableMixin):
    __tablename__ = "character_sheet"

    def __repr__(self):
        return str(self.id)


class CharacterSheetDao(database.BaseRepository[CharacterSheet]):
    __model__ = CharacterSheet

    @classmethod
    async def update_field(cls, pk: int, field: str, data):
        with database.get_session() as session:
            sheet = session.query(cls.__model__).get(pk)
            setattr(sheet, field, data)
            session.commit()
