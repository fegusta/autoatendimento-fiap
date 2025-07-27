from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from app.domain.enums.categoria_produto import CategoriaProduto
from app.domain.value_objects.descricao import Descricao
from app.domain.value_objects.nome import Nome
from app.domain.value_objects.preco import Preco


class Produto:
    def __init__(
        self,
        nome: Nome,
        descricao: Descricao,
        preco: Preco,
        categoria: CategoriaProduto,
        id: Optional[UUID] = None,
        imagem_url: Optional[str] = None,
        data_criacao: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.imagem_url = imagem_url
        self.data_criacao = data_criacao or datetime.utcnow()
