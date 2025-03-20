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
    assert response.json() == {"detail": f"Game not found with Name {test_name}"}


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


def test_endpoint_games_by_publisher_not_found():
    test_publisher = "Audi"
    response = client.get(f"/games/publisher/{test_publisher}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Publisher {test_publisher}"}


def test_endpoint_games_by_platform():
    test_platform = "Wii"
    response = client.get(f"/games/platform/{test_platform}")
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
            "Rank": 14,
            "Name": "Wii Fit",
            "Platform": "Wii",
            "Year": 2007,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 8.94,
            "EU_Sales": 8.03,
            "JP_Sales": 3.6,
            "Other_Sales": 2.15,
            "Global_Sales": 22.72,
        },
        {
            "Rank": 15,
            "Name": "Wii Fit Plus",
            "Platform": "Wii",
            "Year": 2009,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 9.09,
            "EU_Sales": 8.59,
            "JP_Sales": 2.53,
            "Other_Sales": 1.79,
            "Global_Sales": 22,
        },
        {
            "Rank": 40,
            "Name": "Super Smash Bros. Brawl",
            "Platform": "Wii",
            "Year": 2008,
            "Genre": "Fighting",
            "Publisher": "Nintendo",
            "NA_Sales": 6.75,
            "EU_Sales": 2.61,
            "JP_Sales": 2.66,
            "Other_Sales": 1.02,
            "Global_Sales": 13.04,
        },
        {
            "Rank": 49,
            "Name": "Super Mario Galaxy",
            "Platform": "Wii",
            "Year": 2007,
            "Genre": "Platform",
            "Publisher": "Nintendo",
            "NA_Sales": 6.16,
            "EU_Sales": 3.4,
            "JP_Sales": 1.2,
            "Other_Sales": 0.76,
            "Global_Sales": 11.52,
        },
        {
            "Rank": 61,
            "Name": "Just Dance 3",
            "Platform": "Wii",
            "Year": 2011,
            "Genre": "Misc",
            "Publisher": "Ubisoft",
            "NA_Sales": 6.05,
            "EU_Sales": 3.15,
            "JP_Sales": 0,
            "Other_Sales": 1.07,
            "Global_Sales": 10.26,
        },
    ]


def test_endpoint_games_by_platform_not_found():
    test_platform = "Consola"
    response = client.get(f"/games/platform/{test_platform}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Platform {test_platform}"}


def test_endpoint_games_by_genre():
    test_genre = "Shooter"
    response = client.get(f"/games/genre/{test_genre}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
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
        {
            "Rank": 30,
            "Name": "Call of Duty: Modern Warfare 3",
            "Platform": "X360",
            "Year": 2011,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 9.03,
            "EU_Sales": 4.28,
            "JP_Sales": 0.13,
            "Other_Sales": 1.32,
            "Global_Sales": 14.76,
        },
        {
            "Rank": 32,
            "Name": "Call of Duty: Black Ops",
            "Platform": "X360",
            "Year": 2010,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 9.67,
            "EU_Sales": 3.73,
            "JP_Sales": 0.11,
            "Other_Sales": 1.13,
            "Global_Sales": 14.64,
        },
        {
            "Rank": 34,
            "Name": "Call of Duty: Black Ops 3",
            "Platform": "PS4",
            "Year": 2015,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 5.77,
            "EU_Sales": 5.81,
            "JP_Sales": 0.35,
            "Other_Sales": 2.31,
            "Global_Sales": 14.24,
        },
        {
            "Rank": 35,
            "Name": "Call of Duty: Black Ops II",
            "Platform": "PS3",
            "Year": 2012,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 4.99,
            "EU_Sales": 5.88,
            "JP_Sales": 0.65,
            "Other_Sales": 2.52,
            "Global_Sales": 14.03,
        },
        {
            "Rank": 36,
            "Name": "Call of Duty: Black Ops II",
            "Platform": "X360",
            "Year": 2012,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 8.25,
            "EU_Sales": 4.3,
            "JP_Sales": 0.07,
            "Other_Sales": 1.12,
            "Global_Sales": 13.73,
        },
        {
            "Rank": 37,
            "Name": "Call of Duty: Modern Warfare 2",
            "Platform": "X360",
            "Year": 2009,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 8.52,
            "EU_Sales": 3.63,
            "JP_Sales": 0.08,
            "Other_Sales": 1.29,
            "Global_Sales": 13.51,
        },
        {
            "Rank": 38,
            "Name": "Call of Duty: Modern Warfare 3",
            "Platform": "PS3",
            "Year": 2011,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 5.54,
            "EU_Sales": 5.82,
            "JP_Sales": 0.49,
            "Other_Sales": 1.62,
            "Global_Sales": 13.46,
        },
        {
            "Rank": 41,
            "Name": "Call of Duty: Black Ops",
            "Platform": "PS3",
            "Year": 2010,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 5.98,
            "EU_Sales": 4.44,
            "JP_Sales": 0.48,
            "Other_Sales": 1.83,
            "Global_Sales": 12.73,
        },
        {
            "Rank": 44,
            "Name": "Halo 3",
            "Platform": "X360",
            "Year": 2007,
            "Genre": "Shooter",
            "Publisher": "Microsoft Game Studios",
            "NA_Sales": 7.97,
            "EU_Sales": 2.83,
            "JP_Sales": 0.13,
            "Other_Sales": 1.21,
            "Global_Sales": 12.14,
        },
    ]


