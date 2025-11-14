from app import db
from app.models.titulo_projeto_model import TituloProjeto


def get_titulo_projeto():
    titulos = TituloProjeto.query.all()
    return titulos

def add_titulo_projeto(titulo_projeto):
    titulo = TituloProjeto(id_titulo_projeto=titulo_projeto.id_titulo_projeto,nome=titulo_projeto.nome)

    db.session.add(titulo)
    db.session.commit()

def put_titulo_projeto(id, id_titulo_projeto, nome):
    titulo = TituloProjeto.query.filter_by(id=id).first()
    titulo.id_titulo_projeto = id_titulo_projeto
    titulo.nome = nome
    db.session.commit()

def get_titulo_projeto_by_id_titulo_projeto(id_titulo_projeto):
    titulo_projeto = TituloProjeto.query.filter_by(id_titulo_projeto=id_titulo_projeto).first()
    return titulo_projeto