
# 📝 Decisions - Sistema de Bilhetagem (Case Técnico Itaú)

Este documento registra as principais decisões técnicas adotadas no projeto.

---

## 1️⃣ Arquitetura Geral

**Padrão escolhido:** Microserviços baseados em ECS Fargate, com API Gateway e mensageria SQS.

**Motivação:**

- Separação clara de responsabilidades por domínio (eventos, ingressos, pedidos, usuários, pagamentos).
- Isolamento de falhas e escalabilidade independente.
- Desacoplamento de componentes através de SQS.
- Uso de serviços gerenciados para reduzir complexidade operacional.

---

## 2️⃣ Linguagem e Stack

**Stack escolhida:** Python + FastAPI + PostgreSQL + Docker + AWS Services

**Motivação:**

- Python pela produtividade e bibliotecas maduras.
- FastAPI por performance, tipagem e documentação automática.
- PostgreSQL por consistência forte e suporte ACID.
- Docker para portabilidade.
- AWS como provedor cloud (foco do desafio).

---

## 3️⃣ Gerenciamento de APIs

**Decisão:** Uso de API Gateway com autenticação Cognito.

**Motivação:**

- Centralização de políticas de segurança e rate limiting.
- Suporte nativo a OAuth2 e JWT tokens.
- Fácil integração com serviços AWS e WAF.

---

## 4️⃣ Orquestração de processos

**Decisão:** Uso de SQS como camada de mensageria entre microservices.

**Motivação:**

- Desacoplar serviços para maior resiliência.
- Permitir retrials e Dead Letter Queues.
- Simplificar fluxos assíncronos como confirmação de pagamento e emissão de ingressos.

---

## 5️⃣ Persistência de dados

**Decisão:** RDS PostgreSQL Multi-AZ.

**Motivação:**

- Banco relacional robusto, transacional e com failover automático.
- Compatível com drivers e ORMs populares.
- Backup automatizado e Multi-AZ.

---

## 6️⃣ Observabilidade e segurança

**Componentes:**

- CloudWatch para métricas e logs.
- AWS X-Ray para tracing.
- Secrets Manager para gestão segura de secrets.
- IAM para controle de permissões.
- WAF para proteção contra ameaças comuns.

**Motivação:**

- Alinhamento com o AWS Well-Architected Framework (pilares de segurança e excelência operacional).
- Facilidade de troubleshooting e rastreamento.

---

## 7️⃣ Deploy e execução

**Local:** docker-compose para desenvolvimento.

**Prod:** deploy automatizado para ECS Fargate com scripts + Terraform (infra opcional).

**Motivação:**

- Simplificar onboarding de novos devs.
- Garantir consistência entre ambientes.
- Manter baixo custo e alta disponibilidade em produção.

---

