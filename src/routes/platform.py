from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, games_db, platform_db
from src.models.platform_model import Platform, PlatformCreate, PlatformUpdate

router = APIRouter(prefix="/platform", tags=["Platform"])


@router.get("/")
def get_platforms(db: db_session):
    return games_db.get_games_field(db, Platform)


@router.get("/name/{name}")
def get_platform_by_name(name: str, db: db_session):
    return platform_db.get_platform_by_name(db, name)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_platform(db: db_session, game_info: PlatformCreate):
    created_platform = platform_db.create_platform(db, game_info)
    return created_platform


@router.delete("/id/{id}")
def delete_platform_by_id(db: db_session, id: UUID):
    deleted_platform = platform_db.delete_platform_by_id(db, id)
    return deleted_platform


@router.get("/id/{id}")
def get_platform_by_id(db: db_session, id: UUID):
    platform = platform_db.get_platform_by_id(db, id)
    if not platform:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Platform not found with id {id}",
        )

    return platform


@router.patch("/")
def update_platform(db: db_session, new_platform: PlatformUpdate):
    return platform_db.update_platform(db, new_platform)
