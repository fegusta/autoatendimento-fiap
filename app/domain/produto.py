from uuid import UUID
from datetime import datetime
from typing import Optional
from enum import Enum


class CategoriaProduto(str, Enum):
    LANCHE = "LANCHE"
    ACOMPANHAMENTO = "ACOMPANHAMENTO"
    BEBIDA = "BEBIDA"
    SOBREMESA = "SOBREMESA"


class Produto:
    def __init__(
        self,
        id: UUID,
        nome: str,
        descricao: Optional[str],
        preco: float,
        imagem_url: Optional[str],
        categoria: CategoriaProduto,
        data_criacao: datetime
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.imagem_url = imagem_url
        self.categoria = categoria
        self.data_criacao = data_criacao
