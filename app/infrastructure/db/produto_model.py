from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Enum as SqlEnum, Numeric
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional

from app.domain.enums.categoria_produto import CategoriaProduto
from app.domain.produto import Produto
from app.domain.value_objects.nome import Nome
from app.domain.value_objects.descricao import Descricao
from app.domain.value_objects.preco import Preco

from app.infrastructure.db.base import Base


class ProdutoModel(Base):
    __tablename__ = "produtos"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    preco: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    imagem_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    categoria: Mapped[CategoriaProduto] = mapped_column(SqlEnum(CategoriaProduto), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_entity(self) -> Produto:
        return Produto(
            id=self.id,
            nome=Nome(self.nome),
            descricao=Descricao(self.descricao),
            preco=Preco(self.preco),
            categoria=self.categoria,
            imagem_url=self.imagem_url,
            data_criacao=self.data_criacao
        )
