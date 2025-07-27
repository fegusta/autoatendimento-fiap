from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.external.mercado_pago_client import MercadoPagoClient
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.infrastructure.db.produto_repository import ProdutoRepository


class CriarPagamentoQRCodeUseCase:
    def __init__(
        self,
        pedido_repository: PedidoRepository,
        produto_repository: ProdutoRepository,
        mercado_pago_client: MercadoPagoClient,
        db: AsyncSession
    ):
        self.pedido_repository = pedido_repository
        self.produto_repository = produto_repository
        self.mercado_pago_client = mercado_pago_client
        self.db = db

    async def execute(self, pedido_id: UUID) -> dict:
        pedido = await self.pedido_repository.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError("Pedido não encontrado")

        if not pedido.produtos_ids:
            raise ValueError("Pedido não possui produtos")

        # Busca os produtos e soma o valor
        produtos = [
            await self.produto_repository.buscar_por_id(pid)
            for pid in pedido.produtos_ids
        ]
        valor_total = sum(p.preco.valor for p in produtos if p)

        # Cria o pagamento no Mercado Pago
        pagamento = await self.mercado_pago_client.criar_pagamento_qr_code(
            valor=valor_total,
            pedido_id=str(pedido_id)
        )

        return {
            "pedido_id": str(pedido_id),
            "valor_total": valor_total,
            "qr_code_url": pagamento.get("init_point"),
            "mercado_pago_id": pagamento.get("id")
        }
