from app.adapters.repositories.produto_repository_impl import ProdutoRepositoryImpl
from app.application.services.produto_service import ProdutoService
from app.adapters.repositories.pedido_repository_impl import PedidoRepositoryImpl
from app.application.services.pedido_service import PedidoService
from app.adapters.db import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_produto_service(session = Depends(get_session)) -> ProdutoService:
    repository = ProdutoRepositoryImpl(session)
    return ProdutoService(repository)

async def get_pedido_service(session: AsyncSession = Depends(get_session)) -> PedidoService:
    repository = PedidoRepositoryImpl(session)
    return PedidoService(repository)
    