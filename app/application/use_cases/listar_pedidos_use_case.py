from app.infrastructure.db.pedido_repository import PedidoRepository
from app.domain.enums.status_pedido import StatusPedido

class ListarPedidosUseCase:
    def __init__(self, pedido_repository: PedidoRepository):
        self.pedido_repository = pedido_repository

    async def execute(self):
        pedidos = await self.pedido_repository.listar_todos()

        # Excluir finalizados
        pedidos = [p for p in pedidos if p.status != StatusPedido.FINALIZADO]

        # Ordenar por status e data
        status_ordem = {
            StatusPedido.PRONTO: 0,
            StatusPedido.EM_PREPARACAO: 1,
            StatusPedido.RECEBIDO: 2
        }

        pedidos.sort(key=lambda p: (status_ordem.get(p.status, 99), p.data_criacao))
        return pedidos
