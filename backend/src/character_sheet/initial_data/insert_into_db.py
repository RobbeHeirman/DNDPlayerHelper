import itertools
import json
import os
from typing import Type, Dict, Iterable

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

import src.character_sheet.models.expansion as expansion
import src.character_sheet.models.race as race
from src.core.database import BaseRepository
from src.core.map import Map
from src.core.models import BaseTableMixin


def read_json(filename: str):
    with open(filename) as f:
        json_str = f.read()
    return json.loads(json_str)


def _truncate_table(session: Session, table: Type[BaseTableMixin]):
    s = text(f"DELETE FROM {table.__tablename__}")
    session.execute(s)


def repopulate_table(json_lst: Iterable[Dict[str, str]], table: Type[BaseTableMixin], truncate=True):
    records = list(map(lambda obj: table(**obj), json_lst))
    with BaseRepository.get_session(autocommit=False) as session:
        if truncate:
            _truncate_table(session, table)
        session.bulk_save_objects(records)
        session.commit()


def remap_foreign_key(json_lst: Iterable[Dict], column_name: str, table_to: type(SQLModel)):
    foreign_objects = Map()
    nw_jsons = []
    with BaseRepository.get_session(autocommit=False) as session:
        def compute_callback(key):
            return session.query(table_to).filter(table_to.name == key).first()

        for json_obj in json_lst:
            if not (n_key := json_obj.get(column_name, False)):
                json_obj[column_name] = None
                nw_jsons.append(json_obj)
                continue
            foreign_object = foreign_objects.compute_if_absent(n_key, compute_callback)
            json_obj[column_name] = foreign_object.id
            nw_jsons.append(json_obj)
        return nw_jsons


def update_column(jsons: [{str, (str | int)}], column: [str], table: Type[BaseTableMixin]):
    # json_obj[column] is the new value of our table.
    same_column_value = Map()

    def callback(_):
        return []

    for json_obj in jsons:
        same_column_value.compute_if_absent(json_obj[column], callback).append(json_obj["name"])

    with BaseRepository.get_session(autocommit=False) as session:
        for key, val in same_column_value.items():
            session.query(table).filter(table.name.in_(val)).update({column: key})
        session.commit()


def repopulate_expansions():
    json_lst = read_json("expansion.json")
    repopulate_table(json_lst, expansion.Expansion)


def repopulate_races():
    files = map(lambda f: os.path.join("race", f), os.listdir('race'))
    jsons = itertools.chain(*map(read_json, files))
    jsons = remap_foreign_key(jsons, "expansion", expansion.Expansion)

    # Build initial table. Without Parent race relation
    repopulate_table(jsons, race.Race)

    # Update the parent race relation
    jsons = remap_foreign_key(jsons, "parent_race", race.Race)
    update_column(jsons, 'parent_race', race.Race)


def main():
    repopulate_races()


if __name__ == "__main__":
    main()
