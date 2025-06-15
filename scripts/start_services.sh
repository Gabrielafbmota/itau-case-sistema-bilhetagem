#!/bin/bash
set -e

echo "🔧 Iniciando os serviços..."

BASE_DIR=$(dirname "$0")

# USER SERVICE
echo "📦 Instalando dependências do user-service..."
pip install -r "$BASE_DIR/user-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando user-service na porta 8000..."
python3 "$BASE_DIR/user-service/main.py" &

# Aguarda 5 segundos para garantir que o serviço de usuário esteja ativo
sleep 5

# PRODUCT SERVICE
echo "📦 Instalando dependências do product-service..."
pip install -r "$BASE_DIR/product-service/requirements.txt" --break-system-packages

echo "🚀 Iniciando product-service na porta 8001..."
python3 "$BASE_DIR/product-service/main.py" &

echo "✅ Todos os serviços foram iniciados!"
wait
