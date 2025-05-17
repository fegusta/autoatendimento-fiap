from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Enum as SqlEnum, Numeric
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional
from app.domain.produto import Produto, CategoriaProduto
from app.adapters.models.base import Base


class ProdutoModel(Base):
    __tablename__ = "produtos"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[Optional[str]] = mapped_column(String(255))
    preco: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    imagem_url: Mapped[str] = mapped_column(String(255), nullable=True)
    categoria: Mapped[CategoriaProduto] = mapped_column(SqlEnum(CategoriaProduto), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_entity(self) -> Produto:
        return Produto(
            id=self.id,
            nome=self.nome,
            descricao=self.descricao,
            preco=self.preco,
            imagem_url=self.imagem_url,
            categoria=self.categoria,
            data_criacao=self.data_criacao,
        )

    @staticmethod
    def from_entity(produto: Produto) -> "ProdutoModel":
        return ProdutoModel(
            id=produto.id,
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            imagem_url=produto.imagem_url,
            categoria=produto.categoria,
            data_criacao=produto.data_criacao,
        )
