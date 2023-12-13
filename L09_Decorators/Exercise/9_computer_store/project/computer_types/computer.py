from abc import ABC, abstractmethod
from math import sqrt


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError('Manufacturer name cannot be empty.')

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError('Model name cannot be empty.')

        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def ram_sizes(self):
        pass

    @property
    @abstractmethod
    def computer_type(self):
        pass

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(
                f'{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')

        if ram not in self.ram_sizes:
            raise ValueError(
                f'{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')

        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor] + self.ram_sizes[ram]

        return f'Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$.'

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

# In the computer.py file, the class Computer should be implemented.
# It is a base class for any type of computer, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • manufacturer: str
#     • A string that represents the manufacturer's name.
#     • If the string is empty or contains only whitespaces,
#     raise ValueError with the message: "Manufacturer name cannot be empty."
#     • model: str
#     • A string that represents the computer's model name.
#     • If the string is empty or contains only whitespaces,
#     raise ValueError with the message: "Model name cannot be empty."
#     • processor: str
#     • A string that represents the computer's processor.
#     • Should be set to None upon initialization
#     • ram: int
#     • An integer that represents the computer's RAM memory.
#     • Should be set to None upon initialization
#     • price: int
#     • An integer that represents the computer's price.
#     • Should be set to 0 upon initialization
# Methods
# __init__(manufacturer: str, model: str)
#     • In the __init__ method, all the needed attributes must be set.
#  configure_computer(processor: str, ram,: int)
#     • Every type of computer should be configurable
#     • Valid types: "Laptop", "Desktop Computer"
# __repr__()
#     • Representsts the class as: "{ manufacturer } { model } with { processor } and { ram }GB RAM"
