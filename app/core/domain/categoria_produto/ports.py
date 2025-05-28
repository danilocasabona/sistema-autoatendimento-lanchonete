from abc import ABC, abstractmethod
from typing import Optional

from app.core.domain.categoria_produto.models import CategoriaProduto

class CategoriaProdutoRepositoryPort(ABC):
    
    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[CategoriaProduto]:
        pass