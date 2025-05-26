from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from app.application.schemas.pedido_schema import PedidoCreate, PedidoRead, PedidoUpdate
from app.core.services.pedido_service import PedidoService
from app.application.schemas.pedido_schema import AtualizarStatusPedidoSchema
from app.dependencies import get_pedido_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("", response_model=PedidoRead)
async def criar_pedido(pedido: PedidoCreate, service: PedidoService = Depends(get_pedido_service)):
    return await service.criar_pedido(pedido)

@router.get("/andamento", response_model=List[PedidoRead])
async def listar_pedidos_em_andamento(service: PedidoService = Depends(get_pedido_service)):
    return await service.listar_pedidos_em_andamento()

@router.get("", response_model=List[PedidoRead])
async def listar_pedidos(service: PedidoService = Depends(get_pedido_service)):
    return await service.listar_todos()

@router.get("/{pedido_id}", response_model=PedidoRead)
async def buscar_pedido(pedido_id: UUID, service: PedidoService = Depends(get_pedido_service)):
    pedido = await service.buscar_por_id(pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.patch("/{pedido_id}", response_model=PedidoRead)
async def atualizar_status_pedido_patch(
    pedido_id: UUID,
    update: PedidoUpdate,
    service: PedidoService = Depends(get_pedido_service)):
    return await service.atualizar_status(pedido_id, update.status)

@router.put("/{pedido_id}", response_model=PedidoRead)
async def atualizar_status_pedido_put(
    pedido_id: UUID,
    dados: AtualizarStatusPedidoSchema,
    service: PedidoService = Depends(get_pedido_service)):
    return await service.atualizar_status(pedido_id, dados.status)
