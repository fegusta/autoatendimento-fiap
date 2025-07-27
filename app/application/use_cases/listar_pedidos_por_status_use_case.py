from typing import List
from app.domain.pedido import Pedido
from app.domain.enums.status_pedido import StatusPedido
from app.infrastructure.db.pedido_repository import PedidoRepository

class ListarPedidosPorStatusUseCase:
    def __init__(self, pedido_repository: PedidoRepository):
        self.pedido_repository = pedido_repository

    async def execute(self, status: StatusPedido) -> List[Pedido]:
        return await self.pedido_repository.listar_por_status(status)
