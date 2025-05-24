from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.use_cases.status.status_usecase import StatusUseCase
from app.core.schemas.status import Status
from app.infrastructure.db.database import get_db

router = APIRouter(prefix="/status", tags=["Status"])

@router.get("/{pedido_id}", response_model=Status)
def obter_status(pedido_id: int, db: Session = Depends(get_db)):
    try:
        use_case = StatusUseCase(db)
        return use_case.obter_status(pedido_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/debug-status/{pedido_id}")
def debug_status(pedido_id: int, db: Session = Depends(get_db)):
    use_case = StatusUseCase(db)
    pedido = use_case.repository.buscar_por_pedido_id(pedido_id)

    if not pedido:
        return {"erro": "Pedido não encontrado"}

    print("🧾 status_rel:", pedido.status_rel.status)
    print("📦 repr:", repr(pedido.status_rel.status))

    return {
        "pedido_id": pedido.pedido_id,
        "status_bruto": pedido.status_rel.status,
        "repr_status": repr(pedido.status_rel.status)
    }
