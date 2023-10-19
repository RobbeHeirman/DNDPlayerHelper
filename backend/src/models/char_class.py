# from typing import List
#
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from src.database import Base
#
#
# class Class(Base):
#     __tablename__ = "class"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column()
#
#     character_sheets: Mapped[List["Class"]] = relationship()
