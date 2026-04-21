"""
Guidance:

Work in your groups of 2-3 to make a Pokemon battler (single game for each group)
API documentation: PokéAPI (pokeapi.co)
Recommended early on: Understand the Pokemon starter code (code below) to fully understand accessing data from the API
The Pokémon data MUST come from the PokeApi
Assigning Pokemon to each player:
    Get random Pokémon for at least the CPU player (Human player can be chosen or random)
Game can be for one or two players
Pokémon should fight and a winner should be declared in some way
No Pygame. Focus on interacting with the API, should be a CLI game
Be as creative as you like after this. Can you incorporate different abilities/stats etc.?
Try and work collaboratively on the one repo using Git
"""

import random
import requests
import json

# Get the list of pokemon from the API
def get_pokemon_list():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    response_json = response.json()
    results = response_json["results"]
    pokemon_list = []
    for pokemon in results:
        pokemon_list.append(pokemon["name"])
    # print("\npokemon_list: ", pokemon_list)
    return pokemon_list

def get_random_pokemon():
    pokemon_list = get_pokemon_list()
    rand_pokemon = random.choice(pokemon_list)
    print("\nrandom pokemon: ", rand_pokemon)
    return get_pokemon_details(rand_pokemon)

def get_chosen_pokemon():
    # Ask the user to choose a pokemon
    print('\nEnter your pokemon:')
    # Get the user's choice
    choice = input().lower()
    print("\nchosen pokemon: ", choice)
    return get_pokemon_details(choice)

# Get the specified pokemon's data from the API
def get_pokemon_details(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    response = requests.get(url)
    pokemon_data = json.loads(response.text)
    name = pokemon_data["name"]
    abilities = pokemon_data['abilities'][0]
    ability_name = abilities['ability']['name']
    height = f"{(int(pokemon_data['height']))/10} m"
    weight = f"{(int(pokemon_data['weight']))/10} kgs"
    stats = pokemon_data["stats"]
    hp = stats[0]["base_stat"]
    attack = stats[1]["base_stat"]
    defense = stats[2]["base_stat"]
    speed = stats[5]["base_stat"]
    detail = {"name": name, "ability": ability_name,
            "height": height, "weight": weight,
            "HP": hp, "attack": attack,
            "defense": defense, "speed": speed}
    print("\ndetails: ", detail)
    return detail

if __name__ == "__main__":
    print("Testing pokemon_api_data.py...")
    print(get_random_pokemon())
    print("\nNow testing chosen pokemon:")
    details = get_chosen_pokemon()
    print(details)








