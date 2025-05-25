from fastapi import APIRouter, HTTPException, Depends
from fastapi import Response
from sqlalchemy.orm import Session
from typing import List

from app.adapters.out.status_pedido_repository import StatusPedidoRepository
from app.infrastructure.db.database import get_db
from app.core.schemas.status_pedido import StatusPedidoCreateSchema, StatusPedidoResponseSchema, StatusPedidoUpdateSchema
from app.core.use_cases.status.status_pedido_use_case import StatusPedidoUseCase

router = APIRouter(prefix="/status_pedido", tags=["status_pedido"])

def get_status_repository(db: Session = Depends(get_db)) -> StatusPedidoRepository:
    return StatusPedidoRepository(db_session=db)

@router.post("/", response_model=StatusPedidoResponseSchema, status_code=201)
def criar(data: StatusPedidoCreateSchema, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).criar(dataRequest=data)
    except ValueError as e:
        mensagem = str(e)
        
        raise HTTPException(status_code=400, detail=mensagem)

@router.get("/{id}", response_model=StatusPedidoResponseSchema)
def buscar_status(id: int, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).buscar_por_id(id)
    except ValueError as e:
        mensagem = str(e)

        raise HTTPException(status_code=404, detail=mensagem)

@router.get("/", response_model=List[StatusPedidoResponseSchema])
def listar_todos(repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).listar_todos()
    except ValueError as e:
        mensagem = str(e)

        raise HTTPException(status_code=400, detail=mensagem)

@router.put("/{id}", response_model=StatusPedidoResponseSchema)
def atualizar(id: int, data: StatusPedidoUpdateSchema, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).atualizar(id=id, dataRequest=data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}")
def deletar(id: int, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:
        StatusPedidoUseCase(repository).deletar(id=id)

        return Response(status_code=204)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))