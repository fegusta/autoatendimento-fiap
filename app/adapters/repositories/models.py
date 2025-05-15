from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, DateTime
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional
from app.domain.cliente import Cliente

Base = declarative_base()

class ClienteModel(Base):
    __tablename__ = "clientes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    nome: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    cpf: Mapped[Optional[str]] = mapped_column(String(14), nullable=True)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_entity(self) -> Cliente:
        return Cliente(
            id=self.id,
            nome=self.nome,
            email=self.email,
            cpf=self.cpf,
            data_criacao=self.data_criacao,
        )

    @staticmethod
    def from_entity(cliente: Cliente) -> "ClienteModel":
        return ClienteModel(
            id=cliente.id,
            nome=cliente.nome,
            email=str(cliente.email) if cliente.email else None,
            cpf=cliente.cpf,
            data_criacao=cliente.data_criacao,
        )
