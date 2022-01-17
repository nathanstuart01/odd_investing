from typing import List
from pydantic import BaseModel
from datetime import datetime


class CreateNewGame(BaseModel):
    start_time: datetime = datetime(2022, 1, 1, 1, 1)
    team_1_id: int
    team_2_id: int
    season_id: int


class CreateNewGames(BaseModel):
    new_games: List[CreateNewGame]
