
# Autoatendimento Fast Food - FIAP Challenge

Este projeto é uma API backend desenvolvida em FastAPI utilizando arquitetura hexagonal para um sistema de autoatendimento de fast food.

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker & Docker Compose
- Pydantic
- Uvicorn
- Arquitetura Hexagonal (Ports & Adapters)

---

## 📂 Organização do Projeto

```
app/
├── adapters/
│   ├── models/               # Modelos ORM (SQLAlchemy)
│   └── repositories/         # Implementações dos repositórios
├── api/                      # Rotas da API (FastAPI)
├── db/                       # Configuração de banco
├── domain/                   # Entidades do domínio
├── ports/                    # Interfaces (ports)
├── schemas/                  # Pydantic Schemas
├── services/                 # Regras de negócio
main.py                       # Entry point
dependencies.py               # Dependency injection
```

---

## 📋 Funcionalidades (Fase 1)

- [x] Cadastro e listagem de clientes
- [x] Cadastro, listagem e busca de produtos por categoria
- [x] Criação de pedidos com ou sem cliente
- [x] Atualização do status do pedido (`Recebido`, `Em preparação`, `Pronto`, `Finalizado`)
- [x] Fila de pedidos gerenciada diretamente no banco de dados
- [x] Listagem dos pedidos em andamento
- [ ] Containerização com Docker
- [ ] Script para criação de tabelas (`execute_ddl.py`)
- [ ] Vídeo de demonstração

---

## 🔧 Como executar

### 1. Com Docker (em breve)

```bash
docker-compose up --build
```

### 2. Manualmente

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Rode a API
uvicorn app.main:app --reload
```

---

## 📬 Rotas principais

- `POST /clientes`
- `POST /produtos`
- `POST /pedidos`
- `GET /pedidos/andamento`
- `PUT /pedidos/{id}` (atualizar status)

Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📌 Observações

Este projeto foi desenvolvido como parte do Tech Challenge da FIAP. Utilizamos princípios de DDD, arquitetura hexagonal e boas práticas de clean code.

---

## ✍️ Autor

Felipe Nascimento - [@fegusta](https://github.com/fegusta)
