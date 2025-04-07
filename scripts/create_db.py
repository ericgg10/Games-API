from pathlib import Path

import pandas as pd
from sqlmodel import Session, SQLModel, select

from src.database import engine, platform_db
from src.models.game_model import Game
from src.models.game_sales_model import GameSales
from src.models.genre_model import Genre
from src.models.platform_model import Platform
from src.models.publisher_model import Publisher

database = pd.read_csv("data/games.csv")


# -----FUNCTIONS----------
def create_tables():
    SQLModel.metadata.create_all(engine)


def insert_values():
    with Session(engine) as session:
        for _, row in database.iterrows():
            # Comprobamos si existe el genero y si no existe lo añadimos
            genre = session.exec(select(Genre).filter_by(name=row["Genre"])).first()
            if not genre:
                genre = Genre(name=row["Genre"])
                session.add(genre)
            # Comprobamos si existe el publisher y si no existe lo añadimos
            publisher = session.exec(select(Publisher).filter_by(name=row["Publisher"])).first()
            if not publisher:
                publisher = Publisher(name=row["Publisher"])
                session.add(publisher)
            # Comprobamos si existe la plataforma y si no existe lo añadimos
            platform = session.exec(select(Platform).filter_by(name=row["Platform"])).first()
            if not platform:
                platform = Platform(name=row["Platform"])
                session.add(platform)
            # Insertamos las ventas
            sales = GameSales(
                Na_sales=row["NA_Sales"],
                Eu_sales=row["EU_Sales"],
                Jp_sales=row["JP_Sales"],
                Other_sales=row["Other_Sales"],
                Global_sales=row["Global_Sales"],
            )
            session.add(sales)
            session.flush()
            # Insertamos los juegos
            game = session.exec(select(Game).filter_by(name=row["Name"])).first()
            if not game:
                game = Game(
                    name=row["Name"],
                    year=row["Year"],
                    genre_id=genre.id,
                    publisher_id=publisher.id,
                    platform_id=platform.id,
                    gamesales_id=sales.id,
                )
                session.add(game)
        session.commit()


def execute_querys():
    with Session(engine) as session:
        query = select(Game).where(Game.id == "4")
        result = session.exec(query)
        print(result.all())


def delete_game_by_id(game_id):
    with Session(engine) as session:
        query = select(Game).where(Game.id == game_id)
        result = session.exec(query).first()
        session.delete(result)
        session.commit()


def update_game_year_by_id(game_id, year):
    with Session(engine) as session:
        query = select(Game).where(Game.id == game_id)
        result = session.exec(query).first()
        result.year = year
        session.commit()


def get_games_field(table, column):
    with Session(engine) as session:
        query = select(table)
        result = session.exec(query)
        nombres = []
        for column in result:
            nombres.append(column.name)
        print(nombres)


def get_games_between(column, field_1, field_2):
    with Session(engine) as session:
        query = (
            select(Game.name)
            .join(GameSales, Game.gamesales_id == GameSales.id)
            .where(column >= field_1)
            .where(column <= field_2)
        )
        result = session.exec(query)
        print(result.all())


# -----MAIN-------
def main():
    if not Path("databasegames.db").exists():
        create_tables()
        insert_values()
    execute_querys()
    print("---Get Games Field---")
    print("GENRE")
    get_games_field(Genre, "name")
    print("PUBLISHER")
    get_games_field(Publisher, "name")
    print("PLATFORM")
    get_games_field(Platform, "name")
    print("--------------")
    print("---Get Games Between---")
    print("NA_SALES")
    get_games_between(GameSales.Na_sales, 4.99, 6.6)
    print("EU_SALES")
    get_games_between(GameSales.Eu_sales, 4.99, 6.6)
    print("JP_SALES")
    get_games_between(GameSales.Jp_sales, 4.99, 6.6)
    print("OTHER_SALES")
    get_games_between(GameSales.Other_sales, 0.77, 3.31)
    print("GLOBAL")
    get_games_between(GameSales.Global_sales, 4.99, 6.6)
    with Session(engine) as session:
        platform_db.get_platform_by_name(session, name="Wii")
    # platform_database.create_platform(session, "Prueba")
    # platform_db.delete_platform_by_id(session, 33)


if __name__ == "__main__":
    main()
