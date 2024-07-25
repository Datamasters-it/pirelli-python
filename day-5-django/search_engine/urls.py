# pokemon/urls.py

from django.urls import path
from .views import PokemonSearch

urlpatterns = [
    path('search/', PokemonSearch.as_view(), name='pokemon-search'),
]
