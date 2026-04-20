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

import requests
import json
from pprint import pprint

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
print("\njson:", response.json())
print("\ncontent:", response.content)
pokemon_list = json.loads(response.text)['results']
print("\nlist: ", pokemon_list)

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)
print("\npokemon_data", pokemon_data)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height /10
weight_formatted = weight /10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) +"(kgs)")
print('Height: {}'.format(height_formatted) +"(m)")
print('Ability: {}'.format(ability['name']))