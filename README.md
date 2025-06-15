
# Product & User Services

Este repositório contém dois microsserviços construídos com **FastAPI** seguindo os princípios da **Clean Architecture**:

- `user-service`: Gerenciamento de usuários e autenticação JWT.
- `product-service`: CRUD de produtos com controle de acesso baseado em roles (usuário comum e admin).

---

## 🧱 Estrutura

Cada serviço segue o padrão:

```
src/
├── application/         # Use Cases e Services
├── domain/              # Entities, Schemas e Interfaces
├── infrastructure/      # Banco de dados e Repositórios
├── presentation/        # Rotas
├── core/                # Segurança, Config, Logger
```

---

## 🚀 Como executar

### 1. Ative seu ambiente virtual Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Execute os serviços com o script

```bash
chmod +x start_services.sh
./start_services.sh
```

---

## 🔐 Autenticação

- Autenticação baseada em JWT.
- Acesse `/token` com `username` e `password` para obter um token.
- Use o token como `Bearer` nos headers das requisições.

---

## 🛠️ Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- passlib[bcrypt]
- requests

---

## 📮 Endpoints principais

### `user-service`

| Método | Rota        | Descrição               |
|--------|-------------|--------------------------|
| POST   | /users      | Criação de usuário       |
| POST   | /token      | Login (JWT)              |
| GET    | /users/me   | Usuário autenticado      |

### `product-service`

| Método | Rota              | Descrição               |
|--------|-------------------|--------------------------|
| GET    | /products         | Lista todos os produtos |
| POST   | /products         | Cria produto (admin)     |
| PUT    | /products/{id}    | Atualiza produto (admin) |
| DELETE | /products/{id}   | Remove produto (admin)   |

---

## 📌 Observações

- O `product-service` depende do `user-service` para validação de token.
- Ambos os serviços devem rodar em `localhost`, portas padrão: **8000** (`user-service`) e **8001** (`product-service`).


