#!/bin/bash

echo "👉 Instalando dependências..."

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

for service in services/*/requirements.txt; do
    echo "🔹 Instalando dependências de $(dirname $service)"
    pip install -r $service
done

echo "✅ Ambiente preparado com sucesso."