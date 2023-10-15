from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from src.database import Base

class CharacterSheet(Base):
    __tablename__ = "CharacterSheet"

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return str(self.id)
