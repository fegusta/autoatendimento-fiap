from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from datetime import datetime
from enum import Enum


class CategoriaProdutoEnum(str, Enum):
    LANCHE = "LANCHE"
    ACOMPANHAMENTO = "ACOMPANHAMENTO"
    BEBIDA = "BEBIDA"
    SOBREMESA = "SOBREMESA"


class ProdutoRequest(BaseModel):
    nome: str = Field(..., max_length=100)
    descricao: Optional[str] = Field(None, max_length=255)
    preco: float
    imagem_url: Optional[str]
    categoria: CategoriaProdutoEnum


class ProdutoResponse(BaseModel):
    id: UUID
    nome: str
    descricao: Optional[str]
    preco: float
    imagem_url: Optional[str]
    categoria: CategoriaProdutoEnum
    data_criacao: datetime
