import requests

def get_pokemones():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=10"
    r = requests.get(url)
    pokemones = r.json()
    pokemon_list = []
    for i in range(len(pokemones['results'])):
        pokemon_list.append(pokemones['results'][i])
    return pokemon_list

def get_detalles():
    url = "https://pokeapi.co/api/v2/pokemon/1"
    r = requests.get(url)
    detalles = r.json()
    detalles_list = []
    for i in range(len(detalles['abilities'])):
        detalles_list.append(detalles['abilities'][i])
    return detalles_list