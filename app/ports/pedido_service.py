from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from app.core.domain.pedido import Pedido


class PedidoService(ABC):
    @abstractmethod
    def criar_pedido(self, dados: dict) -> Pedido:
        pass

    @abstractmethod
    def listar_pedidos_em_andamento(self) -> List[Pedido]:
        pass

    @abstractmethod
    def atualizar_status_pedido(self, pedido_id: UUID, novo_status: str) -> None:
        pass

    @abstractmethod
    async def listar_pedidos_em_andamento(self) -> List[Pedido]:
        pass

    @abstractmethod
    async def atualizar_status_pedido(self, pedido_id: UUID, novo_status: str) -> None:
        pass
