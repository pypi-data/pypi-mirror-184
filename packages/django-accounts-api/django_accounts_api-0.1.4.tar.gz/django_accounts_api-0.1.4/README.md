# Django Accounts API

Scenario to support is a compiled javascript capable frontend needing to provide authentication features over api

Caveat enptor, very early days, still being tested in it's first project

# Requirements
- Python 3.7 - 3.11
- Django 3.2 - 4

# Usage

- `pip install ...` or equivalent
- add `'django_accounts_api',` to INSTALLED_APPS
- add `path('/accounts_api/', include('django_accounts_api.urls'))` to your urls
- implement your frontend to use the urls

## Features

See docs...


## Development
1. Install Poetry https://python-poetry.org/docs/#installation

2. Use a virtual environment https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment

3. `poetry install --with dev --no-root` installs dependencies for development

4. `poetry run pre-commit install` installs the pre-commit hooks

5. `pytest` runs tests
