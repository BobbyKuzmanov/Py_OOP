from project.clients.base_client import BaseClient


class Adult(BaseClient):
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 4.0)

    def increase_clients_interest(self):
        self.interest += 2.0


# In the adult.py file, the class Adult should be implemented.
# The adult is a type of client. Each adult has an initial interest of 4.0 percent.
# Methods
# __init__(name: str, client_id: str, income: float)
#     • In the __init__ method, all the needed attributes must be set.
# increase_clients_interest()
#     • The method increases the client’s interest by 2.0 percent.
