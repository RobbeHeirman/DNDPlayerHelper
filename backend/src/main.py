from typing import Union

from fastapi import FastAPI
from database import Base, engine, SessionLocal
from models.character_sheet import CharacterSheet

app = FastAPI()
db = SessionLocal()

# db.add(CharacterSheet(id=0))
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
