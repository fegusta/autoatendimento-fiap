from abc import ABC, abstractmethod
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.infrastructure.db.produto_repository import ProdutoRepository

class UnitOfWork(ABC):
    pedidos: PedidoRepository
    produtos: ProdutoRepository

    @abstractmethod
    async def __aenter__(self): ...
    
    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
