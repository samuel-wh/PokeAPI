from django.conf.urls import url
from views import  pokemon_details, pokemon_list, type_list

urlpatterns = [
    
    url(r'^$', pokemon_list, name='pokemon_listar'),
    url(r'^detalle/(?P<id_pokemon>\d+)/$', pokemon_details, name='pokemon_detalle'),
    url(r'^tipo/(?P<id_tipo>\d+)/$', type_list, name='pokemon_tipo'),
]
