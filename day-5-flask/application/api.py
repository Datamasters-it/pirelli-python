from fastapi import FastAPI, Request, HTTPException, Query, Depends
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel
from typing import List, Optional
import numpy as np

from flask import Flask, render_template
import uvicorn

from application.pokemon.db import KNNSearchEngine
from application.pokemon.models import PokemonResponse, PokemonFeatures

app = FastAPI()
flask_app = Flask(__name__)

app.mount("/blog", WSGIMiddleware(flask_app))


@flask_app.get("/")
async def blog_page():
    return "Blog page"

@flask_app.get("/about")
async def about_page():
    return "About page"




@app.get("/")
async def read_root():
    return {"text": "YO!"}


@app.get("/knn_cozzalo", response_model=List[PokemonResponse])
async def search_knn(
    hp: int,
    attack: int,
    defense: int,
    sp_atk: int,
    sp_def: int,
    speed: int,
    k: int = 5
):
    model = KNNSearchEngine("application/pokemon/assets/pokemon.csv")
    query = np.array([[hp, attack, defense, sp_atk, sp_def, speed]])
    try:
        neighbors_indices = model.knn_search(query, k)
        results = model.df.iloc[neighbors_indices]
        return results.to_dict(orient='records')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_pokemon_features(
    hp: int = Query(...),
    attack: int = Query(...),
    defense: int = Query(...),
    sp_atk: int = Query(...),
    sp_def: int = Query(...),
    speed: int = Query(...)
) -> PokemonFeatures:
    return PokemonFeatures(
        hp=hp, 
        attack=attack, 
        defense=defense, 
        sp_atk=sp_atk, 
        sp_def=sp_def, 
        speed=speed
    )



@app.get("/knn", response_model=List[PokemonResponse])
async def search_knn(features: PokemonFeatures = Depends(get_pokemon_features), k: int = 5):
    model = KNNSearchEngine("application/pokemon/assets/pokemon.csv")
    query = np.array([[features.hp, features.attack, features.defense, features.sp_atk, features.sp_def, features.speed]])
    try:
        neighbors_indices = model.knn_search(query, k)
        results = model.df.iloc[neighbors_indices]
        return results.to_dict(orient='records')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/search", response_model=list[PokemonResponse])
async def search_pokemon(query: Optional[str] = None) -> list[PokemonResponse]:
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    # Inizializza il database dei Pokémon
    model = KNNSearchEngine("application/pokemon/assets/pokemon.csv")
    results = model(query)
    return results


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
