from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import fake_games as db_games

router = APIRouter(prefix="/games", tags=["Games"])


@router.get("/id/{id}")
def get_game(id: int):
    limit = 1
    if not db_games.is_game_id(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with id {id}",
        )

    return db_games.get_games_by_field_num("Rank", id, limit)


@router.get("/name/{name}")
def get_name(name: str):
    limit = 1
    game = db_games.get_games_by_field("Name", name, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Name {name}",
        )
    return db_games.get_games_by_field("Name", name, limit)


@router.get("/publisher/{publisher}")
def get_name_games_by_publisher(publisher: str, limit: int = 10):
    game = db_games.get_games_by_field("Publisher", publisher, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Publisher {publisher}",
        )

    return db_games.get_games_by_field("Publisher", publisher, limit)


@router.get("/platform/{platform}")
def get_name_games_by_platform(platform: str, limit: int = 10):
    game = db_games.get_games_by_field("Platform", platform, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Platform {platform}",
        )
    return db_games.get_games_by_field("Platform", platform, limit)


@router.get("/genre/{genre}")
def get_name_games_by_genre(genre: str, limit: int = 10):
    game = db_games.get_games_by_field("Genre", genre, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Genre {genre}",
        )
    return db_games.get_games_by_field("Genre", genre, limit)


@router.get("/year/{year}")
def get_name_games_by_year(year: int, limit: int = 10):
    game = db_games.get_games_by_field_num("Year", year, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Year {year}",
        )
    return db_games.get_games_by_field_num("Year", year, limit)


# GET GAMES
@router.get("/year/")
def get_years():
    return db_games.get_games_field("Year")


# GET GAMES BETWEEN
@router.get("/year/{year_1}/{year_2}")
def get_name_games_between_year(year_1: int, year_2: int, limit: int = 10):
    if year_2 <= year_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return db_games.get_games_between_int("Year", year_1, year_2, limit)


@router.get("/eu_sales/{eu_sales_1}/{eu_sales_2}")
def get_name_games_between_eu_sales(eu_sales_1: float, eu_sales_2: float, limit: int = 10):
    if eu_sales_2 <= eu_sales_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return db_games.get_games_between_float("EU_Sales", eu_sales_1, eu_sales_2, limit)


@router.get("/na_sales/{na_sales_1}/{na_sales_2}")
def get_name_games_between_na_sales(na_sales_1: float, na_sales_2: float, limit: int = 10):
    if na_sales_2 <= na_sales_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return db_games.get_games_between_float("NA_Sales", na_sales_1, na_sales_2, limit)
