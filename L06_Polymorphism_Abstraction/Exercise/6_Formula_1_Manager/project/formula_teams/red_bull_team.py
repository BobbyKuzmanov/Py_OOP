from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1_500_000,
                2: 800_000,
            },
            "Honda": {
                8: 20_000,
                10: 10_000,
            },
        }

    @property
    def expenses_for_one_race(self):
        return 250_000

# In the red_bull_team.py, the class RedBullTeam should be implemented.
# Methods
# __init__(budget: int)
#     • In the __init__ method, all the needed attributes must be set.
#  calculate_revenue_after_race(race_pos: int)
#     • Red Bull sponsors:
#         ◦ Oracle:
#             ▪ 1st place – 1 500 000$
#             ▪ 2nd place – 800 000$
#         ◦ Honda:
#             ▪ 8th place – 20 000$
#             ▪ 10th place – 10 000$
#     • Red Bull expenses per race – 250 000$
#     • To calculate the revenue from the race, sum the earned money from the sponsors depending
#     on the position in the race and subtract the expenses
#     • After that, add the result to the team's budget and
#     return the following message: "The revenue after the race is { revenue }$.
#     Current budget { current budget }$"
# Note: Each sponsor gives the money for the best position only.
# If you are 1st and the sponsor gives money for 1st and 2nd positions,
# you get the money only for the 1st position!
