from fastapi import APIRouter

from src.database import db_session, games_db
from src.models.genre_model import Genre

router = APIRouter(prefix="/genre", tags=["Genre"])


@router.get("/")
def get_genres(db: db_session):
    return games_db.get_games_field(db, Genre)
