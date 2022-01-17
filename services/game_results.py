from sqlalchemy.orm import Session

from services._db_service import DbService
from models.game_results import GameResult
from models.game import Game


class GameResultsService(DbService):
    def __init__(self, db: Session):
        super().__init__(db)

    def save_game_result_to_db(self, game: Game, game_info: dict):
        """Saves updated game result to db"""
        result = GameResult()
        result.winning_team_id = result.determine_winner(game_info, game)
        result.game_id = game.id
        result.payout = result.calculate_payout(self.db, game.id, result.winning_team_id)
        self.db.add(result)
        self.db.commit()

