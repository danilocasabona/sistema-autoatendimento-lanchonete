from sqlalchemy.orm import Session
from app.core.schemas.produto import ProdutoCreateSchema
from app.core.models.produto import Produto

# 🧩 Função para criar um novo produto
def criar_produto(db: Session, produto: ProdutoCreateSchema):
    novo_produto = Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# 🧩 Função para listar todos os produtos
def listar_produtos(db: Session):
    return db.query(Produto).all()

# 🧩 Função para buscar um produto pelo ID
def buscar_produto_por_id(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

# 🧩 Função para atualizar um produto existente
def atualizar_produto(db: Session, produto_id: int, produto: ProdutoCreateSchema):
    produto_db = buscar_produto_por_id(db, produto_id)
    if produto_db:
        produto_db.nome = produto.nome
        produto_db.descricao = produto.descricao
        produto_db.preco = produto.preco
        db.commit()
        db.refresh(produto_db)
    return produto_db

# 🧩 Função para deletar um produto
def deletar_produto(db: Session, produto_id: int):
    produto_db = buscar_produto_por_id(db, produto_id)
    if produto_db:
        db.delete(produto_db)
        db.commit()
    return produto_db
