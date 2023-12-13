from project.supply.supply import Supply


class Drink(Supply):

    def __init__(self, name: str):
        super().__init__(name, energy=15)

    @property
    def supply_type(self):
        return 'Drink'
# In the drink.py file, the class Drink should be implemented.
# The drink is a type of supply. Each drink has 15 initial units of energy.
