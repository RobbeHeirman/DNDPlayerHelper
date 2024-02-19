# from sqlalchemy.orm import mapped_column, Mapped
#
# import src.core.database as database
# from src.core.models import BaseTableMixin
# #
# #
# class CharacterSheet(BaseTableMixin):
#     __tablename__ = "character_sheet"

#     # Core info
#     character_name: Mapped[str] = mapped_column(default="")
#
#     # lvl: int = Field(default=1, ge=1, le=20)
#     # experience: int = Field(default=0, ge=0)
#     #
#     # # Abilities
#     # strength: int = Field(default=10, ge=0)
#     # dexterity: int = Field(default=10, ge=0)
#     # intelligence: int = Field(default=10, ge=0)
#     # wisdom: int = Field(default=10, ge=0)
#     # charisma: int = Field(default=10, ge=0)
#
#
# class CharacterSheetDao(database.BaseRepository[CharacterSheet]):
#     __model__ = CharacterSheet
#
#     @classmethod
#     async def update_field(cls, pk: int, field: str, data):
#         async with cls.get_async_session() as session:
#             sheet = await session.get(cls.__model__, pk)
#             setattr(sheet, field, data)
#             await session.commit()
