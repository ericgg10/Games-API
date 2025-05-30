from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.auth import validate_token

# from src.database import fake_games as db_games
from src.database import db_session, games_sales_db
from src.models.game_sales_model import GameSales, GameSalesCreate, GameSalesUpdate

router = APIRouter(prefix="/game-sales", tags=["GameSales"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_game_sales(token: validate_token, db: db_session, game_sales_info: GameSalesCreate):
    new_game_sales = GameSales(**game_sales_info.model_dump())
    created_sales = games_sales_db.create_game_sales(db, new_game_sales)
    return created_sales


@router.delete("/id/{id}")
def delete_game_sales_by_id(token: validate_token, db: db_session, id: UUID):
    deleted_game_sales = games_sales_db.delete_game_sales_by_id(db, id)
    return deleted_game_sales


@router.get("/id/{id}")
def get_game_sales(token: validate_token, db: db_session, id: UUID):
    game_sales = games_sales_db.get_games_sales_by_id(db, id)
    if not game_sales:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game Sales not found with id {id}",
        )

    return game_sales


@router.patch("/")
def update_games_sales(token: validate_token, db: db_session, new_games_sales: GameSalesUpdate):
    return games_sales_db.update_games_sales(db, new_games_sales)
