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


def update_games_sales(db: Session, new_games_sales: GameSales):
    query = select(GameSales).where(GameSales.id == new_games_sales.id)
    old_games_sales = db.exec(query).first()

    old_games_sales.Na_sales = (
        new_games_sales.Na_sales if new_games_sales.Na_sales else old_games_sales.Na_sales
    )
    old_games_sales.Eu_sales = (
        new_games_sales.Eu_sales if new_games_sales.Eu_sales else old_games_sales.Eu_sales
    )
    old_games_sales.Jp_sales = (
        new_games_sales.Jp_sales if new_games_sales.Jp_sales else old_games_sales.Jp_sales
    )
    old_games_sales.Other_sales = (
        new_games_sales.Other_sales if new_games_sales.Other_sales else old_games_sales.Other_sales
    )
    old_games_sales.Global_sales = (
        new_games_sales.Global_sales
        if new_games_sales.Global_sales
        else old_games_sales.Global_sales
    )

    db.commit()
    db.refresh(old_games_sales)
    return old_games_sales
