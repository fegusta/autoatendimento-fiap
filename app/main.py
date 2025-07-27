from fastapi import FastAPI
from app.api.routes_cliente import router as cliente_router
from app.api.routes_produto import router as produto_router
from app.api.routes_pedido import router as pedido_router
from app.api.routes_checkout import router as checkout_router
from app.api.routes_pagamento import router as pagamento_router
from app.api.routes_webhook import router as webhook_router

from app.infrastructure.db.base import Base
from app.infrastructure.db.db import engine

app = FastAPI(title="API Autoatendimento FIAP")

# Inclui as rotas da API
app.include_router(cliente_router)
app.include_router(produto_router)
app.include_router(pedido_router)
app.include_router(checkout_router)
app.include_router(pagamento_router)
app.include_router(webhook_router)

# Cria tabelas ao iniciar (opcional, pode deixar só no execute_ddl.py depois)
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
