from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class CheckoutRequest(BaseModel):
    produtos_ids: List[UUID]
    cliente_id: Optional[UUID] = None


class CheckoutResponse(BaseModel):
    pedido_id: UUID
