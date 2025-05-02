from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, users_db
from src.models.users_model import User, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_session, user_info: User):
    created_user = users_db.create_user(db, user_info)
    return created_user


@router.delete("/id/{id}")
def delete_user_by_id(db: db_session, id: UUID):
    deleted_user = users_db.delete_user_by_id(db, id)
    return deleted_user


@router.get("/id/{id}")
def get_users_by_id(db: db_session, id: UUID):
    user = users_db.get_user_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with id {id}",
        )

    return user


@router.patch("/")
def update_user(db: db_session, new_user: UserUpdate):
    return users_db.update_user(db, new_user)
