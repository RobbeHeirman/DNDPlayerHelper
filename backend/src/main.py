import os.path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

import src.character_sheet.routes as char_sheet_routes

origins = [
    "http://127.0.0.1:5173",
    "http://localhost"
]


def custom_generate_unique_id(route: APIRoute):
    tag = route.tags[0] if route.tags else ""
    return f"{tag}-{route.name}"


app = FastAPI(servers=[{"url": "http://localhost:8000", "description": "development"}],generate_unique_id_function=custom_generate_unique_id)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(char_sheet_routes.router)

path = os.path.dirname(os.path.realpath(__file__))
app.mount("/", StaticFiles(directory=os.path.join(path, "../static"), html=True), name="static")


@app.get("/")
def index():
    return {"Hello": "World"}


def start(host="localhost", port=8000):
    """Launched with `poetry run start` at root level"""
    uvicorn.run("src.main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    start()
