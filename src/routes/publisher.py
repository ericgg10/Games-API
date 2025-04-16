from fastapi import APIRouter

from src.database import db_session, games_db
from src.models.publisher_model import Publisher

router = APIRouter(prefix="/publisher", tags=["Publisher"])


@router.get("/")
def get_publishers(db: db_session):
    return games_db.get_games_field(db, Publisher)
