from sqlalchemy.orm import Mapped

import src.core.models as models
import src.game.models.expansion as expansion


class GameEntity(models.EntityTableMixin):
    __abstract__ = True
    expansion: Mapped[int] = models.RelationField(expansion.Expansion)
