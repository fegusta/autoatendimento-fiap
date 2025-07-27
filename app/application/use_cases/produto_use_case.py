from uuid import UUID
from typing import List, Optional

from app.domain.produto import Produto, CategoriaProduto
from app.domain.value_objects.preco import Preco
from app.domain.value_objects.nome import Nome
from app.domain.value_objects.descricao import Descricao
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate
from app.infrastructure.db.produto_repository import ProdutoRepository


class ProdutoUseCase:
    def __init__(self, repository: ProdutoRepository):
        self.repository = repository

    async def criar_produto(self, data: ProdutoCreate) -> Produto:
        produto = Produto(
            nome=Nome(data.nome),
            descricao=Descricao(data.descricao) if data.descricao else Descricao(""),
            preco=Preco(data.preco),
            categoria=CategoriaProduto(data.categoria)
        )
        return await self.repository.criar_produto(produto)

    async def atualizar_produto(self, produto_id: UUID, data: ProdutoUpdate) -> Produto:
        produto_existente = await self.repository.buscar_por_id(produto_id)
        if not produto_existente:
            raise ValueError("Produto não encontrado.")

        # Atualiza somente os campos fornecidos
        if data.nome:
            produto_existente.nome = Nome(data.nome)

        if data.descricao:
            produto_existente.descricao = Descricao(data.descricao)

        if data.categoria:
            produto_existente.categoria = CategoriaProduto(data.categoria)

        if data.preco:
            produto_existente.preco = Preco(data.preco)

        return await self.repository.atualizar(produto_existente)

    async def remover_produto(self, produto_id: UUID) -> None:
        await self.repository.remover(produto_id)

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        return await self.repository.buscar_por_id(produto_id)

    async def listar_produtos(self) -> List[Produto]:
        return await self.repository.listar_produtos()

    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        return await self.repository.listar_por_categoria(categoria)
