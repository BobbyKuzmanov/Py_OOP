from project.vehicle import Vehicle


class Car(Vehicle):
    def drive(self):
        return "driving..."

# Car with a single method drive() that returns: "driving..."
# Car should inherit from Vehicle