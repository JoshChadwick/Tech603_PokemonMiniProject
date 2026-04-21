from PokemonObject import *
from pokemon_api_data import get_pokemon_list, get_chosen_pokemon, get_random_pokemon, get_pokemon_details



class Game():
    def __init__(self):
        self.p1
        self.p2


    def decide_pokemon(self):
        #PRINT LIST OF POKEMON
        name = input("Choose ")

        name, attack, defense, moves = pokeJson.get_pokemon()
        self.p1 = PokemonObject(name, attack, defense, moves)

        #PRINT LIST OF POKEMON
        name = input("Choose ")

        name, attack, defense, moves = pokeJson.get_pokemon()
        self.p2 = PokemonObject(name, attack, defense, moves)


    def main(self):

        self.decide_pokemon()
        while True:
            self.p2.take_damage(self.p1.calculate_damage(self.p2.defense))

            self.p1.take_damage(self.p2.calculate_damage(self.p1.defense))

            print("Name:",self.p1.name)
            print("Hp:",self.p1.hp)

            print("Name:",self.p2.name)
            print("Hp:",self.p2.hp)


            if not self.p1.isAlive():
                print(f"{self.p1.name} is DEAD!")


            if not self.p2.isAlive():
                print(f"{self.p1.name} is DEAD!")

            input()



