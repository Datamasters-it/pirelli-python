# pokemon/management/commands/load_pokemon_data.py

from django.core.management.base import BaseCommand
from search_engine.views import load_data_from_csv


class Command(BaseCommand):
    help = 'Load Pokémon data from CSV file'

    def handle(self, *args, **kwargs):
        load_data_from_csv()
        self.stdout.write(self.style.SUCCESS('Successfully loaded Pokémon data'))
