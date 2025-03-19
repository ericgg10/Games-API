from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_by_id():
    test_id = 1
    response = client.get(f"/games/id/{test_id}")
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
        }
    ]


def test_endpoint_games_by_id_not_found():
    test_id = 0
    response = client.get(f"/games/id/{test_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Game not found with id 0"}


def test_endpoint_games_by_name():
    test_name = "Wii Play"
    response = client.get(f"/games/name/{test_name}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
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
        }
    ]


def test_endpoint_games_by_name_not_found():
    test_name = "Chicken Little"
    response = client.get(f"/games/name/{test_name}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Game not found with Name Chicken Little"}


def test_endpoint_games_by_publisher():
    test_publisher = "Nintendo"
    response = client.get(f"/games/publisher/{test_publisher}")
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


"""
def test_endpoint_games_by_publisher_not_found():
    test_publisher = "Audi"
    response = client.get(f"/games/publisher/{test_publisher}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Game not found with publisher Audi"}
"""
