from uuid import UUID
from app.infrastructure.external.mercado_pago_client import MercadoPagoClient
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.domain.enums.status_pedido import StatusPedido

class PagamentoUseCase:
    def __init__(self, pedido_repository: PedidoRepository, mp_client: MercadoPagoClient):
        self.pedido_repository = pedido_repository
        self.mp_client = mp_client

    async def processar_webhook(self, payload: dict):
        if payload.get("type") != "payment":
            return

        payment_id = str(payload["data"]["id"])
        pagamento = await self.mp_client.buscar_detalhes_pagamento(payment_id)

        status = pagamento.get("status")
        external_reference = pagamento.get("external_reference")  # deve conter o pedido_id

        if not external_reference:
            return  # ou lançar um erro

        pedido_id = UUID(external_reference)

        if status == "approved":
            await self.pedido_repository.atualizar_status(pedido_id, StatusPedido.RECEBIDO)
        elif status == "rejected":
            await self.pedido_repository.atualizar_status(pedido_id, StatusPedido.CANCELADO)
