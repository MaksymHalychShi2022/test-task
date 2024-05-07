# Python Test Task

## To open documentation go to /api/v1/swagger

## Run code with docker compose
```shell
docker compose build
docker compose up
```

## Run code manually 
```shell
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py create_superuser
python manage.py runserver
```

