import asyncio
from app.main import Base, engine

async def criar_tabelas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(criar_tabelas())
