from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from connections.postgres import Base


class Spread(Base):
    __tablename__ = 'spreads'

    id = Column(Integer, primary_key=True)
    spread = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    spread_source = Column(String)
    timestamp = Column(DateTime)

    team = relationship('Team', back_populates='spreads')
    game = relationship('Game', back_populates='spreads')