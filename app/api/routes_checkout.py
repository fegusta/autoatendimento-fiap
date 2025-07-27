from fastapi import APIRouter, Depends
from app.schemas.checkout_schema import CheckoutRequest, CheckoutResponse
from app.infrastructure.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.pedido_repository import PedidoRepository
from app.application.use_cases.pedido_use_case import PedidoUseCase

router = APIRouter(prefix="/checkout", tags=["Checkout"])


@router.post("/", response_model=CheckoutResponse)
async def realizar_checkout(
    dados: CheckoutRequest,
    db: AsyncSession = Depends(get_session)
):
    use_case = PedidoUseCase(PedidoRepository(db))
    pedido_id = await use_case.realizar_checkout(
        produtos_ids=dados.produtos_ids,
        cliente_id=dados.cliente_id
    )
    return CheckoutResponse(pedido_id=pedido_id)
