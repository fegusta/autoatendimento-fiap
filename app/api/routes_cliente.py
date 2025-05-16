from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List
from app.domain.cliente import Cliente
from app.services.cliente_service import ClienteService
from app.adapters.repositories.cliente_repository_impl import ClienteRepositoryImpl
from app.adapters.repositories.models import Base
from app.schemas.cliente_schema import ClienteCreateSchema, ClienteReadSchema
from app.dependencies import get_session, get_cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("", response_model=ClienteReadSchema)
async def criar(cliente_data: ClienteCreateSchema, service: ClienteService = Depends(get_cliente_service)):
    cliente = Cliente(
        nome=cliente_data.nome,
        email=cliente_data.email,
        cpf=cliente_data.cpf,
    )
    return await service.criar_cliente(cliente)


@router.get("/{cliente_cpf}", response_model=ClienteReadSchema)
async def buscar_por_cpf(cliente_cpf: str, service: ClienteService = Depends(get_cliente_service)):
    cliente = await service.buscar_por_cpf(cliente_cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.get("", response_model=List[ClienteReadSchema])
async def listar(service: ClienteService = Depends(get_cliente_service)):
    return await service.listar_clientes()
