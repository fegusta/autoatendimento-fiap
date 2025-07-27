from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from uuid import uuid4, UUID
from datetime import datetime

from app.infrastructure.db.base import Base


class ClienteModel(Base):
    __tablename__ = "clientes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
