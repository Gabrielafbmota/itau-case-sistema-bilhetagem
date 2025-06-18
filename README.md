
# 🎟️ Sistema de Bilhetagem - Case Técnico Itaú

---

## 🎯 Objetivo

Este projeto entrega uma solução completa e escalável para um sistema de bilhetagem:

- Solicitação, reserva e compra de ingressos
- Oferta de produtos adicionais
- Geração de tickets PDF
- Observabilidade e segurança
- Arquitetura moderna em microserviços

---

## 🧱 Arquitetura (AWS)

- WAF
- API Gateway + Lambda Authorizer + Cognito
- ECS Fargate (Multi-AZ)
- RDS PostgreSQL Multi-AZ
- SQS (orquestração)
- S3 (tickets PDF)
- CloudWatch + X-Ray + IAM + Secrets Manager
- Lambda (expiração)

(Ver `docs/architecture.png`)

---

## 🏗️ Estrutura do projeto

```
ticketing-system/
├── services/
│   ├── user-service/
│   ├── event-service/
│   ├── product-service/
│   ├── ticket-service/
│   ├── reservation-service/
│   ├── order-service/
│   ├── payment-service/
├── infra/
│   ├── terraform/
│   └── docker/
├── scripts/
│   └── deploy.sh
├── docs/
│   ├── architecture.png
│   ├── decisions.md
│   └── run-instructions.md
├── .github/
│   └── workflows/ci-cd.yml
└── README.md
```

---

## ⚙️ Como rodar

👉 Ver `docs/run-instructions.md`

---

## 📋 Documentação de decisões

👉 Ver `docs/decisions.md`

---

## ✨ Considerações finais

A arquitetura foi desenhada com foco em:

- **Alta disponibilidade**
- **Desempenho**
- **Segurança**
- **Desacoplamento**
- **Observabilidade**
- **Custos otimizados**

Pronta para ser escalada e operada em ambiente corporativo (AWS).

---
