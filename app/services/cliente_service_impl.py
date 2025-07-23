from app.ports.cliente_service import ClienteService
from app.ports.cliente_repository import ClienteRepository
from app.core.domain.cliente import Cliente

from uuid import uuid4, UUID
from datetime import datetime
from typing import List, Optional


class ClienteServiceImpl(ClienteService):
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    async def registrar_cliente(self, dados: dict) -> Cliente:
        novo_cliente = Cliente(
            id=uuid4(),
            nome=dados.get("nome"),
            email=dados.get("email"),
            cpf=dados.get("cpf"),
            data_criacao=datetime.utcnow()
        )
        return await self.repo.criar(novo_cliente)

    async def buscar_por_id(self, cliente_id: UUID) -> Optional[Cliente]:
        return await self.repo.buscar_por_id(cliente_id)

    async def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        return await self.repo.buscar_por_cpf(cpf)

    async def listar_todos(self) -> List[Cliente]:
        return await self.repo.listar_todos()
