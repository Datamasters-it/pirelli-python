# pokemon/views.py

import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializers import PokemonSerializer
import pandas as pd

class PokemonSearch(APIView):
    def get(self, request):
        serializer = PokemonSerializer(data=request.GET)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        name = request.GET.get('name', None)
        type = request.GET.get('type', None)

        if not name and not type:
            return Response({"detail": "At least one query parameter (name or type) is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Pokemon.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        if type:
            queryset = queryset.filter(type__icontains=type)
        
        serializer = PokemonSerializer(queryset, many=True)
        return Response(serializer.data)

# Funzione per caricare i dati dal CSV
def load_data_from_csv():
    csv_file = os.path.join(os.path.dirname(__file__), 'data', 'pokemon.csv')
    data = pd.read_csv(csv_file)
    for _, row in data.iterrows():
        Pokemon.objects.get_or_create(name=row['name'], type=row['type1'])
