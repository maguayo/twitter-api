# Twitter API

## Install
Create a virtualenv
```shell
virtualenv -p python3 env
source env/bin/activate
```

And then install the requirements.txt
```shell
pip install -r requirements.txt
```

## Development

```bash
python manage.py runserver
```

## Tests
```
pytest -v
pytest --cov=project tests/
```

