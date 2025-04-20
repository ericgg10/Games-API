from sqlmodel import Session, SQLModel, select

from src.models.publisher_model import Publisher


# CREATE PUBLISHER
def create_publisher(db: Session, game_info: Publisher):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info


# DELETE PUBLISHER
def delete_publisher_by_id(db: Session, publisher_id):
    query = select(Publisher).where(Publisher.id == publisher_id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


# GET PUBLISHER_BY_ID
def get_publisher_by_id(db: Session, publisher_id: int):
    return db.get(Publisher, publisher_id)
