
from django.shortcuts import render
from django.core.urlresolvers import reverse
import requests


# Create your views here.
def index(request):
    return render(request, 'base/base.html')

def pokemon_data(results):
    pokemon_info = []
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
                'id':id_pokemon,    
            }
            pokemon_info.append(dir)

    return pokemon_info

def pokemon_list(request):
    # Endpoint
    offset= request.GET.get("offset",0)
    limit = request.GET.get("limit", 10)
    url = "https://pokeapi.co/api/v2/pokemon/?offset={}&limit={}".format(offset, limit)
    
    response = requests.get(url)
    pokemon_info = []
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
        siguiente = payload['next']
        anterior = payload['previous']
        if anterior:
            anterior = reverse("pokemon_listar") + "?" + (anterior.split("?"))[1]
        dir2 = {
            'next': reverse("pokemon_listar") + "?" + (siguiente.split("?"))[1],
            'previous': anterior
        }
        if results:
            pokemon_info = pokemon_data(results)
    return render(request,'pokemon/index.html',{'pokemon':pokemon_info,'direccion':dir2})

def type_list(request,id_tipo):
    # Endpoint
    url = "https://pokeapi.co/api/v2/type/{}".format(id_tipo)
    response = requests.get(url)
    pokemon_info = []
    pokemon = []
    if response.status_code == 200:
        payload = response.json()
        pokemones = payload.get('pokemon',[])
        if pokemones:
            for pokemones in pokemones:
                pokemon.append(pokemones['pokemon'])
            pokemon_info = pokemon_data(pokemon)
    return render(request,'pokemon/pokemon_tipo.html',{'pokemon':pokemon_info})
def pokemon_details(request, id_pokemon):
    args = id_pokemon
    url = "https://pokeapi.co/api/v2/pokemon/"
    url+= args
    ability_list = []
    type_list = []
    move_list = []
    response = requests.get(url)
    if response.status_code == 200:
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

        abilities = payload.get('abilities',[])
        if abilities:
            for abilities in abilities:
                ability = abilities['ability']
                ability_dir = {'habilidad':ability}
                ability_list.append(ability_dir)
        types = payload.get('types',[])
        if types:
            for types in types:
                type = types['type']
                response = requests.get(type['url'])
                if response.status_code == 200:
                    payload = response.json()
                    id_tipo = payload['id']
                    type_dir = {'type':type,'id':id_tipo}
                    type_list.append(type_dir)

        moves = payload.get('moves',[])
        if moves:
            for moves in moves:
                move_dir = {'move':moves}
                move_list.append(move_dir) 
    else:
        dir1 = {}
    return render(request, 'pokemon/pokemon_detalles.html', {'detalle':dir1, 'tipos':type_list, 'habilidades':ability_list, 'movimientos':move_list})
