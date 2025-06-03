from app.application.schemas.cliente_schema import ClienteCreateSchema
from app.core.domain.interfaces.cliente_repository import ClienteRepository
from app.core.domain.cliente import Cliente
from typing import List, Optional

from app.core.domain.value_objects.cpf import CPF
from app.core.domain.value_objects.email import Email
from app.core.domain.value_objects.nome import Nome


class ClienteService:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    async def criar_cliente(self, cliente_schema: ClienteCreateSchema) -> Cliente:
        cliente = Cliente(
            nome=Nome(cliente_schema.nome),
            email=Email(cliente_schema.email),
            cpf=CPF(cliente_schema.cpf),            
        )
        
        return await self.repository.salvar(cliente)

    async def buscar_por_cpf(self, cliente_cpf: str) -> Optional[Cliente]:
        return await self.repository.buscar_por_cpf(cliente_cpf)

    async def listar_clientes(self) -> List[Cliente]:
        return await self.repository.listar_todos()
