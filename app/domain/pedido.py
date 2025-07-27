from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Optional

from app.domain.enums.status_pedido import StatusPedido

class Pedido:
    def __init__(
        self,
        produtos_ids: List[UUID],
        cliente_id: Optional[UUID] = None,
        status: StatusPedido = StatusPedido.RECEBIDO,
        id: Optional[UUID] = None,
        data_criacao: Optional[datetime] = None,
    ):
        if not produtos_ids:
            raise ValueError("O pedido deve conter pelo menos um produto.")
        
        self.id = id or uuid4()
        self.produtos_ids = produtos_ids
        self.cliente_id = cliente_id
        self.status = status
        self.data_criacao = data_criacao or datetime.utcnow()
