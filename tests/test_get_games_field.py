from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_endpoint_games_genre():
    response = client.get("/games/genre/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        "Sports",
        "Platform",
        "Racing",
        "Role-Playing",
        "Puzzle",
        "Misc",
        "Shooter",
        "Simulation",
        "Action",
        "Fighting",
        "Adventure",
        "Strategy",
    ]


def test_endpoint_games_publisher():
    response = client.get("/games/publisher/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 578


def test_endpoint_games_platforms():
    response = client.get("/games/platform/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        "Wii",
        "NES",
        "GB",
        "DS",
        "X360",
        "PS3",
        "PS2",
        "SNES",
        "GBA",
        "3DS",
        "PS4",
        "N64",
        "PS",
        "XB",
        "PC",
        "2600",
        "PSP",
        "XOne",
        "GC",
        "WiiU",
        "GEN",
        "DC",
        "PSV",
        "SAT",
        "SCD",
        "WS",
        "NG",
        "TG16",
        "3DO",
        "GG",
        "PCFX",
    ]


def test_endpoint_games_years():
    response = client.get("/games/year/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        2006,
        1985,
        2008,
        2009,
        1996,
        1989,
        1984,
        2005,
        1999,
        2007,
        2010,
        2013,
        2004,
        1990,
        1988,
        2002,
        2001,
        2011,
        1998,
        2015,
        2012,
        2014,
        1992,
        1997,
        1993,
        1994,
        1982,
        2003,
        1986,
        2000,
        1995,
        2016,
        1991,
        1981,
        1987,
        1980,
        1983,
        2020,
        2017,
    ]
