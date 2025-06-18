.PHONY: prepare reset_database start_services start

prepare:
	bash scripts/prepare.sh

reset_database:
	cd scripts && bash reset_database.sh

start_services:
	bash scripts/start_services.sh

start:
	make reset_database && make start_services

