from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.adapters.models.produto_model import ProdutoModel
from app.domain.produto import Produto, CategoriaProduto
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
            categoria=CategoriaProduto(produto.categoria).value,
            imagem_url=produto.imagem_url,
            data_criacao=produto.data_criacao
        )
        self.session.add(db_produto)
        await self.session.commit()
        await self.session.refresh(db_produto)
        return Produto(
            id=db_produto.id,
            nome=db_produto.nome,
            descricao=db_produto.descricao,
            preco=db_produto.preco,
            categoria=CategoriaProduto(db_produto.categoria),
            imagem_url=db_produto.imagem_url,
            data_criacao=db_produto.data_criacao
        )

    async def buscar_por_id(self, produto_id: UUID) -> Optional[Produto]:
        result = await self.session.get(ProdutoModel, produto_id)
        if result:
            return Produto(
                id=result.id,
                nome=result.nome,
                descricao=result.descricao,
                preco=result.preco,
                categoria=CategoriaProduto(result.categoria),
                imagem_url=result.imagem_url,
                data_criacao=result.data_criacao
            )
        return None

    async def listar_todos(self) -> List[Produto]:
        result = await self.session.execute(select(ProdutoModel))
        produtos = result.scalars().all()
        return [
            Produto(
                id=p.id,
                nome=p.nome,
                descricao=p.descricao,
                preco=p.preco,
                categoria=CategoriaProduto(p.categoria),
                imagem_url=p.imagem_url,
                data_criacao=p.data_criacao
            ) for p in produtos
        ]

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
            db_produto.categoria = produto.categoria.value
            db_produto.imagem_url = produto.imagem_url
            await self.session.commit()
            await self.session.refresh(db_produto)
            return Produto(
                id=db_produto.id,
                nome=db_produto.nome,
                descricao=db_produto.descricao,
                preco=db_produto.preco,
                categoria=CategoriaProduto(db_produto.categoria),
                imagem_url=db_produto.imagem_url,
                data_criacao=db_produto.data_criacao
            )
        raise ValueError("Produto não encontrado")

    async def buscar_por_categoria(self, categoria: str) -> List[Produto]:
        result = await self.session.execute(
            select(ProdutoModel).where(ProdutoModel.categoria == categoria)
        )
        produtos = result.scalars().all()
        return [
            Produto(
                id=p.id,
                nome=p.nome,
                descricao=p.descricao,
                preco=p.preco,
                categoria=CategoriaProduto(p.categoria),
                imagem_url=p.imagem_url,
                data_criacao=p.data_criacao
            ) for p in produtos
        ]

    async def listar_por_categoria(self, categoria: str) -> List[Produto]:
        # Evite duplicação se o comportamento for o mesmo
        return await self.buscar_por_categoria(categoria)
