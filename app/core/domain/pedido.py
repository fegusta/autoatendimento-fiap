from uuid import UUID, uuid4
from datetime import datetime
from app.core.domain.enums.status_pedido import StatusPedido
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.adapters.models.pedido_model import PedidoModel

class Pedido:
    def __init__(
        self,
        produtos_ids: List[UUID],
        cliente_id: Optional[UUID] = None,
        status: StatusPedido = StatusPedido.RECEBIDO,
        id: Optional[UUID] = None,
        data_criacao: Optional[datetime] = None
    ):
        if not produtos_ids or len(produtos_ids) == 0:
            raise ValueError("O pedido deve conter pelo menos um produto.")
        
        self.id = id or uuid4()
        self.produtos_ids = produtos_ids
        self.cliente_id = cliente_id
        self.status = status
        self.data_criacao = data_criacao or datetime.utcnow()

    @staticmethod
    def from_model(model: "PedidoModel") -> "Pedido":
        return Pedido(
            id=model.id,
            produtos_ids=model.produtos_ids,
            cliente_id=model.cliente_id,
            status=model.status,
            data_criacao=model.data_criacao,
        )
