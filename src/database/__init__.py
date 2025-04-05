from sqlmodel import create_engine

engine = create_engine("sqlite:///databasegames.db")  # noqa: F401
