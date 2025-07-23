from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.core.domain.produto import Produto


class ProdutoServicePort(ABC):
    @abstractmethod
    async def listar_produtos(self) -> List[Produto]:
        pass

    @abstractmethod
    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        pass

    @abstractmethod
    async def criar_produto(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    async def deletar_produto(self, produto_id: UUID) -> None:
        pass
