from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: dict[Topping.topping_type, Topping.weight] = {}
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())


# Create a class called Pizza. Upon initialization, it should receive:
#  • name: str - if the name is an empty string,
#     raise a ValueError with the message "The name cannot be an empty string"
#  • dough: Dough - if the dough is None,
#     raise a ValueError with the message "You should add dough to the pizza"
#  • max_number_of_toppings: int – represents the maximum number of toppings the
#  pizza should have. If it is 0 or less,
#  raise a ValueError with the message "The maximum number of toppings cannot be less or equal to zero"
#  • toppings: dict – empty dictionary upon initialization that will contain the topping
#  type as a key and the topping's weight as a value.
# The class should also have 2 instance methods:
#     • add_topping(topping: Topping)
#         ◦ Add a new topping to the dictionary
#     • If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
#     • If the topping is already in the dictionary, increase the value of its weight.
#     • calculate_total_weight() - returns the total weight of the pizza (dough's weight and toppings' weight)
# Hint: Use Getters and Setters.