from sqlmodel import Session, SQLModel, select

from src.models.game_sales_model import GameSales


# CREATE GAME-SALES
def create_game_sales(db: Session, game_info: GameSales):
    db.add(game_info)
    db.commit()
    db.refresh(game_info)
    return game_info
