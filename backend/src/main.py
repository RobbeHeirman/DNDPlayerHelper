import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import src.character_sheet.routes as char_sheet_routes

origins = [
    "http://127.0.0.1:5173"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(char_sheet_routes.router)


@app.get("/")
def index():
    return {"Hello": "World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    start()
