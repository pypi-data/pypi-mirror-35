# Flask-PonyAPI

API creation for Pony ORM Entities with no effort.

**Version**: Beta 0.0.1

**Note**: Works only for Python 3

# Quickstart

```python
from flask import Flask
from pony.orm import Database, Required, Optional, db_session

from flask_ponyapi import PonyAPI

app = Flask(__name__)
db = Database()

class Person(db.Entity):
    name = Required(str)
    age = Optional(int)

    class Meta:
        route_base = 'persons'
        route_prefix = '/api'

api = PonyAPI(app, db)


if __name__ == '__main__':
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    with db_session:
        p1 = Person(name='John',  age=20)
        p2 = Person(name="fda", age=123)
    app.run(debug=True)

```

API

| Endpoint | Method | Description |
| --- | --- | --- |
| /api/persons | GET | List all persons |
| /api/persons | POST | Create new  person |
| /api/persons/1 | GET | Single Person |
| /api/persons/1 | PUT | Update single Person |
| /api/persons/1 | Delete | Delete Person |
