import enum

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
import src.game.models.game_entity as game

class ActionType(enum.Enum):
    RACE = enum.auto()
    CLASS = enum.auto()
    SPELL = enum.auto()


class Action(game.GameEntity):
    description: Mapped[str] = mapped_column(default="")
    action_type: Mapped[ActionType] = mapped_column(Enum(ActionType), nullable=False)

    # damage_type =

