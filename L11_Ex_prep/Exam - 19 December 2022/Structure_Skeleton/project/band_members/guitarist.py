from project.band_members.musician import Musician


class Guitarist(Musician):
    __skills = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.skills = []

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.__class__.__skills:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."



# In the guitarist.py file, the class Guitarist should be implemented. The guitarist is a type of musician. The skills a guitarist can have or learn are:
#     • "play metal"
#     • "play rock"
#     • "play jazz"
# Methods
# The class should have the following attributes:
# __init__(name: str, age: int)
# In the __init__ method, all the needed attributes must be set.
# learn_new_skill(new_skill: str)
# Add the new skill to the guitarist's skills if the skill is valid and has not been learned already.