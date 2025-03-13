from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from src.database.fake_games import get_game_by_name, get_games_by_id, is_game_id, get_games_by_genre, get_games_genres, get_games_publisher, get_games_platform, get_games_years, get_games_by_publisher, get_games_by_platform, get_games_by_genre, get_games_by_year, get_games_between_years, get_games_between_eu_sales, get_games_between_na_sales

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
def get_name_games_by_publisher(publisher:str, limit:int=10):
    return get_games_by_publisher(publisher, limit)


@app.get("/games/platform/{platform}")
def get_name_games_by_platform(platform:str, limit:int=10):
    return get_games_by_platform(platform, limit)


@app.get("/games/genre/{genre}")
def get_name_games_by_genre(genre:str, limit:int=10):
    return get_games_by_genre(genre, limit)


@app.get("/games/year/{year}")
def get_name_games_by_year(year:int, limit:int=10):
    return get_games_by_year(year, limit)


@app.get("/games/year/{year_1}/{year_2}")
def get_name_games_between_year(year_1: int, year_2: int, limit:int=10):
    return get_games_between_years(year_1, year_2, limit)


@app.get("/games/eu_sales/{eu_sales_1}/{eu_sales_2}")
def get_name_games_between_eu_sales(eu_sales_1: float, eu_sales_2: float, limit:int=10):
    return get_games_between_eu_sales(eu_sales_1, eu_sales_2, limit)


@app.get("/games/na_sales/{na_sales_1}/{na_sales_2}")
def get_name_games_between_na_sales(na_sales_1: float, na_sales_2: float, limit:int=10):
    return get_games_between_na_sales(na_sales_1, na_sales_2, limit)