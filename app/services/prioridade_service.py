from app import db
from app.models.prioridade_model import Prioridade


def get_prioridade():
    prioridades = Prioridade.query.all()
    return prioridades

def add_prioridade(prioridade):
    prioridade = Prioridade(id_prioridade=prioridade.id_prioridade, nome=prioridade.nome)

    db.session.add(prioridade)
    db.session.commit()

def put_prioridade(id, id_prioridade, nome):
    prioridade = Prioridade.query.filter_by(id=id).first()
    prioridade.id_prioridade = id_prioridade
    prioridade.nome = nome
    db.session.commit()

def get_prioridade_by_id_prioridade(id_prioridade):
    prioridade = Prioridade.query.filter_by(id_prioridade=id_prioridade).first()
    return prioridade