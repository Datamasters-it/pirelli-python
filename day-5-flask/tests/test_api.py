# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from application.api import app as a

client = TestClient(a)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"text": "YO!"}

def test_search_pokemon_no_query():
    response = client.get("/search")
    assert response.status_code == 400
    assert response.json() == {"detail": "Query parameter is required"}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Portal Gun"
    assert data[1]["name"] == "Plumbus"
    
def test_blog_page():
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.text == "Blog page"

def test_about_page():
    response = client.get("/blog/about")
    assert response.status_code == 200
    assert response.text == "About page"

def test_search_pokemon_with_query():
    '''
    Usare "params" -> dict per passare dei parametri all'endpoint di ricerca
    controllare che dato di ritorno:
    - sia una lista
    - abbia lunghezza > 0
    - tutti i campi siano presenti nella risposta
    '''
    pass

def test_search_pokemon_with_query():
    '''
    Usare "params" -> dict per passare dei parametri all'endpoint di ricerca
    controllare che dato di ritorno:
    - sia una lista
    - abbia lunghezza = 0
    '''
    pass