from uuid import UUID
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.produto import Produto, CategoriaProduto
from app.infrastructure.db.produto_model import ProdutoModel
from app.schemas.produto_schema import ProdutoResponse
from app.schemas.produto_schema import ProdutoCreate
from uuid import uuid4
from app.domain.value_objects.preco import Preco
from datetime import datetime

class ProdutoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def criar_produto(self, produto: Produto) -> Produto:
        db_produto = ProdutoModel(
            id=produto.id,
            nome=str(produto.nome),
            descricao=str(produto.descricao),
            preco=produto.preco.valor,
            categoria=produto.categoria,
            imagem_url=produto.imagem_url,
            data_criacao=produto.data_criacao
        )
        self.session.add(db_produto)
        await self.session.commit()
        await self.session.refresh(db_produto)
        return db_produto.to_entity()

    async def atualizar(self, produto: Produto) -> Produto:
        db_produto = await self.session.get(ProdutoModel, produto.id)
        if not db_produto:
            raise ValueError("Produto não encontrado")

        db_produto.nome = str(produto.nome)
        db_produto.descricao = str(produto.descricao)
        db_produto.preco = produto.preco.valor
        db_produto.categoria = produto.categoria
        db_produto.imagem_url = produto.imagem_url

        await self.session.commit()
        await self.session.refresh(db_produto)
        return db_produto.to_entity()

    async def remover(self, produto_id: UUID) -> None:
        db_produto = await self.session.get(ProdutoModel, produto_id)
        if db_produto:
            await self.session.delete(db_produto)
            await self.session.commit()

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        db_produto = await self.session.get(ProdutoModel, produto_id)
        return db_produto.to_entity() if db_produto else None

    async def listar_produtos(self) -> list[Produto]:
        stmt = select(ProdutoModel)
        result = await self.session.execute(stmt)
        return [p.to_entity() for p in result.scalars().all()]

    async def listar_por_categoria(self, categoria: CategoriaProduto) -> List[Produto]:
        result = await self.session.execute(
            select(ProdutoModel).where(ProdutoModel.categoria == categoria)
        )
        produtos = result.scalars().all()
        return [p.to_entity() for p in produtos]
