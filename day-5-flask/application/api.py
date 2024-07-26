from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from pydantic import BaseModel
from typing import List, Optional

from flask import Flask, render_template
import uvicorn

from application.pokemon.db import KNNSearchEngine
from application.pokemon.models import PokemonResponse

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
