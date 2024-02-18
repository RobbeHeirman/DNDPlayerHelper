from sqlalchemy import Column, String
from sqlalchemy_utils import ChoiceType
from sqlmodel import Enum, Field

from src.core.models import EntityTableMixin


class ActionType(str, Enum):
    RACE = "race"
    CLASS = "class"
    spell = "spell"


class Action(EntityTableMixin):
    __tablename__ = "action"
    action_type: ActionType = Field(sa_column=Column(ChoiceType(ActionType, impl=String()), nullable=False))
