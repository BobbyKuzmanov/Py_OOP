import math
from abc import ABC, abstractmethod
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        avg_team_protection = math.floor(sum(e.protection for e in self.equipment) / len(self.equipment)) \
            if self.equipment else 0
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {sum(e.price for e in self.equipment):.2f}\n"
                f"Average Protection: {avg_team_protection}")

# In the base_team.py file, the class BaseTeam should be implemented. It is a base class for any type of
# team, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • name: str
#         ◦ The value represents the name of the team.
#         ◦ If the name is an empty string or contains only white spaces,
#         raise a ValueError with the message: "Team name cannot be empty!"
#     • country: str
#         ◦ The value represents the country of origin of a team. It should be at least 2 symbols
#         long (no leading or trailing white spaces count).
#         ◦ If the team’s country is less than 2 symbols long,
#         raise a ValueError with the message: "Team country should be at least 2 symbols long!"
#     • advantage: int
#         ◦ The value represents the advantage in points that each team has.
#         ◦ If the team’s advantage is less than or equal to 0,
#         raise a ValueError with the message: "Advantage must be greater than zero!"
#     • budget: float
#         ◦ The value represents the team’s budget.
#     • wins: int
#         ◦ The value represents the team’s wins, initially set to 0.
#     • equipment: list
#         ◦ Empty list that will contain equipment(objects) each team has.
# Methods
# __init__(name: str, country: str, advantage: int, budget: float)
#     • In the __init__ method, all the needed attributes must be set.
# win()
#     • Increases the team’s advantage and the number of wins.
#     Keep in mind that each type of team implements the method differently.
# get_statistics()
# The method returns the statistics about the team in the following format, each line on a new row:
# "Name: {team_name}
# Country: {team_country}
# Advantage: {team_advantage} points
# Budget: {team_budget}EUR
# Wins: {number_of_wins}
# Total Equipment Price: {total_price_of_team_equipment}
# Average Protection: {avg_team_protection}"
#     • The budget and the total equipment price should be formatted to the second decimal places.
#     • Average Protection refers to the property protection of each piece of equipment that the team has in its equipment collection. Round the average protection to the smaller integer.
