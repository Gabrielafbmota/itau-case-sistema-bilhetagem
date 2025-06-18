#!/bin/bash

# Services
SERVICES=(user-service product-service event-service ticket-service reservation-service order-service)

echo "👉 Iniciando serviços..."
for service in "${SERVICES[@]}"; do
    echo "🔹 Iniciando $service"
    (cd services/$service && uvicorn src.main:app --host 0.0.0.0 --port $(grep API_PORT .env | cut -d '=' -f2) &)
    sleep 2
done

echo "✅ Todos os serviços foram iniciados."