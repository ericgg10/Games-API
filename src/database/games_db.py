from sqlmodel import Session, SQLModel, select

from src.database import engine
from src.models.game_model import Game
from src.models.game_sales_model import GameSales
from src.models.genre_model import Genre
from src.models.platform_model import Platform
from src.models.publisher_model import Publisher


def get_games_by_id(db: Session, game_id: int):
    return db.get(Game, game_id)


# GET GAMES BY
def get_games_by_field(
    db: Session,
    column: SQLModel,
    field_value: str,
    limit: int = 10,
):
    query = (
        select(Game)
        .join(Publisher, Game.publisher_id == Publisher.id)
        .join(Genre, Game.genre_id == Genre.id)
        .join(Platform, Game.platform_id == Platform.id)
        .where(field_value == column)
        .limit(limit)
    )
    result = db.exec(query)
    return result.all()


# GET GAMES FIELD
def get_games_field(db: Session, table: SQLModel):
    query = select(table)
    result = db.exec(query)
    nombres = []
    for column in result:
        nombres.append(column.name)
    return nombres


# GET GAMES BETWEEN
def get_games_between(db: Session, column, field_1, field_2, limit):
    query = (
        select(Game.name)
        .join(GameSales, Game.gamesales_id == GameSales.id)
        .where(column >= field_1)
        .where(column <= field_2)
        .limit(limit)
    )
    result = db.exec(query)
    return result.all()


# DELETE GAME
def delete_game_by_id(db: Session, game_id):
    query = select(Game).where(Game.id == game_id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


# CREATE GAME
def create_game(db: Session, game_info: Game):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info


def update_game(db: Session, new_game: Game):
    query = select(Game).where(Game.id == new_game.id)
    old_game = db.exec(query).first()
    old_game.name = new_game.name if new_game.name else old_game.name
    old_game.year = new_game.year if new_game.year else old_game.year
    old_game.genre_id = new_game.genre_id if new_game.genre_id else old_game.genre_id
    old_game.platform_id = new_game.platform_id if new_game.platform_id else old_game.platform_id

    db.commit()
    db.refresh(old_game)
    return old_game
