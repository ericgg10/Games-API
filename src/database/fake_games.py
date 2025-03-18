import pandas as pd

database_data = pd.read_csv("data/games.csv")


# GET GAMES BY
def get_games_by_field(field: str, field_value: str, limit=int):
    query = f"{field} == '{field_value}'"
    result = database_data.query(query)["Name"].unique().tolist()[0:limit]
    return result


def get_games_by_field_num(field: int, field_value: int, limit=int):
    query = f"{field} == {field_value}"
    result = database_data.query(query)["Name"].unique().tolist()[0:limit]
    return result


# GET GAMES FIELD
def get_games_field(field: str):
    result = database_data[field].dropna().unique().tolist()
    return result


# TEST
def is_game_id(id: int):
    query = f"Rank == {id}"
    result = len(database_data.query(query)) == 1
    return result


# GET GAMES BETWEEN
def get_games_between_int(field: int, field_1_value: int, field_2_value: int, limit: int):
    query = f"{field}>= {field_1_value} & {field}<={field_2_value}"
    result = database_data.query(query)["Name"].unique().tolist()[0:limit]
    return result


def get_games_between_float(field: float, field_1_value: float, field_2_value: float, limit: int):
    query = f"{field}>= {field_1_value} & {field}<={field_2_value}"
    result = database_data.query(query)["Name"].unique().tolist()[0:limit]
    return result
