class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."




# In the band.py file, the class Band should be implemented.
# Structure
# The class should have the following attributes:
#     • name: str
#     • A string that represents the name of the band.
#     • If the name is an empty string, raise a ValueError with the message: "Band name should contain at least one character!"
#     • members: list
#     • An empty list that will contain the members (musician objects) of the band.
# Methods
# __init__(name: str)
#     • In the __init__ method, all the needed attributes must be set.
# __str__()
# The method returns the following string: "{name of the band} with {total number of members} members."