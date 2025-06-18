
# 🚀 Plano de Melhoria - Sistema de Bilhetagem (Case Técnico Itaú)

Este plano detalha as melhorias sugeridas para complementar a entrega do case, com foco em:

✅ Demonstrar aderência completa ao **AWS Well-Architected Framework**  
✅ Demonstrar maturidade em Engenharia de Software  
✅ Fortalecer a entrega do case para a banca técnica do Itaú

---

## 📋 Itens de melhoria

### 1️⃣ Testes automatizados

- Criar pasta `tests/` por service
- Implementar:
  - Unit tests (UseCases, Services, Repositories)
  - Integration tests (API calls)
  - E2E (checkout completo)

**Ferramentas:** `pytest`, `pytest-httpx`  
**Tempo estimado:** 1 dia

---

### 2️⃣ CI/CD com GitHub Actions

- Criar workflow `.github/workflows/ci.yml`
- Incluir steps:
  - Lint (`black`, `flake8`)
  - Tests (`pytest --cov`)
  - Build
  - Deploy automatizado (`deploy.yml`)

**Tempo estimado:** 0.5 dia

---

### 3️⃣ Observability (X-Ray + CloudWatch)

- Instrumentar serviços com X-Ray middleware
- Configurar Task Role no ECS
- Criar dashboards no CloudWatch

**Tempo estimado:** 1 dia

---

### 4️⃣ Mensageria SQS (Producer/Consumer)

- Implementar publish de eventos via boto3 SQS client
- Implementar consumer (worker async ou celery)

**Tempo estimado:** 1 dia

---

### 5️⃣ Resiliência e Retry

- Implementar retry com `tenacity` em chamadas críticas
- Garantir idempotência de Order/Payment

**Tempo estimado:** 0.5 dia

---

### 6️⃣ Segurança de API (JWT com Cognito)

- Integrar `fastapi-cognito` ou `fastapi-jwt-auth`
- Proteger rotas sensíveis com JWT validation

**Tempo estimado:** 1 dia

---

### 7️⃣ Produtos adicionais no fluxo

- Integrar produtos complementares no payload da order
- Incluir no subtotal e fatura gerada

**Tempo estimado:** 0.5 dia

---

## 🗺️ Resumão de esforço

| Item                         | Complexidade | Tempo estimado |
|------------------------------|--------------|----------------|
| Testes unitários + E2E       | Média        | 1 dia          |
| CI/CD com GitHub Actions     | Baixa        | 0.5 dia        |
| X-Ray + observability        | Média        | 1 dia          |
| Producer/Consumer SQS        | Média        | 1 dia          |
| Retry e Resiliência          | Baixa        | 0.5 dia        |
| JWT com Cognito              | Média        | 1 dia          |
| Produtos adicionais no fluxo | Baixa        | 0.5 dia        |

---

## 🎯 Objetivo final

Elevar a entrega para um nível **próximo a produção real**, demonstrando domínio:

- Engenharia de software sênior
- Arquitetura AWS
- Observabilidade
- Testabilidade
- Segurança de APIs
- CI/CD moderno

---

