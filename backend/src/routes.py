from fastapi import APIRouter
from sqlmodel import Session

import models.character_sheet as char_sheet_schemas
import src.database as database
router = APIRouter(
    prefix="/character_sheet"
)


@router.get("/")
def read_root():
    print("print called?")
    return {"TODO": "Character sheet overview"}


@router.get("/{sheet_id}")
def read_item(sheet_id: int):
    return {"sheet_id": sheet_id}


@router.post("/create_sheet")
def create_sheet(char_sheet: char_sheet_schemas.CharacterSheetPostSchema) -> char_sheet_schemas.CharacterSheetTable:
    with database.get_setssion() as session:
        db_sheet = char_sheet_schemas.CharacterSheetTable.from_orm(char_sheet)
        session.add(db_sheet)
        session.commit()
        session.refresh(db_sheet)
        return db_sheet
