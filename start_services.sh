#!/bin/bash
set -e

echo "🔧 Iniciando os microsserviços..."

BASE_DIR=$(dirname "$0")

# USER SERVICE (iniciar primeiro)
echo "📦 Instalando dependências do user-service..."
pip install -r "$BASE_DIR/user-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando user-service na porta 8000..."
python3 "$BASE_DIR/user-service/main.py" &

# Aguarda para garantir que o serviço esteja disponível
sleep 5

# EVENT SERVICE
echo "📦 Instalando dependências do event-service..."
pip install -r "$BASE_DIR/event-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando event-service na porta 8001..."
python3 "$BASE_DIR/event-service/main.py" &

# PRODUCT SERVICE
echo "📦 Instalando dependências do product-service..."
pip install -r "$BASE_DIR/product-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando product-service na porta 8002..."
python3 "$BASE_DIR/product-service/main.py" &

# TICKET SERVICE
echo "📦 Instalando dependências do ticket-service..."
pip install -r "$BASE_DIR/ticket-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando ticket-service na porta 8003..."
python3 "$BASE_DIR/ticket-service/main.py" &

# ORDER SERVICE
echo "📦 Instalando dependências do order-service..."
pip install -r "$BASE_DIR/order-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando order-service na porta 8004..."
python3 "$BASE_DIR/order-service/main.py" &

echo "✅ Todos os serviços foram iniciados!"
wait
