import pandas as pd


database_data = pd.read_csv("data/games.csv")


def get_games_by_id(id: int):
    query = f"Rank == {id}"
    result=database_data.query(query).to_dict(orient="records")[0]
    return result


def is_game_id(id: int):
    query = f"Rank == {id}"
    result= len(database_data.query(query)) == 1
    return result


def get_game_by_name(name: str):
    query = f"Name == '{name}'"
    result=database_data.query(query).to_dict(orient="records")[0]
    return result


def get_games_by_genre(genre: str):
    query= f"Genre == '{genre}'"
    result= database_data.query(query).to_dict(orient="records")[0:100]
    return result