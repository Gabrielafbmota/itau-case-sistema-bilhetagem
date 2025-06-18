
# 📝 Decisions - Sistema de Bilhetagem (Case Técnico Itaú)

---

## 1️⃣ Arquitetura Geral

**Padrão escolhido:** Microserviços baseados em ECS Fargate, API Gateway e SQS.

**Motivação:**

- Separação clara de responsabilidades por domínio (usuário, evento, ingresso, pedido, pagamento, produtos).
- Isolamento de falhas e escalabilidade independente por serviço.
- Desacoplamento através de SQS (resiliência e tolerância a falhas).
- Serviços gerenciados para reduzir a complexidade operacional.
- Foco em segurança e observabilidade (WAF, Cognito, CloudWatch, X-Ray).

---

## 2️⃣ Linguagem e Stack

**Stack escolhida:** Python + FastAPI + PostgreSQL + Docker + AWS Services.

**Motivação:**

- Python pela produtividade e bibliotecas maduras.
- FastAPI por alta performance, tipagem e documentação automática.
- PostgreSQL pela consistência forte e suporte transacional (ACID).
- Docker para portabilidade local e em produção.
- AWS como nuvem target (como pedido no desafio).

---

## 3️⃣ Gerenciamento de APIs

**Decisão:** API Gateway com Lambda Authorizer e Cognito.

**Motivação:**

- Centralizar políticas de segurança e rate limiting.
- Integração nativa com WAF, OAuth2 e JWT.
- Lambda Authorizer para customização adicional.
- Facilita controle de acesso e auditoria.

---

## 4️⃣ Orquestração de processos

**Decisão:** Amazon SQS para orquestração entre serviços.

**Motivação:**

- Desacoplamento para maior resiliência.
- Retentativa automática e DLQ.
- Fluxos assíncronos (ex: reserva → expiração, pagamento → emissão).

---

## 5️⃣ Persistência de dados

**Decisão:** RDS PostgreSQL Multi-AZ.

**Motivação:**

- Banco relacional transacional e consistente.
- Suporte Multi-AZ (alta disponibilidade).
- Backup automatizado e failover automático.

---

## 6️⃣ Observabilidade e segurança

**Componentes:**

- AWS WAF → proteção contra OWASP Top 10, DDoS.
- IAM + Secrets Manager → controle de identidade e gestão de segredos.
- CloudWatch + Alarms → logs e métricas.
- X-Ray → tracing distribuído.

**Motivação:**

- Alinhamento com AWS Well-Architected Framework.
- Visibilidade completa do sistema.
- Detecção precoce de problemas.

---

## 7️⃣ Deploy e execução

**Local (desenvolvimento):**

- Docker Compose (PostgreSQL local ou SQLite).

**Produção:**

- Deploy automatizado para ECS Fargate com múltiplas AZs.
- Infra as code com Terraform (opcional).
- Pipelines de CI/CD com GitHub Actions.

---

## 8️⃣ Outros

- Ingressos armazenados em S3 (PDF).
- Processos de expiração com Lambda e DynamoDB.
- Notificações com SES.

---
