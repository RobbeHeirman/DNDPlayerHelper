from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

import src.database
from src.models.char_class import Class
from src.models.race import Race


class CharacterSheet(src.database.Base):
    __tablename__ = "character_sheet"

    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(default="")

    # Core info
    lvl: Mapped[int] = mapped_column(default=1)
    experience: Mapped[int] = mapped_column(default=0)

    # Abilities
    strength: Mapped[int] = mapped_column(default=10)
    dexterity: Mapped[int] = mapped_column(default=10)
    intelligence: Mapped[int] = mapped_column(default=10)
    wisdom: Mapped[int] = mapped_column(default=10)
    charisma: Mapped[int] = mapped_column(default=10)

    # Core info foreign models
    class_id: Mapped[int] = mapped_column(ForeignKey(f"{Class.__tablename__}.id"))
    race_id: Mapped[int] = mapped_column(ForeignKey(f"{Race.__tablename__}.id"))

    def __repr__(self):
        return str(self.id)
