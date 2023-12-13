from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {
            "Petronas": {
                1: 1_000_000,
                3: 500_000,
            },
            "TeamViewer": {
                5: 100_000,
                7: 50_000,
            },
        }

    @property
    def expenses_for_one_race(self):
        return 200_000

# In the mercedes_team.py, the class MercedesTeam should be implemented.
# Methods
# __init__(budget: int)
#     • In the __init__ method, all the needed attributes must be set.
#  calculate_revenue_after_race(race_pos: int)
#     • Mercedes sponsors:
#         ◦ Petronas:
#             ▪ 1st place – 1 000 000$
#             ▪ 3rd place – 500 000$
#         ◦ TeamViewer:
#             ▪ 5th  place – 100 000$
#             ▪ 7th  place – 50 000$
#     • Mercedes expenses per race – 200 000$
#     • To calculate the revenue from the race, sum the earned money from the sponsors depending on
#  the position in the race and subtract the expenses
#     • After that, add the result to the team's budget and
#  return the following message: "The revenue after the race is { revenue }$. Current budget { current budget }$"
# Note: Each sponsor gives the money for the best position only.
# If you are 1st and the sponsor gives money for 1st and 2nd positions,
# you get the money only for the 1st position!
