import pandas as pd

database_data = pd.read_csv("data/games.csv")


def get_games_by_id(id: int):
    query = f"Rank == {id}"
    result = database_data.query(query).to_dict(orient="records")[0]
    return result


def is_game_id(id: int):
    query = f"Rank == {id}"
    result = len(database_data.query(query)) == 1
    return result


def get_game_by_name(name: str):
    query = f"Name == '{name}'"
    result = database_data.query(query).to_dict(orient="records")[0]
    return result


def get_games_field(field: str):
    result = database_data[field].dropna().unique().tolist()
    return result


def get_games_by_publisher(publisher: str, limit: int):
    query = f"Publisher=='{publisher}'"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result


def get_games_by_platform(platform: str, limit: int):
    query = f"Platform=='{platform}'"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result


def get_games_by_genre(genre: str, limit: int):
    query = f"Genre=='{genre}'"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
    return result


def get_games_by_year(year: int, limit: int):
    query = f"Year=={year}"
    result = database_data.query(query)["Name"].drop_duplicates().tolist()[0:limit]
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
