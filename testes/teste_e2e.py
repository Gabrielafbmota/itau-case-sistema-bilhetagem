import requests
from datetime import datetime, timedelta

BASE_URLS = {
    "user": "http://localhost:8000",
    "event": "http://localhost:8001",
    "product": "http://localhost:8002",
    "ticket": "http://localhost:8003",
    "order": "http://localhost:8004",
}


def criar_usuario():
    response = requests.post(
        f"{BASE_URLS['user']}/users",
        json={
            "name": "Gabriela Mota",
            "email": "gabriela98670876@gmail.com",
            "password": "senha123",
        },
    )
    response.raise_for_status()
    return response.json()["user_id"]


def criar_evento(user_id):
    response = requests.post(
        f"{BASE_URLS['event']}/events",
        json={
            "title": "Rock in Rio",
            "description": "Festival de música",
            "location": "Rio de Janeiro",
            "start_time": (datetime.utcnow() + timedelta(days=1)).isoformat(),
            "end_time": (datetime.utcnow() + timedelta(days=1, hours=2)).isoformat(),
            "created_by": user_id,
        },
    )
    response.raise_for_status()
    return response.json()["event_id"]


def criar_produto():
    response = requests.post(
        f"{BASE_URLS['product']}/products",
        json={
            "name": "Pipoca",
            "description": "Pacote grande",
            "price": 10.0,
            "stock": 100,
        },
    )
    response.raise_for_status()
    return response.json()["product_id"]


def criar_ticket(event_id):
    response = requests.post(
        f"{BASE_URLS['ticket']}/tickets",
        json={
            "event_id": 1,
            "price": 200.0,
            "quantity_total": 100,
            "quantity_available": 100,
            "type": "Inteira",
        },
    )
    response.raise_for_status()
    return response.json()["ticket_id"]


def criar_pedido(user_id, ticket_id, product_id):
    response = requests.post(
        f"{BASE_URLS['order']}/orders",
        json={
            "user_id": 1,
            "event_id": 1,
            "items": [{"ticket_id": 2, "quantity": 1, "unit_price": 50.0}],
            "products": [{"product_id": 1, "quantity": 1, "unit_price": 10.0}],
            "total": 60.0,
        },
    )
    response.raise_for_status()
    return response.json()["order_id"]


if __name__ == "__main__":
    print("🔐 Criando usuário...")
    user_id = criar_usuario()

    print("📆 Criando evento...")
    event_id = criar_evento(user_id)

    print("🎫 Criando ticket...")
    ticket_id = criar_ticket(event_id)

    print("🛍️ Criando produto...")
    product_id = criar_produto()

    print("📦 Criando pedido...")
    order_id = criar_pedido(user_id, ticket_id, product_id)

    print(f"\n✅ Pedido criado com sucesso! ID: {order_id}")
