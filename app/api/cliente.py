from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
#from app.core.database import get_db
from app.adapters.db.database import get_db
from app.core.schemas.cliente import ClienteCreateSchema, ClienteUpdateSchema, ClienteResponseSchema
from app.core.services import cliente as cliente_service
from typing import List

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=List[ClienteResponseSchema])
def listar_clientes(db: Session = Depends(get_db)):
    return cliente_service.list_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteResponseSchema)
def buscar_cliente_por_id(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.get_cliente_by_id(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.post("/", response_model=ClienteResponseSchema, status_code=201)
def criar_cliente(cliente_data: ClienteCreateSchema, db: Session = Depends(get_db)):
    return cliente_service.create_cliente(db, cliente_data)

@router.put("/{cliente_id}", response_model=ClienteResponseSchema)
def atualizar_cliente(cliente_id: int, cliente_data: ClienteUpdateSchema, db: Session = Depends(get_db)):
    return cliente_service.update_cliente(db, cliente_id, cliente_data)

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_service.delete_cliente(db, cliente_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)