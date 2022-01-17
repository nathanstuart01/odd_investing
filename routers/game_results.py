from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from requests.game_results import SaveGameResult
from connections.postgres import get_db
from services.games import GameService
from services.game_results import GameResultsService

router = APIRouter(
    prefix='/game_results',
    tags=['GameResults'],
    responses={404: {'description': 'Not Found'}}
)


@router.post('/create', status_code=201)
async def create_new_result(req: SaveGameResult, db: Session = Depends(get_db)) -> dict:
    """Saves a new game result to the db"""
    try:
        game = GameService(db).get_game(req.game_id)
        GameResultsService(db).save_game_result_to_db(game, req.game_result)
        return {'success': 'saved game result to db'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
