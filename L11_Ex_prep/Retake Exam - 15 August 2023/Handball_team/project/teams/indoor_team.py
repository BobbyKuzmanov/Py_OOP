from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500.0)

    def win(self):
        self.advantage += 145
        self.wins += 1


# In the indoor_team.py file, the class IndoorTeam should be implemented.
# The indoor team is a type of team. Each indoor team has an initial budget of 500.0 EUR.
# Methods
# __init__(name: str, country: str, advantage: int)
#     • In the __init__ method, all the needed attributes must be set.
# win()
#     • The method increases the team’s advantage by 145 points. Remember to increase the winning
#     number as well.