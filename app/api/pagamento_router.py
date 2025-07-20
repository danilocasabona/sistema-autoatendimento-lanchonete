from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session

from app.gateways.pagamento_gateway import PagamentoGateway
from app.infrastructure.db.database import get_db
from app.schemas.pagamento import PagamentoCreateSchema, PagamentoResponseSchema, PagamentoAtualizaSchema
from app.controllers.pagamento_controller import PagamentoController

router = APIRouter(prefix="/pagamento", tags=["pagamento"])

def get_pagamento_gateway(db: Session = Depends(get_db)) -> PagamentoGateway:
    
    return PagamentoGateway(db_session=db)

@router.post("/", response_model=PagamentoResponseSchema, status_code=status.HTTP_201_CREATED, summary="Criar pagamento do pedido", responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao salvar o pagamento"
                }
            }
        }
    }
})
def efetuar_pagamento_pedido(pedido_id: PagamentoCreateSchema, gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        
        return PagamentoController().criar_pagamento(pedido_id, gateway)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{codigo_pagamento}", response_model=PagamentoResponseSchema, responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar o pagamento"
                }
            }
        }
    },
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pagamento não encontrado"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def buscar_pagamento(codigo_pagamento: str, gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        
        return PagamentoController().buscar_pagamento_por_codigo(codigo_pagamento, gateway)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=list[PagamentoResponseSchema], summary="Listar todos os pagamentos realizado", responses={
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao buscar os pagamentos"
                }
            }
        }
    }
}, openapi_extra={
    "responses": {
        "422": None  
    }
})
def listar_pagamentos(gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        
        return PagamentoController().listar_pagamentos(gateway)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.put("/{codigo_pagamento}", response_model=PagamentoResponseSchema, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pagamento não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao atualizar o pagamento"
                }
            }
        }
    }
})
def atualizar_pagamento(codigo_pagamento: str, pagamento_data: PagamentoAtualizaSchema, gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        
        return PagamentoController().atualizar_pagamento(codigo_pagamento, pagamento_data, gateway)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{codigo_pagamento}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Pagamento não encontrado"
                }
            }
        }
    },
    400: {
        "description": "Erro de validação",
        "content": {
            "application/json": {
                "example": {
                    "message": "Erro de integridade ao remover o pagamento"
                }
            }
        }
    },
    204: {
        "description": "Pagamento deletado com sucesso",
        "content": {
            "application/json": {
                "example": {}
            }
        }
    }
})
def deletar_pagamento(codigo_pagamento: str, gateway: PagamentoGateway = Depends(get_pagamento_gateway)):
    try:
        PagamentoController().deletar_pagamento(codigo_pagamento, gateway)
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
