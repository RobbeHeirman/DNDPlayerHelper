import json
from typing import Type

from sqlalchemy import text

from character_sheet.models.expansion import Expansion
from src.core.database import BaseRepository
from src.core.models import BaseTableMixin


def read_json(filename: str):
    with open(filename) as f:
        json_str = f.read()
    return json.loads(json_str)


def repopulate_table(file: str, table: Type[BaseTableMixin]):
    records = list(map(lambda obj: table(**obj), read_json(file)))
    with BaseRepository.get_session(autocommit=False) as session:
        s = text(f"DELETE FROM {table.__tablename__}")
        session.execute(s)
        session.bulk_save_objects(records)
        session.commit()


def main():
    pop_data = [
        ("expansion.json", Expansion)
    ]
    for pop in pop_data:
        repopulate_table(*pop)

if __name__ == "__main__":
    main()
