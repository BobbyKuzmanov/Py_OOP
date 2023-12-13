from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS_TYPES = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception(f"Invalid equipment type!")
        equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS_TYPES:
            raise Exception(f"Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        team = self.VALID_TEAMS_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1
        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        team1_points = self.get_team_points(team1)
        team2_points = self.get_team_points(team2)
        winner = team1 if team1_points > team2_points else team2 if team2_points > team1_points else None
        if winner is None:
            return "No winner in this game."
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:"]
        [result.append(t.get_statistics()) for t in teams]
        return "\n".join(result)

    @staticmethod
    def get_team_points(team: BaseTeam):
        return team.advantage + sum(e.protection for e in team.equipment)

# In the tournament.py file, the class Tournament should be implemented.
# It will contain the functionality of the project.
# Structure
# The class should have the following attributes:
#     • name: str
#         ◦ The value represents the name of the tournament.
#         ◦ The name should contain letters and digits only. If the name has other symbols,
#         raise a ValueError with the message: "Tournament name should contain letters and digits only!"
#     • capacity: int
#         ◦ The number of teams а Tournament can have.
#     • equipment: list
#         ◦ Empty list that will contain all equipment (objects) that are created.
#     • teams: list
#         ◦ Empty list that will contain all teams (objects) that are created.
# Methods
# __init__(name: str, capacity: int)
#     • In the __init__ method, all the needed attributes must be set.
# add_equipment(equipment_type: str)
# The method creates equipment of the given type and adds it to the equipment collection.
#     • If the equipment’s type is not valid, raise an Exception with the following message:
# "Invalid equipment type!"
#     • Otherwise, create the equipment, add it to the equipment list, and return the following message:
# "{equipment_type} was successfully added."
#     • Valid types of equipment are: "KneePad" and "ElbowPad"
# add_team(team_type: str, team_name: str, country: str, advantage: int)
# The method creates a team of the given type and adds it to the teams’ collection.
# All teams’ names will be unique.
#     • First, check if the team type is valid, and if not raise an Exception with the following message:
# "Invalid team type!"
#     • Then, check if there is an available tournament capacity, and if not return the following message:
# "Not enough tournament capacity."
#     • Otherwise, create the team, add it to the teams’ list, and return the following message:
# "{team_type} was successfully added."
#
#     • Valid types of teams are: "OutdoorTeam" and "IndoorTeam".
# sell_equipment(equipment_type: str, team_name: str)
# The method adds the equipment of the given type to the team’s equipment collection. Both equipment and team will always exist.
#     • First, check if the equipment can be sold to the team. If the team’s budget is not enough to buy the equipment, raise an Exception with the following message:
# "Budget is not enough!"
#     • If the equipment can be sold to the team, remove it from the tournament's equipment collection, and add it to the team’s equipment collection. Decrease the budget with the equipment’s price. Return the following message:
# "Successfully sold {equipment_type} to {team_name}."
#     • Take the last equipment of the given type from the collection.
# remove_team(team_name: str)
# The method removes the team with the given name from the tournament.
#     • First, check if there is a team with the given name in the team’s collection. If not, raise an Exception with the following message:
# "No such team!"
#     • Then, check if the team has any wins. If so, raise an Exception with the following message:
# "The team has {number_of_wins} wins! Removal is impossible!"
#     • If the team can be removed successfully, remove it from the tournament, and return the following message: "Successfully removed {team_name}."
# increase_equipment_price(equipment_type: str)
# The method increases the price for all equipment of the given type that is in the tournament’s equipment collection. The equipment type will be one of the valid types (KneePad or ElbowPad). When all prices for the given equipment type are successfully changed (hint: use increase_price() method), return the following message:
# "Successfully changed {number_of_changed_equipment}pcs of equipment."
#     • Equipment that is already sold to teams should not be affected.
# play(team_name1: str, team_name2: str)
# The method starts a game between two teams. The team’s names will always exist and will be unique.
#     • First, check if both teams are from the same type (IndoorTeam or OutdoorTeam). If not, raise an Exception with the following message:
# "Game cannot start! Team types mismatch!"
#     • Then, sum the points of advantage and the total protection for each team. You will need to compare the results:
#         ◦ The team with the greater result (the sum of advantage points and total protection) wins. You have to increase the winner’s points of advantage and the number of wins. You can use the team’s win() method. Return the following message:
# "The winner is {team_name_of_winner}."
#         ◦ In case the teams happen to be with equal results, return the following message:
# "No winner in this game."
# get_statistics()
# Returns information about the tournament and the teams in the tournament, sorted by number of wins, descending. Each on a new line. Use the team’s get_statistics() method.
# "Tournament: {tournament_name}
# Number of Teams: {number_of_teams}
# Teams:
# {team1_statistics}
# {team2_statistics}
# …
# {teamN_statistics}"
