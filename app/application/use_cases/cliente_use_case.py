from uuid import UUID
from typing import List, Optional

from app.schemas.cliente_schema import ClienteCreate
from app.infrastructure.db.cliente_repository import ClienteRepository
from app.domain.cliente import Cliente


class ClienteUseCase:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    async def cadastrar_cliente(self, cliente_data: ClienteCreate) -> Cliente:
        return await self.repository.create(cliente_data)

    async def listar_clientes(self) -> List[Cliente]:
        return await self.repository.list_all()

    async def buscar_por_id(self, cliente_id: UUID) -> Optional[Cliente]:
        return await self.repository.get_by_id(cliente_id)
