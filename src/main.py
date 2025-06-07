import uvicorn
from fastapi import FastAPI

from src.config import settings
from src.routes import game_sales, games, genre, platform, publisher, users

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
)

app.include_router(publisher.router)
app.include_router(games.router)
app.include_router(platform.router)
app.include_router(genre.router)
app.include_router(game_sales.router)
app.include_router(users.router)


@app.get("/")
def example():
    return {"message": "Hello Eric"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
