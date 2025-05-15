from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.adapters.db.database import get_db
from app.core.schemas.pagamento import PagamentoSchemas

router = APIRouter(prefix="/pagamento", tags=["pagamento"])

@router.post('/pedido')
def pagamento_pedido(pedido_id: PagamentoSchemas, db: Session = Depends(get_db)):
    return {'status_code': 200, 'pedido': pedido_id }