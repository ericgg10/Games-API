from sqlmodel import Session, SQLModel, select

from src.models.game_sales_model import GameSales


# CREATE GAME-SALES
def create_game_sales(db: Session, game_info: GameSales):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info


# DELETE GAME-SALES
def delete_game_sales_by_id(db: Session, game_sales_id):
    query = select(GameSales).where(GameSales.id == game_sales_id)
    result = db.exec(query).first()
    db.delete(result)
    db.commit()
    return result


# GET GAME_SALES_BY_ID
def get_games_sales_by_id(db: Session, game_id: int):
    return db.get(GameSales, game_id)
