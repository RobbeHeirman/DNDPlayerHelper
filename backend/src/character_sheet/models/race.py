# from pydantic.class_validators import Optional
# from sqlmodel import Field
#
# from src.character_sheet.models.expansion import Expansion
# from src.core.models import BaseModel
#
#
# class Race(BaseModel):
#     __tablename__ = "race"
#
#     name: str = Field()
#
#     set: int = Field(foreign_key=Expansion.get_foreign_key_reference())
#     parent_race: Optional[int] = Field(foreign_key=Expansion.get_foreign_key_reference())
