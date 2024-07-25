from rest_framework import serializers
from .models import Pokemon

def validate_name(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name must be at least 2 characters long")
    return value

def validate_type(value):
    if len(value) < 3:
        raise serializers.ValidationError("Type must be at least 3 characters long")
    return value

class PokemonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name], required=False, allow_blank=True)
    type = serializers.CharField(validators=[validate_type], required=False, allow_blank=True)

    class Meta:
        model = Pokemon
        fields = ['name', 'type']