def test_endpoint_games_by_genre_not_found():
    test_genre = "Genero"
    response = client.get(f"/games/genre/{test_genre}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Genre {test_genre}"}


def test_endpoint_games_by_year():
    test_year = "2009"
    response = client.get(f"/games/year/{test_year}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
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
            "Rank": 15,
            "Name": "Wii Fit Plus",
            "Platform": "Wii",
            "Year": 2009,
            "Genre": "Sports",
            "Publisher": "Nintendo",
            "NA_Sales": 9.09,
            "EU_Sales": 8.59,
            "JP_Sales": 2.53,
            "Other_Sales": 1.79,
            "Global_Sales": 22,
        },
        {
            "Rank": 37,
            "Name": "Call of Duty: Modern Warfare 2",
            "Platform": "X360",
            "Year": 2009,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 8.52,
            "EU_Sales": 3.63,
            "JP_Sales": 0.08,
            "Other_Sales": 1.29,
            "Global_Sales": 13.51,
        },
        {
            "Rank": 46,
            "Name": "Pokemon HeartGold/Pokemon SoulSilver",
            "Platform": "DS",
            "Year": 2009,
            "Genre": "Action",
            "Publisher": "Nintendo",
            "NA_Sales": 4.4,
            "EU_Sales": 2.77,
            "JP_Sales": 3.96,
            "Other_Sales": 0.77,
            "Global_Sales": 11.9,
        },
        {
            "Rank": 56,
            "Name": "Call of Duty: Modern Warfare 2",
            "Platform": "PS3",
            "Year": 2009,
            "Genre": "Shooter",
            "Publisher": "Activision",
            "NA_Sales": 4.99,
            "EU_Sales": 3.69,
            "JP_Sales": 0.38,
            "Other_Sales": 1.63,
            "Global_Sales": 10.69,
        },
        {
            "Rank": 84,
            "Name": "The Sims 3",
            "Platform": "PC",
            "Year": 2009,
            "Genre": "Simulation",
            "Publisher": "Electronic Arts",
            "NA_Sales": 0.98,
            "EU_Sales": 6.42,
            "JP_Sales": 0,
            "Other_Sales": 0.71,
            "Global_Sales": 8.11,
        },
        {
            "Rank": 103,
            "Name": "Just Dance",
            "Platform": "Wii",
            "Year": 2009,
            "Genre": "Misc",
            "Publisher": "Ubisoft",
            "NA_Sales": 3.51,
            "EU_Sales": 3.03,
            "JP_Sales": 0,
            "Other_Sales": 0.73,
            "Global_Sales": 7.27,
        },
        {
            "Rank": 120,
            "Name": "Uncharted 2: Among Thieves",
            "Platform": "PS3",
            "Year": 2009,
            "Genre": "Action",
            "Publisher": "Sony Computer Entertainment",
            "NA_Sales": 3.27,
            "EU_Sales": 2.25,
            "JP_Sales": 0.21,
            "Other_Sales": 1,
            "Global_Sales": 6.73,
        },
        {
            "Rank": 134,
            "Name": "Halo 3: ODST",
            "Platform": "X360",
            "Year": 2009,
            "Genre": "Shooter",
            "Publisher": "Microsoft Game Studios",
            "NA_Sales": 4.34,
            "EU_Sales": 1.35,
            "JP_Sales": 0.06,
            "Other_Sales": 0.61,
            "Global_Sales": 6.36,
        },
    ]


def test_endpoint_games_by_year_not_found():
    test_year = "1800"
    response = client.get(f"/games/year/{test_year}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Game not found with Year {test_year}"}
