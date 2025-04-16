from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_genre():
    response = client.get("/genre/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 12


def test_endpoint_games_publisher():
    response = client.get("/publisher/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 636


def test_endpoint_games_platforms():
    response = client.get("/platform/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 31
