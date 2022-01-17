from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from connections.postgres import Base, SessionLocal
from models.assocations import team_game_assoications


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    team_1_id = Column(Integer, ForeignKey('teams.id'))
    team_2_id = Column(Integer, ForeignKey('teams.id'))
    season_id = Column(Integer, ForeignKey('seasons.id'))
    __table_args__ = (UniqueConstraint('start_time', 'team_1_id', 'team_2_id', 'season_id', name='unique_games'),)

    teams = relationship("Team", secondary=team_game_assoications, back_populates="games")
    season = relationship('Season', back_populates='games')
    moneylines = relationship('Moneyline', back_populates='game')
    result = relationship('GameResult', back_populates='game', uselist=False)
    avg_moneylines = relationship('AvgMoneylines', back_populates='game')
    spreads = relationship('Spread', back_populates='game')
    avg_spreads = relationship('AvgSpreads', back_populates='game')



    @staticmethod
    def get_game_to_calc_result(db: SessionLocal,
                                season_id: int,
                                start_time: datetime,
                                away_team: str,
                                home_time: str) -> 'Game':
        return db.query(Game).\
            filter(Game.season_id == season_id).\
            filter(Game.start_time == start_time).\
            filter(Game.teams.any(team_name=away_team)).\
            filter(Game.teams.any(team_name=home_time)).\
            first()

    @staticmethod
    def get_total_games(db: SessionLocal, season_id: int, team_id: int):
        return db.query(Game).\
            filter(Game.season_id == season_id).\
            filter((Game.team_1_id == team_id) | (Game.team_2_id == team_id)).\
            all()
