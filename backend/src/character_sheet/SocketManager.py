import asyncio

from pydantic import BaseModel
from starlette.websockets import WebSocket


class SheetUpdateMessage(BaseModel):
    # TODO: We may want to write a validator that checks if field is part of the SheetModel.
    field: str
    data: str


class ConnectionManager:
    """
    Manages sheet connections.
    A socket can be connected, disconnected and can broadcast messages through the manager.
    """
    def __init__(self):
        self.active_connections: {int: [WebSocket]} = {}

    async def connect(self, websocket: WebSocket, sheet_id) -> None:
        await websocket.accept()
        self.active_connections.setdefault(sheet_id, []).append(websocket)

    def disconnect(self, websocket: WebSocket, sheet_id: int) -> None:
        self.active_connections.get(sheet_id).remove(websocket)

    async def broadcast(self, message: SheetUpdateMessage, sheet_id: int, source_socket: WebSocket) -> None:
        encoded_msg = message.json()
        sockets = filter(lambda socket: socket != source_socket, self.active_connections[sheet_id])
        promises = map(lambda socket: socket.send_text(encoded_msg), sockets)
        await asyncio.gather(*promises)
