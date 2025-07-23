from typing import List
from fastapi import APIRouter, Depends
from app.ports.pedido_service import PedidoService
from app.services.pedido_service_impl import PedidoServiceImpl
from app.ports.pedido_repository import PedidoRepository
from app.adapters.repositories.pedido_repository_impl import PedidoRepositoryImpl
from app.schemas.pedido_schema import PedidoRequest, PedidoResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_session
from app.schemas.pedido_schema import AtualizarStatusRequest
from app.schemas.pedido_schema import WebhookPagamentoRequest
from app.ports.produto_port import ProdutoServicePort

router = APIRouter(prefix="/pedido", tags=["Pedido"])

# Injeção de dependência do serviço
def get_pedido_service(session: AsyncSession = Depends(get_session)) -> PedidoService:
    repo: PedidoRepository = PedidoRepositoryImpl(session)
    return PedidoServiceImpl(repo)

@router.post("/pagamento/webhook")
async def pagamento_webhook(
    payload: WebhookPagamentoRequest,
    service: PedidoService = Depends(get_pedido_service)
):
    if payload.status_pagamento.lower() == "approved":
        await service.atualizar_status_pedido(payload.pedido_id, "EM_PREPARACAO")
    return {"message": "Webhook recebido"}

@router.get("/andamento", response_model=List[PedidoResponse])
async def listar_pedidos_em_andamento(
    service: PedidoService = Depends(get_pedido_service)
):
    pedidos = await service.listar_pedidos_em_andamento()
    return [
        PedidoResponse(
            id=p.id,
            produtos_ids=p.produtos_ids,
            cliente_id=p.cliente_id,
            status=p.status.value,
            data_criacao=p.data_criacao
        )
        for p in pedidos
    ]

@router.post("/checkout", response_model=PedidoResponse)
async def criar_pedido(
    pedido: PedidoRequest,
    service: PedidoService = Depends(get_pedido_service)
):
    novo_pedido = await service.criar_pedido(pedido.dict())
    return PedidoResponse(
        id=novo_pedido.id,
        produtos_ids=novo_pedido.produtos_ids,
        cliente_id=novo_pedido.cliente_id,
        status=novo_pedido.status.value
    )

@router.put("/status")
async def atualizar_status(
    body: AtualizarStatusRequest,
    service: PedidoService = Depends(get_pedido_service)
):
    await service.atualizar_status_pedido(body.pedido_id, body.novo_status)
    return {"message": "Status atualizado com sucesso"}
