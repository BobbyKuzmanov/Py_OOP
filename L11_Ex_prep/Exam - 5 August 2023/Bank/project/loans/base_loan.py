from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        pass


# In the base_loan.py file, the class BaseLoan should be implemented.
# It is a base class for any type of loan, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • interest_rate: float
#         ◦ The value represents the interest rate of the loan.
#     • amount: float
#         ◦ The value represents the amount of the loan.
# Methods
# __init__(interest_rate: float, amount: float)
#     • In the __init__ method, all the needed attributes must be set.
# increase_interest_rate()
#     • Method increases the loan’s interest rate.
#     Keep in mind that each type of loan implements the method differently.
