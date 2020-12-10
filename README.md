# HumanaEthica website

This is a Django-CMS based project. Currently no apps exist, but they can be
easily incorporated into the site.

## Prepare environment

1. Install Python >=3.7
2. [Install Poetry](https://python-poetry.org/docs/)
3. Install dependencies in virtualenv  
   `poetry install`
4. Switch to virtualenv  
   `poetry shell`

## Run a development server

`./manage.py runserver`

## Run a production server

- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
- https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

## Translation

```bash
# Collect translation strings
./manage.py makemessages -l pt

# ... translate the file in locale/pt/LC_MESSAGES/django.po ...

# Compile the messages back
./manage.py compilemessages
```
