# Sistema de Bilhetagem - Visão Geral

Este documento complementa o `README.md` com detalhes de arquitetura, serviços e rotas expostas pelo projeto.

## Estrutura de Pastas
Cada microsserviço em `services/` segue a seguinte organização baseada em Clean Architecture:

```
src/
├── application/         # Use cases e serviços de negócio
├── domain/              # Entidades, schemas e interfaces
├── infrastructure/      # Repositórios e acesso a dados
├── adapters/            # Camada de apresentação (routers)
├── core/                # Configurações, log, segurança
```

Os ports de cada serviço são definidos via variável de ambiente `API_PORT` e lidos pela função `get_env_var` apresentada em `src/core/config.py`.

## Serviços Disponíveis

| Serviço | Porta padrão | Principais responsabilidades |
|---------|--------------|--------------------------------|
| **user-service**   | 8000 | Cadastro de usuários e autenticação JWT |
| **event-service**  | 8001 | CRUD de eventos |
| **product-service**| 8002 | Gerenciamento de produtos auxiliares |
| **ticket-service** | 8003 | Controle de ingressos e geração de PDF |
| **order-service**  | 8004 | Criação e listagem de pedidos |
| **reservation-service** | 8005 | Reservas de ingressos |

### Endpoints por Serviço

Abaixo está um resumo das principais rotas implementadas.

#### user-service
- `POST /users` cria usuário
- `GET /users/{user_id}` consulta usuário
- `POST /token` obtém JWT
- `GET /users/me` dados do usuário autenticado

#### event-service
- `POST /events` cria evento
- `GET /events` lista eventos
- `GET /events/{event_id}` consulta evento
- `PUT /events/{event_id}` atualiza evento
- `DELETE /events/{event_id}` remove evento

#### product-service
- `GET /products` lista produtos
- `GET /products/{product_id}` consulta produto
- `POST /products` cria produto
- `PUT /products/{id}` atualiza produto
- `DELETE /products/{id}` remove produto

#### ticket-service
- `POST /tickets` cria ticket
- `GET /tickets/event/{event_id}` ingressos de um evento
- `GET /tickets/{ticket_id}` consulta ticket
- `PUT /tickets/{ticket_id}` atualiza ticket
- `DELETE /tickets/{ticket_id}` remove ticket
- `POST /tickets/{ticket_id}/decrement` decrementa estoque
- `POST /tickets/{ticket_id}/increment` incrementa estoque
- `GET /tickets/{ticket_id}/pdf` download do PDF gerado

#### order-service
- `POST /orders` cria pedido
- `GET /orders/{order_id}` consulta pedido
- `GET /orders` lista pedidos

#### reservation-service
- `POST /reservations` cria reserva
- `GET /reservations/{reservation_id}` consulta reserva
- `GET /reservations/user/{user_id}` reservas por usuário
- `POST /reservations/{reservation_id}/cancel` cancela
- `POST /reservations/{reservation_id}/confirm` confirma

## Execução Local
Utilize o script `scripts/start_services.sh` para subir todos os serviços simultaneamente:

```bash
chmod +x scripts/start_services.sh
./scripts/start_services.sh
```

As tabelas do banco SQLite podem ser criadas via `scripts/create_sqlite.py`.

## Variáveis de Ambiente
Cada serviço lê algumas configurações via `os.environ`:

- `API_PORT`: define a porta em que o serviço irá escutar.
- `DATABASE_URL`: string de conexão do banco. Nos exemplos deste repositório é utilizado SQLite (`sqlite:///../event_ticketing.db`).

Para executar localmente, exporte essas variáveis antes de subir o serviço ou defina um arquivo `.env` carregado pela função `get_env_var`.

## Autenticação
O `user-service` oferece a rota `POST /token` que retorna um JWT válido por 30 minutos. Envie `username` e `password` no corpo da requisição via `application/x-www-form-urlencoded`:

```bash
curl -X POST http://localhost:8000/token -d "username=gabriela@gmail.com&password=senha123"
```

Inclua o token retornado no header `Authorization` para acessar os demais serviços:

```bash
Authorization: Bearer <seu_token>
```

## Testes
O arquivo `testes/teste_e2e.py` demonstra um fluxo ponta-a-ponta consumindo todas as APIs. Os testes automatizados podem ser executados com:

```bash
pytest -q
```

