from datetime import datetime

from sqlalchemy.orm import Session
from models.game import Game
from services._db_service import DbService


class GameService(DbService):
    def __init__(self, db: Session):
        super().__init__(db)

    def create_new_game(self, start_time: datetime, team_1_id: int, team_2_id: int, season_id: int):
        """Creates new game in the db"""
        new_game = Game()
        new_game.start_time = start_time
        new_game.team_1_id = team_1_id
        new_game.team_2_id = team_2_id
        new_game.season_id = season_id
        self.db.add(new_game)
        self.db.commit()

    def create_new_games(self, games: list):
        """Creates new games in the db"""
        for game in games:
            new_game = Game()
            new_game.start_time = game.start_time
            new_game.team_1_id = game.team_1_id
            new_game.team_2_id = game.team_2_id
            new_game.season_id = game.season_id
            self.db.add(new_game)
        self.db.commit()

    def get_game(self, game_id: int) -> Game:
        """Returns a Game model based on supplied game_id"""
        return self.db.query(Game).filter(Game.id == game_id).first()
