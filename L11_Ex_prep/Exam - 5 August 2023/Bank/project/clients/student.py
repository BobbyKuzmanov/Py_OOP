from project.clients.base_client import BaseClient


class Student(BaseClient):
    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, 2.0)

    def increase_clients_interest(self):
        self.interest += 1.0

# In the student.py file, the class Student should be implemented.
# The student is a type of client. Each student has an initial interest of 2.0 percent.
# Methods
# __init__(name: str, client_id: str, income: float)
#     • In the __init__ method, all the needed attributes must be set.
# increase_clients_interest()
#     • The method increases the client’s interest by 1.0 percent.
