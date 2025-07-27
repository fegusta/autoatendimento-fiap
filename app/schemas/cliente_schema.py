from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr
    cpf: str

class ClienteResponse(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    cpf: str
    data_criacao: datetime

    class Config:
        from_attributes = True
