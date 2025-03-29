from fastapi import APIRouter

from src.database import fake_games as db_games

router = APIRouter(prefix="/genre", tags=["Genre"])


@router.get("/")
def get_genres():
    return db_games.get_games_field("Genre")
