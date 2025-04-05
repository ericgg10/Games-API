from sqlmodel import Field, SQLModel


class GameSales(SQLModel, table=True):
    id: int = Field(primary_key=True)
    Na_sales: float
    Eu_sales: float
    Jp_sales: float
    Other_sales: float
    Global_sales: float
