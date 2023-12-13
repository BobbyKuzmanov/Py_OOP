class Player:
    player_names = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name not valid!")

        if value in Player.player_names:
            raise Exception(f"Name {value} is already used!")

        Player.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True

        return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
# In the player.py file, the class Player should be implemented. It will store the info of each player.
# Structure
# The class should have the following attributes:
#     • name: str
#         ◦ If it's set to an empty string, raise ValueError with the message "Name not valid!"
#         ◦ There should not be two players with the same name (they all should be unique).
#         If a second player is created with the same name,
#         raise Exception with the message "Name {name} is already used!"
#     • age: int
#         ◦ If the player is under 12 years old,
#         raise ValueError with the message "The player cannot be under 12 years old!"
#     • stamina: int
#         ◦ An optional parameter, 100 by default
#         ◦ Stamina's max value is 100, and its min value is 0
#         ◦ If it is less than zero or more than 100, raise ValueError with the message "Stamina not valid!"
#     • need_sustenance: bool
#         ◦ Returns if the player's stamina is less than 100. It is read-only, and it should not be able to be set
# Methods
# __init__(name: str, age: int, stamina: int)
# Upon initialization, all the needed attributes must be set.
# __str__()
#       Override the method so that its return the player's data in the format:
#       "Player: {player_name}, {age}, {stamina}, {need_sustenance}"
