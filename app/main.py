from app.infrastructure.api.fastapi import app, Depends

#from app.infrastructure.db.database import get_db
#from sqlalchemy.orm import Session

# import
from app.adapters.entrance import check_router
from app.adapters.entrance import cliente_router
from app.adapters.entrance import pagamento_router
from app.adapters.entrance import pedido_router
from app.adapters.entrance import produto_router
from app.adapters.entrance import status_pedido_router

# declare
app.include_router(check_router.router)
app.include_router(cliente_router.router)
app.include_router(pagamento_router.router)
app.include_router(pedido_router.router)
app.include_router(produto_router.router)
app.include_router(status_pedido_router.router)