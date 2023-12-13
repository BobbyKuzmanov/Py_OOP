from abc import ABC, abstractmethod


class Supply(ABC):

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be an empty string.")

        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value: int):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")

        self.__energy = value

    @property
    @abstractmethod
    def supply_type(self):
        pass

    def details(self):
        return f"{self.supply_type}: {self.name}, {self.energy}"

# In the file supply.py, the class Supply should be implemented. It is a base class of any type of supply,
# and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • name: str
#         ◦ If it is an empty string, raise ValueError with the message "Name cannot be an empty string."
#     • energy: int
#         ◦ If it is a negative number, raise ValueError with the message "Energy cannot be less than zero."
# Methods
# __init__(name: str, energy: int)
# The __init__ method should receive a name and energy.
# details()
# Return the supply's type, name and energy in the format: "{type}: {name}, {energy}".
# The type of the supply is either "Food" or "Drink".
# Hint: override the method in the child classes.
