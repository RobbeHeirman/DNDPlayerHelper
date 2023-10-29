from typing import List

from fastapi import APIRouter
from starlette.websockets import WebSocket

import src.character_sheet.models.character_sheet as model
from src.character_sheet.models.sheet_socket_message import SheetUpdateMessage

MAIN_TAG = "character_sheet"
router = APIRouter(
    prefix="/character_sheet",
    tags=[MAIN_TAG]
)


@router.get("/{sheet_id}")
def get_sheet(sheet_id: int):
    return model.CharacterSheetDao.get(sheet_id)


@router.get("/character_sheets")
def get_sheets() -> List[model.CharacterSheet]:
    return model.CharacterSheetDao.get_list()


@router.post("/create_sheet")
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
        sheet_message = SheetUpdateMessage.parse_raw(data)
        model.CharacterSheetDao.update_field(sheet_message.id, sheet_message.field, sheet_message.data)