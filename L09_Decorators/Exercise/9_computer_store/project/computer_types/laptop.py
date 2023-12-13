from project.computer_types.computer import Computer
from math import sqrt


class Laptop(Computer):
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    @property
    def ram_sizes(self):
        return {2 ** p: p * 100 for p in range(1, int(sqrt(Laptop.MAX_RAM))) if 2 ** p <= Laptop.MAX_RAM}

    @property
    def computer_type(self):
        return 'laptop'

# In the laptop.py file, the class Laptop should be implemented.
# Methods
# __init__(manufacturer: str, model: str)
#     • In the __init__ method, all the needed attributes must be set.
#  configure_computer(processor: str, ram: int)
#     • Laptops can be built only with the available processors for laptops, which are:
#         ◦ AMD Ryzen 9 5950X: 900$
#         ◦ Intel Core i9-11900H: 1050$
#         ◦ Apple M1 Pro: 1200$
#     • Laptops can have a max RAM of 64GB
#         ◦ Valid RAM sizes are 2, 4, 8…64. In other words, all the powers of the number 2 to the max size.
#         ◦ RAM price is defined by the power of the number 2, which gives the RAM size, multiplied by 100.
# For example: 2GB RAM will cost 100$ because 2 = 21  and 1 * 100 = 100. 4GB will be 200$.
#     • If a processor is not in the available processors, raise ValueError with the message:
#     "{ processor } is not compatible with laptop { manufacturer name } { model name }!"
#     • If RAM is not a valid size or is above the max size, raise ValueError with the message:
#     "{ RAM }GB RAM is not compatible with laptop { manufacturer name } { model name }!"
#     • If everything is valid, attach the processor to the computer, attach the RAM, and update the price.
#     Return the following message:
#     "Created { manufacturer name } { model name } with { processor } and { ram }GB RAM for { computer price }$."
