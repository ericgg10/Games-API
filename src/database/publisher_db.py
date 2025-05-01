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


def update_publisher(db: Session, new_publisher: Publisher):
    query = select(Publisher).where(Publisher.id == new_publisher.id)
    old_publisher = db.exec(query).first()

    old_publisher.name = new_publisher.name if new_publisher.name else old_publisher.name
    db.commit()
    db.refresh(old_publisher)
    return old_publisher
