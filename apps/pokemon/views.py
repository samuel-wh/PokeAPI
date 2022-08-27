
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, 'base/base.html')


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
    return render(request,'pokemon/index.html',{'pokemon':pokemon_info})


def type_list(request,nombre):
    # Endpoint
    url = "https://pokeapi.co/api/v2/pokemon/"
    url+=id_pokemon
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        print(payload.keys())
        """ results = payload.get('results',[])
        
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
    return render(request,'pokemon/index.html',{'pokemon':pokemon_info}) """

def pokemon_details(request, id_pokemon):
    
    url = "https://pokeapi.co/api/v2/pokemon/"
    id_pokemon
    url+=id_pokemon
    response = requests.get(url)
    if response.status_code == 200:
        dir1 = {}
        payload = response.json()
        name = payload['name']
        sprites = payload.get('sprites',[])
        sprite = sprites['front_default']
        weight = payload['weight']
        height = payload['height']
        dir1 = {
            'img':sprite,
            'peso':weight,
            'altura':height,
            'nombre':name
        }
    

        types = payload.get('types',[])
        if types:
            type_list = []
            type_dir = {}
            for types in types:
                type = types['type']
                response.request.get(type['url'])
                if response.status_code == 200:
                    payload = response.json()
                    id_tipo = payload['id']
            type_dir = {'type':type}
            type_list.append(type_dir)

                

        print("\n")
        print(type_list)     

        abilities = payload.get('abilities',[])
        if abilities:
            ability_list = []
            ability_dir = {}
            for abilities in abilities:
                ability = abilities['ability']
                ability_dir = {'ability':ability}
                ability_list.append(ability_dir)

        moves = payload.get('moves',[])
        if moves:
            move_list = []
            move_dir = {}
            for moves in moves:
                move = moves['move']
                move_dir = {'move':move}
                move_list.append(move_dir) 
    return render(request, 'pokemon/pokemon_detalles.html', {'detalle':dir1, 'tipos':type_list, 'habilidades':ability_list, 'movimientos':move_list})