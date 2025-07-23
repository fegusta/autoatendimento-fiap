from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from enum import Enum

class StatusPedidoEnum(str, Enum):
    RECEBIDO = "RECEBIDO"
    EM_PREPARACAO = "EM_PREPARACAO"
    PRONTO = "PRONTO"
    FINALIZADO = "FINALIZADO"

class AtualizarStatusRequest(BaseModel):
    pedido_id: UUID
    novo_status: StatusPedidoEnum

class PedidoRequest(BaseModel):
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID] = None


class PedidoResponse(BaseModel):
    id: UUID
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID]
    status: str
    data_criacao: datetime

class WebhookPagamentoRequest(BaseModel):
    pedido_id: UUID
    status_pagamento: str
