from fastapi import APIRouter, Depends
from app.ports.cliente_service import ClienteService
from app.ports.cliente_repository import ClienteRepository
from app.services.cliente_service_impl import ClienteServiceImpl
from app.adapters.repositories.cliente_repository_impl import ClienteRepositoryImpl
from app.schemas.cliente_schema import ClienteRequest, ClienteResponse
from app.db.dependencies import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

router = APIRouter(prefix="/cliente", tags=["Cliente"])

def get_cliente_service(session: AsyncSession = Depends(get_session)) -> ClienteService:
    repo: ClienteRepository = ClienteRepositoryImpl(session)
    return ClienteServiceImpl(repo)


@router.post("", response_model=ClienteResponse)
async def registrar_cliente(
    body: ClienteRequest,
    service: ClienteService = Depends(get_cliente_service)
):
    cliente = await service.registrar_cliente(body.dict())
    return ClienteResponse(**cliente.__dict__)


@router.get("/{cliente_id}", response_model=ClienteResponse)
async def buscar_por_id(
    cliente_id: UUID,
    service: ClienteService = Depends(get_cliente_service)
):
    cliente = await service.buscar_por_id(cliente_id)
    return ClienteResponse(**cliente.__dict__)


@router.get("/cpf/{cpf}", response_model=ClienteResponse)
async def buscar_por_cpf(
    cpf: str,
    service: ClienteService = Depends(get_cliente_service)
):
    cliente = await service.buscar_por_cpf(cpf)
    return ClienteResponse(**cliente.__dict__)


@router.get("", response_model=List[ClienteResponse])
async def listar_todos(
    service: ClienteService = Depends(get_cliente_service)
):
    clientes = await service.listar_todos()
    return [ClienteResponse(**c.__dict__) for c in clientes]
