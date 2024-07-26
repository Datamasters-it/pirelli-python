# Pokémon Search Engine

Questo progetto fornisce un motore di ricerca per Pokémon basato su Django. Puoi scegliere di eseguire il progetto direttamente sul tuo ambiente locale o utilizzare Docker per una configurazione containerizzata.

## Setup Locale

### 1. Creazione di un Ambiente Virtuale
Usa conda per creare un nuovo ambiente virtuale:
```bash
conda create -n pirelli-day5-django
```

### 2. Attivazione dell'Ambiente Virtuale

Attiva l'ambiente virtuale appena creato:

```bash
conda activate pirelli-day5-django
```

### 3. Installazione di Django e Altre Dipendenze
Installa Django, Django Rest Framework e Pandas:
```bash
pip install django djangorestframework pandas
```

### 4. Creazione di un Nuovo Progetto Django
Crea un nuovo progetto Django chiamato pokemon:
```bash
django-admin startproject pokemon .
```
### 5. Creazione di una Nuova App
Crea una nuova app all'interno del progetto, ad esempio `search_engine`:
```bash
python manage.py startapp search_engine
```

### 6. Aggiungi la App alle INSTALLED_APPS

Aggiungi `"search_engine"` all'elenco delle `INSTALLED_APPS` nel file `pokemon/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'search_engine',
]

```

### 7. Esegui il Comando per Caricare i Pokémon

Esegui il comando per effettuare le migrazioni iniziali e caricare i dati dei Pokémon nel database:
```bash
python manage.py migrate
python manage.py load_pokemon_data
```



## Setup con Docker

### 1. Avviare i Servizi con Docker Compose

Usa Docker Compose per costruire e avviare i servizi:

```bash
docker-compose up
```


### 2. Caricare i Dati dei Pokémon

Esegui il comando per caricare i dati dei Pokémon nel database utilizzando Docker:
```bash
docker-compose run web python manage.py load_pokemon_data
```


## Accesso all'Applicazione

Puoi accedere all'applicazione all'indirizzo:

```bash
http://localhost:8000
```

Questo conclude le istruzioni di setup per il progetto Pokémon Search Engine. Buon divertimento!