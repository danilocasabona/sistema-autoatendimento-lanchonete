class PagamentoEntity():
    def __init__(self, pedido: int, codigo_pagamento: str, status: str):
        self.pedido = pedido
        self.codigo_pagamento = codigo_pagamento
        self.status = status

    model_config = {
        "from_attributes": True
    }