import uuid

from sqlmodel import Field, SQLModel


class Game(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    year: int | None
    genre_id: uuid.UUID = Field(foreign_key="genre.id")
    publisher_id: uuid.UUID = Field(foreign_key="publisher.id")
    platform_id: uuid.UUID = Field(foreign_key="platform.id")
    gamesales_id: uuid.UUID = Field(foreign_key="gamesales.id", ondelete="CASCADE")


class GameUpdate(SQLModel):
    id: uuid.UUID
    name: str
    year: int | None
    genre_id: int
    platform_id: int


class GameCreate(SQLModel):
    name: str
    year: int | None
    genre_id: int
    publisher_id: int
    platform_id: int
    gamesales_id: int


class GamePublic(SQLModel):
    id: uuid.UUID
    name: str
    year: int | None
    genre_name: str
    publisher_name: str
    platform_name: str
