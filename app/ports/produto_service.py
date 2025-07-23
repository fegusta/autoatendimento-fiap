from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.core.domain.produto import Produto, CategoriaProduto


class ProdutoService(ABC):
    @abstractmethod
    async def criar_produto(self, dados: dict) -> Produto:
        pass

    @abstractmethod
    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        pass

    @abstractmethod
    async def listar_todos(self) -> List[Produto]:
        pass

    @abstractmethod
    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        pass

    @abstractmethod
    async def atualizar_produto(self, produto_id: UUID, dados: dict) -> Produto:
        pass

    @abstractmethod
    async def remover_produto(self, produto_id: UUID) -> None:
        pass
