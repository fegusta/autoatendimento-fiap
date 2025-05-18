from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.domain.enums.status_pedido import StatusPedido


class PedidoCreate(BaseModel):
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID] = None

class AtualizarStatusPedidoSchema(BaseModel):
    status: StatusPedido

class PedidoUpdate(BaseModel):
    status: StatusPedido


class PedidoRead(BaseModel):
    id: UUID
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID]
    status: StatusPedido
    data_criacao: datetime

    class Config:
        from_attributes = True
