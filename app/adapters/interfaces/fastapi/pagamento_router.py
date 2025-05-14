from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.adapters.db.database import get_db
from app.core.schemas.pagamento import PagamentoSchemas

router = APIRouter(prefix="/pagamento", tags=["pagamento"])

@router.post('/pedido')
def pagamento_pedido(pedido: PagamentoSchemas, db: Session = Depends(get_db)):
    pass
