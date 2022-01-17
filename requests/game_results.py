from datetime import datetime

from pydantic import BaseModel


class SaveGameResult(BaseModel):
    game_id: int
    game_result: dict = {'away_team': 'Away Team Name',
                         'away_score': 1,
                         'home_team': 'Home Team Name',
                         'home_score': 2,
                         'game_date': datetime(2022, 1, 1, 1, 1)}
