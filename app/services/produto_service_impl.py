from app.ports.produto_service import ProdutoService
from app.ports.produto_repository import ProdutoRepository
from app.core.domain.produto import Produto, CategoriaProduto

from uuid import uuid4, UUID
from datetime import datetime
from typing import List, Optional


class ProdutoServiceImpl(ProdutoService):
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    async def criar_produto(self, dados: dict) -> Produto:
        produto = Produto(
            id=uuid4(),
            nome=dados["nome"],
            descricao=dados.get("descricao"),
            preco=dados["preco"],
            imagem_url=dados.get("imagem_url"),
            categoria=CategoriaProduto(dados["categoria"]),
            data_criacao=datetime.utcnow()
        )
        return await self.repo.criar(produto)

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        return await self.repo.buscar_por_id(produto_id)

    async def listar_todos(self) -> List[Produto]:
        return await self.repo.listar_todos()

    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        return await self.repo.listar_por_categoria(categoria)

    async def atualizar_produto(self, produto_id: UUID, dados: dict) -> Produto:
        produto_existente = await self.repo.buscar_por_id(produto_id)
        if not produto_existente:
            raise ValueError("Produto não encontrado")

        produto_atualizado = Produto(
            id=produto_existente.id,
            nome=dados.get("nome", produto_existente.nome),
            descricao=dados.get("descricao", produto_existente.descricao),
            preco=dados.get("preco", produto_existente.preco),
            imagem_url=dados.get("imagem_url", produto_existente.imagem_url),
            categoria=CategoriaProduto(dados.get("categoria", produto_existente.categoria.value)),
            data_criacao=produto_existente.data_criacao
        )

        return await self.repo.atualizar(produto_atualizado)

    async def remover_produto(self, produto_id: UUID) -> None:
        await self.repo.remover(produto_id)
