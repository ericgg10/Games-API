from fastapi import APIRouter

from src.database import db_session, games_db, platform_db
from src.models.platform_model import Platform

router = APIRouter(prefix="/platform", tags=["Platform"])


@router.get("/")
def get_platforms(db: db_session):
    return games_db.get_games_field(db, Platform)


@router.get("/name/{name}")
def get_platform_by_name(name: str, db: db_session):
    return platform_db.get_platform_by_name(db, name)
