from sqlmodel import Field

import src.core.models as base_model

print("Im ran twice?")

class Expansion(base_model.BaseTableMixin):
    __tablename__ = "expansion"

    name: str = Field()