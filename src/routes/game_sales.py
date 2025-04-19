from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

# from src.database import fake_games as db_games
from src.database import db_session, games_sales_db
from src.models.game_sales_model import GameSales

router = APIRouter(prefix="/game-sales", tags=["GameSales"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_sales(db: db_session, game_info: GameSales):
    created_sales = games_sales_db.create_game_sales(db, game_info)
    return created_sales
