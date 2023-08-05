# Django NoSQL

> Stream model changes to an upstream NoSQL database

**Supported backends:**

* FireStore
* Mock

## Installation

```
pip install django-nosql
```

## Setup

### Add to installed apps:

```python
INSTALLED_APPS = [
    ...,
    'django_nosql',
    ...
]
```

### Configure NoSQL backends:

In settings.py:

```python
# you can have multiple backends:
NOSQL_BACKENDS = ['firestore']

#  FireStore settings
FIRESTORE_CREDENTIALS_FILE = '/path/to/credentials.json'
```

### Mark up your models:

In `models.py`

```python

Todo(models.model):
    # the nosql collection you'd like to use
    collection = 'todos'
    # A Django Rest Framework serializer for serializing your instance
    serializer_path = 'example_app.models.TodoSerializer'
    # inform django_nosql that you'd like to sync this model
    readonly_sync = True
```

Add signals:

```python
from django_nosql.signals import (
    sync_readonly_db,
    sync_remove_readonly_db
)
```

### Test it out:

There is an example app included in this repo.

To see the sync in action try.

`python manage.py shell` or `docker-compose run --rm web python manage.py shell`

```python

from example_app.models import Todo
todo = Todo.objects.create(text='Setup django nosql')
# you should see this reflected in the 'todos' collection in Firebase
# note: you need to manually refresh the db view when adding a new collection
# you should see the rest of these updates in realtime

# try update:
todo.done = True
todo.save()
# you should see your change reflected in firestore

# delete it:
todo.delete()
# it's gone from Firestore!
```

