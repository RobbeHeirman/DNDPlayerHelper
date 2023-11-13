import src.core.models as models
import src.character_sheet.models.race as race
import src.character_sheet.models.damage_type as damage_type


class RaceResistance(models.base_relation_table_factory(race.Race, damage_type.DamageType, relation1_args={"index": True})):
    __tablename__ = "race_resistance"
