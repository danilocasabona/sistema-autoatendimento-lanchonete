from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.adapters.db.database import get_db
from app.core.schemas.produto import ProdutoCreateSchema, ProdutoResponseSchema
from app.core.services import produto as service_produto

router = APIRouter(prefix="/produtos", tags=["Produtos"])

# 🧩 Criar um novo produto
@router.post("/", response_model=ProdutoResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreateSchema, db: Session = Depends(get_db)):
    return service_produto.criar_produto(db, produto)

# 🧩 Listar todos os produtos
@router.get("/", response_model=List[ProdutoResponseSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return service_produto.listar_produtos(db)

# 🧩 Buscar um produto pelo ID
@router.get("/{produto_id}", response_model=ProdutoResponseSchema)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = service_produto.buscar_produto_por_id(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# 🧩 Atualizar um produto existente
@router.put("/{produto_id}", response_model=ProdutoResponseSchema)
def atualizar_produto(produto_id: int, produto: ProdutoCreateSchema, db: Session = Depends(get_db)):
    produto_atualizado = service_produto.atualizar_produto(db, produto_id, produto)
    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto_atualizado

# 🧩 Deletar um produto
@router.delete("/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = service_produto.deletar_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return
