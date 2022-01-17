from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from connections.postgres import Base, SessionLocal


class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    league_name = Column(String)

    teams = relationship("Team", back_populates="league")
    seasons = relationship("Season", back_populates='league')

    @staticmethod
    def get_league_id(db: SessionLocal, league_name: str) -> int:
        return db.query(League).filter(League.league_name == league_name).first().id
