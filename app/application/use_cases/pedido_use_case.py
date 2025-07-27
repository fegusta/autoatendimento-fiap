from uuid import UUID
from typing import List, Optional

from app.domain.pedido import Pedido
from app.domain.enums.status_pedido import StatusPedido
from app.schemas.pedido_schema import PedidoCreate
from app.infrastructure.db.pedido_repository import PedidoRepository


class PedidoUseCase:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    async def criar_pedido(self, pedido_data: PedidoCreate) -> Pedido:
        pedido = Pedido(
            produtos_ids=pedido_data.produtos_ids,
            cliente_id=pedido_data.cliente_id,
        )
        return await self.repository.criar(pedido)

    async def buscar_por_id(self, pedido_id: UUID) -> Optional[Pedido]:
        return await self.repository.buscar_por_id(pedido_id)

    async def listar_pedidos(self) -> List[Pedido]:
        return await self.repository.listar_todos()

    async def atualizar_status(self, pedido_id: UUID, novo_status: StatusPedido) -> Pedido:
        return await self.repository.atualizar_status(pedido_id, novo_status)

    async def listar_por_status(self, status: StatusPedido) -> List[Pedido]:
        return await self.repository.listar_por_status(status)

    async def listar_em_andamento(self) -> List[Pedido]:
        return await self.repository.buscar_em_andamento()
    
    async def realizar_checkout(self, produtos_ids: List[UUID], cliente_id: Optional[UUID] = None) -> UUID:
        novo_pedido = Pedido(produtos_ids=produtos_ids, cliente_id=cliente_id)
        pedido_criado = await self.repository.criar(novo_pedido)
        return pedido_criado.id
