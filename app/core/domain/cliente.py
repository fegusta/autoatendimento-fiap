from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from typing import Optional


class Cliente:
    def __init__(self, nome: Optional[str], email: Optional[EmailStr], cpf: Optional[str], id: Optional[UUID] = None, data_criacao: Optional[datetime] = None):
        self.id = id or uuid4()
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_criacao = data_criacao or datetime.utcnow()
