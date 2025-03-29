from fastapi import FastAPI

from src.routes import games, genre, platform, publisher

app = FastAPI()

app.include_router(publisher.router)
app.include_router(games.router)
app.include_router(platform.router)
app.include_router(genre.router)


@app.get("/")
def example():
    return {"message": "Hello Eric"}
