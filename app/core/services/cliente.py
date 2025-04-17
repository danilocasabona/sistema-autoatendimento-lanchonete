from sqlalchemy.orm import Session
from app.core.models.cliente import Cliente
from app.core.schemas.cliente import ClienteCreateSchema, ClienteUpdateSchema
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def get_cliente_by_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def get_cliente_by_cpf(db: Session, cpf: str):
    return db.query(Cliente).filter(Cliente.cpf == cpf).first()

def create_cliente(db: Session, cliente_data: ClienteCreateSchema):
    if get_cliente_by_cpf(db, cliente_data.cpf):
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    novo_cliente = Cliente(**cliente_data.model_dump())
    db.add(novo_cliente)
    try:
        db.commit()
        db.refresh(novo_cliente)
        return novo_cliente
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email ou CPF já cadastrado")

def update_cliente(db: Session, cliente_id: int, cliente_data: ClienteUpdateSchema):
    cliente = get_cliente_by_id(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    for key, value in cliente_data.model_dump(exclude_unset=True).items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    return cliente

def delete_cliente(db: Session, cliente_id: int):
    cliente = get_cliente_by_id(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(cliente)
    db.commit()
    return {"message": "Cliente deletado com sucesso"}

def list_clientes(db: Session):
    return db.query(Cliente).all()