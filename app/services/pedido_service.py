from uuid import UUID
from typing import List
from app.domain.pedido import Pedido
from app.ports.pedido_repository import PedidoRepository
from app.schemas.pedido_schema import PedidoCreate
from app.domain.enums.status_pedido import StatusPedido

class PedidoService:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    async def criar_pedido(self, pedido_data: PedidoCreate) -> Pedido:
        pedido = Pedido(
            produtos_ids=pedido_data.produtos_ids,
            cliente_id=pedido_data.cliente_id
        )
        return await self.repository.criar(pedido)

    async def buscar_por_id(self, pedido_id: UUID) -> Pedido:
        return await self.repository.buscar_por_id(pedido_id)

    async def listar_todos(self) -> List[Pedido]:
        return await self.repository.listar_todos()

    async def atualizar_status(self, pedido_id: UUID, status: StatusPedido) -> Pedido:
        return await self.repository.atualizar_status(pedido_id, status)
