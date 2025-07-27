from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from typing import List

from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from app.infrastructure.db.database import get_session
from app.infrastructure.db.produto_repository import ProdutoRepository
from app.application.use_cases.produto_use_case import ProdutoUseCase
from app.domain.enums.categoria_produto import CategoriaProduto

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
async def criar_produto(produto: ProdutoCreate, db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    produto_criado = await use_case.criar_produto(produto)
    return ProdutoResponse.from_entity(produto_criado)


@router.get("/", response_model=List[ProdutoResponse])
async def listar_produtos(db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    produtos = await use_case.listar_produtos()
    return [ProdutoResponse.from_entity(p) for p in produtos]


@router.get("/{produto_id}", response_model=ProdutoResponse)
async def buscar_produto(produto_id: UUID, db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    produto = await use_case.buscar_por_id(produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return ProdutoResponse.from_entity(produto)


@router.put("/{produto_id}", response_model=ProdutoResponse)
async def atualizar_produto(produto_id: UUID, produto: ProdutoUpdate, db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    produto_atualizado = await use_case.atualizar_produto(produto_id, produto)
    return ProdutoResponse.from_entity(produto_atualizado)


@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_produto(produto_id: UUID, db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    await use_case.remover_produto(produto_id)


@router.get("/categorias/{categoria}", response_model=List[ProdutoResponse])
async def listar_por_categoria(categoria: str, db: AsyncSession = Depends(get_session)):
    use_case = ProdutoUseCase(ProdutoRepository(db))
    try:
        categoria_enum = CategoriaProduto(categoria)
    except ValueError:
        raise HTTPException(status_code=400, detail="Categoria inválida")
    produtos = await use_case.listar_por_categoria(categoria_enum)
    return [ProdutoResponse.from_entity(p) for p in produtos]
