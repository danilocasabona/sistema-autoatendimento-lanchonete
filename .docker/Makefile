.PHONY: create-folder create-docker run-docker permission-folder stop-docker clean-docker

create-folder:
	mkdir -p data/postgres/pgdata

create-docker:
	docker compose build --no-cache

run-docker:
	docker compose up -d

permission-folder:
	sudo chmod 777 data/postgres/pgdata -R

stop-docker:
	docker compose down -v

clean-docker:
	sudo rm -r data/postgres -R