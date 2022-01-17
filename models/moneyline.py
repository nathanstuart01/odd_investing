from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from connections.postgres import Base


class Moneyline(Base):
    __tablename__ = 'moneylines'

    id = Column(Integer, primary_key=True)
    money_line = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    line_source = Column(String)
    timestamp = Column(DateTime)

    team = relationship('Team', back_populates='moneylines')
    game = relationship('Game', back_populates='moneylines')
