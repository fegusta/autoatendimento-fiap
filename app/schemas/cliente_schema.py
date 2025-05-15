from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


class ClienteCreateSchema(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    cpf: Optional[str]


class ClienteReadSchema(BaseModel):
    id: UUID
    nome: Optional[str]
    email: Optional[EmailStr]
    cpf: Optional[str]
    data_criacao: datetime

    class Config:
        from_attributes = True
