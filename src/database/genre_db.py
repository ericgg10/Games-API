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


def update_genre(db: Session, new_genre: Genre):
    query = select(Genre).where(Genre.id == new_genre.id)
    old_genre = db.exec(query).first()

    old_genre.name = new_genre.name if new_genre.name else old_genre.name
    db.commit()
    db.refresh(old_genre)
    return old_genre
