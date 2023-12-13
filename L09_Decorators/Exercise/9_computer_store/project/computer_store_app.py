from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    COMPUTER_VALID_TYPES = {
        "Laptop": Laptop,
        "Desktop Computer": DesktopComputer
    }

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ComputerStoreApp.COMPUTER_VALID_TYPES:
            raise ValueError(f'{type_computer} is not a valid type computer!')

        new_computer = ComputerStoreApp.COMPUTER_VALID_TYPES[type_computer](manufacturer, model)
        new_computer_configuration = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)

        return new_computer_configuration

    def find_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.ram >= wanted_ram and wanted_processor == computer.processor:
                return computer

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_to_sell = self.find_computer(client_budget, wanted_processor, wanted_ram)

        if not computer_to_sell:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer_to_sell.price
        self.warehouse.remove(computer_to_sell)

        return f'{computer_to_sell} sold for {client_budget}$.'

# In the computer_store_app.py file, the class ComputerStoreApp should be implemented.
# It will contain all the functionality of the project.
# Structure
# The class should have the following attributes:
#     • warehouse: list
#     • A list that will store the built computers.
#     • Should be empty upon initialization
#     • profits: int
#     • An integer that represents the store profits.
#     • Should be set to 0 on initialization
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# build_computer(type_computer: str, manufacturer: str, model: str, processor: str, ram: int)
#     • Valid types of computers are: "Desktop Computer", "Laptop"
#     • If a computer type isn't valid, raise ValueError with the message:
#     "{ type computer } is not a valid type computer!"
#     • Otherwise, configure the computer, add it to the warehouse, and return the result from the configuration.
# sell_computer(client_budget: int, wanted_processor: str, wanted_ram: int)
#     • Search for a computer in the warehouse. To sell a computer, it has to meet the following criteria:
#         ◦ The computer's price is less than or equal to the client's budget.
#         ◦ The computer has the same processors as the one requested by the client.
#         ◦ The computer's RAM is more or equal to the one requested by the client.
#     • If you can't find a computer to sell, raise an Exception with the message:
#     "Sorry, we don't have a computer for you."
#     • If you find a computer that meets the criteria, sell it at the client's budget price,
#     add the difference between the sale price and the build price to the store profits,
#     and return the following message: "{ computer } sold for { client budget }$."
