from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List

from app.adapters.db.database import get_db
from app.core.schemas.pedido import PedidoResponseSchema, PedidoCreateSchema
from app.core.services import pedido as service_pedido

router = APIRouter(prefix="/pedido", tags=["Pedido"])

# 🧩 Criar um novo Pedido
@router.post("/", response_model=PedidoResponseSchema, status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoCreateSchema, db: Session = Depends(get_db)) -> JSONResponse:
    pedido = service_pedido.criar_pedido(db, pedido)
    return JSONResponse(content=pedido)

