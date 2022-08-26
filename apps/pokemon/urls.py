from django.conf.urls import url
from views import GetPokemones, PokemonDetalles, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pokemon/listar$', GetPokemones.as_view(), name='pokemon_listar'),
    url(r'^pokemon/detalles$', PokemonDetalles.as_view(), name='pokemon-detalles'),
]
