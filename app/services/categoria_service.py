from app import db
from app.models.categoria_model import Categoria

def get_categoria():
    categorias = Categoria.query.all()
    return categorias

def add_categoria(categoria):
    categoria_obj = Categoria(nome=categoria.nome, id_categoria=categoria.id_categoria, titulo_projeto_id=categoria.titulo_projeto_id)
    db.session.add(categoria_obj)

def put_categoria(id, nome, id_categoria, titulo_projeto_id):
    categoria = Categoria.query.filter_by(id=id).first()
    categoria.nome = nome
    categoria.id_categoria = id_categoria
    categoria.titulo_projeto_id = titulo_projeto_id
    db.session.commit()
