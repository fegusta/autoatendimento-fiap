from uuid import UUID
from typing import List
from app.domain.produto import Produto
from app.ports.produto_repository import ProdutoRepository
from app.schemas.produto_schema import ProdutoCreate

class ProdutoService:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository

    async def criar_produto(self, produto_data: ProdutoCreate) -> Produto:
        produto = Produto(
            nome=produto_data.nome,
            descricao=produto_data.descricao,
            preco=produto_data.preco,
            categoria=produto_data.categoria
        )
        return await self.repository.criar(produto)

    async def buscar_produto_por_id(self, produto_id: UUID) -> Produto:
        produto = await self.repository.buscar_por_id(produto_id)
        if not produto:
            raise ValueError("Produto não encontrado")
        return produto

    async def listar_produtos(self) -> List[Produto]:
        return await self.repository.listar_todos()

    async def remover_produto(self, produto_id: UUID) -> None:
        return await self.repository.remover(produto_id)

    async def atualizar_produto(self, produto: Produto) -> Produto:
        return await self.repository.atualizar(produto)

    async def buscar_por_categoria(self, categoria: str) -> List[Produto]:
        return await self.repository.buscar_por_categoria(categoria)
