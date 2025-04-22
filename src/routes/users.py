from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.database import db_session, users_db
from src.models.users_model import User

router = APIRouter(prefix="/users", tags=["Users"])
