from app.infrastructure.api.fastapi import app, Depends

from app.api import check_router
from app.api import cliente
from app.api import pagamento_router
from app.api import pedido_router
from app.api import produto_router
from app.api import status_pedido_router
from app.webhooks import pagamento as pagamento_webhook

# declare
app.include_router(check_router.router)
app.include_router(cliente.router)
app.include_router(pagamento_router.router)
app.include_router(pedido_router.router)
app.include_router(produto_router.router)
app.include_router(status_pedido_router.router)
app.include_router(pagamento_webhook.router)