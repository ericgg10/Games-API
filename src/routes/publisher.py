from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.auth import validate_token
from src.database import db_session, games_db, publisher_db
from src.models.publisher_model import Publisher, PublisherCreate, PublisherUpdate

router = APIRouter(prefix="/publisher", tags=["Publisher"])


@router.get("/")
def get_publishers(token: validate_token, db: db_session):
    return games_db.get_games_field(db, Publisher)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_publisher(token: validate_token, db: db_session, publisher_info: PublisherCreate):
    new_publisher = Publisher(**publisher_info.model_dump())
    created_publisher = publisher_db.create_publisher(db, new_publisher)
    return created_publisher


@router.delete("/id/{id}")
def delete_publisher_by_id(token: validate_token, db: db_session, id: UUID):
    deleted_publisher = publisher_db.delete_publisher_by_id(db, id)
    return deleted_publisher


@router.get("/id/{id}")
def get_publisher_by_id(token: validate_token, db: db_session, id: UUID):
    publisher = publisher_db.get_publisher_by_id(db, id)
    if not publisher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Publisher not found with id {id}",
        )

    return publisher


@router.patch("/")
def update_publisher(token: validate_token, db: db_session, new_publisher: PublisherUpdate):
    return publisher_db.update_publisher(db, new_publisher)
