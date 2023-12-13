from abc import ABC, abstractmethod
from typing import List

from project.loans.base_loan import BaseLoan


class BaseClient(ABC):

    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: List[BaseLoan] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value: str):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value: float):
        if value <= 0.0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass

# In the base_client.py file, the class BaseClient should be implemented.
# It is a base class for any type of client, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • name: str
#         ◦ The value represents the name of the client.
#         ◦ If the name is an empty string or contains only white spaces,
#         raise a ValueError with the message: "Client name cannot be empty!"
#     • client_id: str
#         ◦ The value represents the id number of a client. It should contain exactly 10 symbols.
#         ◦ If the client’s id is not 10 symbols long,
#         raise a ValueError with the message: "Client ID should be 10 symbols long!"
#     • income: float
#         ◦ The value represents the income of a client.
#         ◦ If the client’s income is less than or equal to 0.0,
#         raise a ValueError with the message: "Income must be greater than zero!"
#     • interest: float
#         ◦ The value represents the client’s interest.
#     • loans: list
#         ◦ Empty list that will contain loans (objects) each client has.
# Methods
# __init__(name: str, client_id: str, income: float, interest: float)
#     • In the __init__ method, all the needed attributes must be set.
# increase_clients_interest()
#     • Increases the client’s interest. Keep in mind that each type of client implements the method differently.
