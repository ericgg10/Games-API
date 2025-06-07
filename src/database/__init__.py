from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from src.config import settings

engine = create_engine(settings.DATABASE_URL)  # noqa: F401


def get_session():
    with Session(engine) as session:
        yield session


db_session = Annotated[Session, Depends(get_session)]
