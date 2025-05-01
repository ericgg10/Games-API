import uuid

from sqlmodel import Field, SQLModel


class Genre(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str


class GenreUpdate(SQLModel):
    id: uuid.UUID
    name: str


class GenreCreate(SQLModel):
    id: uuid.UUID
    name: str
