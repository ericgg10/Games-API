from uuid import UUID

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, users_db
from src.models.users_model import User, UserCreate, UserPublic, UserUpdate
from src.utils import get_password_hash, verify_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_session, user_info: UserCreate):
    new_user = User(**user_info.model_dump(), role=0)
    created_user = users_db.create_user(db, new_user)
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


@router.get("/name/{name}")
def get_users_by_username(db: db_session, name: str):
    user = users_db.get_user_by_username(db, name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with name {name}",
        )

    return user


@router.get("/", response_model=list[UserPublic])
def get_all_users(db: db_session):
    return users_db.get_all_users(db)


@router.patch("/name/{name}")
def change_user_password(
    db: db_session,
    name: str,
    old_password: str,
    new_password_1: str,
    new_password_2: str,
):
    user = users_db.get_user_by_username(db, name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found with name {name}",
        )
    if not verify_password(old_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña anterior es incorrecta",
        )
    if old_password == new_password_1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña nueva es igual que la contraseña anterior",
        )
    if new_password_1 != new_password_2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Las nuevas contraseñas no coinciden",
        )

    user.password = get_password_hash(new_password_1)
    user = users_db.update_user(db, user)
    return {"content": user, "message": "password update successfully"}
