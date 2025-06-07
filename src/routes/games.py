from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.auth import validate_token

# from src.database import fake_games as db_games
from src.database import db_session, games_db
from src.models.game_model import Game, GameCreate, GamePublic, GameUpdate
from src.models.game_sales_model import GameSales
from src.models.genre_model import Genre
from src.models.platform_model import Platform
from src.models.publisher_model import Publisher

router = APIRouter(prefix="/games", tags=["Games"])


@router.get("/id/{id}")
def get_game(db: db_session, id: UUID, token: validate_token):
    game = games_db.get_games_by_id(db, id)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with id {id}",
        )

    return game


@router.get("/", response_model=list[GamePublic])
def get_all_games(
    token: validate_token,
    db: db_session,
    page_size: int = 50,
    page_index: int = 0,
):
    return games_db.get_public_game(db, page_size, page_index)


@router.get("/name/{name}", response_model=list[GamePublic])
def get_game_by_name(db: db_session, name: str, token: validate_token):
    game = games_db.get_games_by_field(db, Game.name, name, limit=1)
    print(game)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Name {name}",
        )
    return game


@router.get("/publisher/{publisher}", response_model=list[GamePublic])
def get_name_games_by_publisher(token: validate_token, db: db_session, publisher: str, limit=10):
    game = games_db.get_games_by_field(db, Publisher.name, publisher, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Publisher {publisher}",
        )
    return game


@router.get("/platform/{platform}")
def get_name_games_by_platform(
    token: validate_token, db: db_session, platform: str, limit: int = 10
):
    game = games_db.get_games_by_field(db, Platform.name, platform, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Platform {platform}",
        )
    return game


@router.get("/genre/{genre}")
def get_name_games_by_genre(token: validate_token, db: db_session, genre: str, limit: int = 10):
    game = games_db.get_games_by_field(db, Genre.name, genre, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Genre {genre}",
        )
    return game


@router.get("/year/{year}")
def get_name_games_by_year(token: validate_token, db: db_session, year: int, limit: int = 10):
    game = games_db.get_games_by_field(db, Game.year, year, limit)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game not found with Year {year}",
        )
    return game


#     return game


# # GET GAMES BETWEEN
@router.get("/year/{year_1}/{year_2}")
def get_name_games_between_year(
    token: validate_token,
    db: db_session,
    year_1: int,
    year_2: int,
    limit: int = 10,
):
    if year_2 <= year_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return games_db.get_games_between(db, Game.year, year_1, year_2, limit)


@router.get("/eu_sales/{eu_sales_1}/{eu_sales_2}")
def get_name_games_between_eu_sales(
    token: validate_token,
    db: db_session,
    eu_sales_1: float,
    eu_sales_2: float,
    limit: int = 10,
):
    if eu_sales_2 <= eu_sales_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return games_db.get_games_between(db, GameSales.Eu_sales, eu_sales_1, eu_sales_2, limit)


@router.get("/na_sales/{na_sales_1}/{na_sales_2}")
def get_name_games_between_na_sales(
    token: validate_token,
    db: db_session,
    na_sales_1: float,
    na_sales_2: float,
    limit: int = 10,
):
    if na_sales_2 <= na_sales_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters.",
        )
    return games_db.get_games_between(db, GameSales.Na_sales, na_sales_1, na_sales_2, limit)


@router.delete("/id/{id}")
def delete_game_by_id(db: db_session, id: UUID, token: validate_token):
    deleted_game = games_db.delete_game_by_id(db, id)
    return deleted_game


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_game(db: db_session, game_info: GameCreate, token: validate_token):
    new_game = Game(**game_info.model_dump())
    created_game = games_db.create_game(db, new_game)
    return created_game


@router.patch("/")
def update_game(db: db_session, new_game: GameUpdate, token: validate_token):
    return games_db.update_game(db, new_game)
