from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List
from uuid import UUID

from app.core.domain.cliente import Cliente
from app.ports.cliente_repository import ClienteRepository
from app.adapters.models.cliente_model import ClienteModel


class ClienteRepositoryImpl(ClienteRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, cliente: Cliente) -> Cliente:
        db_cliente = ClienteModel.from_entity(cliente)
        self.session.add(db_cliente)
        await self.session.commit()
        await self.session.refresh(db_cliente)
        return db_cliente.to_entity()

    async def buscar_por_id(self, cliente_id: UUID) -> Optional[Cliente]:
        result = await self.session.get(ClienteModel, cliente_id)
        return result.to_entity() if result else None

    async def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        result = await self.session.execute(
            select(ClienteModel).where(ClienteModel.cpf == cpf)
        )
        cliente = result.scalars().first()
        return cliente.to_entity() if cliente else None

    async def listar_todos(self) -> List[Cliente]:
        result = await self.session.execute(select(ClienteModel))
        clientes = result.scalars().all()
        return [c.to_entity() for c in clientes]
