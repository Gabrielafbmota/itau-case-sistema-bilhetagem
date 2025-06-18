
# 🚀 Como rodar o projeto - Sistema de Bilhetagem

---

## Pré-requisitos

- Python 3.12+
- Docker / Docker Compose
- AWS CLI configurado (opcional)
- Make (Linux ou Windows + WSL)

---

## Rodando localmente

### Passo 1: Clonar repositório

```bash
git clone git@github.com:seuusuario/itau-case-sistema-bilhetagem.git
cd itau-case-sistema-bilhetagem
```

### Passo 2: Instalar dependências

```bash
make prepare
```

### Passo 3: Rodar com SQLite

```bash
make run_local
```

### Passo 4: Rodar com PostgreSQL via Docker Compose

```bash
docker-compose up --build
```

---

## Rodando em produção (AWS)

### Build e push das imagens

```bash
make build
make push
```

### Deploy para ECS Fargate

```bash
bash scripts/deploy.sh
```

### Infra as code (opcional)

```bash
cd infra/terraform
terraform apply
```

---

## Acessando as APIs

- API pública: através do API Gateway
- Autenticação: via Cognito (OAuth2 / JWT)

---
