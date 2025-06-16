#!/bin/bash



echo "🚀 Iniciando todos os serviços com python main.py..."

(cd services/user-service && API_PORT=8000 python3 main.py) &
(cd services/event-service && API_PORT=8001 python3 main.py) &
(cd services/product-service && API_PORT=8002 python3 main.py) &
(cd services/ticket-service && API_PORT=8003 python3 main.py) &
(cd services/order-service && API_PORT=8004 python3 main.py) &

wait
