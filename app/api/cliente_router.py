from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from app.adapters.out.cliente_repository import ClienteRepository
from app.infrastructure.db.database import get_db
from app.core.schemas.cliente import ClienteCreateSchema, ClienteResponseSchema, ClienteUpdateSchema
from app.core.use_cases.cliente.cliente_use_case import ClienteUseCase

router = APIRouter(prefix="/clientes", tags=["clientes"])

# Dependência para injetar o service
def get_cliente_repository(db: Session = Depends(get_db)) -> ClienteRepository:
    
    return ClienteRepository(db_session=db)

@router.post("/", response_model=ClienteResponseSchema, status_code=status.HTTP_201_CREATED, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao criar cliente"
                }
            }
        }
    }
})
def criar_cliente(cliente_data: ClienteCreateSchema, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).criarCliente(cliente_data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# Buscar cliente por CPF
@router.get("/cpf/{cpf}", response_model=ClienteResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Cliente não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": ""
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_cliente_por_cpf(cpf: str, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).buscar_cliente_por_cpf(cpf)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{cliente_id}", response_model=ClienteResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Cliente não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": ""
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_cliente(cliente_id: int, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).buscar_cliente_por_id(cliente_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[ClienteResponseSchema], responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": ""
                }
            }
        }
    }
}, 
openapi_extra={
    "responses": {
        "422": None  
    }
})
def listar_clientes(repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).listar_clientes()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/{cliente_id}", response_model=ClienteResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Cliente não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao atualizar o cliente"
                }
            }
        }
    }
})
def atualizar_cliente(cliente_id: int, cliente_data: ClienteUpdateSchema, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).atualizar_cliente(cliente_id=cliente_id, clienteRequest=cliente_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Cliente não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao deletar o cliente"
                }
            }
        }
    },
    204: {
        "description": "Pedido deletado com sucesso",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
})
def deletar_cliente(cliente_id: int, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:
        ClienteUseCase(repository).deletar_cliente(cliente_id=cliente_id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))