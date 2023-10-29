from pydantic import BaseModel
class SheetUpdateMessage(BaseModel):
    id: int
    field: str
    data: str
