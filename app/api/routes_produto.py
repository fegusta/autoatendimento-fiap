from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from typing import List

from app.schemas.produto_schema import ProdutoRequest, ProdutoResponse, CategoriaProdutoEnum
from app.core.domain.produto import CategoriaProduto
from app.ports.produto_port import ProdutoServicePort
from app.services.produto_service_impl import ProdutoService
from app.db.dependencies import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/produto", tags=["Produto"])


def get_produto_service(session: AsyncSession = Depends(get_session)) -> ProdutoServicePort:
    return ProdutoService(session)


@router.post("/", response_model=ProdutoResponse)
async def criar_produto(
    request: ProdutoRequest,
    service: ProdutoServicePort = Depends(get_produto_service),
):
    produto = await service.criar_produto(request)
    return produto


@router.get("/", response_model=List[ProdutoResponse])
async def listar_produtos(
    service: ProdutoServicePort = Depends(get_produto_service),
):
    return await service.listar_produtos()


@router.get("/{produto_id}", response_model=ProdutoResponse)
async def obter_produto_por_id(
    produto_id: UUID,
    service: ProdutoServicePort = Depends(get_produto_service),
):
    produto = await service.obter_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.get("/categoria/{categoria}", response_model=List[ProdutoResponse])
async def listar_por_categoria(
    categoria: CategoriaProdutoEnum,
    service: ProdutoServicePort = Depends(get_produto_service),
):
    return await service.listar_produtos_por_categoria(CategoriaProduto(categoria))


@router.put("/{produto_id}", response_model=ProdutoResponse)
async def atualizar_produto(
    produto_id: UUID,
    request: ProdutoRequest,
    service: ProdutoServicePort = Depends(get_produto_service),
):
    return await service.atualizar_produto(produto_id, request)


@router.delete("/{produto_id}")
async def deletar_produto(
    produto_id: UUID,
    service: ProdutoServicePort = Depends(get_produto_service),
):
    await service.remover_produto(produto_id)
    return {"message": "Produto removido com sucesso"}
