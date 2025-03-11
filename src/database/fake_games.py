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

def get_games_genres():
    result = database_data['Genre'].drop_duplicates().tolist()
    return result

def get_games_publisher():
    result = database_data['Publisher'].drop_duplicates().tolist()[0:33]
    return result

def get_games_platform():
    result = database_data['Platform'].drop_duplicates().tolist()
    return result

def get_games_years():
    result= database_data['Year'].drop_duplicates().tolist()[0:30]
    return result

def get_games_by_publisher(publisher:str):
    query= f"Publisher=='{publisher}'"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_by_platform(platform:str):
    query= f"Platform=='{platform}'"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_by_genre(genre:str):
    query= f"Genre=='{genre}'"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_by_year(year:int):
    query= f"Year=={year}"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_between_years(year_1: int, year_2: int ):
    query= f"Year>={year_1} and Year<={year_2} or Year>={year_2} and Year<={year_1}"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_between_eu_sales(eu_sales_1: float, eu_sales_2: float ):
    query= f"EU_Sales>={eu_sales_1} and EU_Sales<={eu_sales_2} or EU_Sales>={eu_sales_2} and EU_Sales<={eu_sales_1}"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result

def get_games_between_na_sales(na_sales_1: float, na_sales_2: float):
    query= f"NA_Sales>={na_sales_1} and NA_Sales<={na_sales_2} or NA_Sales>={na_sales_2} and NA_Sales<={na_sales_1}"
    result=database_data.query(query)['Name'].drop_duplicates().tolist()[0:100]
    return result