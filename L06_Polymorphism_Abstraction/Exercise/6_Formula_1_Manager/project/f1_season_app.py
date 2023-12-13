from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name, budget):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name, red_bull_pos, mercedes_pos):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        return self.get_race_results(race_name, red_bull_pos, mercedes_pos)

    def get_race_results(self, race_name, red_bull_pos, mercedes_pos):
        ahead_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_revenue}. " \
               f"Mercedes: {mercedes_revenue}. " \
               f"{ahead_team} is ahead at the {race_name} race."

# In the f1_season_app.py file, the class F1SeasonApp should be implemented.
# It will contain all the functionality of the project.
# Structure
# The class should have the following attributes:
#     • red_bull_team: RedBullTeam
#         ◦ It should be set to None on initialization.
#     • mercedes_team: MercedesTeam
#         ◦ It should be set to None on initialization.
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# register_team_for_season(team_name: str, budget: int)
#     • Valid team names: "Red Bull", "Mercedes"
#     • If a team name is valid, register the team with the corresponding name and return the following message:
# "{ team name } has joined the new F1 season."
#     • If a team name is invalid, raise ValueError with the message: "Invalid team name!"
# Note: There won't be a case where a valid team tries to register for a second time.
#  new_race_results(race_name: str, red_bull_pos: int, mercedes_pos: int)
#     • If Red Bull or Mercedes haven't registered yet,
#     raise an Exception with the following message: "Not all teams have registered for the season."
#     • Otherwise, find which team has the better position in the race, calculate every team's revenue,
#     update their budget, and return the following message: "Red Bull: { Red Bull revenue message }.
#     Mercedes: { Mercedes revenue message }. { team with better position } is ahead at the { race name } race."
#     • Note: Teams' positions will always be valid.