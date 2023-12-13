class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: float):
        consumed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= consumed_fuel:
            self.fuel -= consumed_fuel

# Create a base class Vehicle. It should contain the following attributes:
#     • DEFAULT_FUEL_CONSUMPTION: float (constant)
#     • fuel_consumption: float - represents the fuel consumption per kilometer
#     • fuel: float - represents the quantity of fuel in a specific vehicle
#     • horse_power: int
# Upon initialization, the class should receive fuel and horse_power. The DEFAULT_FUEL_CONSUMPTION
# value should be set to the fuel_consumption value.
# Each class should have the following methods:
#     • drive(kilometers) - reduces the fuel based on the traveled kilometers and
#     fuel consumption (km * fuel consumption).
# Keep in mind that you can start driving the vehicle only if you have enough fuel to finish the driving.
# The default fuel consumption for the different vehicles is:
#     • Vehicle is 1.25
#     • SportCar is 10
#     • RaceMotorcycle is 8
#     • Car is 3