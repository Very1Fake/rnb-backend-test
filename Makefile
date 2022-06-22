compose_file := docker-compose.yaml
compose := docker compose -f $(compose_file)

build:
	$(compose) build

migrate:
	$(compose) exec web python manage.py migrate

up:
	$(compose) up -d

up-build: build
	$(compose) up -d

down:
	$(compose) down
