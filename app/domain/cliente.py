from uuid import UUID
from datetime import datetime
from typing import Optional


class Cliente:
    def __init__(
        self,
        id: UUID,
        nome: Optional[str],
        email: Optional[str],
        cpf: Optional[str],
        data_criacao: datetime
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_criacao = data_criacao
