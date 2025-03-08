from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from src.database.fake_games import get_game_by_name, get_games_by_id, is_game_id, get_games_by_genre

app = FastAPI()


@app.get("/")
def example():
    return {"message": "Hello Eric"}


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

@app.get("/games/genre/{genre}")
def get_genre(genre: str):
    return get_games_by_genre(genre)
