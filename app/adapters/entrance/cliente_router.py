from fastapi import APIRouter, Depends, HTTPException, Response
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

@router.post("/", response_model=ClienteResponseSchema, status_code=201)
def criar_cliente(cliente_data: ClienteCreateSchema, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).criarCliente(cliente_data)
    except ValueError as e:
        mensagem = str(e)
        
        if "duplicado" in mensagem.lower():
            raise HTTPException(status_code=409, detail="E-mail ou CPF já existente.")
        
        raise HTTPException(status_code=400, detail=mensagem)

# Buscar cliente por CPF
@router.get("/cpf/{cpf}", response_model=ClienteResponseSchema)
def buscar_cliente_por_cpf(cpf: str, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).buscar_cliente_por_cpf(cpf)
    except ValueError as e:
        mensagem = str(e)

        raise HTTPException(status_code=404, detail=mensagem)

@router.get("/{cliente_id}", response_model=ClienteResponseSchema)
def buscar_cliente(cliente_id: int, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).buscar_cliente_por_id(cliente_id)
    except ValueError as e:
        mensagem = str(e)

        raise HTTPException(status_code=404, detail=mensagem)

@router.get("/", response_model=List[ClienteResponseSchema])
def listar_clientes(repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).listar_clientes()
    except ValueError as e:
        mensagem = str(e)

        raise HTTPException(status_code=400, detail=mensagem)

@router.put("/{cliente_id}", response_model=ClienteResponseSchema)
def atualizar_cliente(cliente_id: int, cliente_data: ClienteUpdateSchema, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:

        return ClienteUseCase(repository).atualizar_cliente(cliente_id=cliente_id, clienteRequest=cliente_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, repository: ClienteRepository = Depends(get_cliente_repository)):
    try:
        ClienteUseCase(repository).deletar_cliente(cliente_id=cliente_id)

        return Response(status_code=204)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))