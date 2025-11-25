from app import db
from app.models.nota_model import Nota

def get_notas():
    notas = Nota.query.filter_by(ativo=True).all()
    return notas

def post_nota(nota):
    n = Nota(titulo=nota.titulo, demanda_id=nota.demanda_id, prioridade_id=nota.prioridade_id, data_criacao=nota.data_criacao, ativo=nota.ativo)
    db.session.add(n)
    db.session.commit()

def put_nota(id, titulo, demanda_id, prioridade_id):
    nota = Nota.query.filter_by(id=id).first()
    nota.titulo = titulo
    nota.demanda_id = demanda_id
    nota.prioridade_id = prioridade_id
    db.session.commit()

def get_nota_by_id(id):
    nota = Nota.query.filter_by(id=id).first()
    return nota

def del_nota(id):
    nota = Nota.query.filter_by(id=id).first()
    nota.ativo = False
    db.session.commit()