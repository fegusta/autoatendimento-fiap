from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.infrastructure.db.db import get_session
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.infrastructure.external.mercado_pago_client import MercadoPagoClient

from app.application.use_cases.pagamento_use_case import PagamentoUseCase

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/pagamento")
async def receber_webhook(
    request: Request,
    db: AsyncSession = Depends(get_session)
):
    payload = await request.body()
    dados = json.loads(payload)

    if not dados.get("data", {}).get("id"):
        raise HTTPException(status_code=400, detail="ID do pagamento não encontrado")

    use_case = PagamentoUseCase(
        pedido_repository=PedidoRepository(db),
        mp_client=MercadoPagoClient()
    )

    try:
        await use_case.processar_webhook(dados)
        return {"mensagem": "Webhook processado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
