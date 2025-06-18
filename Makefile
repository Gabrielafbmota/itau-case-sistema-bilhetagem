.PHONY: up_db up_services start

up_db:
	cd scripts && bash start_db.sh

up_services:
	bash scripts/start_services.sh

start: up_db up_services