#!/bin/bash
ls -a
DB_PATH="../event_ticketing.db"

# Se o banco de dados existir, remove
if [ -f "$DB_PATH" ]; then
  echo "Removendo banco de dados existente: $DB_PATH"
  rm -rf "$DB_PATH"
fi

# Cria o novo banco de dados
echo "Criando novo banco de dados..."
python create_sqlite.py

# Ajusta permissões
chmod +w "$DB_PATH"

echo "Banco de dados criado e permissões ajustadas."