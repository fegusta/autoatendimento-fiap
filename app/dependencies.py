from app.adapters.repositories.cliente_repository_impl import ClienteRepositoryImpl
from app.services.cliente_service import ClienteService
from app.adapters.repositories.produto_repository_impl import ProdutoRepositoryImpl
from app.services.produto_service import ProdutoService
from app.db.db import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_cliente_service(session: AsyncSession = Depends(get_session)) -> ClienteService:
    repository = ClienteRepositoryImpl(session)
    return ClienteService(repository)

async def get_produto_service(session = Depends(get_session)) -> ProdutoService:
    repository = ProdutoRepositoryImpl(session)
    return ProdutoService(repository)