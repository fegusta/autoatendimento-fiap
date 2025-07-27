from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.infrastructure.db.pedido_model import PedidoModel
from app.domain.pedido import Pedido
from app.domain.enums.status_pedido import StatusPedido

class PedidoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = PedidoModel

    async def criar(self, pedido: Pedido) -> Pedido:
        db_pedido = PedidoModel.from_entity(pedido)
        self.session.add(db_pedido)
        await self.session.commit()
        await self.session.refresh(db_pedido)
        return db_pedido.to_entity()

    async def buscar_por_id(self, pedido_id: UUID) -> Optional[Pedido]:
        result = await self.session.get(PedidoModel, pedido_id)
        return result.to_entity() if result else None

    async def listar_todos(self) -> List[Pedido]:
        result = await self.session.execute(select(PedidoModel))
        pedidos = result.scalars().all()
        return [p.to_entity() for p in pedidos]

    async def atualizar_status(self, pedido_id: UUID, novo_status: StatusPedido) -> Pedido:
        pedido = await self.session.get(PedidoModel, pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        pedido.status = novo_status.value
        await self.session.commit()
        await self.session.refresh(pedido)
        return pedido.to_entity()

    async def listar_por_status(self, status: StatusPedido) -> List[Pedido]:
        result = await self.session.execute(
            select(PedidoModel).where(PedidoModel.status == status.value)
        )
        pedidos = result.scalars().all()
        return [p.to_entity() for p in pedidos]

    async def buscar_em_andamento(self) -> List[Pedido]:
        result = await self.session.execute(
            select(PedidoModel).where(PedidoModel.status != StatusPedido.FINALIZADO.value).order_by(PedidoModel.data_criacao)
        )
        pedidos = result.scalars().all()
        return [p.to_entity() for p in pedidos]
    
