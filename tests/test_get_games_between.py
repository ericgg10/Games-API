from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_between_year():
    test_year_1 = 1999
    test_year_2 = 2006
    response = client.get(f"/games/year/{test_year_1}/{test_year_2}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "Rank": 1,
            "Name": "Wii Sports",
            "Platform": "Wii",
            "Year": 2006,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 41.49,
            "EU_Sales": 29.02,
            "JP_Sales": 3.77,
            "Other_Sales": 8.46,
            "Global_Sales": 82.74,
        },
        {
            "Rank": 7,
            "Name": "New Super Mario Bros.",
            "Platform": "DS",
            "Year": 2006,
            "Genre": "Platform",
            "Publisher": "Nintendo",
            "NA_Sales": 11.38,
            "EU_Sales": 9.23,
            "JP_Sales": 6.5,
            "Other_Sales": 2.9,
            "Global_Sales": 30.01,
        },
        {
            "Rank": 8,
            "Name": "Wii Play",
            "Platform": "Wii",
            "Year": 2006,
            "Genre": "Misc",
            "Publisher": "Nintendo",
            "NA_Sales": 14.03,
            "EU_Sales": 9.2,
            "JP_Sales": 2.93,
            "Other_Sales": 2.85,
            "Global_Sales": 29.02,
        },
        {
            "Rank": 11,
            "Name": "Nintendogs",
            "Platform": "DS",
            "Year": 2005,
            "Genre": "Simulation",
            "Publisher": "Nintendo",
            "NA_Sales": 9.07,
            "EU_Sales": 11,
            "JP_Sales": 1.93,
            "Other_Sales": 2.75,
            "Global_Sales": 24.76,
        },
        {
            "Rank": 12,
            "Name": "Mario Kart DS",
            "Platform": "DS",
            "Year": 2005,
            "Genre": "Racing",
            "Publisher": "Nintendo",
            "NA_Sales": 9.81,
            "EU_Sales": 7.57,
            "JP_Sales": 4.13,
            "Other_Sales": 1.92,
            "Global_Sales": 23.42,
        },
        {
            "Rank": 13,
            "Name": "Pokemon Gold/Pokemon Silver",
            "Platform": "GB",
            "Year": 1999,
            "Genre": "Role-Playing",
            "Publisher": "Nintendo",
            "NA_Sales": 9,
            "EU_Sales": 6.18,
            "JP_Sales": 7.2,
            "Other_Sales": 0.71,
            "Global_Sales": 23.1,
        },
        {
            "Rank": 18,
            "Name": "Grand Theft Auto: San Andreas",
            "Platform": "PS2",
            "Year": 2004,
            "Genre": "Action",
            "Publisher": "Take-Two Interactive",
            "NA_Sales": 9.43,
            "EU_Sales": 0.4,
            "JP_Sales": 0.41,
            "Other_Sales": 10.57,
            "Global_Sales": 20.81,
        },
        {
            "Rank": 20,
            "Name": "Brain Age: Train Your Brain in Minutes a Day",
            "Platform": "DS",
            "Year": 2005,
            "Genre": "Misc",
            "Publisher": "Nintendo",
            "NA_Sales": 4.75,
            "EU_Sales": 9.26,
            "JP_Sales": 4.16,
            "Other_Sales": 2.05,
            "Global_Sales": 20.22,
        },
        {
            "Rank": 21,
            "Name": "Pokemon Diamond/Pokemon Pearl",
            "Platform": "DS",
            "Year": 2006,
            "Genre": "Role-Playing",
            "Publisher": "Nintendo",
            "NA_Sales": 6.42,
            "EU_Sales": 4.52,
            "JP_Sales": 6.04,
            "Other_Sales": 1.37,
            "Global_Sales": 18.36,
        },
        {
            "Rank": 25,
            "Name": "Grand Theft Auto: Vice City",
            "Platform": "PS2",
            "Year": 2002,
            "Genre": "Action",
            "Publisher": "Take-Two Interactive",
            "NA_Sales": 8.41,
            "EU_Sales": 5.49,
            "JP_Sales": 0.47,
            "Other_Sales": 1.78,
            "Global_Sales": 16.15,
        },
    ]


def test_endpoint_games_between_year_invalid():
    test_year_1 = 2006
    test_year_2 = 1999
    response = client.get(f"/games/year/{test_year_1}/{test_year_2}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters."
    }


