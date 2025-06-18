#!/bin/bash

# Função para preparar o ambiente
prepare() {
    bash scripts/prepare.sh
}

# Função para resetar o banco de dados
reset_database() {
    cd scripts && bash reset_database.sh && cd ..
}

# Função para iniciar os serviços
start_services() {
    bash scripts/start_services.sh
}

# Função para executar reset_database e start_services em sequência
run() {
    reset_database
    start_services
}

# Menu para selecionar a tarefa
case $1 in
    prepare)
        prepare
        ;;
    reset_database)
        reset_database
        ;;
    start_services)
        start_services
        ;;
    run)
        run
        ;;
    *)
        echo "Uso: $0 {prepare|reset_database|start_services|run}"
        exit 1
        ;;
esac