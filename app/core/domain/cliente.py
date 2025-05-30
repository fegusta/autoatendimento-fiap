from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.core.domain.value_objects.cpf import CPF
from app.core.domain.value_objects.email import Email
from app.core.domain.value_objects.nome import Nome


class Cliente:
    def __init__(
        self,
        nome: Nome,
        email: Email,
        cpf: CPF,
        id: Optional[UUID] = None,
        data_criacao: Optional[datetime] = None
    ):
        self.id = id or uuid4()
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_criacao = data_criacao or datetime.utcnow()
