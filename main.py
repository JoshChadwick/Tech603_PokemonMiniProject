from PokemonObject import *
from pokemon_api_data import *
from pokemon_api_data import get_pokemon_list, get_chosen_pokemon, get_random_pokemon, get_pokemon_details



class Game():
    def __init__(self):
        self.p1 = None
        self.p2 = None


    def decide_pokemon(self):
        for pokemon_name in get_pokemon_list():
            print(pokemon_name)
        name = input("Choose ")

        details = get_pokemon_details(name)
        self.p1 = PokemonObject(details["name"], details["ability"], details["height"], details["weight"], details["attack"], details["defense"], details["speed"],100)

        for pokemon_name in get_pokemon_list():
            print(pokemon_name)
        name = input("Choose ")

        details = get_pokemon_details(name)
        self.p2 = PokemonObject(details["name"], details["ability"], details["height"], details["weight"], details["attack"], details["defense"], details["speed"],100)


    def main(self):

        self.decide_pokemon()
        while True:
            self.p2.take_damage(self.p1.calculate_damage(self.p2.defense))

            self.p1.take_damage(self.p2.calculate_damage(self.p1.defense))

            print("Name:",self.p1.name)
            print("Hp:",self.p1.hp)

            print("Name:",self.p2.name)
            print("Hp:",self.p2.hp)


            if not self.p1.is_alive():
                print(f"{self.p1.name} is DEAD!")


            if not self.p2.is_alive():
                print(f"{self.p1.name} is DEAD!")

            input()


game = Game()
game.main()
