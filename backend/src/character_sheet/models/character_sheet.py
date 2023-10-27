from src.util.decorators import make_fields_optional
from sqlmodel import Field, SQLModel

import src.database as database


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


class CharacterSheet(CharacterSheetBase, table=True):
    __tablename__ = "character_sheet"
    id: int = Field(primary_key=True, default=None)

    # Core info foreign character_sheet.models
    # class_id: int = Field(ForeignKey(f"{Class.__tablename__}.id"))
    # race_id: int = Field(ForeignKey(f"{Race.__tablename__}.id"))

    def __repr__(self):
        return str(self.id)


class CharacterSheetDao(database.BaseRepository[CharacterSheet]):
    __model__ = CharacterSheet
