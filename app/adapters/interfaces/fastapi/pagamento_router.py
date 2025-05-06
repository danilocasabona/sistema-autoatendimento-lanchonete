from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List
from app.adapters.db.database import get_db
from app.core.schemas.pagamento import PagamentoCreateSchema, PagamentoResponseSchema

router = APIRouter(prefix="/pagamento", tags=["Pagamento"])

# 🧩 Criar pagamento do pedido
@router.post("/pedido", response_model=PagamentoResponseSchema, status_code=201, summary="Realizar pagamento do pedido")
def criar_pagamento_pedido(criar_pagamento: PagamentoCreateSchema):
    return {
        "pedido_id": criar_pagamento
    } 