from fastapi import APIRouter, status

from src.database import db_session, games_db, publisher_db
from src.models.publisher_model import Publisher

router = APIRouter(prefix="/publisher", tags=["Publisher"])


@router.get("/")
def get_publishers(db: db_session):
    return games_db.get_games_field(db, Publisher)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_game_sales(db: db_session, game_info: Publisher):
    created_publisher = publisher_db.create_publisher(db, game_info)
    return created_publisher


@router.delete("/id/{id}")
def delete_publisher_by_id(db: db_session, id: int):
    deleted_publisher = publisher_db.delete_publisher_by_id(db, id)
    return deleted_publisher
