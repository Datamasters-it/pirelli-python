import json

class JsonMixin:
    @classmethod
    def from_json(cls, s):
        d = json.loads(s)
        return cls(**d)
    
    def to_json(self):
        return json.dumps(self.__dict__)


class Book(JsonMixin):
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year = year


    
    
b = Book(title="Il nome della rosa", author="Umberto Eco", year=1980)

print(b.to_json())

s = '{"title": "Il nome della rosa", "author": "Umberto Eco", "year": 1980}'

libro = Book.from_json(s)

print(libro.author)
