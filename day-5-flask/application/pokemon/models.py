# pokemon/models.py

from pydantic import BaseModel
from typing import Any

class PokemonResponse(BaseModel):
    name      : str
    type1     : str
    type2     : Any
    total     : int
    hp        : int
    attack    : int
    defense   : int
    sp_atk    : int
    sp_def    : int
    speed     : int
    generation: int
    legendary : bool


class PokemonFeatures(BaseModel):
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int