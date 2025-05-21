from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List

from app.adapters.out.cliente_repository import ClienteRepository
from app.infrastructure.db.database import get_db
from app.core.services.cliente_service import ClienteService
from app.core.domain.cliente.models import Cliente
from app.core.domain.cliente.ports import ClienteRepositoryPort
from app.core.schemas.cliente import ClienteCreateSchema, ClienteResponseSchema, ClienteUpdateSchema

router = APIRouter(prefix="/clientes", tags=["clientes"])

# Dependência para injetar o service
def get_cliente_service(db: Session = Depends(get_db)) -> ClienteService:
    repository = ClienteRepository(db)
    
    return ClienteService(repository)

@router.post("/", response_model=ClienteResponseSchema, status_code=201)
def criar_cliente(cliente_data: ClienteCreateSchema, service: ClienteService = Depends(get_cliente_service)):
    cliente = Cliente(**cliente_data.model_dump())
    try:
        return service.criar_cliente(cliente)
    except ValueError as e:
        mensagem = str(e)
        if "duplicado" in mensagem.lower():
            raise HTTPException(status_code=409, detail="E-mail ou CPF já existente.")
        raise HTTPException(status_code=400, detail=mensagem)


@router.get("/{cliente_id}", response_model=ClienteResponseSchema)
def buscar_cliente(cliente_id: int, service: ClienteService = Depends(get_cliente_service)):
    cliente = service.buscar_cliente_por_id(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# Buscar cliente por CPF
@router.get("/cpf/{cpf}", response_model=ClienteResponseSchema)
def buscar_cliente_por_cpf(cpf: str, service: ClienteService = Depends(get_cliente_service)):
    cliente = service.buscar_cliente_por_cpf(cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.get("/", response_model=List[ClienteResponseSchema])
def listar_clientes(service: ClienteService = Depends(get_cliente_service)):
    return service.listar_clientes()

@router.put("/{cliente_id}", response_model=ClienteResponseSchema)
def atualizar_cliente(cliente_id: int, cliente_data: ClienteUpdateSchema, service: ClienteService = Depends(get_cliente_service)):
    cliente = Cliente(id=cliente_id, **cliente_data.model_dump())
    return service.atualizar_cliente(cliente)

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, service: ClienteService = Depends(get_cliente_service)):
    service.deletar_cliente(cliente_id)
    return Response(status_code=204)