def test_endpoint_games_between_eu_sales():
    test_eu_sales_1 = 5.44
    test_eu_sales_2 = 29.02
    response = client.get(f"/games/eu_sales/{test_eu_sales_1}/{test_eu_sales_2}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "Rank": 1,
            "Name": "Wii Sports",
            "Platform": "Wii",
            "Year": 2006,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 41.49,
            "EU_Sales": 29.02,
            "JP_Sales": 3.77,
            "Other_Sales": 8.46,
            "Global_Sales": 82.74,
        },
        {
            "Rank": 3,
            "Name": "Mario Kart Wii",
            "Platform": "Wii",
            "Year": 2008,
            "Genre": "Racing",
            "Publisher": "Nintendo",
            "NA_Sales": 15.85,
            "EU_Sales": 12.88,
            "JP_Sales": 3.79,
            "Other_Sales": 3.31,
            "Global_Sales": 35.82,
        },
        {
            "Rank": 4,
            "Name": "Wii Sports Resort",
            "Platform": "Wii",
            "Year": 2009,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 15.75,
            "EU_Sales": 11.01,
            "JP_Sales": 3.28,
            "Other_Sales": 2.96,
            "Global_Sales": 33,
        },
        {
            "Rank": 5,
            "Name": "Pokemon Red/Pokemon Blue",
            "Platform": "GB",
            "Year": 1996,
            "Genre": "Role-Playing",
            "Publisher": "Nintendo",
            "NA_Sales": 11.27,
            "EU_Sales": 8.89,
            "JP_Sales": 10.22,
            "Other_Sales": 1,
            "Global_Sales": 31.37,
        },
        {
            "Rank": 7,
            "Name": "New Super Mario Bros.",
            "Platform": "DS",
            "Year": 2006,
            "Genre": "Platform",
            "Publisher": "Nintendo",
            "NA_Sales": 11.38,
            "EU_Sales": 9.23,
            "JP_Sales": 6.5,
            "Other_Sales": 2.9,
            "Global_Sales": 30.01,
        },
        {
            "Rank": 8,
            "Name": "Wii Play",
            "Platform": "Wii",
            "Year": 2006,
            "Genre": "Misc",
            "Publisher": "Nintendo",
            "NA_Sales": 14.03,
            "EU_Sales": 9.2,
            "JP_Sales": 2.93,
            "Other_Sales": 2.85,
            "Global_Sales": 29.02,
        },
        {
            "Rank": 9,
            "Name": "New Super Mario Bros. Wii",
            "Platform": "Wii",
            "Year": 2009,
            "Genre": "Platform",
            "Publisher": "Nintendo",
            "NA_Sales": 14.59,
            "EU_Sales": 7.06,
            "JP_Sales": 4.7,
            "Other_Sales": 2.26,
            "Global_Sales": 28.62,
        },
        {
            "Rank": 11,
            "Name": "Nintendogs",
            "Platform": "DS",
            "Year": 2005,
            "Genre": "Simulation",
            "Publisher": "Nintendo",
            "NA_Sales": 9.07,
            "EU_Sales": 11,
            "JP_Sales": 1.93,
            "Other_Sales": 2.75,
            "Global_Sales": 24.76,
        },
        {
            "Rank": 12,
            "Name": "Mario Kart DS",
            "Platform": "DS",
            "Year": 2005,
            "Genre": "Racing",
            "Publisher": "Nintendo",
            "NA_Sales": 9.81,
            "EU_Sales": 7.57,
            "JP_Sales": 4.13,
            "Other_Sales": 1.92,
            "Global_Sales": 23.42,
        },
        {
            "Rank": 13,
            "Name": "Pokemon Gold/Pokemon Silver",
            "Platform": "GB",
            "Year": 1999,
            "Genre": "Role-Playing",
            "Publisher": "Nintendo",
            "NA_Sales": 9,
            "EU_Sales": 6.18,
            "JP_Sales": 7.2,
            "Other_Sales": 0.71,
            "Global_Sales": 23.1,
        },
    ]


def test_endpoint_games_between_eu_sales_invalid():
    test_eu_sales_1 = 4.99
    test_eu_sales_2 = 2.99
    response = client.get(f"/games/eu_sales/{test_eu_sales_1}/{test_eu_sales_2}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters."
    }


def test_endpoint_games_between_na_sales():
    na_sales_1 = 15.85
    na_sales_2 = 41.49
    response = client.get(f"/games/na_sales/{na_sales_1}/{na_sales_2}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "Rank": 1,
            "Name": "Wii Sports",
            "Platform": "Wii",
            "Year": 2006,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 41.49,
            "EU_Sales": 29.02,
            "JP_Sales": 3.77,
            "Other_Sales": 8.46,
            "Global_Sales": 82.74,
        },
        {
            "Rank": 2,
            "Name": "Super Mario Bros.",
            "Platform": "NES",
            "Year": 1985,
            "Genre": "Platform",
            "Publisher": "Nintendo",
            "NA_Sales": 29.08,
            "EU_Sales": 3.58,
            "JP_Sales": 6.81,
            "Other_Sales": 0.77,
            "Global_Sales": 40.24,
        },
        {
            "Rank": 3,
            "Name": "Mario Kart Wii",
            "Platform": "Wii",
            "Year": 2008,
            "Genre": "Racing",
            "Publisher": "Nintendo",
            "NA_Sales": 15.85,
            "EU_Sales": 12.88,
            "JP_Sales": 3.79,
            "Other_Sales": 3.31,
            "Global_Sales": 35.82,
        },
        {
            "Rank": 6,
            "Name": "Tetris",
            "Platform": "GB",
            "Year": 1989,
            "Genre": "Puzzle",
            "Publisher": "Nintendo",
            "NA_Sales": 23.2,
            "EU_Sales": 2.26,
            "JP_Sales": 4.22,
            "Other_Sales": 0.58,
            "Global_Sales": 30.26,
        },
        {
            "Rank": 10,
            "Name": "Duck Hunt",
            "Platform": "NES",
            "Year": 1984,
            "Genre": "Shooter",
            "Publisher": "Nintendo",
            "NA_Sales": 26.93,
            "EU_Sales": 0.63,
            "JP_Sales": 0.28,
            "Other_Sales": 0.47,
            "Global_Sales": 28.31,
        },
    ]


def test_endpoint_games_between_na_sales_invalid():
    test_na_sales_1 = 4.99
    test_na_sales_2 = 2.99
    response = client.get(f"/games/na_sales/{test_na_sales_1}/{test_na_sales_2}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters."
    }
