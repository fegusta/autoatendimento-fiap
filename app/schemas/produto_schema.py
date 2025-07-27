from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.domain.produto import Produto

class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str]
    preco: float
    categoria: str    


class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    preco: Optional[float]
    categoria: Optional[str]


class ProdutoResponse(BaseModel):
    id: UUID
    nome: str
    descricao: Optional[str]
    preco: float
    categoria: str
    imagem_url: Optional[str]
    data_criacao: datetime

    class Config:
        from_attributes = True
        
    @classmethod
    def from_entity(cls, produto: Produto) -> "ProdutoResponse":
        return cls(
            id=produto.id,
            nome=str(produto.nome) if produto.nome else "",
            descricao=str(produto.descricao) if produto.descricao else "",
            preco=float(produto.preco.valor) if produto.preco else 0.0,
            categoria=produto.categoria.value if hasattr(produto.categoria, "value") else str(produto.categoria),
            imagem_url=produto.imagem_url,
            data_criacao=produto.data_criacao,
        )
