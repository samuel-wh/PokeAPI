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
                    id_pokemon = payload['id']
                    sprite = sprites['front_default']
                    dir = {
                        'name':name, 
                        'sprite':sprite, 
                        'id':id_pokemon
                    }
                    pokemon_info.append(dir)
    return render(request,'pokemon/pokemon_listar.html',{'pokemon':pokemon_info})

