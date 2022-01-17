from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from requests.games import CreateNewGame, CreateNewGames
from services.games import GameService
from connections.postgres import get_db

router = APIRouter(
    prefix='/games',
    tags=['Games'],
    responses={404: {'description': 'Not Found'}}
)


@router.post("/create", status_code=201)
async def create_new_game(req: CreateNewGame, db: Session = Depends(get_db)) -> dict:
    """Creates a new game and saves to db"""
    try:
        GameService(db).create_new_game(req.start_time, req.team_1_id, req.team_2_id, req.season_id)
        return {'success': 'created new game'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post("/create_games", status_code=201)
async def create_new_games(req: CreateNewGames, db: Session = Depends(get_db)) -> dict:
    """Creates new games and saves them to db"""
    try:
        GameService(db).create_new_games(req.new_games)
        return {'success': 'created new games'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
