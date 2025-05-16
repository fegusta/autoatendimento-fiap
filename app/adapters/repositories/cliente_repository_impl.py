from app.domain.cliente import Cliente
from app.ports.cliente_repository import ClienteRepository
from uuid import UUID
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.adapters.repositories.models import ClienteModel


class ClienteRepositoryImpl(ClienteRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def salvar(self, cliente: Cliente) -> Cliente:
        model = ClienteModel.from_entity(cliente)
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model.to_entity()

    async def buscar_por_cpf(self, cliente_cpf: str) -> Optional[Cliente]:
        stmt = select(ClienteModel).where(ClienteModel.cpf == cliente_cpf)
        result = await self.session.execute(stmt)
        row = result.scalar_one_or_none()
        return row.to_entity() if row else None

    async def listar_todos(self) -> List[Cliente]:
        result = await self.session.execute(select(ClienteModel))
        return [c.to_entity() for c in result.scalars().all()]
