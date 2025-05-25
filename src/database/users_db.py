from sqlmodel import Session, select

from src.models.users_model import User
from src.utils import get_password_hash


def create_user(db: Session, user_info: User):
    user_info.password = get_password_hash(user_info.password)
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info


def delete_user_by_id(db: Session, id: int):
    query = select(User).where(User.id == id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)


def update_user(db: Session, new_user: User):
    query = select(User).where(User.id == new_user.id)
    old_user = db.exec(query).first()

    old_user.name = new_user.name if new_user.name else old_user.name
    old_user.password = new_user.password if new_user.password else old_user.password
    db.commit()
    db.refresh(old_user)
    return old_user


def get_user_by_username(db: Session, username: str):
    query = select(User).where(User.name == username)
    result = db.exec(query).first()
    return result


def get_all_users(db: Session):
    query = select(User)
    result = db.exec(query).all()
    return result
