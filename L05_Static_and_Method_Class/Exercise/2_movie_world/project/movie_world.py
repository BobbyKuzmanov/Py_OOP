from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(filter(lambda a: a.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda a: a.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return "\n".join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds]
        ])


# The MovieWorld class should receive one parameter upon initialization: name: str.
# Each MovieWorld instance should also have 2 more attributes: customers (empty list of Customer objects),
# dvds (empty list of DVD objects). The class should also have the following methods:
#     • dvd_capacity() - returns 15 - the DVD capacity of a movie world
#     • customer_capacity() - returns 10 - the customer capacity of a movie world
#     • add_customer(customer: Customer) - add the customer if capacity is not exceeded
#     • add_dvd(dvd: DVD) - add the DVD if capacity is not exceeded
#     • rent_dvd(customer_id: int, dvd_id: int)
#         ◦ If the customer has already rented that DVD return "{customer_name} has already rented {dvd_name}"
#         ◦ If the DVD is rented by someone else, return "DVD is already rented"
#         ◦ If the customer is not allowed to rent the DVD,
#     return "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
#         ◦ Otherwise, the rent is successful (the DVD is rented and added to the customer('s DVDs).
#         'Return "{customer_name} has successfully rented {dvd_name}")
#     • return_dvd(customer_id, dvd_id) - if the DVD is in the customer,
# he/she should return it and the method should return
# the message "{customer_name} has successfully returned {dvd_name}".
# Otherwise, return "{customer_name} does not have that DVD"
#     • __repr__() - return the string representation of each customer and each DVD on separate lines