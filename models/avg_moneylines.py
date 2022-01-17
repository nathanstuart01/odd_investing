from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from connections.postgres import Base, SessionLocal
from models.moneyline import Moneyline
from models.game import Game


class AvgMoneylines(Base):
    __tablename__ = 'avg_moneylines'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    line_avg = Column(Float)

    team = relationship('Team', back_populates='avg_moneylines')
    game = relationship('Game', back_populates='avg_moneylines')

    @staticmethod
    def get_line_avg_away_team(db: SessionLocal, game: Game) -> float:
        return float(db.query(func.avg(Moneyline.money_line).label('moneyline_avg')).
                     filter(Moneyline.game_id == game.id).
                     filter(Moneyline.team_id == game.team_1_id).
                     scalar())

    @staticmethod
    def get_line_avg_home_team(db: SessionLocal, game: Game) -> float:
        return float(db.query(func.avg(Moneyline.money_line).label('moneyline_avg')).
                     filter(Moneyline.game_id == game.id).
                     filter(Moneyline.team_id == game.team_2_id).
                     scalar())
