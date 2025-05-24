from decimal import Decimal
<<<<<<< HEAD
from app.core.enums.categoria import CategoriaEnum
from app.core.models.produto import Produto
=======
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
from sqlalchemy.exc import IntegrityError

from app.core.domain.produto.ports import ProdutoRepositoryPort
from app.core.domain.produto.models import Produto
from app.core.enums.categoria import CategoriaEnum
from app.core.models.produto import Produto
from app.core.schemas.produto import ProdutoResponseSchema

class ProdutoRepository(ProdutoRepositoryPort):
    def __init__(self, db_session):
        self.db_session = db_session

<<<<<<< HEAD
    def salvar(self, produto: Produto) -> Produto:
=======
    def criar_produto(self, produto: Produto) -> Produto:
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
        from app.core.models.produto import Produto

        db_produto = Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            preco=Decimal(produto.preco),
            categoria=produto.categoria
        )
        self.db_session.add(db_produto)
        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro de integridade ao salvar produto: {e}")
        self.db_session.refresh(db_produto)

        produto = ProdutoResponseSchema.model_validate(db_produto, from_attributes=True)
        return produto

    def buscar_por_id(self, produto_id: int) -> Produto:
<<<<<<< HEAD
        db_produto = self.db_session.query(Produto).filter(Produto.id == produto_id).first()
=======
        db_produto = self.db_session.query(Produto).filter(Produto.produto_id == produto_id).first()
        
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
        if not db_produto:
            raise ValueError("Produto não encontrado")
        produto = ProdutoResponseSchema.model_validate(db_produto, from_attributes=True)

        return produto

    def listar_todos(self) -> list[Produto]:
        db_produtos = self.db_session.query(Produto).all()
        produtos = []
        for db_produto in db_produtos:
            produto = ProdutoResponseSchema.model_validate(db_produto, from_attributes=True)
            produtos.append(produto)
        return produtos

<<<<<<< HEAD
    def deletar(self, produto_id: int) -> None:
        db_produto = self.db_session.query(Produto).filter(Produto.id == produto_id).first()
=======
    def deletar_produto(self, produto_id: int) -> None:
        db_produto = self.db_session.query(Produto).filter(Produto.produto_id == produto_id).first()
        
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
        if not db_produto:
            raise ValueError("Produto não encontrado")
        self.db_session.delete(db_produto)
        self.db_session.commit()
        #self.db_session.flush()

<<<<<<< HEAD
    def atualizar(self, produto_id: int, produto_data: Produto) -> Produto:
        db_produto = self.db_session.query(Produto).filter(Produto.id == produto_id).first()
=======
    def atualizar_produto(self, produto_id: int, produto_data: Produto) -> Produto:
        db_produto = self.db_session.query(Produto).filter(Produto.produto_id == produto_id).first()
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
        if not db_produto:
            raise ValueError("Produto não encontrado")

        db_produto.nome = produto_data.nome
        db_produto.descricao = produto_data.descricao
        db_produto.preco = Decimal(produto_data.preco)
        db_produto.categoria = produto_data.categoria

        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            raise ValueError(f"Erro de integridade ao atualizar produto: {e}")
        self.db_session.refresh(db_produto)

        produto = ProdutoResponseSchema.model_validate(db_produto, from_attributes=True)
        return produto
    
    def listar_por_categoria(self, categoria: CategoriaEnum) -> list[Produto]:
<<<<<<< HEAD
        db_produtos = self.db_session.query(Produto).filter(Produto.categoria == categoria.value).all()
=======
        db_produtos = self.db_session.query(Produto).filter(Produto.categoria == categoria).all()
>>>>>>> a46bd34a851478509f221f283c95751bffbe1290
        produtos = []

        for db_produto in db_produtos:
            produto = ProdutoResponseSchema.model_validate(db_produto, from_attributes=True)
            produtos.append(produto)

        return produtos