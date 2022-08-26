from django.conf.urls import url
from views import GetPokemones, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pokemon/listar$', GetPokemones.as_view(), name='pokemon_listar'),
]
