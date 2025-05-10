import uuid

from sqlmodel import Field, SQLModel


class Publisher(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str | None


class PublisherUpdate(SQLModel):
    id: uuid.UUID
    name: str


class PublisherCreate(SQLModel):
    name: str
