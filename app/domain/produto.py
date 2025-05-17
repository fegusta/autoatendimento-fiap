from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from enum import Enum


class CategoriaEnum(str, Enum):
    LANCHE = "Lanche"
    ACOMPANHAMENTO = "Acompanhamento"
    BEBIDA = "Bebida"
    SOBREMESA = "Sobremesa"


class Produto:
    def __init__(
        self,
        nome: str,
        descricao: str,
        preco: float,
        categoria: CategoriaEnum,
        id: Optional[UUID] = None,
        data_criacao: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.data_criacao = data_criacao or datetime.utcnow()
