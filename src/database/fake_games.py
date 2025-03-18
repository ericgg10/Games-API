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


# OTROS
def is_game_id(id: int):
    query = f"Rank == {id}"
    result = len(database_data.query(query)) == 1
    return result


def get_games_between_years(year_1: int, year_2: int, limit: int):
    query = f"Year>={year_1} and Year<={year_2} or Year>={year_2} and Year<={year_1}"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result


def get_games_between_eu_sales(eu_sales_1: float, eu_sales_2: float, limit: int):
    query = f"EU_Sales>={eu_sales_1} and EU_Sales<={eu_sales_2} or EU_Sales>={eu_sales_2} and EU_Sales<={eu_sales_1}"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result


def get_games_between_na_sales(na_sales_1: float, na_sales_2: float, limit: int):
    query = f"NA_Sales>={na_sales_1} and NA_Sales<={na_sales_2} or NA_Sales>={na_sales_2} and NA_Sales<={na_sales_1}"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result
