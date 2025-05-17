from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.adapters.repositories.models import ProdutoModel
from app.domain.produto import Produto
from app.ports.produto_repository import ProdutoRepository


class ProdutoRepositoryImpl(ProdutoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar(self, produto: Produto) -> Produto:
        db_produto = ProdutoModel(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            categoria=produto.categoria,
            imagem_url=produto.imagem_url,
            data_criacao=produto.data_criacao
        )
        self.session.add(db_produto)
        await self.session.commit()
        await self.session.refresh(db_produto)
        return Produto.from_orm(db_produto)

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        result = await self.session.get(ProdutoModel, produto_id)
        if result:
            return Produto.from_orm(result)
        return None

    async def listar_todos(self) -> List[Produto]:
        result = await self.session.execute(select(ProdutoModel))
        produtos = result.scalars().all()
        return [Produto.from_orm(p) for p in produtos]

    async def remover(self, produto_id: UUID) -> None:
        produto = await self.session.get(ProdutoModel, produto_id)
        if produto:
            await self.session.delete(produto)
            await self.session.commit()

    async def atualizar(self, produto: Produto) -> Produto:
        db_produto = await self.session.get(ProdutoModel, produto.id)
        if db_produto:
            db_produto.nome = produto.nome
            db_produto.descricao = produto.descricao
            db_produto.preco = produto.preco
            db_produto.categoria = produto.categoria
            db_produto.imagem_url = produto.imagem_url
            await self.session.commit()
            await self.session.refresh(db_produto)
            return Produto.from_orm(db_produto)
        raise ValueError("Produto não encontrado")

    async def buscar_por_categoria(self, categoria: str) -> List[Produto]:
        result = await self.session.execute(
            select(ProdutoModel).where(ProdutoModel.categoria == categoria)
        )
        produtos = result.scalars().all()
        return [Produto.from_orm(p) for p in produtos]
