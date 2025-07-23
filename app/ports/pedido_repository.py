from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.core.domain.pedido import Pedido
from app.core.domain.enums.status_pedido import StatusPedido


class PedidoRepository(ABC):
    @abstractmethod
    async def criar(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    async def buscar_por_id(self, pedido_id: UUID) -> Optional[Pedido]:
        pass

    @abstractmethod
    async def buscar_em_andamento(self) -> List[Pedido]:
        pass

    @abstractmethod
    async def atualizar_status(self, pedido_id: UUID, status: StatusPedido) -> Pedido:
        pass
