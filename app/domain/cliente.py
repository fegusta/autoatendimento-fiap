from uuid import UUID
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Cliente:
    id: UUID
    nome: str
    email: str
    cpf: str
    data_criacao: Optional[datetime] = None
