from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name: str, energy=25):
        super().__init__(name, energy)

    @property
    def supply_type(self):
        return 'Food'

# In the food.py file, the class Food should be implemented. The food is a type of supply.
# A food has 25 units of energy as an optional parameter.
