from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base
import src.models.character_sheet as char_sheet


class CharacterResistance(Base):
    __tablename__ = "character_resistance"

    id: Mapped[int] = mapped_column(primary_key=True)
    character_sheet_id: Mapped[int] = mapped_column(ForeignKey(f"{char_sheet.CharacterSheet.__tablename__}.id"))
