from typing import List

from fastapi import APIRouter
from starlette.websockets import WebSocket

import src.character_sheet.models.character_sheet as model

router = APIRouter(
    prefix="/character_sheet"
)

MAIN_TAG = "character_sheet"

# @router.get("/{sheet_id}")
# async def read_item(sheet_id: int):
#     return {"sheet_id": sheet_id}
#

@router.get("/character_sheets", tags=[MAIN_TAG])
def get_sheets() -> List[model.CharacterSheet]:
    return model.CharacterSheetDao.get_list()


@router.post("/create_sheet", tags=[MAIN_TAG])
def create_sheet(char_sheet: model.CharacterSheetPostSchema = model.CharacterSheetPostSchema()) -> model.CharacterSheet:
    """
    Creates a new empty character sheet. Can be optionally set with starting values from the CharacterSheetPostSchema.
    :param char_sheet: a character sheet with initial values or None.
    :return: values of a newly created character sheet.
    """
    return model.CharacterSheetDao.create(char_sheet)

@router.websocket("/socket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")