from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from typing import List, Optional

from app.domain.cliente import Cliente
from app.infrastructure.db.cliente_model import ClienteModel
from app.schemas.cliente_schema import ClienteCreate


class ClienteRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, data: ClienteCreate) -> Cliente:
        cliente_model = ClienteModel(
            nome=data.nome,
            email=data.email,
            cpf=data.cpf
        )
        self.db.add(cliente_model)
        await self.db.commit()
        await self.db.refresh(cliente_model)
        return self._to_domain(cliente_model)

    async def get_by_id(self, cliente_id: UUID) -> Optional[Cliente]:
        result = await self.db.execute(
            select(ClienteModel).where(ClienteModel.id == cliente_id)
        )
        cliente_model = result.scalars().first()
        return self._to_domain(cliente_model) if cliente_model else None

    async def list_all(self) -> List[Cliente]:
        result = await self.db.execute(select(ClienteModel))
        clientes = result.scalars().all()
        return [self._to_domain(cliente) for cliente in clientes]

    def _to_domain(self, model: ClienteModel) -> Cliente:
        return Cliente(
            id=model.id,
            nome=model.nome,
            email=model.email,
            cpf=model.cpf,
            data_criacao=model.data_criacao
        )
