from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from connections.postgres import Base, SessionLocal
from models.assocations import team_season_associations


class Season(Base):
    __tablename__ = 'seasons'

    id = Column(Integer, primary_key=True)
    season_end_year = Column(Integer)
    league_id = Column(Integer, ForeignKey('leagues.id'))

    teams = relationship('Team', secondary=team_season_associations, back_populates='seasons')
    league = relationship('League', back_populates='seasons')
    games = relationship('Game', back_populates='season')

    @staticmethod
    def get_season_id(db: SessionLocal,
                      league_id: int,
                      season_end_year: int) -> int:
        return db.query(Season).\
            filter(Season.league_id == league_id).\
            filter(Season.season_end_year == season_end_year).\
            first().id
