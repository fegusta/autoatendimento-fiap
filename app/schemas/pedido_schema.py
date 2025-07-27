from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime

from app.domain.enums.status_pedido import StatusPedido
from app.domain.pedido import Pedido


class PedidoCreate(BaseModel):
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID] = None


class PedidoUpdate(BaseModel):
    status: StatusPedido


class PedidoResponse(BaseModel):
    id: UUID
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID]
    status: StatusPedido
    data_criacao: datetime

    class Config:
        from_attributes = True

    @classmethod
    def from_entity(cls, pedido: Pedido) -> "PedidoResponse":
        return cls(
            id=pedido.id,
            produtos_ids=pedido.produtos_ids,
            cliente_id=pedido.cliente_id,
            status=pedido.status,
            data_criacao=pedido.data_criacao
        )
