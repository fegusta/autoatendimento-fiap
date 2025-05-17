from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.domain.produto import Produto, CategoriaProduto


class ProdutoRepository(ABC):

    @abstractmethod
    async def criar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    async def atualizar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    async def remover(self, produto_id: UUID) -> None:
        pass

    @abstractmethod
    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        pass

    @abstractmethod
    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        pass
