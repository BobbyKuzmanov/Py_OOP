from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []  # [Pokemon("pickachu", 100), Pokemon(..., ...)]

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])

        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())

trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))

print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())


# The Trainer class should receive a name (string).
# The Trainer should also have an attribute pokemons (list, empty by default). The Trainer has three methods:
#     • add_pokemon(pokemon: Pokemon)
#         ◦ Adds the pokemon to the collection and returns "Caught {pokemon_name} with health {pokemon_health}".
# Hint: use the pokemon's details method.
#         ◦ If the pokemon is already in the collection, return "This pokemon is already caught"
#         ◦ Hint: to import the Pokemon class, you should add "from project.pokemon import Pokemon"
#     • release_pokemon(pokemon_name: string)
#         ◦ Check if you have a pokemon with that name and remove it from the collection. In the end,
# returns "You have released {pokemon_name}"
#         ◦ If there is no pokemon with that name in the collection, return "Pokemon is not caught"
#     • trainer_data()
#         ◦ The method returns the information about the trainer and his pokemon's collection in the format:
# "Pokemon Trainer {trainer_name}
#  Pokemon count {the amount of pokemon caught}
#  - {pokemon_details1}
#  ...
#  - {pokemon_detailsN}"