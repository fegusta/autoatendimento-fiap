from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.domain.pedido import Pedido


class PedidoRepository(ABC):

    @abstractmethod
    async def criar(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    async def buscar_por_id(self, pedido_id: UUID) -> Optional[Pedido]:
        pass

    @abstractmethod
    async def listar_todos(self) -> List[Pedido]:
        pass

    @abstractmethod
    async def atualizar_status(self, pedido_id: UUID, novo_status: str) -> Pedido:
        pass

    @abstractmethod
    async def listar_por_status(self, status: str) -> List[Pedido]:
        pass
