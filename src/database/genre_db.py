from sqlmodel import Session, select

from src.models.genre_model import Genre


def create_genre(db: Session, game_info: Genre):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info


def delete_genre_by_id(db: Session, id: int):
    query = select(Genre).where(Genre.id == id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


# GET GENRE_BY_ID
def get_genre_by_id(db: Session, genre_id: int):
    return db.get(Genre, genre_id)
