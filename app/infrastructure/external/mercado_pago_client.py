import os
import httpx

MERCADO_PAGO_BASE_URL = "https://api.mercadopago.com"
ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")

class MercadoPagoClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

    async def buscar_detalhes_pagamento(self, payment_id: str) -> dict:
        url = f"{MERCADO_PAGO_BASE_URL}/v1/payments/{payment_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def criar_pagamento_qr_code(self, valor: float, pedido_id: str) -> dict:
        url = f"{MERCADO_PAGO_BASE_URL}/checkout/preferences"
        payload = {
            "items": [
                {
                    "title": f"Pedido {pedido_id}",
                    "quantity": 1,
                    "currency_id": "BRL",
                    "unit_price": float(valor)
                }
            ],
            "external_reference": pedido_id,
            "notification_url": os.getenv("MP_WEBHOOK_URL")
        }
        print(f"\n[DEBUG] Enviando para Mercado Pago: {payload}\n")

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, json=payload)
            print(f"\n[DEBUG] Resposta Mercado Pago: {response.status_code} - {response.text}\n")
            response.raise_for_status()
            return response.json()
