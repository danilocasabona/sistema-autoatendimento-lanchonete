from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List

from app.adapters.out.status_pedido_repository import StatusPedidoRepository
from app.infrastructure.db.database import get_db
from app.core.schemas.status_pedido import StatusPedidoCreateSchema, StatusPedidoResponseSchema, StatusPedidoUpdateSchema
from app.core.use_cases.status.status_pedido_use_case import StatusPedidoUseCase

router = APIRouter(prefix="/status_pedido", tags=["status_pedido"])

def get_status_repository(db: Session = Depends(get_db)) -> StatusPedidoRepository:
    return StatusPedidoRepository(db_session=db)

@router.post("/", response_model=StatusPedidoResponseSchema, status_code=status.HTTP_201_CREATED, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao criar o status"
                }
            }
        }
    }
})
def criar(data: StatusPedidoCreateSchema, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).criar(dataRequest=data)
    except Exception as e:       
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{id}", response_model=StatusPedidoResponseSchema, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar o status"
                }
            }
        }
    },
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Status não encontrado"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_status(id: int, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).buscar_por_id(id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:       
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[StatusPedidoResponseSchema], responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar os statuses"
                }
            }
        }
    }
}
,openapi_extra={
    "responses": {
        "422": None
    }
})
def listar_todos(repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).listar_todos()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/{id}", response_model=StatusPedidoResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Status não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao atualizar o status"
                }
            }
        }
    }
})
def atualizar(id: int, data: StatusPedidoUpdateSchema, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:

        return StatusPedidoUseCase(repository).atualizar(id=id, dataRequest=data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Status não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao excluir o status"
                }
            }
        }
    },
    204: {
        "description": "Status deletado com sucesso",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
})
def deletar(id: int, repository: StatusPedidoRepository = Depends(get_status_repository)):
    try:
        StatusPedidoUseCase(repository).deletar(id=id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))