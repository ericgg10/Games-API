from pathlib import Path

import pandas as pd
from sqlmodel import Field, Session, SQLModel, create_engine, select

from src.database import games_db

database = pd.read_csv("data/games.csv")


# -----TABLES----------
class Game(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    year: int | None
    genre_id: int = Field(foreign_key="genre.id")
    publisher_id: int = Field(foreign_key="publisher.id")
    platform_id: int = Field(foreign_key="platform.id")
    gamesales_id: int = Field(foreign_key="gamesales.id")


class GameSales(SQLModel, table=True):
    id: int = Field(primary_key=True)
    Na_sales: float
    Eu_sales: float
    Jp_sales: float
    Other_sales: float
    Global_sales: float


class Genre(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str


class Publisher(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str | None


class Platform(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str


engine = create_engine("sqlite:///databasegames.db")


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

    with Session(engine) as session:
        print("Get games by id (3): ")
        print(games_db.get_games_by_id(3, Game, session))


if __name__ == "__main__":
    main()
