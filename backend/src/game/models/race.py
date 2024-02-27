from sqlalchemy.orm import Mapped, mapped_column

from src.game.models.game_entity import GameEntity


class Race(GameEntity):
    parent_race: Mapped[int] = mapped_column(foreign_key='race.id', nullable=True)

    # Ability score increases:
    strength_modifier: Mapped[int] = mapped_column(default=0)
    dexterity_modifier: Mapped[int] = mapped_column(default=0)
    intellect_modifier: Mapped[int] = mapped_column(default=0)
    wisdom_modifier: Mapped[int] = mapped_column(default=0)
    charisma_modifier: Mapped[int] = mapped_column(default=0)
