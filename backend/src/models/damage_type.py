from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base


class DamageType(Base):
    __tablename__ = "damage_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(default="")
