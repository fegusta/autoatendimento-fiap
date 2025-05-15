from app.ports.cliente_repository import ClienteRepository
from app.domain.cliente import Cliente
from typing import List, Optional
from uuid import UUID


class ClienteService:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    async def criar_cliente(self, cliente: Cliente) -> Cliente:
        return await self.repository.salvar(cliente)

    async def buscar_por_id(self, cliente_id: UUID) -> Optional[Cliente]:
        return await self.repository.buscar_por_id(cliente_id)

    async def listar_clientes(self) -> List[Cliente]:
        return await self.repository.listar_todos()
