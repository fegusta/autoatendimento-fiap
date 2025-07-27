from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID

from app.schemas.pedido_schema import (
    PedidoCreate,
    PedidoResponse,
    PedidoUpdate
)
from app.infrastructure.db.database import get_session
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.application.use_cases.pedido_use_case import PedidoUseCase
from app.domain.enums.status_pedido import StatusPedido
from app.application.use_cases.criar_pagamento_qrcode_use_case import CriarPagamentoQRCodeUseCase
from app.infrastructure.external.mercado_pago_client import MercadoPagoClient
from app.application.interfaces.unit_of_work import UnitOfWork
from app.application.use_cases.listar_pedidos_use_case import ListarPedidosUseCase
from app.application.use_cases.listar_pedidos_por_status_use_case import ListarPedidosPorStatusUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Query


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/", response_model=list[PedidoResponse])
async def listar_pedidos(
    db: AsyncSession = Depends(get_session)
):
    use_case = ListarPedidosUseCase(PedidoRepository(db))
    pedidos = await use_case.execute()
    return [PedidoResponse.from_entity(p) for p in pedidos]

@router.post("/", response_model=PedidoResponse, status_code=status.HTTP_201_CREATED)
async def criar_pedido(pedido: PedidoCreate, session=Depends(get_session)):
    use_case = PedidoUseCase(PedidoRepository(session))
    pedido_criado = await use_case.criar_pedido(pedido)
    return PedidoResponse.from_entity(pedido_criado)

@router.get("/andamento", response_model=List[PedidoResponse])
async def listar_pedidos_em_andamento(session=Depends(get_session)):
    use_case = PedidoUseCase(PedidoRepository(session))
    return [PedidoResponse.from_entity(p) for p in await use_case.listar_em_andamento()]

@router.get("/por-status", response_model=List[PedidoResponse])
async def listar_pedidos_por_status(
    status: StatusPedido = Query(...),
    session: AsyncSession = Depends(get_session)
):
    use_case = ListarPedidosPorStatusUseCase(PedidoRepository(session))
    pedidos = await use_case.execute(status)
    return [PedidoResponse.from_entity(p) for p in pedidos]

@router.get("/{pedido_id}", response_model=PedidoResponse)
async def buscar_pedido(pedido_id: UUID, session=Depends(get_session)):
    use_case = PedidoUseCase(PedidoRepository(session))
    pedido = await use_case.buscar_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return PedidoResponse.from_entity(pedido)

@router.put("/{pedido_id}", response_model=PedidoResponse)
async def atualizar_status_pedido(
    pedido_id: UUID,
    dados: PedidoUpdate,
    session=Depends(get_session)
):
    use_case = PedidoUseCase(PedidoRepository(session))
    pedido_atualizado = await use_case.atualizar_status(pedido_id, dados.status)
    return PedidoResponse.from_entity(pedido_atualizado)

@router.post("/{pedido_id}/pagar")
async def gerar_qrcode_pagamento(pedido_id: UUID):
    uow = UnitOfWork()
    mp_client = MercadoPagoClient()
    use_case = CriarPagamentoQRCodeUseCase(uow, mp_client)

    try:
        result = await use_case.execute(pedido_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
