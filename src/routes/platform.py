from fastapi import APIRouter

from src.database import db_session, platform_db
from src.database import fake_games as db_games

router = APIRouter(prefix="/platform", tags=["Platform"])


@router.get("/")
def get_platforms():
    return db_games.get_games_field("Platform")


@router.get("/name/{name}")
def get_platform_by_name(name: str, db: db_session):
    return platform_db.get_platform_by_name(db, name)
