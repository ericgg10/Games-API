from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, users_db
from src.models.users_model import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_session, user_info: User):
    created_user = users_db.create_user(db, user_info)
    return created_user


@router.delete("/id/{id}")
def delete_user_by_id(db: db_session, id: int):
    deleted_user = users_db.delete_user_by_id(db, id)
    return deleted_user
