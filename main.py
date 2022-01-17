from fastapi import FastAPI

from routers import games, moneylines, game_results

tags_metadata = [
    {
        "name": "Games",
        "description": "Create new games"
    },
    {
        "name": "Moneylines",
        "description": "Create new moneylines"
    },
    {
        "name": "GameResults",
        "description": "Create new game results"
    }
]

app = FastAPI(
    title='Management API for odd investing',
    version="0.0.1",
    openapi_tags=tags_metadata,
    docs_url='/'
)

app.include_router(games.router)
app.include_router(moneylines.router)
app.include_router(game_results.router)
