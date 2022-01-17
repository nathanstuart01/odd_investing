from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from connections.postgres import Base, SessionLocal
from models.avg_moneylines import AvgMoneylines
from models.game import Game


class GameResult(Base):
    __tablename__ = 'games_results'

    id = Column(Integer, primary_key=True)
    winning_team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    payout = Column(Float)

    game = relationship('Game', back_populates='result')
    team = relationship('Team', back_populates='results')

    @staticmethod
    def calculate_payout(db: SessionLocal, game_id: int, team_id: int) -> float:
        data = db.query(AvgMoneylines).\
            filter(AvgMoneylines.game_id == game_id).\
            filter(AvgMoneylines.team_id == team_id).\
            first()
        if data.line_avg >= 0:
            return data.line_avg * 1
        else:
            return abs((1 / data.line_avg) * 100)

    @staticmethod
    def determine_winner(game_result: dict, game: Game):
        if game_result['away_score'] > game_result['home_score']:
            return game.team_1_id
        elif game_result['away_score'] < game_result['home_score']:
            return game.team_2_id
        else:
            return None

    @staticmethod
    def calculate_season_winnings(db: SessionLocal, season_id: int, team_id: int):
        total_payout = 0
        games_lost = 0
        total_games = Game().get_total_games(db, season_id, team_id)
        for game in total_games:
            if game.result.winning_team_id == team_id:
                total_payout += game.result.payout
            else:
                games_lost += 1
        return total_payout - games_lost


