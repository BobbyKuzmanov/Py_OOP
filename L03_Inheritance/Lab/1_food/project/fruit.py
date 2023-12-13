from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        self.name = name
        super().__init__(expiration_date)

# In the fruit.py file, create a class called Fruit which will receive a name (str) and
# an expiration_date (str) upon initialization.
# Fruit should be inherited from Food.