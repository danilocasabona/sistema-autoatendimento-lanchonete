.PHONY: create-folder create-docker run-docker permission-folder stop-docker clean-docker

# subir o projeto
create-folder:
	mkdir -p data/postgres/pgdata

create-clear-docker:
	docker compose build --no-cache

create-docker:
	docker compose build

run-debug-docker:
	docker compose up -d

run-docker:
	docker compose up

permission-folder:
	sudo chmod 777 data/postgres/pgdata -R

# parar o projeto
stop-clear-docker:
	docker compose down -v

stop-docker:
	docker compose down

clean-docker:
	sudo rm -r data/postgres -R