from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]
        return cls(name, id, year, month_name[month], age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. "
                f"Status: {'rented' if self.is_rented else 'not rented'}")


# Upon initialization, the DVD class should receive the following parameters:
#     name: str, id: int, creation_year: int, creation_month: str, age_restriction: int.
#     Each DVD should also have an attribute called is_rented (False by default)
# Create a method called from_date(id:
#     int, name: str, date: str, age_restriction: int) - it should create a new instance using the provided data.
#     The date will be in the format "day.month.year" - all of them should be numbers.
# Implement the __repr__ method so it returns the following string:\
#     "{id}: {name} ({creation_month} {creation_year}) has age restriction {age_restriction}.
#    Status: {rented/not rented}"