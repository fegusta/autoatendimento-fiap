from fastapi import FastAPI
from app.api.cliente_routes import router as cliente_router
from app.adapters.repositories.models import Base
from app.db import engine

app = FastAPI(title="API Autoatendimento FIAP")

# Inclui as rotas da API
app.include_router(cliente_router)

# Cria tabelas ao iniciar (opcional, pode deixar só no execute_ddl.py depois)
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
