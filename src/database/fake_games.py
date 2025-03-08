import pandas as pd


database_data = pd.read_csv("data/games.csv")


def get_games_by_id(id: int):
    query = f"Rank == '{id}'"
    return database_data.query(query).to_dict(orient="records")[0]


def is_game_id(id: int):
    query = f"Rank == '{id}'"
    return len(database_data.query(query)) == 1


def get_game_by_name(name: str):
    query = f"Name == '{name}'"
    return database_data.query(query).to_dict(orient="records")[0]
