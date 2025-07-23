from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional
from datetime import datetime

class ClienteRequest(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    cpf: Optional[str]


class ClienteResponse(BaseModel):
    id: UUID
    nome: Optional[str]
    email: Optional[str]
    cpf: Optional[str]
    data_criacao: datetime
