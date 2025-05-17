from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from app.schemas.produto_schema import ProdutoCreate, ProdutoRead, ProdutoUpdate
from app.services.produto_service import ProdutoService
from app.dependencies import get_produto_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("", response_model=ProdutoRead)
async def criar_produto(produto: ProdutoCreate, service: ProdutoService = Depends(get_produto_service)):
    return await service.criar_produto(produto)


@router.get("/{produto_id}", response_model=ProdutoRead)
async def buscar_produto(produto_id: UUID, service: ProdutoService = Depends(get_produto_service)):
    produto = await service.buscar_produto_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto



@router.get("", response_model=List[ProdutoRead])
async def listar_produtos(service: ProdutoService = Depends(get_produto_service)):
    return await service.listar_produtos()


@router.put("/{produto_id}", response_model=ProdutoRead)
async def atualizar_produto(produto_id: UUID, produto: ProdutoUpdate, service: ProdutoService = Depends(get_produto_service)):
    return await service.atualizar_produto(produto_id, produto)


@router.delete("/{produto_id}")
async def remover_produto(produto_id: UUID, service: ProdutoService = Depends(get_produto_service)):
    await service.remover_produto(produto_id)
    return {"detail": "Produto removido com sucesso"}


@router.get("/categoria/{categoria}", response_model=List[ProdutoRead])
async def buscar_por_categoria(categoria: str, service: ProdutoService = Depends(get_produto_service)):
    return await service.buscar_por_categoria(categoria)
