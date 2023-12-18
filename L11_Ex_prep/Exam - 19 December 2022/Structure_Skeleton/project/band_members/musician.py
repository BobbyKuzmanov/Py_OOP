from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, name: str,age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self,new_skill: str):
        if new_skill not in self.__class__.__skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

# learn_new_skill(new_skill: str)
# Each musician can learn a new skill (one at a time):
#     • If the new skill is not in the skills available for the type of musician,
#     raise a ValueError with the message "{new skill} is not a needed skill!"
#     • If the new skill is already learned, raise an Exception with the message "{new skill} is already learned!"
#     • If everything is okay, return the following message: "{musician name} learned to {new skill}."