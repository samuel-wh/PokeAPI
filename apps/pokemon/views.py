from django.shortcuts import render
from django.views.generic import TemplateView
from services import get_detalles, get_pokemones


# Create your views here.
def index(request):
    return render(request, 'base/index.html')


""" def pokemon_list(requests):
    context = {'names': get_name()}
    return render(requests, 'pokemon/pokemon_listar.html', context) """


class GetPokemones(TemplateView):
    template_name = 'pokemon/pokemon_listar.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'pokemones': get_pokemones(),
            'detalles' : get_detalles(),
        }
        return context
