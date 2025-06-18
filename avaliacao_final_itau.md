# Avaliação Final - Desafio Técnico de Engenheira de Software (Itaú)

## Informações Gerais
**Candidata**: Gabriela  
**Projeto**: Sistema de Bilhetagem com arquitetura AWS e microserviços  
**Tecnologias**: Python (FastAPI, SQLAlchemy), PostgreSQL, Docker, AWS (ECS, S3, API Gateway, RDS, CloudWatch, etc.)  

---

## ✅ Pontos Fortes da Entrega

### Arquitetura e Estrutura do Projeto
- Arquitetura orientada a microserviços com separação de responsabilidades (User, Products, Events, Tickets, Orders).
- Uso da **Clean Architecture**, com separação clara entre Domain, Application, Infrastructure e Presentation.
- Boas práticas de **SOLID** e **12 Factor App**.
- Diagrama arquitetural bem elaborado, incluindo componentes de segurança (WAF, IAM), disponibilidade (ECS, S3) e observabilidade (CloudWatch, X-Ray).

### Código e Implementação
- Estrutura de rotas, schemas e validações bem definidas com FastAPI.
- Testes unitários com `unittest` e `pytest` cobrindo os principais casos de uso.
- Uso de Pydantic e tipagem para maior segurança.
- Integração entre serviços via HTTP com clients dedicados.
- Geração de ticket em PDF (previsto para upload futuro no S3).

### Documentação
- Diagrama de integração entre serviços.
- Diagrama de infraestrutura com recursos AWS.
- Scripts SQL para criação e população do banco de dados.
- Docker Compose funcional para execução local.

---

## 🔹 Oportunidades de Melhoria

### 1. Autenticação e Autorizacão
- Faltou implementação de JWT tokens e proteção de rotas por RBAC.
- Recomendado uso de OAuth2 com FastAPI para rotas protegidas.

### 2. Reserva com Expiração
- É mencionado o uso de reservas, mas sem expiração automática.
- Sugere-se o uso de cron job (ex: Lambda com CloudWatch) para limpar reservas expiradas.

### 3. Mock de Pagamento
- A experiência de compra carece de simulação de pagamento (ainda que fake).
- Criar serviço de pagamento mockado ajudaria a fechar o fluxo.

### 4. Notificações
- Não há comunicação com o usuário após a compra.
- Poderia haver mock de envio de e-mail (ou fila SQS simulada).

### 5. Observabilidade e Logging
- O logger está presente, mas falta implementação de correlação de logs, trace ID e logs estruturados.
- Integração real com X-Ray ou Datadog seria bem-vinda.

### 6. Testes de Integração e Contrato
- Ótimos testes unitários, mas falta cobertura de integração entre serviços.
- Sugere-se o uso de `httpx` ou `pytest-httpx` para isso.

### 7. Proteção Adicional
- Faltou um middleware para **rate limiting** ou bloqueio de IPs suspeitos.
- Pode ser feito no API Gateway ou via dependência FastAPI.

### 8. Healthcheck e Metrics
- Não há endpoints `/health` ou `/metrics` para observabilidade.
- Adicioná-los ajuda em ambientes de produção.

---

## 🏆 Conclusão

A entrega é **muito acima da média**, clara, bem estruturada, com arquitetura moderna e aplicação de diversas boas práticas de engenharia.

Mostra profundo conhecimento em:
- Arquitetura de microsserviços
- Princípios de software (SOLID, Clean Arch, 12 Factor)
- AWS e DevOps
- Python backend com FastAPI

### ✅ Indicada para vaga Sênior com destaque.

Sugestões adicionais são apenas incrementais e podem ser implementadas conforme a necessidade real do sistema.

---

Caso queira, posso criar os arquivos com as melhorias propostas (JWT, pagamentos, fila de expiração, etc.) e adicionar ao projeto como sugestão de extensão.

