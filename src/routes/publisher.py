from fastapi import APIRouter

from src.database import fake_games as db_games

router = APIRouter(prefix="/publisher", tags=["Publisher"])


@router.get("/")
def get_publishers():
    return db_games.get_games_field("Publisher")
