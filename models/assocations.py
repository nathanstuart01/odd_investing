from sqlalchemy import Table, Column, ForeignKey

from connections.postgres import Base

team_season_associations = Table('team_season_associations', Base.metadata,
                                 Column('teams_id', ForeignKey('teams.id'), primary_key=True),
                                 Column('seasons_id', ForeignKey('seasons.id'), primary_key=True)
                                 )


team_game_assoications = Table('teams_games_associations', Base.metadata,
                               Column('teams_id', ForeignKey('teams.id'), primary_key=True),
                               Column('games_id', ForeignKey('games.id'), primary_key=True)
                               )

