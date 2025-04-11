# 🗺️ Mapa de Entidades — Sistema de Autoatendimento da Lanchonete

## 📋 Visão Geral

Este documento descreve as entidades principais do sistema, suas responsabilidades e relacionamentos.  
O objetivo é guiar o desenvolvimento do projeto, facilitar a colaboração da equipe e manter a arquitetura do domínio bem definida.

---

## 📦 1. Cliente

Cadastro opcional para identificação do cliente no sistema.

| Atributo     | Tipo             | Descrição                              |
|--------------|------------------|----------------------------------------|
| id           | Integer (PK)     | Identificador único do cliente         |
| nome         | String           | Nome completo do cliente               |
| email        | String           | Email do cliente (único)               |
| telefone     | String           | Telefone para contato                  |
| criado_em    | DateTime         | Data de criação do cadastro            |

**Relacionamentos:**
- Um cliente pode ter vários pedidos.

---

## 📦 2. Produto

Itens disponíveis no cardápio da lanchonete.

| Atributo     | Tipo             | Descrição                              |
|--------------|------------------|----------------------------------------|
| id           | Integer (PK)     | Identificador único do produto         |
| nome         | String           | Nome do produto                        |
| descricao    | String           | Descrição do produto                   |
| preco        | Integer          | Preço do produto (centavos ou reais)   |

**Relacionamentos:**
- Um produto pode estar em vários itens de pedido.

---

## 📦 3. Pedido

Registro de um pedido feito pelo cliente.

| Atributo     | Tipo             | Descrição                              |
|--------------|------------------|----------------------------------------|
| id           | Integer (PK)     | Identificador único do pedido          |
| cliente_id   | Integer (FK)     | Relacionamento com Cliente (opcional)  |
| status       | Enum/String      | Status do pedido ("Em preparo", "Finalizado", etc.) |
| criado_em    | DateTime         | Data de criação do pedido              |

**Relacionamentos:**
- Um pedido pertence a um cliente (opcional).
- Um pedido possui múltiplos itens.

---

## 📦 4. Item do Pedido

Relação entre pedido e produtos, permitindo múltiplos produtos por pedido.

| Atributo         | Tipo             | Descrição                              |
|------------------|------------------|----------------------------------------|
| id               | Integer (PK)     | Identificador único do item            |
| pedido_id        | Integer (FK)     | Referência ao pedido                   |
| produto_id       | Integer (FK)     | Referência ao produto                  |
| quantidade       | Integer          | Quantidade do produto no pedido        |
| preco_unitario   | Integer          | Preço unitário do produto no momento do pedido |

**Relacionamentos:**
- Cada item pertence a um pedido.
- Cada item referencia um produto.

---

## 📦 5. Pagamento (Opcional para escopo inicial)

Registro do pagamento do pedido.

| Atributo          | Tipo             | Descrição                              |
|-------------------|------------------|----------------------------------------|
| id                | Integer (PK)     | Identificador único do pagamento       |
| pedido_id         | Integer (FK)     | Pedido relacionado                     |
| valor_total       | Integer          | Valor total do pagamento               |
| forma_pagamento   | String           | Dinheiro, Cartão, etc.                 |
| status_pagamento  | Enum/String      | Pendente, Confirmado, Cancelado        |
| criado_em         | DateTime         | Data de criação do pagamento           |

**Relacionamentos:**
- Um pagamento está associado a um pedido.

---

## 🔗 Relacionamentos Resumidos