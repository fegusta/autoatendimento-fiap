from uuid import UUID
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from app.domain.value_objects.cpf import CPF
from app.domain.value_objects.email import Email
from app.domain.value_objects.nome import Nome

@dataclass
class Cliente:
    id: UUID
    nome: Nome
    email: Email
    cpf: CPF
    data_criacao: Optional[datetime] = None
