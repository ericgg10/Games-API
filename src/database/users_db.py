from sqlmodel import Session, select

from src.models.users_model import User


def create_user(db: Session, user_info: User):
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info
