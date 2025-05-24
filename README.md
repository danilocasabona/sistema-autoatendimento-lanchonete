# 🍔 Sistema de Autoatendimento - Lanchonete

Bem-vindo ao repositório oficial do projeto de autoatendimento para lanchonete!

Este projeto faz parte do Tech Challenge da pós-graduação em Arquitetura de Sistemas (FIAP) e aplica os conceitos de arquitetura hexagonal, modularização, testabilidade com BDD e documentação viva com FastAPI.

## 📂 Estrutura do Projeto

```
project_root/
├── .docker/           # Concentra os arquivos de configuração do container
├── app/               # Código principal da aplicação
├── tests/             # Testes unitários, integração e BDD
├── docs/              # Documentação técnica do projeto
└── README.md          # Este arquivo
```

## 🧭 Fluxo do Projeto

1. Cliente acessa a API FastAPI de autoatendimento
2. Consulta de cardápio com possibilidade de cache
3. Montagem do pedido e escolha de produtos
4. Realização do pagamento
5. Registro do pedido e atualização de status
6. Monitoramento e health-check da aplicação

## 🧩 Documentação Técnica

- [🗺️ Mapa de Entidades](docs/arquitetura/mapa-de-entidades.md)
- [📚 Estudos e Referências](docs/estudo/)
- [🖼️ Imagens e Diagramas](docs/imagens/)

## 🧠 Mapa Mental do Projeto

![Mapa Mental](/docs/imagens/mapa_mental_arquitetura_lanchonete.jpeg)

## 🚀 Tecnologias e Conceitos Aplicados

- Python 3.x
- FastAPI
- Arquitetura Hexagonal (Ports and Adapters)
- Testes unitários e BDD com pytest-bdd
- Docker e Docker Compose
- Documentação viva via Swagger / OpenAPI
- Modularização de código e separação de responsabilidades

## 📦 Como iniciar o projeto

1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd project_root
```

2. Execute o docker do projeto

2.1 Acesse a pasta do docker
```bash
cd .docker
```
2.1 Necessário criar uma pasta onde vai ser armazenado os dados oriundos do banco, gerenciado pelo nosso container.
 > Utilizamos o arquivo Makefile para isso.
```bash
make create-folder
```
2.2 Crie os containers da aplicação:
```bash
make create-docker
```
Ao finalizar a criação do docker, vamos subir os containers:
```bash
make run-docker
```

Com os containers ativos, precisamos dar a permissão para escrever na pasta do banco de dados:

```bash
make permission-folder
```

3. Crie e ative o ambiente virtual (opcional, mas recomendado)

3.1. Acesse o ambiente do container da aplicação
```bash
docker exec -it lanchonete_app /bin/bash
```

3.2. Dê inicio a aplicação
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3.3. Instale as dependências

```bash
pip install -r ./.docker/bin/webserver/config/requirements.txt
```

4. Execute a aplicação

```bash
uvicorn app.api.main:app --reload
```

Acesse a documentação automática da API em: `http://localhost:8000/docs`

## ✅ Progresso do Projeto

- [x] Estrutura inicial do projeto
- [x] Guia de estudos personalizado
- [x] Mapeamento dos conceitos
- [x] Mapa mental do projeto
- [ ] Desenvolvimento das funcionalidades principais
- [ ] Implementação dos testes BDD e unitários
- [ ] Finalização e entrega do Tech Challenge

## 📝 Contribuição

Este projeto faz parte de um desafio educacional e está aberto para melhorias e contribuições pessoais para aprendizado!

## 📫 Contato

Danilo Casabona  
[LinkedIn](https://www.linkedin.com/in/danilocasabona/)

---

> "Construindo sistemas com propósito: escaláveis, testáveis e preparados para o futuro."
