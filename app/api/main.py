from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.adapters.db.database import get_db
from app.api import produto
from app.api import cliente

app = FastAPI(
    title="Sistema de Autoatendimento da Lanchonete",
    description="Documentação automática via Swagger e Redoc",
    version="1.0.0",
)

app.include_router(produto.router)
app.include_router(cliente.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def health_db_check(db: Session = Depends(get_db)):
    return {"status": "connected"}