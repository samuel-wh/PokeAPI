from django.conf.urls import url
from views import  index, pokemon_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pokemon/listar$', pokemon_list, name='pokemon_listar'),

]
