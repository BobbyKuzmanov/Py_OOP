from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price *= 1.1




# In the elbow_pad.py file, the class ElbowPad should be implemented. An elbow pad is a type of equipment. Each elbow pad has a protection of 90 and a price of 25.0 EUR.
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# increase_price()
#     • The method increases the price by 10% (ten percent).