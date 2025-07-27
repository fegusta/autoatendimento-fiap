from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ARRAY
from uuid import uuid4, UUID
from datetime import datetime
from typing import List, Optional

from app.infrastructure.db.base import Base
from app.domain.pedido import Pedido
from app.domain.enums.status_pedido import StatusPedido


class PedidoModel(Base):
    __tablename__ = "pedidos"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    produtos_ids: Mapped[List[UUID]] = mapped_column(ARRAY(PG_UUID(as_uuid=True)))
    cliente_id: Mapped[Optional[UUID]] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("clientes.id"), nullable=True)
    status: Mapped[str] = mapped_column(String, default=StatusPedido.RECEBIDO.value)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_entity(self) -> Pedido:
        return Pedido(
            id=self.id,
            produtos_ids=self.produtos_ids,
            cliente_id=self.cliente_id,
            status=StatusPedido(self.status),
            data_criacao=self.data_criacao,
        )

    @staticmethod
    def from_entity(pedido: Pedido) -> "PedidoModel":
        return PedidoModel(
            id=pedido.id,
            produtos_ids=pedido.produtos_ids,
            cliente_id=pedido.cliente_id,
            status=pedido.status.value,
            data_criacao=pedido.data_criacao,
        )
