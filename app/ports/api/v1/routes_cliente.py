from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.core.domain.cliente import Cliente
from app.application.services.cliente_service import ClienteService
from app.application.schemas.cliente_schema import ClienteCreateSchema, ClienteReadSchema
from app.dependencies import get_cliente_service

router = APIRouter(prefix="v1/clientes", tags=["Clientes"])


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
