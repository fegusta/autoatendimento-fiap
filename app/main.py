from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, DateTime
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, EmailStr
import uuid
import os
from sqlalchemy.future import select
from typing import List
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = "postgresql+asyncpg://postgres:Auto%40Lanche2025@localhost/db"

print("DATABASE_URL lido do .env:", DATABASE_URL)


# SQLAlchemy setup
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

# Modelo uvicorn(Base):
class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    cpf: Mapped[str] = mapped_column(String(14), nullable=True)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

# Schema Pydantic
class ClienteCreate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    cpf: str | None = None

class ClienteRead(BaseModel):
    id: uuid.UUID
    nome: str | None
    email: EmailStr | None
    cpf: str | None
    data_criacao: datetime

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

@app.post("/clientes", response_model=ClienteRead)
async def criar_cliente(cliente: ClienteCreate, session: AsyncSession = Depends(get_session)):
    novo_cliente = Cliente(**cliente.dict())
    session.add(novo_cliente)
    await session.commit()
    await session.refresh(novo_cliente)
    return novo_cliente

@app.get("/clientes/{cliente_id}", response_model=ClienteRead)
async def buscar_cliente(cliente_id: uuid.UUID, session: AsyncSession = Depends(get_session)):
    cliente = await session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.get("/clientes", response_model=List[ClienteRead])
async def listar_clientes(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Cliente))
    clientes = result.scalars().all()
    return clientes
