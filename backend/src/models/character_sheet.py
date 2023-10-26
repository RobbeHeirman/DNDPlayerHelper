from sqlmodel import Field, SQLModel

from models.util.decorators import make_fields_optional


class CharacterSheetBase(SQLModel):
    # Core info
    character_name: str = Field(default="")

    lvl: int = Field(default=1)
    experience: int = Field(default=0)

    # Abilities
    strength: int = Field(default=10)
    dexterity: int = Field(default=10)
    intelligence: int = Field(default=10)
    wisdom: int = Field(default=10)
    charisma: int = Field(default=10)


@make_fields_optional
class CharacterSheetPostSchema(CharacterSheetBase):
    pass


class CharacterSheetTable(CharacterSheetBase, table=True):
    __tablename__ = "character_sheet"
    id: int = Field(primary_key=True, default=None)
    # Core info foreign models
    # class_id: int = Field(ForeignKey(f"{Class.__tablename__}.id"))
    # race_id: int = Field(ForeignKey(f"{Race.__tablename__}.id"))

    def __repr__(self):
        return str(self.id)



test = CharacterSheetBase()
