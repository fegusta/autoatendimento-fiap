from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.adapters.models.pedido_model import PedidoModel
from app.domain.pedido import Pedido
from app.domain.enums.status_pedido import StatusPedido
from app.ports.pedido_repository import PedidoRepository


class PedidoRepositoryImpl(PedidoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, pedido: Pedido) -> Pedido:
        db_pedido = PedidoModel.from_entity(pedido)
        self.session.add(db_pedido)
        await self.session.commit()
        await self.session.refresh(db_pedido)
        return db_pedido.to_entity()

    async def buscar_por_id(self, pedido_id: UUID) -> Optional[Pedido]:
        result = await self.session.get(PedidoModel, pedido_id)
        if result:
            return result.to_entity()
        return None

    async def listar_todos(self) -> List[Pedido]:
        result = await self.session.execute(select(PedidoModel))
        pedidos = result.scalars().all()
        return [p.to_entity() for p in pedidos]

    async def atualizar_status(self, pedido_id: UUID, status: StatusPedido) -> Pedido:
        pedido = await self.session.get(PedidoModel, pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        pedido.status = status
        await self.session.commit()
        await self.session.refresh(pedido)
        return pedido.to_entity()


    async def listar_por_status(self, status: str) -> List[Pedido]:
        result = await self.session.execute(
            select(PedidoModel).where(PedidoModel.status == status)
        )
        pedidos = result.scalars().all()
        return [p.to_entity() for p in pedidos]
    
    async def buscar_em_andamento(self) -> List[Pedido]:
        result = await self.session.execute(
            select(PedidoModel).where(PedidoModel.status != StatusPedido.FINALIZADO).order_by(PedidoModel.data_criacao)
        )
        pedidos = result.scalars().all()
        return [Pedido.from_model(p) for p in pedidos]

