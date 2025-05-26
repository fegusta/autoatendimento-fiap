from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


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


class ProdutoRead(BaseModel):
    id: UUID
    nome: str
    descricao: Optional[str]
    preco: float
    categoria: str
    data_criacao: datetime

    class Config:
        from_attributes = True
