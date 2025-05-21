from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.domain.cliente.models import Cliente
from app.core.domain.cliente.ports import ClienteRepositoryPort
from app.core.models import Cliente as ClienteORM

class ClienteRepository(ClienteRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def buscar_por_cpf(self, cpf: str) -> Optional[Cliente]:
        cliente_orm = self.session.query(ClienteORM).filter_by(cpf=cpf).first()
        if cliente_orm:
            return Cliente.model_validate(cliente_orm)
        return None

    def criar(self, cliente: Cliente) -> Cliente:
        cliente_orm = ClienteORM(**cliente.model_dump())
        self.session.add(cliente_orm)
        try:
            self.session.commit()
            self.session.refresh(cliente_orm)
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError(f"Erro de integridade ao criar cliente: {e}")
        return Cliente.model_validate(cliente_orm)

    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        cliente_orm = self.session.query(ClienteORM).filter_by(id=cliente_id).first()
        if cliente_orm:
            return Cliente.model_validate(cliente_orm)
        return None

    def listar_todos(self) -> List[Cliente]:
        clientes_orm = self.session.query(ClienteORM).all()
        return [Cliente.model_validate(c) for c in clientes_orm]

    def atualizar(self, cliente: Cliente) -> Cliente:
        cliente_orm = self.session.query(ClienteORM).filter_by(id=cliente.id).first()
        if not cliente_orm:
            raise ValueError("Cliente não encontrado")
        for field, value in cliente.model_dump().items():
            setattr(cliente_orm, field, value)
        self.session.commit()
        self.session.refresh(cliente_orm)
        return Cliente.model_validate(cliente_orm)

    def deletar(self, cliente_id: int) -> None:
        cliente_orm = self.session.query(ClienteORM).filter_by(id=cliente_id).first()
        if cliente_orm:
            self.session.delete(cliente_orm)
            self.session.commit()