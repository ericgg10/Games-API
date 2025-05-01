import uuid

from sqlmodel import Field, SQLModel


class Platform(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str


class PlatformUpdate(SQLModel):
    id: uuid.UUID
    name: str


class PlatformCreate(SQLModel):
    id: uuid.UUID
    name: str
