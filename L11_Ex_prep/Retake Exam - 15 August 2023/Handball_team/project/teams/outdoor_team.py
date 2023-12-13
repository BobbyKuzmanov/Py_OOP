from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 1000.0)

    def win(self):
        self.advantage += 115
        self.wins += 1



# In the outdoor_team.py file, the class OutdoorTeam should be implemented.
# The outdoor team is a type of team. Each outdoor team has an initial budget of 1000.0 EUR.
# Methods
# __init__(name: str, country: str, advantage: int)
#     • In the __init__ method, all the needed attributes must be set.
# win()
#     • The method increases the team’s advantage by 115 points. Remember to increase the winning
#     number as well.