class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def __init__(self, position):
        super().__init__(position)

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(self.PRISON_LOCATION[::])
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {tuple(prisoner.PRISON_LOCATION)}")
print(f"The current position of the prisoner: {tuple(prisoner.position)}")

# You are provided with a code containing a class Prisoner and a class Person.
# A prisoner is a person, but since a prisoner is not free to move an arbitrary distance,
# the Person class can be named FreePerson, then the idea that a Prisoner inherits FreePerson is wrong.
# Rewrite the code and apply the LSP (Liskov Substitution Principle).

# Output:
# The prisoner trying to walk to north by 10 and east by -3.
# The location of the prison: [3, 3]
# The current position of the prisoner: [0, 13]
