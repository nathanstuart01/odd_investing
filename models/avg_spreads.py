from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from connections.postgres import Base, SessionLocal
from models.game import Game
from models.spread import Spread


class AvgSpreads(Base):
    __tablename__ = 'avg_spreads'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    spread_avg = Column(Float)

    team = relationship('Team', back_populates='avg_spreads')
    game = relationship('Game', back_populates='avg_spreads')

    @staticmethod
    def get_spread_avg_away_team(db: SessionLocal, game: Game) -> float:
        return float(db.query(func.avg(Spread.spread).label('spread_avg')).
                     filter(Spread.game_id == game.id).
                     filter(Spread.team_id == game.team_1_id).
                     scalar())

    @staticmethod
    def get_spread_avg_home_team(db: SessionLocal, game: Game) -> float:
        return float(db.query(func.avg(Spread.spread).label('spread_avg')).
                     filter(Spread.game_id == game.id).
                     filter(Spread.team_id == game.team_2_id).
                     scalar())
