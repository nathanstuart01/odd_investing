from enum import Enum


class Nflteams(Enum):
    """NFC"""
    """NFC South"""
    ATL = 'Atlanta Falcons'
    CAR = 'Carolina Panthers'
    TAM = 'Tampa Bay Buccaneers'
    NOR = 'New Orleans Saints'
    """NFC West"""
    ARI = 'Arizona Cardinals'
    SEA = 'Seattle Seahawks'
    SFO = 'San Francisco 49ers'
    LAR = 'Los Angeles Rams'
    """NFC East"""
    DAL = 'Dallas Cowboys'
    WAS = 'Washington Football Team'
    NYG = 'New York Giants'
    PHI = 'Philadelphia Eagles'
    """NFC North"""
    GNB = 'Green Bay Packers'
    MIN = 'Minnesota Vikings'
    CHI = 'Chicago Bears'
    DET = 'Detroit Lions'

    """AFC"""
    """AFC South"""
    TEN = 'Tennesse Titans'
    IND = 'Indianapolis Colts'
    HOU = 'Houston Texans'
    JAX = 'Jacksonville Jaguars'
    """AFC West"""
    KAN = 'Kansas City Chiefs'
    LAC = 'Los Angeles Chargers'
    LVR = 'Las Vegas Raiders'
    DEN = 'Denver Broncos'
    """AFC East"""
    BUF = 'Buffalo Bills'
    NWE = 'New England Patriots'
    MIA = 'Miami Dolphins'
    NYJ = 'New York Jets'
    """AFC NORTH"""
    CIN = 'Cincinnati Bengals'
    PIT = 'Pittsburgh Steelers'
    BAL = 'Baltimore Ravens'
    CLE = 'Cleveland Browns'

    def describe_team(self):
        return self.name, self.value

