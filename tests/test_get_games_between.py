from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_between_year():
    test_year_1 = 1999
    test_year_2 = 2006
    response = client.get(f"/games/year/{test_year_1}/{test_year_2}")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


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
    assert len(response.json()) == 10


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
    assert len(response.json()) == 6


def test_endpoint_games_between_na_sales_invalid():
    test_na_sales_1 = 4.99
    test_na_sales_2 = 2.99
    response = client.get(f"/games/na_sales/{test_na_sales_1}/{test_na_sales_2}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "400 Bad Request: The request is malformed or incorrect. Please check the syntax of the URL or the request parameters."
    }
