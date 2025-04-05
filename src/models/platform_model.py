from sqlmodel import Field, SQLModel


class Platform(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
