from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_by_id():
    test_id = 1
    response = client.get(f"/games/id/{test_id}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 7


def test_endpoint_games_by_id_not_found():
    test_id = 0
    response = client.get(f"/games/id/{test_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Game not found with id 0"}


def test_endpoint_games_by_name():
    test_name = "Wii Play"
    response = client.get(f"/games/name/{test_name}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_endpoint_games_by_name_not_found():
    test_name = "Chicken Little"
    response = client.get(f"/games/name/{test_name}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Name {test_name}"}


def test_endpoint_games_by_publisher():
    test_publisher = "Nintendo"
    response = client.get(f"/games/publisher/{test_publisher}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_games_by_publisher_not_found():
    test_publisher = "Audi"
    response = client.get(f"/games/publisher/{test_publisher}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Publisher {test_publisher}"}


def test_endpoint_games_by_platform():
    test_platform = "Wii"
    response = client.get(f"/games/platform/{test_platform}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_games_by_platform_not_found():
    test_platform = "Consola"
    response = client.get(f"/games/platform/{test_platform}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Platform {test_platform}"}


def test_endpoint_games_by_genre():
    test_genre = "Shooter"
    response = client.get(f"/games/genre/{test_genre}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_games_by_genre_not_found():
    test_genre = "Genero"
    response = client.get(f"/games/genre/{test_genre}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Genre {test_genre}"}


def test_endpoint_games_by_year():
    test_year = "2009"
    response = client.get(f"/games/year/{test_year}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_endpoint_games_by_year_not_found():
    test_year = "1800"
    response = client.get(f"/games/year/{test_year}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Year {test_year}"}
