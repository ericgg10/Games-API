from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from src.database import get_game_by_name, get_games_by_id, is_game_id

app = FastAPI()


@app.get("/")
def example():
    return {"message": "Hello World"}


@app.get("/games/id/{id}")
def get_game(id: int):
    if not is_game_id(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with id {id}",
        )

    return get_games_by_id(id)


@app.get("/games/name/{name}")
def get_name(name: str):
    return get_game_by_name(name)
