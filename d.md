
# 🎟️ Sistema de Bilhetagem - Case Técnico Itaú

Este repositório contém a proposta de arquitetura AWS e a solução funcional para o desafio técnico de vaga de Engenheiro(a) de Software no Itaú.

---

## 🏛️ Contexto do desafio técnico

Sistema de bilhetagem com:

- Solicitação de ingressos
- Reserva de ingressos
- Compra de ingressos
- Oferecimento de produtos adicionais (pipoca, chocolate, refrigerante)

**Requisitos adicionais:**

- Propor arquitetura AWS
- Código funcional em 1 solution/repo (mesmo com microserviços)
- Documentação das decisões técnicas

---

## 🏗️ Arquitetura proposta (Well-Architected)

**Pilares:**

- Alta disponibilidade (Multi-AZ, ECS Fargate, RDS Multi-AZ)
- Escalabilidade automática (ECS Auto Scaling)
- Desacoplamento (SQS entre microservices)
- Observabilidade (CloudWatch, X-Ray)
- Segurança (WAF, API Gateway, Cognito, Secrets Manager, IAM)
- Simplicidade de deploy (infra como código, docker compose)

**Diagrama:**

![Arquitetura](docs/architecture.png)

---

## 📦 Serviços AWS utilizados

### WAF
Proteção contra ataques de camada 7 (SQLi, XSS, DDoS).

### API Gateway
Gerenciamento de APIs REST, segurança, throttling, integração com Cognito.

### Cognito
Autenticação de usuários (OAuth2, JWT), login seguro.

### ECS Fargate
Execução de containers (microservices), auto scaling, múltiplas AZs.

**Microservices:**

- event-service
- product-service
- ticket-service
- reservation-service
- order-service
- payment-service
- user-service

### RDS PostgreSQL (Multi-AZ)
Banco transacional ACID, failover automático, backups.

### SQS
Orquestração assíncrona entre microservices (desacoplamento).

### S3
Armazenamento de tickets PDF.

### Observability
CloudWatch, X-Ray, Secrets Manager, Alarms, IAM.

---

## 📋 Atendimento aos requisitos

| Requisito                                | Implementado |
|------------------------------------------|--------------|
| Solicitação de ingressos                 | ✅ |
| Reserva de ingressos                     | ✅ |
| Compra de ingressos                      | ✅ |
| Produtos adicionais                      | ✅ |
| Proposta de arquitetura AWS desenhada    | ✅ |
| Código funcional em 1 solution/repo      | ✅ |
| Documentação breve com decisões técnicas | ✅ |

---

## 🚀 Como rodar o projeto

### Desenvolvimento local:

```bash
docker-compose up --build
```

### Produção:

- ECS Fargate com Auto Scaling
- RDS Multi-AZ
- SQS com DLQ
- API Gateway + Cognito
- WAF na borda

---

## 📝 Resumo final

Esta arquitetura segue os princípios do **AWS Well-Architected Framework**:

- ✔️ Excelência operacional
- ✔️ Segurança
- ✔️ Confiabilidade
- ✔️ Eficiência de performance
- ✔️ Otimização de custos

---
