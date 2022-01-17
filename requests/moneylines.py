from datetime import datetime
from typing import List

from pydantic import BaseModel


class CreateMoneyLine(BaseModel):
    moneyline: int
    team_id: int
    game_id: int
    line_source: str
    timestamp: datetime = datetime(2022, 1, 1, 1, 1)


class CreateMoneyLines(BaseModel):
    moneylines: List[CreateMoneyLine]
