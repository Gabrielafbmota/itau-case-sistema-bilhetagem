# itau-case-sistema-bilhetagem

Desafio Técnico – Vaga de Engenheiro(a) de Software

🎯 O Desafio

Você deverá propor uma arquitetura na AWS e desenvolver uma solução funcional (em sua stack de preferência) para um sistema de bilhetagem com as seguintes características:

O sistema deve permitir solicitação, reserva e compra de ingressos.
Durante o processo de compra, o sistema deve oferecer produtos adicionais como pipoca, chocolate, refrigerante, etc.
A solução deve conter uma única base de código (um único projeto/solution), mesmo que a arquitetura proposta seja orientada a microserviços. Isso facilitará a apresentação e a avaliação do seu trabalho.
 

🛠️ O que esperamos:

Um desenho de arquitetura AWS (pode ser feito com ferramentas como Lucidchart, Draw.io, ou similar).
Código-fonte funcional com instruções claras de como rodar o projeto. (Pode ser compartilhado um repositório GitHub pessoal, ou o envio do código por e-mail).
Documentação breve explicando suas decisões técnicas.
 
# 

Esse repositório é referente ao case técnico do ITAU para vaga de senior. 

Estrutura do projeto
ticketing-system/
├── services/
│   ├── ticket-service/
│   ├── reservation-service/
│   ├── checkout-service/
│   └── ...
├── infra/
│   ├── terraform/            # (infra como código, opcional)
│   └── docker/               # Dockerfiles + compose para dev
├── scripts/
│   └── deploy.sh             # deploy scripts para ECS
├── docs/
│   ├── architecture.png
│   ├── decisions.md
│   └── run-instructions.md
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md



