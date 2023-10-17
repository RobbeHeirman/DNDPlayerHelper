from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.race import Race
from src.database import Base
from src.models.char_class import Class


class CharacterSheet(Base):
    __tablename__ = "character_sheet"

    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(default="")

    # Core info
    lvl: Mapped[int] = mapped_column(default=1)

    # Core info foreign models
    class_id: Mapped[int] = mapped_column(ForeignKey(f"{Class.__tablename__}.id"))
    race_id: Mapped[int] = mapped_column(ForeignKey(f"{Race.__tablename__}.id"))

    def __repr__(self):
        return str(self.id)
