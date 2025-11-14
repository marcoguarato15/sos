from app import db
from app.models.tipo_model import Tipo


def get_tipo():
    tipos = Tipo.query.all()
    return tipos

def add_tipo(tipo):
    tipo = Tipo(id_tipo=tipo.id_tipo, nome=tipo.nome)

    db.session.add(tipo)
    db.session.commit()

def put_tipo(id, id_tipo, nome):
    tipo = Tipo.query.filter_by(id=id).first()
    tipo.id_tipo = id_tipo
    tipo.nome = nome
    db.session.commit()