import asyncio
from typing import List

from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

import src.character_sheet.models.character_sheet as model
from src.character_sheet.SocketManager import ConnectionManager, SheetUpdateMessage

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
def create_sheet(
        char_sheet: model.CharacterSheetPostSchema = model.CharacterSheetPostSchema()) -> model.CharacterSheet:
    """
    Creates a new empty character sheet. Can be optionally set with starting values from the CharacterSheetPostSchema.
    :param char_sheet: a character sheet with initial values or None.
    :return: values of a newly created character sheet.
    """

    return model.CharacterSheetDao.create(char_sheet)


socket_manager = ConnectionManager()


@router.websocket("/socket/{sheet_id}")
async def websocket_endpoint(websocket: WebSocket, sheet_id: int):
    await socket_manager.connect(websocket, sheet_id)
    try:
        while True:
            data = await websocket.receive_text()
            sheet_message = SheetUpdateMessage.parse_raw(data)
            # TODO: We may want to keep our db session open?
            # TODO: Update and broadcast should be atomic?
            update = model.CharacterSheetDao.update_field(sheet_id, sheet_message.field, sheet_message.data)
            broadcast = socket_manager.broadcast(sheet_message, sheet_id, websocket)
            await asyncio.gather(update, broadcast)
    except WebSocketDisconnect:
        socket_manager.disconnect(websocket, sheet_id)
        # TODO: We have to provide a logger.
        print("Socket disconnected")
