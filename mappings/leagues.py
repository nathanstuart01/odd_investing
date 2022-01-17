from enum import Enum


class Leagues(Enum):
    NFL = 'National Football League'

    def describe_league(self):
        return self.name, self.value

    def league_seasons(self):
        if self.value == 'National Football League':
            return [{'season year': 2021}]
        else:
            return None
