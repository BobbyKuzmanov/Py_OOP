from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price *= 1.2


# In the knee_pad.py file, the class KneePad should be implemented.
# The knee pad is a type of equipment. Each knee pad equipment has a protection of 120 and a price of 15.0 EUR.
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# increase_price()
#     • The method increases the price by 20% (twenty percent).