from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.cliente import Cliente


class ClienteRepository(ABC):

    @abstractmethod
    async def salvar(self, cliente: Cliente) -> Cliente:
        pass

    @abstractmethod
    async def buscar_por_cpf(self, cliente_cpf: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def listar_todos(self) -> List[Cliente]:
        pass
