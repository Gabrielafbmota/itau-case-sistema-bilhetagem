
# Microsserviços - Sistema de Bilhetagem

Este repositório contém 5 microsserviços independentes desenvolvidos com **FastAPI**, organizados segundo os princípios da **Clean Architecture**.

## 📦 Serviços incluídos

| Serviço          | Porta | Responsabilidade principal              |
|------------------|-------|------------------------------------------|
| `user-service`   | 8000  | Gerenciamento de usuários e login (JWT)  |
| `event-service`  | 8001  | Cadastro e gerenciamento de eventos      |
| `product-service`| 8002  | Produtos adicionais dos eventos          |
| `ticket-service` | 8003  | Geração e controle de ingressos (PDF)    |
| `order-service`  | 8004  | Checkout e pedidos de compra             |

---

## 🚀 Como executar

### 1. Ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Execute todos os serviços com o script

```bash
chmod +x start_services.sh
./start_services.sh
```

---

## 🔐 Autenticação

- O `user-service` fornece autenticação via **JWT**.
- Os demais serviços dependem do `Authorization: Bearer <token>` no header.
- A rota `/users/me` retorna os dados do usuário autenticado.

---

## 🧱 Estrutura por serviço

Todos os serviços seguem a arquitetura:

```
src/
├── application/         # Use Cases e Services
├── domain/              # Entidades, Schemas e Interfaces
├── infrastructure/      # Repositórios e banco
├── presentation/        # Rotas (routers)
├── core/                # Configurações, segurança, logger
```

---

## 🛠️ Tecnologias

- Python 3.10+
- FastAPI + Uvicorn
- SQLAlchemy
- JWT com OAuth2
- Pydantic
- requests
- passlib[bcrypt]

---

## 📌 Observações

- O `user-service` deve ser o primeiro a subir (controla autenticação).
- Os serviços são independentes e expostos por porta distinta.
- Para ambientes reais, recomenda-se o uso de **Docker** + **Traefik** ou **NGINX**.

Para uma visão geral completa da arquitetura e das rotas disponíveis, consulte o arquivo [docs/SYSTEM_OVERVIEW.md](docs/SYSTEM_OVERVIEW.md).

---

Desenvolvido com 💙 por Gabi
