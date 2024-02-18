import copy
import itertools
import json
import operator
import os
from functools import partial
from operator import is_not
from typing import Type, Dict, Iterable

from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

import src.character_sheet.models.expansion as expansion
import src.character_sheet.models.race as race
import src.character_sheet.models.damage_type as damage_type
from src.core.database import BaseRepository
from src.core.map import Map, ListMultiMap
from src.core.models import BaseTableMixin, EntityTableMixin


def read_json(filename: str):
    with open(filename) as f:
        json_str = f.read()
    return json.loads(json_str)


def _truncate_table(session: Session, table: Type[BaseTableMixin]):
    s = text(f"DELETE FROM {table.__tablename__}")
    session.execute(s)


def repopulate_table(json_lst: Iterable[Dict[str, str]], table: Type[BaseTableMixin], truncate=True):
    """
    Takes a list of jsons and saves them to given table. json keys need to map the given column

    :param json_lst: Iterable of json objects with key vals that
    :param table: table we want to insert in
    :param truncate: boolean if we want to truncate te table before repopulating
    :return:
    """
    records = map(lambda obj: table(**obj), json_lst)
    with BaseRepository.get_session(autocommit=False) as session:
        if truncate:
            _truncate_table(session, table)
        session.bulk_save_objects(records)
        session.commit()


def remap_foreign_key(json_lst: Iterable[Dict], column_name: str, table_to: type(SQLModel)):
    """
    Maps name in foreign key to corresponding id
    :param json_lst:
    :param column_name:
    :param table_to:
    :return:
    """
    foreign_objects = Map()
    nw_jsons = []
    with BaseRepository.get_session(autocommit=False) as session:
        def compute_callback(key):
            return session.query(table_to).filter(table_to.name == key).first()

        for json_obj in json_lst:
            nw_json = copy.deepcopy(json_obj)
            if not (n_key := json_obj.get(column_name, False)):
                nw_json[column_name] = None
            else:
                nw_json[column_name] = foreign_objects.compute_if_absent(n_key, compute_callback).id
            nw_jsons.append(nw_json)
    return nw_jsons


def remap_many_to_one(json_list: Iterable[Dict], column_name: str, table_to: type(SQLModel)):
    found_objects = Map()
    with BaseRepository.get_session(autocommit=False) as session:
        callback = lambda key: session.query(table_to).filter(table_to.name == key).first()

        def remap_json_obj(json_obj):
            if column_name not in json_obj.keys():
                return json_obj
            remap_key = lambda foreign_key: found_objects.compute_if_absent(foreign_key, callback)
            json_obj[column_name] = list(filter(partial(is_not, None), map(remap_key, json_obj[column_name])))
            return json_obj

        return list(filter(partial(operator.ne, None), map(remap_json_obj, json_list)))


def update_column(jsons: [{str, (str | int)}], column: [str], table: Type[EntityTableMixin]):
    # json_obj[column] is the new value of our table.
    # We group all the same values to optimize. Preventing to update rows one by one.
    same_column_value = ListMultiMap()
    for json_obj in jsons:
        same_column_value.add(json_obj[column], json_obj["name"])

    with BaseRepository.get_session(autocommit=False) as session:
        for key, val in same_column_value.items():
            session.query(table).filter(table.name.in_(val)).update({column: key})
        session.commit()


def repopulate_expansions():
    json_lst = read_json("expansion.json")
    repopulate_table(json_lst, expansion.Expansion)


def repopulate_damage_type():
    json_lst = read_json("damage_type.json")
    repopulate_table(json_lst, damage_type.DamageType)


def repopulate_races():
    files = map(lambda f: os.path.join("race", f), os.listdir('race'))
    jsons = itertools.chain(*map(read_json, files))
    jsons = remap_foreign_key(jsons, "expansion", expansion.Expansion)
    jsons = remap_many_to_one(jsons, 'resistance', damage_type.DamageType)

    # Build initial table. Without Parent race relation
    repopulate_table(jsons, race.Race)

    # Update the parent race relation
    jsons = remap_foreign_key(jsons, "parent_race", race.Race)
    update_column(jsons, 'parent_race', race.Race)


def main():
    repopulate_expansions()
    repopulate_damage_type()
    repopulate_races()


if __name__ == "__main__":
    main()
