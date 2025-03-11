from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from src.database.fake_games import get_game_by_name, get_games_by_id, is_game_id, get_games_by_genre, get_games_genres, get_games_publisher, get_games_platform, get_games_years, get_games_by_publisher, get_games_by_platform, get_games_by_genre, get_games_by_year

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


@app.get("/games/genre/")
def get_genres():
    return get_games_genres()


@app.get("/games/publisher/")
def get_publishers():
    return get_games_publisher()


@app.get("/games/platform/")
def get_platforms():
    return get_games_platform()


@app.get("/games/year/")
def get_years():
    return get_games_years()


@app.get("/games/publisher/{publisher}")
def get_name_games_by_publisher(publisher:str):
    return get_games_by_publisher(publisher)


@app.get("/games/platform/{platform}")
def get_name_games_by_platform(platform:str):
    return get_games_by_platform(platform)


@app.get("/games/genre/{genre}")
def get_name_games_by_genre(genre:str):
    return get_games_by_genre(genre)


@app.get("/games/year/{year}")
def get_name_games_by_year(year:int):
    return get_games_by_year(year)

