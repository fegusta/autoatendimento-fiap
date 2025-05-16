from app.adapters.repositories.cliente_repository_impl import ClienteRepositoryImpl
from app.services.cliente_service import ClienteService
from app.db.db import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_cliente_service(session: AsyncSession = Depends(get_session)) -> ClienteService:
    repo = ClienteRepositoryImpl(session)
    return ClienteService(repo)
