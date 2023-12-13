from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []  # [Player("ivan", 100, 100), ...]

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = Player.DEFAULT_GUILD

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        players_info = '\n'.join([p.player_info() for p in self.players])

        return f"Guild: {self.name}\n" + \
               f"{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

# The Guild class receives a name (string). The Guild should also have one instance attribute
# players (an empty list which will contain the players of the guild).
# The class also has 3 additional methods:
#     • assign_player(player: Player)
#         ◦ Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}".
#     Remember to change the player's guild in the player class.
#         ◦ If he is already in the guild, returns "Player {player_name} is already in the guild."
#         ◦ If the player is in another guild, returns "Player {player_name} is in another guild."
#     • kick_player(player_name: str)
#         ◦ Removes the player from the guild and returns "Player {player_name} has been removed from the guild.".
# Remember to change the player's guild in the player class to "Unaffiliated".
#         ◦ If there is no such player in the guild, returns "Player {player_name} is not in the guild."
#     • guild_info()
#         ◦ Returns the guild's information, including the players in the guild, in the format:
# "Guild: {guild_name}
# {first_player's info}
# …
# {Nplayer's info}"
