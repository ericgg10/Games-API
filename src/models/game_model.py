from sqlmodel import Field, SQLModel


class Game(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    year: int | None
    genre_id: int = Field(foreign_key="genre.id")
    publisher_id: int = Field(foreign_key="publisher.id")
    platform_id: int = Field(foreign_key="platform.id")
    gamesales_id: int = Field(foreign_key="gamesales.id")
