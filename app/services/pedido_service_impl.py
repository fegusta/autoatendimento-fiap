from app.ports.pedido_service import PedidoService
from app.ports.pedido_repository import PedidoRepository
from app.core.domain.pedido import Pedido
from app.core.domain.enums.status_pedido import StatusPedido

from uuid import uuid4, UUID
from datetime import datetime
from typing import List


class PedidoServiceImpl(PedidoService):
    def __init__(self, repo: PedidoRepository):
        self.repo = repo

    async def criar_pedido(self, dados: dict) -> Pedido:
        novo_pedido = Pedido(
            id=uuid4(),
            produtos_ids=dados["produtos_ids"],
            cliente_id=dados.get("cliente_id"),
            status=StatusPedido.RECEBIDO,
            data_criacao=datetime.utcnow()
        )
        return await self.repo.criar(novo_pedido)

    async def listar_pedidos_em_andamento(self) -> List[Pedido]:
        return await self.repo.buscar_em_andamento()

    async def atualizar_status_pedido(self, pedido_id: UUID, novo_status: str) -> None:
        status = StatusPedido(novo_status)
        await self.repo.atualizar_status(pedido_id, status)
    
    async def listar_pedidos_em_andamento(self) -> List[Pedido]:
        return await self.repo.buscar_em_andamento()

    async def atualizar_status_pedido(self, pedido_id: UUID, novo_status: str) -> None:
        status_enum = StatusPedido(novo_status)
        await self.repo.atualizar_status(pedido_id, status_enum)
