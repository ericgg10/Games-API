from sqlmodel import Session, select

from src.models.users_model import User


def create_user(db: Session, user_info: User):
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
