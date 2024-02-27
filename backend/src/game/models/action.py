import enum

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

import src.game.models.game_entity as game
from src.core import models
from src.game.models.damage_type import DamageType


class ActionType(enum.Enum):
    RACE = enum.auto()
    CLASS = enum.auto()
    SPELL = enum.auto()


class ActionUsage(enum.Enum):
    ACTION = enum.auto()
    BONUS_ACTION = enum.auto()


class Recharge(enum.Enum):
    SHORT_REST = enum.auto()
    LONG_REST = enum.auto()


class Ability(enum.Enum):
    STRENGTH = enum.auto()
    DEXTERITY = enum.auto()
    CONSTITUTION = enum.auto()
    INTELLIGENCE = enum.auto()
    WISDOM = enum.auto()


class Action(game.GameEntity):
    description: Mapped[str] = mapped_column(default="")
    action_type: Mapped[ActionType] = mapped_column(Enum(ActionType), nullable=False)
    damage_type: Mapped[int] = models.RelationField(DamageType)
    usage: Mapped[ActionUsage] = mapped_column(Enum(ActionUsage), nullable=False)
    recharge: Mapped[Recharge] = mapped_column(Enum(Recharge), nullable=False)

    saving_throw_type: Mapped[Ability] = mapped_column(Enum(Ability), nullable=False)
    saving_throw_DC_base: Mapped[int] = mapped_column()
    saving_throw_DC_ability_modifier: Mapped[int] = mapped_column(Enum(Ability))
    saving_throw_DC_use_proficiency: Mapped[bool] = mapped_column()
    saving_throw_success_damage_modifier: Mapped[float] = mapped_column()


class ActionDamage(game.GameEntity):
    # From what lvl the dmg applies.
    lvl: Mapped[int] = mapped_column(nullable=False)
    action: Mapped[int] = models.RelationField(Action)

    d4_count: Mapped[int] = mapped_column(default=0)
    d6_count: Mapped[int] = mapped_column(default=0)
    d8_count: Mapped[int] = mapped_column(default=0)
    d10_count: Mapped[int] = mapped_column(default=0)
    d12_count: Mapped[int] = mapped_column(default=0)
    d20_count: Mapped[int] = mapped_column(default=0)
