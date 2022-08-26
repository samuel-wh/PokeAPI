
import requests
# Funcion para obtener la lista de los pokemones





def get_detalles(pokemon_list):
    # Obtenemos la lista de los pokemones
    for pokemones in pokemon_list:
        # Almacenamos el nombre
        pokemon_name = pokemones['name']
        # Cambiamos el endpoint con el nombre del pokemon para obtener los detalles
        url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name)
        response = requests.get(url)
        if response.status_code == 200:
            # Obtenemos el json del endpoint
            payload = response.json()

            sprites = payload['sprites']
            sprite = sprites['front_default']

            weight = payload['weight']
            height = payload['height']

            types = payload.get('types')
            if types:
                for types in types:
                    type_list= types['type']
            
            abilities = payload.get('abilities')
            if abilities:
                for abilities in abilities:
                    ability_list = abilities['ability']
            
            moves = payload.get('moves')
            if moves:
                for moves in moves:
                    move_list = moves['move']

        details_list = []


                

            
            