
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, 'base/index.html')


def pokemon_list(request):
    # Endpoint
    url = "https://pokeapi.co/api/v2/pokemon/?limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
        if results:
            pokemon_info = []
            dir = {}
            for pokemon in results:
                name = pokemon['name']
                response = requests.get(pokemon['url'])
                if response.status_code == 200:
                    payload = response.json()
                    sprites = payload.get('sprites',[])
                    id_pokemon = payload.get('id',[])
                    sprite = sprites['front_default']
                    dir = {
                        'name':name, 
                        'sprite':sprite, 
                        'id':id_pokemon
                    }
                    pokemon_info.append(dir)
    return render(request,'pokemon/pokemon_listar.html',{'pokemon':pokemon_info})

def pokemon_details(request, id_pokemon):
    

    url = "https://pokeapi.co/api/v2/pokemon/{}".format(id_pokemon)
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_details = []
        dir1 = {}
        payload = response.json()

        sprites = payload.get('sprites',[])
        sprite = sprites['front_default']
        weight = payload['weight']
        height = payload['height']
        dir1 = {
                'sprite':sprite,
                'weight':weight,
                'height':height,
        }

        """ types = payload.get('types',[])
        if types:
            type_list = []
            dir_type = {}
            for types in types:
                type = types['type']

        abilities = payload.get('abilities',[])
        ability = abilities['ability']

        moves = payload.get('moves',[])
        move = moves['move'] """

        
        pokemon_details.append(dir1)
    return render(request, 'pokemon/pokemon_detalles.html', {'detalle':pokemon_details})