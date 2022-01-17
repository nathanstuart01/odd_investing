from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from connections.postgres import Base, SessionLocal
from models.assocations import team_season_associations
from models.assocations import team_game_assoications


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    team_name = Column(String)
    league_id = Column(Integer, ForeignKey('leagues.id'))

    league = relationship("League", back_populates='teams')
    seasons = relationship('Season', secondary=team_season_associations, back_populates='teams')
    games = relationship('Game', secondary=team_game_assoications, back_populates='teams')
    moneylines = relationship('Moneyline', back_populates='team')
    results = relationship('GameResult', back_populates='team')
    avg_moneylines = relationship('AvgMoneylines', back_populates='team')
    spreads = relationship('Spread', back_populates='team')
    avg_spreads = relationship('AvgSpreads', back_populates='team')

    @staticmethod
    def get_team_game_ids(db: SessionLocal, team_1_name: str, team_2_name) -> dict:
        team_ids = dict()
        team_ids['team_1_id'] = db.query(Team).filter(Team.team_name == team_1_name).first().id
        team_ids['team_2_id'] = db.query(Team).filter(Team.team_name == team_2_name).first().id
        return team_ids

    @staticmethod
    def get_team_id(db: SessionLocal, team_name: str, league_id: int) -> int:
        return db.query(Team).filter(Team.team_name == team_name).filter(Team.league_id == league_id).first().id
