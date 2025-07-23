from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List
from uuid import UUID

from app.core.domain.produto import Produto, CategoriaProduto
from app.ports.produto_repository import ProdutoRepository
from app.adapters.models.produto_model import ProdutoModel


class ProdutoRepositoryImpl(ProdutoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, produto: Produto) -> Produto:
        db_produto = ProdutoModel.from_entity(produto)
        self.session.add(db_produto)
        await self.session.commit()
        await self.session.refresh(db_produto)
        return db_produto.to_entity()

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        result = await self.session.get(ProdutoModel, produto_id)
        return result.to_entity() if result else None

    async def listar_todos(self) -> List[Produto]:
        result = await self.session.execute(select(ProdutoModel))
        produtos = result.scalars().all()
        return [p.to_entity() for p in produtos]

    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        result = await self.session.execute(
            select(ProdutoModel).where(ProdutoModel.categoria == categoria)
        )
        produtos = result.scalars().all()
        return [p.to_entity() for p in produtos]

    async def atualizar(self, produto: Produto) -> Produto:
        db_produto = await self.session.get(ProdutoModel, produto.id)
        if not db_produto:
            raise ValueError("Produto não encontrado")

        # Atualiza campos
        db_produto.nome = produto.nome
        db_produto.descricao = produto.descricao
        db_produto.preco = produto.preco
        db_produto.imagem_url = produto.imagem_url
        db_produto.categoria = produto.categoria

        await self.session.commit()
        await self.session.refresh(db_produto)
        return db_produto.to_entity()

    async def remover(self, produto_id: UUID) -> None:
        produto = await self.session.get(ProdutoModel, produto_id)
        if produto:
            await self.session.delete(produto)
            await self.session.commit()
