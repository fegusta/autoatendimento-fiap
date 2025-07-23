from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.core.domain.cliente import Cliente


class ClienteService(ABC):
    @abstractmethod
    async def registrar_cliente(self, dados: dict) -> Cliente:
        pass

    @abstractmethod
    async def buscar_por_id(self, cliente_id: UUID) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        pass

    @abstractmethod
    async def listar_todos(self) -> List[Cliente]:
        pass
