from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, games_db, genre_db
from src.models.genre_model import Genre, GenreCreate, GenreUpdate

router = APIRouter(prefix="/genre", tags=["Genre"])


@router.get("/")
def get_genres(db: db_session):
    return games_db.get_games_field(db, Genre)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_genre(db: db_session, genre_info: GenreCreate):
    new_genre = Genre(**genre_info.model_dump())
    created_genre = genre_db.create_genre(db, new_genre)
    return created_genre


@router.delete("/id/{id}")
def delete_genre_by_id(db: db_session, id: UUID):
    deleted_genre = genre_db.delete_genre_by_id(db, id)
    return deleted_genre


@router.get("/id/{id}")
def get_genre_by_id(db: db_session, id: UUID):
    genre = genre_db.get_genre_by_id(db, id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Genre not found with id {id}",
        )

    return genre


@router.patch("/")
def update_genre(db: db_session, new_genre: GenreUpdate):
    return genre_db.update_genre(db, new_genre)
