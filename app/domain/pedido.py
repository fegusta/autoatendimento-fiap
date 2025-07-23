from uuid import UUID
from datetime import datetime
from typing import List, Optional
from app.core.domain.enums.status_pedido import StatusPedido


class Pedido:
    def __init__(
        self,
        id: UUID,
        produtos_ids: List[UUID],
        cliente_id: Optional[UUID],
        status: StatusPedido,
        data_criacao: datetime
    ):
        self.id = id
        self.produtos_ids = produtos_ids
        self.cliente_id = cliente_id
        self.status = status
        self.data_criacao = data_criacao

    def atualizar_status(self, novo_status: StatusPedido):
        # Aqui você pode validar transições se quiser
        self.status = novo_status
