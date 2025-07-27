from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from app.schemas.cliente_schema import ClienteCreate, ClienteResponse
from app.infrastructure.db.database import get_session
from app.infrastructure.db.cliente_repository import ClienteRepository
from app.application.use_cases.cliente_use_case import ClienteUseCase

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteCreate, db: AsyncSession = Depends(get_session)):
    use_case = ClienteUseCase(ClienteRepository(db))
    return await use_case.cadastrar_cliente(cliente)

@router.get("/", response_model=List[ClienteResponse])
async def listar_clientes(db: AsyncSession = Depends(get_session)):
    use_case = ClienteUseCase(ClienteRepository(db))
    return await use_case.listar_clientes()

@router.get("/{cliente_id}", response_model=ClienteResponse)
async def buscar_cliente(cliente_id: UUID, db: AsyncSession = Depends(get_session)):
    use_case = ClienteUseCase(ClienteRepository(db))
    cliente = await use_case.buscar_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente
