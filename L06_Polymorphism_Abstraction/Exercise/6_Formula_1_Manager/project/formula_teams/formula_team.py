from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_for_one_race(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos):
        revenue = 0

        for positions in self.sponsors.values():
            for pos in positions:
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        revenue -= self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

# In the formula_team.py file, the class FormulaTeam should be implemented.
# It is a base class for any type of formula team, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • budget: int
#     • An integer that represents the budget of the team.
#     • If the budget is less than 1 000 000,
#     raise ValueError with the message: "F1 is an expensive sport, find more sponsors!"
# Methods
# __init__(budget: int)
#     • In the __init__ method, all the needed attributes must be set.
#  calculate_revenue_after_race(race_pos: int)
#     • Each team should be able to calculate their revenue
#     • Each team has its unique sponsors
#         ◦ Sponsors give the team money if they finish in a certain position or better
#     • Each team has a different amount of expenses
