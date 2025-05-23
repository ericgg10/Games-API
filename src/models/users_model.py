import uuid

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str | None
    password: int
    role: int


class UserUpdate(SQLModel):
    id: uuid.UUID
    name: str | None
    password: int


class UserCreate(SQLModel):
    name: str | None
    password: int
