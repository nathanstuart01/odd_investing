from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from requests.moneylines import CreateMoneyLine, CreateMoneyLines
from services.moneylines import MoneylineService
from connections.postgres import get_db

router = APIRouter(
    prefix='/moneylines',
    tags=['Moneylines'],
    responses={404: {'description': 'Not Found'}}
)


@router.post('/create', status_code=201)
async def create_new_moneyline(req: CreateMoneyLine, db: Session = Depends(get_db)) -> dict:
    """Creates a new moneyline in the db"""
    try:
        MoneylineService(db).save_moneyline(req.moneyline, req.team_id, req.game_id, req.line_source, req.timestamp)
        return {'success': 'created new moneyline'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post('/create_moneylines', status_code=201)
async def create_new_moneylines(req: CreateMoneyLines, db: Session = Depends(get_db)) -> dict:
    """Creates all supplied new moneylines in the db"""
    try:
        MoneylineService(db).save_moneylines(req.moneylines)
        return {'success': 'created all new moneylines'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())

