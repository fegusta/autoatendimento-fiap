from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
import json

from app.infrastructure.db.db import get_session
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.infrastructure.db.produto_repository import ProdutoRepository
from app.infrastructure.external.mercado_pago_client import MercadoPagoClient

from app.application.use_cases.pedido_use_case import PedidoUseCase
from app.application.use_cases.criar_pagamento_qrcode_use_case import CriarPagamentoQRCodeUseCase

router = APIRouter(prefix="/pagamento", tags=["Pagamento"])


@router.get("/{pedido_id}/status")
async def consultar_status_pagamento(
    pedido_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    use_case = PedidoUseCase(PedidoRepository(db))
    try:
        status_pagamento = await use_case.consultar_status_pagamento(pedido_id)
        return {"status_pagamento": status_pagamento}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/{pedido_id}/qrcode")
async def gerar_qr_code_pagamento(
    pedido_id: UUID,
    db: AsyncSession = Depends(get_session)
):
    use_case = CriarPagamentoQRCodeUseCase(
        pedido_repository=PedidoRepository(db),
        produto_repository=ProdutoRepository(db),
        mercado_pago_client=MercadoPagoClient(),
        db=db
    )

    try:
        result = await use_case.execute(pedido_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao gerar QR Code")
