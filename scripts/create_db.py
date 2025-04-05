from pathlib import Path

import pandas as pd
from sqlmodel import Session, SQLModel, select

from src.database import engine, platform_database
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


# -----MAIN-------
def main():
    if not Path("databasegames.db").exists():
        create_tables()
        insert_values()
    execute_querys()
    with Session(engine) as session:
        platform_database.get_platform_by_name(session, name="Wii")
        # platform_database.create_platform(session, "Prueba")
        platform_database.delete_platform_by_id(session, 33)


if __name__ == "__main__":
    main()
