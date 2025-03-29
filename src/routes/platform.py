from fastapi import APIRouter

from src.database import fake_games as db_games

router = APIRouter(prefix="/platform", tags=["Platform"])


@router.get("/")
def get_platforms():
    return db_games.get_games_field("Platform")
