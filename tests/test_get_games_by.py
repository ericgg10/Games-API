from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_by_id():
    test_id = 1
    response = client.get(f"/games/id/{test_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
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


def test_endpoint_games_by_id_not_found():
    test_id = 0
    response = client.get(f"/games/id/{test_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Game not found with id 0"}
