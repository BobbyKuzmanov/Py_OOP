from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        pass



# In the base_equipment.py file, the class BaseEquipment should be implemented. It is a base class for any type of equipment, and it should not be able to be instantiated.
# Structure
# The class should have the following attributes:
#     • protection: int
#         ◦ The value represents the protection of the equipment.
#     • price: float
#         ◦ The value represents the price of the equipment.
# Methods
# __init__(protection: int, price: float)
#     • In the __init__ method, all the needed attributes must be set.
# increase_price()
#     • Method increases the equipment’s price. Keep in mind that each type of equipment implements the method differently.