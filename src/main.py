from fastapi import FastAPI

from src.routes import game_sales, games, genre, platform, publisher

app = FastAPI()

app.include_router(publisher.router)
app.include_router(games.router)
app.include_router(platform.router)
app.include_router(genre.router)
app.include_router(game_sales.router)


@app.get("/")
def example():
    return {"message": "Hello Eric"}
