import uuid

from sqlmodel import Field, SQLModel


class GameSales(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    Na_sales: float
    Eu_sales: float
    Jp_sales: float
    Other_sales: float
    Global_sales: float
