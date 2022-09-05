# {{cookiecutter.inmanta_module_name}} Module

## Running tests

1. Setup a virtual env

```bash
mkvirtualenv inmanta-test -p python3
pip install -r requirements.txt -r requirements.dev.txt
inmanta -vvv module install -e .
```

2. Run tests

```bash
pytest tests
```
