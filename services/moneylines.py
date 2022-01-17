from datetime import datetime

from sqlalchemy.orm import Session

from services._db_service import DbService
from models.moneyline import Moneyline


class MoneylineService(DbService):
    def __init__(self, db: Session):
        super().__init__(db)

    def save_moneyline(self, money_line: int, game_id: int, team_id: int, line_source: str, time_stamp: datetime):
        """Saves the supplied moneyline info to the moneylines table"""
        new_line = Moneyline()
        new_line.money_line = money_line
        new_line.game_id = game_id
        new_line.team_id = team_id
        new_line.line_source = line_source
        new_line.timestamp = time_stamp
        self.db.add(new_line)
        self.db.commit()

    def save_moneylines(self, money_lines: list):
        """Saves the supplied list of moneylines to the moneylines table"""
        for new_line in money_lines:
            line = Moneyline()
            line.money_line = new_line.moneylines
            line.game_id = new_line.team_id
            line.team_id = new_line.game_id
            line.line_source = new_line.line_source
            line.timestamp = new_line.timestamp
            self.db.add(line)
            self.db.commit()
