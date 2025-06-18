# 📝 Decisions - Sistema de Bilhetagem (Case Técnico Itaú)

Este documento descreve as principais decisões técnicas e de arquitetura adotadas no projeto, com foco em atender aos requisitos do desafio e aos pilares do **AWS Well-Architected Framework**.

---

## 1️⃣ Arquitetura Geral

**Padrão arquitetural:** Microserviços baseados em **ECS Fargate**, com **API Gateway**, **mensageria SQS** e **RDS PostgreSQL** Multi-AZ.

**Motivação:**

- Separação clara por domínios de negócio:
  - eventos
  - ingressos
  - pedidos
  - usuários
  - pagamentos
- Independência de escala: cada microservice escala de forma autônoma conforme demanda.
- Isolamento de falhas: falha em um serviço não afeta os demais.
- Desacoplamento via SQS, permitindo resiliência e tolerância a falhas temporárias.
- Uso intensivo de serviços gerenciados para reduzir overhead operacional.
- Suporte a múltiplas zonas de disponibilidade (AZs) para alta disponibilidade.

**Topologia de rede:**

- Subnets públicas: WAF, API Gateway, Cognito.
- Subnets privadas (Multi-AZ): ECS Fargate tasks, RDS.
- Integração com CloudWatch e X-Ray para observabilidade.

---

## 2️⃣ Linguagem e Stack Tecnológica

**Stack escolhida:**

- Linguagem: Python 3.x
- Framework: FastAPI
- Banco de dados: PostgreSQL (via RDS)
- Containers: Docker
- Orquestração: ECS Fargate
- CI/CD: GitHub Actions + Terraform (opcional)
- Infraestrutura: AWS

**Motivação:**

- Python: ampla adoção em back-end, ótima produtividade e ecossistema maduro.
- FastAPI: API RESTful de alta performance (ASGI), com suporte nativo a documentação OpenAPI (Swagger), tipagem forte com Pydantic.
- PostgreSQL: banco relacional maduro, com suporte ACID, ideal para controle de transações e consistência dos dados.
- Docker: ambiente reprodutível e portável para desenvolvimento e produção.
- AWS: padrão de mercado, foco do desafio.

---

## 3️⃣ Gerenciamento de APIs e Autenticação

**Decisão:** Uso de **API Gateway** na borda, com integração com **AWS WAF** e **Amazon Cognito** para autenticação.

**Motivação:**

- API Gateway provê throttling, caching, roteamento e proteção DDoS L7 integrada.
- Integração nativa com WAF para proteção contra ameaças comuns (OWASP Top 10).
- Cognito provê OAuth2 e JWT para autenticação robusta e escalável.
- Evita necessidade de desenvolver e manter uma solução própria de auth.

---

## 4️⃣ Orquestração e Comunicação entre Microservices

**Decisão:** Uso de **Amazon SQS** para mensageria e desacoplamento.

**Motivação:**

- Evita acoplamento direto entre serviços.
- Permite **processamento assíncrono** de etapas como:
  - confirmação de pagamento
  - geração de tickets
  - envio de notificações
- Suporta **retry**, **DLQ** e garante **durabilidade** da fila.
- Permite isolamento e resiliência: se um consumidor estiver indisponível, a fila retém as mensagens.

---

## 5️⃣ Persistência de Dados

**Decisão:** Uso de **Amazon RDS PostgreSQL** com Multi-AZ habilitado.

**Motivação:**

- Banco relacional robusto e transacional.
- Suporte ACID, ideal para processos críticos de bilhetagem (compra, reserva, pagamento).
- Failover automático para alta disponibilidade.
- Backups automáticos e snapshots.
- Menor custo operacional vs. gerenciar PostgreSQL em EC2.

---

## 6️⃣ Observabilidade e Segurança

**Componentes implementados:**

- **CloudWatch Logs & Metrics**: logs centralizados, monitoramento.
- **AWS X-Ray**: tracing distribuído entre microservices.
- **AWS Secrets Manager**: gestão segura de segredos e senhas.
- **AWS IAM**: controle granular de permissões e identidade.
- **AWS WAF**: firewall de aplicação gerenciado.

**Motivação:**

- Conformidade com os pilares de **Segurança** e **Excelência Operacional** do Well-Architected.
- Capacidade de rastrear transações ponta a ponta (crucial em sistema financeiro).
- Proteção contra vulnerabilidades conhecidas.
- Gestão e rotação de segredos automatizada.

---

## 7️⃣ Deploy e Operação

**Ambiente local:**

- Desenvolvimento com Docker Compose.
- Banco de dados local via Docker.
- Scripts de seed para popular banco de dados.

**Produção:**

- Deploy automatizado via GitHub Actions para ECS Fargate.
- Infraestrutura como código com Terraform (opcional).
- Auto Scaling de ECS com base em métricas (CPU/Memory).
- Multi-AZ para RDS e ECS tasks.

**Motivação:**

- Simplificação do onboarding de novos desenvolvedores.
- Ambiente de desenvolvimento similar à produção (paridade).
- Automação de deploy e rollback.
- Suporte nativo a escalabilidade horizontal.

---

## 8️⃣ Considerações Finais

Esta arquitetura foi pensada para atender os 5 pilares do **AWS Well-Architected Framework**:

1. **Excelência Operacional**
2. **Segurança**
3. **Confiabilidade**
4. **Eficiência de performance**
5. **Otimização de custos**

Além disso, privilegia o uso de serviços **gerenciados e serverless**, reduzindo o overhead operacional e permitindo maior foco no desenvolvimento do negócio.

---