from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return "barking..."

# Dog with a single method bark() that returns: "barking..."
# Both Dog and Cat should inherit from Animal.