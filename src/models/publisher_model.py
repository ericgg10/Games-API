from sqlmodel import Field, SQLModel


class Publisher(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str | None
