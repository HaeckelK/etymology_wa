# etymology_wa 1.0.0

## Introduction
Small scale flask web app to provide links to etymology resources for a given word. Landing page provides input form to enter word, which will check search urls for wiktionary, etymologyonline and dictionary.com. If the search urls are status 200, will redirect to a html page for the word with the links presented.

Searched for words and status 200 urls are saved in sqlite database (path specified in config.ini).

## Initial Setup
- Copy config_template.ini to config.ini and add database path included .db extension.

## Production


## Development
### Launcing
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --port=5007
flask run --host=1.0.0.0
```
### Releasing
```bash
bump2version minor --dry-run --verbose
bump2version major
```

### Code checks
From root
```bash
mypy .
pytest
flake8 --max-line-length 120
```

## curl example
