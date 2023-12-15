makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

build:
	docker compose up --build -d --remove-orphans