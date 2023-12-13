from typing import List
from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player]= []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"

    def get_players(self):
        return self.__players


# Create a class called Team. Upon initialization, it should receive:
#     • Private attribute name: string
#     • Private attribute rating: int
# The class should also have a private instance attribute:
# - players: list - empty list upon initialization that will contain all the players (objects)
# The Team class has the following methods:
#     • add_player(player: Player)
#     • If the player is already in the team, return "Player {name} has already joined"
#     • Otherwise, add the player to the team and return "Player {name} joined team {team_name}"
#     • remove_player(player_name: str)
#     • Remove the player and return him
#     • If the player is not in the team, return "Player {player_name} not found"
